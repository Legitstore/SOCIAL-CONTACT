from django.urls import path
from .import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('add_user', views.add_user, name='add-user'),
    path('view_list', views.view_list, name='view-list'),
    path('delete_user/<str:pk>', views.delete_user, name='delete-user'),
    path('update_user/<str:pk>', views.update_user, name='update-user'),
    path('view_text', views.view_text, name='view-text'),
    path('view_pdf', views.view_pdf, name='view-pdf'),

    path('search_view', views.search_view, name='search-view'),
]