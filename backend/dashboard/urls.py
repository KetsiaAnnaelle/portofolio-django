from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.api_register, name='api_register'),
    path('api/login/', views.api_login, name='api_login'),
    path('api/about/', views.api_about, name='api_about'),
    path('api/portfolio/', views.api_portfolio, name='api_portfolio'),
    path('api/skills/', views.api_skills, name='api_skills'),
    path('api/qualifications/', views.api_qualifications, name='api_qualifications'),
    path('api/services/', views.api_services, name='api_services'),
    path('api/testimonials/', views.api_testimonials, name='api_testimonials'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/dashboard/', views.dashboard_home, name='dashboard_home'),
    path('api/', views.public_index, name='public_index'),
    #path('api/api/portfolio/', views.public_index, name='public_index'),
] 