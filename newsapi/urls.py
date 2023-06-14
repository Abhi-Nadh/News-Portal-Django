from django.urls import path
from . import views

urlpatterns = [
        path('loginapi',views.loginapi,name='loginapi'),
        path('signupapi',views.signupapi,name='signupapi'),
        path('',views.list_news,name='listnewsapi'),
        path('addnewsapi',views.add_news,name='addnewsapi'),
        path('editnewsapi/<int:uid>',views.edit_news,name='editnewsapi'),
        path('deleteapi/<int:uid>',views.delete_news,name='deletenewsapi'),
            ]