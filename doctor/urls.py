from django.urls import path
from doctor import views
urlpatterns=[
   path('',views.index,name='index'),
   path('login/',views.login,name='login'),
   path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('appoinment/',views.appoinment,name='appoinment'),
    path('appname/<int:id>',views.appname,name='appname'),
    path('bill/',views.bill,name='bill'),
    path('search/',views.search,name='search'),
]
