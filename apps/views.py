from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, DetailView

from apps.forms import RegisterForm, EmailForm
from apps.mixins import NotLoginRequiredMixin
from apps.models import Blog


class BlogListView(ListView):
    paginate_by = 5
    template_name = 'apps/blogs/blog-list.html'
    queryset = Blog.objects.order_by('-created_at')
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        if search := self.request.GET.get("search"):
            return queryset.filter(name__icontains=search)
        return queryset


class BlogDetailView(DetailView):
    queryset = Blog.objects.order_by('-created_at')
    template_name = 'apps/blogs/blog-details-left-sidebar.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'blog'


class IndexView(TemplateView):
    template_name = 'apps/index.html'


class CustomLoginView(NotLoginRequiredMixin, LoginView):
    template_name = 'apps/login-register.html'
    next_page = 'index_page'


class RegisterFormView(FormView):
    template_name = 'apps/login-register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('register_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EmailView(FormView):
    template_name = 'apps/base.html'
    form_class = EmailForm
    success_url = '.'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('.', self.get_context_data(form=form))
