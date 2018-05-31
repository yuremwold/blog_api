from django.urls import path

# from .views import Index
from .views import UserApiView, UserDetailApiView, BlogApiListView, BlogApiDetailView

urlpatterns = [
    path('user/list/', UserApiView.as_view(), name='api-user_list'),
    path('user/detail/<int:pk>/', UserDetailApiView.as_view(), name='api-user_detail'),

    path('blog/list/', BlogApiListView.as_view(), name='api-blog_list'),
    path('blog/detail/<int:pk>/', BlogApiDetailView.as_view(), name='api-blog_detail'),

]
