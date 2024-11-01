from django.contrib import admin
from django.urls import path
from. import views

app_name= 'adminapp'


urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('pagedivcall/',views.pagedivcall, name='pagedivcall'),
    path('pagedivlogic/',views.pagedivlogic, name='pagedivlogic'),
    path('exceptionpagecall',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic',views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randompagelogic/',views.randompagelogic,name='randompagelogic'),
    path('calculatorlogic',views.calculatorlogic,name='calculatorlogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('log_out/', views.log_out, name='log_out'),
    path('get_time_details/', views.get_time_details, name='get_time_details'),
    path('calculate_future_date/',views.calculate_future_date, name='calculate_future_date'),
    path('add_student/' ,views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('upload_file/',views.upload_file, name='upload_file'),
    path('contact_list', views.contact_list, name='contact_list'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
