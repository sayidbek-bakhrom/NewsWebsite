from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article-<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article-edit-<int:pk>/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article-delete-<int:pk>/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('article-new/', views.ArticleCreateView.as_view(), name='article-new')
]