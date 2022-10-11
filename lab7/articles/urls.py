from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', views.ArticleDeletelView.as_view(), name='article_delete'),

]
