
from django.urls import path
from . import views
urlpatterns = [
    path('profile/', views.profile, name = 'profile'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('changepass/', views.change_password, name = 'changepass'),
    path('changepass2/', views.change_password2, name = 'changepass2'),
]
