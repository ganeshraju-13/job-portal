from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.job_list,
        name='job_list'
    ),

    path(
        'job/<int:id>/',
        views.job_detail,
        name='job_detail'
    ),

    path(
        'job/<int:id>/edit/',
        views.edit_job,
        name='edit_job'
    ),

    path(
        'job/<int:id>/delete/',
        views.delete_job,
        name='delete_job'
    ),

    path(
        'job/<int:id>/apply/',
        views.apply_job,
        name='apply_job'
    ),

    path(
        'application/<int:id>/status/',
        views.application_status,
        name='application_status'
    ),

    path(
        'my-applications/',
        views.my_applications,
        name='my_applications'
    ),
    path(
        'admin-dashboard/',
         views.admin_dashboard,
         name='admin_dashboard'
    ),

    path(
        'admin-applications/',
        views.admin_applications,
        name='admin_applications'
    ),
    path(
        'admin-applications/<int:id>/update/',
         views.update_application_status,
         name='update_application_status'
    ),
    path(
        'admin-applications/<int:id>/details/',
         views.admin_application_detail,
         name='admin_application_detail'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.login_user,
        name='login'
    ),

    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),
]