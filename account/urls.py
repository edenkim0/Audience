from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='account_login'),
    path('logout/', views.UserLogOutView.as_view(), name='account_logout'),
    path('applicant/create/', views.create_applicant, name='create_applicant'),
    path('employer/create/', views.create_employer, name='create_employer'),
    path('username/search/', views.search_username, name='search_username'),
    path('password/search/', views.search_password, name='search_password'),
    path('password/check/', views.check_user_password, name='check_user_password'),
    path('password/update/', views.change_password, name='update_password'),
    path('update/', views.update_account, name='update_account'),
    path('delete/', views.delete_account, name='delete_account'),
    path('posts/detail/', views.my_posts_detail, name='my_posts_detail'),
    path('signup/finish/', views.signup_finish, name='signup_finish'),
    path('signup/', views.signup_page, name='signup_page'),
    path('search_id_pw/', views.search_id_pw, name='search_id_pw'),
    path('mypage/', views.my_page, name='my_page')
]
