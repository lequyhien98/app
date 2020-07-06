from django.urls import path, include

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.Home, name='home'),
    path('create/', views.ProductCreate.as_view(), name='create'),
    path('update/<int:id>/', views.ProductUpdate.as_view(), name='update'),
    path('delete/<int:id>/', views.ProductDelete.as_view(), name='delete'),
    path('<int:id>/', views.Detail, name='detail'),
]