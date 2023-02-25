from django.urls import path
from . import views
app_name='stop_app'
urlpatterns=[
    path('',views.SearchResult,name='SearchResult'),
]
