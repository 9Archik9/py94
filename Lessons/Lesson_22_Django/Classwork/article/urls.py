from django.urls import path
from article import views

urlpatterns = [
    path('article/', views.article_page, name='article')
]
