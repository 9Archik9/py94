from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.comment_page, name='comment')
]
