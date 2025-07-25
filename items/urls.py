from django.urls import path
from . import views

app_name = "items"
app_name = "items"


urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path("<int:pk>/", views.detail, name="detail"),
    path('category/<int:category_id>/', views.category_items, name='category_items'),
    path('items/<int:pk>/delete/', views.delete, name='delete'),
    path('items/<int:pk>/edit/', views.edit, name='edit'),
]