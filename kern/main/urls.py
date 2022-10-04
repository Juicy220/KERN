from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index),
    path('graph', views.kern_graph),
    path('kern2',views.kern2),
    path('acc',views.acc),
    path('acc2',views.acc2)
]
