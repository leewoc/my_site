from django.urls import path

from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path("<int:blog_id>", views.blog_details, name="blog_details"),
    path("type/<int:blog_type_pk>", views.blog_with_type, name="blog_with_type"),
    path("data/<int:year>/<int:month>", views.blog_with_date, name="blog_with_date"),
]
