from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', views.login, name='login'),
    # path('', views.index, name='index'),
    # path('login/', login, {'template_name': 'agent_app/login.html'}),
    # path('auth/', include('social_django.urls', namespace='social')),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', views.register, name='register'),
    # path('accounts/logout/', views.logout_view, name='logout'),
    # path('accounts/logout/', logout, {'template_name': 'registration/logout.html'}),
    # path('accounts/change-password/', views.change_password, name='change_password'),
    # path('accounts/reset-password/', password_reset, {'template_name': 'registration/reset_password.html'},
    #      name='reset_password'),
    # path('accounts/reset-password/done/', password_reset_done, {'template_name': 'registration/reset_password_done.html'},
    #      name='password_reset_done'),
    # re_path(r'^/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm,
    #         {'template_name': 'registration/reset_password_confirm.html'}, name='password_reset_confirm'),
    # re_path(r'^reset-password/complete/$', password_reset_complete,
    #         {'template_name': 'registration/reset_password_complete.html'}, name='password_reset_complete'),


]
