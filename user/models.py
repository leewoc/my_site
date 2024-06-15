from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)  # 创建外键，与User关联。一对一字段，一个Profile
    # 对应一个User，一个User对应一个Profile
    nickname = models.CharField(max_length=20, verbose_name='昵称', blank=True)
    # 电话号码字段
    phone = models.CharField(max_length=20, verbose_name='号码', blank=True)
    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True,
                               default='avatar/default.jpg')
    # 个人简介
    bio = RichTextUploadingField(blank=True, null=True, default='这个家伙很神秘')

    def __str__(self):  # 显示字符串
        # return '<Profile: %s for %s>' % (self.nickname, self.user.username)
        return "{}".format(self.user.__str__())


def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''


def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return self.username


def has_nickname(self):
    return Profile.objects.filter(user=self).exists()


User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname


# 我们现在将定义信号，这样当我们创建/更新用户实例时，我们的Profile模型将自动创建/更新

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
