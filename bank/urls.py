from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('banks/', views.bank_list, name='bank-list'),
    path('banks/<int:pk>/', views.bank_detail, name='bank-detail'),
    path('branches/', views.branch_list, name='branch-list'),
    path('branches/<str:ifsc>/', views.branch_detail, name='branch-detail'),
]
