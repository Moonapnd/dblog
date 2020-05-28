from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    ########################################################################
    path('', views.index, name='blog_index'),

    # posts urls for crud operations
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:tag_id>', views.PostListByTag.as_view(), name='post_list'),
    path('posts/<str:username>', views.PostListForSpecificUser.as_view(), name='post_list'),
    path('post/add/', views.PostCreate.as_view(), name='post_add'),
    path('post/<int:pk>/detail/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),

    # path('post/like_post/', views.like_post, name='like_post'),

]

