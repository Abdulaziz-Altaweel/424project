from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.item_list), name='item_list'),  # List all items
    path('item/<int:pk>/', views.item_detail, name='item_detail'),  # View a specific item
    path('item/<int:pk>/purchase/', views.purchase_item, name='purchase_item'),
    path('item/add/', views.item_create, name='item_create'),  # Add a new item
    path('item/<int:pk>/edit/', views.item_update, name='item_update'),  # Edit an item
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),  # Delete an item
    path('register/', views.register, name='register'),  # User registration
    path('login/', views.login, name='login'),  # User login
    path('logout/', views.logout, name='logout'),
]
