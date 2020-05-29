

# This project contain 2 application :

**1- accounts**
**2- blog**
 
# 1- accounts:
Application for user authentication

**accounts.urls.py**\
`
    # initial url show the dashboard\
    path('', views.dashboard, name='dashboard'),\
    # login urls \
    path('login/', auth_views.LoginView.as_view(), name='login'),\
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),\
    # change password urls\
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),\
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),\
    # reset password urls\
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),\
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),\
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),\
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),\

    # register new user\
    path('register/', views.register, name='register'),\
    # edit Profile\
    path('edit/', views.edit, name='edit'),\

`

# 2- blog:
Blog application that allow users to crud a post (comments are not added yet)

**blog.urls.py**\
`
    path('', views.index, name='blog_index'),\

    # posts urls for crud operations\
    path('posts/', views.PostList.as_view(), name='post_list'),\
    path('posts/<int:tag_id>', views.PostListByTag.as_view(), name='post_list'),\
    path('posts/<str:username>', views.PostListForSpecificUser.as_view(), name='post_list'),\
    path('post/add/', views.PostCreate.as_view(), name='post_add'),\
    path('post/<int:pk>/detail/', views.PostDetail.as_view(), name='post_detail'),\
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),\
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),\

`

