
from django.urls import path
from . import views

urlpatterns = [
        path('',views.newsListview.as_view(),name='newslist'),
        path('signup',views.signup_user,name='signup'),
        path('login',views.login_user,name='login'),
        path('logout',views.logout_user,name='logout'),
        path('addnews',views.addnews,name='addnews'),
        path('mynews',views.user_added_,name='mynews'),
        path('editnews/<int:uid>',views.updatenews,name='editnews'),
        path('detailnews/<int:uid>',views.detailnews,name='detailnews'),
        path('delete/<int:uid>',views.deletenews,name='deletenews'),
                ]