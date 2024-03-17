from django.urls import path

from blogpost.apps import BlogPostConfig
from blogpost.views import BlogPostCreateView, BlogPostDetailView, BlogPostListView, BlogPostUpdateView, \
    BlogPostDeleteView

app_name = BlogPostConfig.name

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('view/', BlogPostListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
]