from django.urls import path
from .import views

app_name = 'index_page'
urlpatterns = [
    # path('', views.index_page,name = 'index'),
    path('', views.IndexPageView.as_view(),name = 'index'),
]