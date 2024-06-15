import datetime
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone
from blog.models import Blog
from read_count.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data


def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = (Blog.objects.filter(read_details__date__lt=today, read_details__date__gte=date)
             .values('id', 'title')).annotate(read_num_sum=Sum('read_details__read_num')).order_by('-read_num_sum')
    return blogs[:7]


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)
    today_hot_data = get_today_hot_data(blog_content_type)
    yesterday_hot_data = get_yesterday_hot_data(blog_content_type)

    # 获取七天热门博客缓存数据
    hot_7_days_blogs = cache.get('hot_7_days_blogs')
    if hot_7_days_blogs is None:
        hot_7_days_blogs = get_7_days_hot_blogs()
        cache.set('hot_7_days_blogs', hot_7_days_blogs, 3600)
        print("save cache")
    else:
        print('use cache')

    context = {'read_nums': read_nums, 'dates': dates, 'today_hot_data': today_hot_data,
               'yesterday_hot_data': yesterday_hot_data, 'hot_7_days_blogs': hot_7_days_blogs}
    return render(request, 'home.html', context)



