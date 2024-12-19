from . import views
from django.urls import path


# /product1

urlpatterns=[
    path('',views.index,name='index'),
]