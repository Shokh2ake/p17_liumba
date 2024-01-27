from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path, include

from apps.tascks import task_send_email
from apps.views import IndexView, CustomLoginView, RegisterFormView, BlogListView, BlogDetailView, EmailView
from root import urls


def custom_view(request, email):
    response = task_send_email.delay('Temasi', 'Xabar', ['shokhake6690@gmail.com'])
    # response = task_send_email('Temasi', 'xabari', ['shokhake6690@gmail.com'])
    return response({'status': 'success'})


urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('blog-list', BlogListView.as_view(), name='blog_list_page'),
    path('logout', LogoutView.as_view(next_page='index_page'), name='logout'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('register', RegisterFormView.as_view(), name='register_page'),
    path('blogdetails/<int:pk>', BlogDetailView.as_view(), name='blog_details'),
    path('newsletters/', EmailView.as_view(), name='newsletters'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

]


def page_404(request, *args, **kwargs):
    return render(request, 'apps/404.html', status=404)


urls.handler404 = 'apps.urls.page_404'
