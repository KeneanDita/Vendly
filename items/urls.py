from django.urls import path
from . import views

app_name = "items"
app_name = "items"


urlpatterns = [
    path('new/', views.new, name='new'),
    path("<int:pk>/", views.detail, name="detail"),
    path("int:pk>/delete/", views.delete, name='delete'),
]