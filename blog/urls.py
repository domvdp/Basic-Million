from django.urls import path
from .views import PostListView, PostDetailView
from . import views


urlpatterns = [
    # path('', PostListView.as_view(), name='blog-home'),
    path('', views.home, name='blog-home'),
    path('saving/', views.saving, name='blog-saving'),
    path('investing/', views.investing, name='blog-investing'),
    path('mindset/', views.mindset, name='blog-mindset'),
    path('motivation/', views.motivation, name='blog-motivation'),
    path('about/', views.about, name='blog-about'),
    path('postcard/', views.postcard, name='blog-postcard'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
