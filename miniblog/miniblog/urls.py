from django.contrib import admin
from django.urls import path, include
from blog_app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('addblog/', views.add_blog, name='addblog'),
    path('updateblog/<int:id>/', views.update_blog, name='updateblog'), 
    path('deleteblog/<int:id>/', views.delete_blog, name='deleteblog'), 

    path("accounts/", include("allauth.urls")),
]
