from django.urls import path
from learn.views import RegisterViewSet

urlpatterns = [
    path('register/',RegisterViewSet.as_view({'get':'list','post':'create'}),name='learn_register'),
    path('register/<int:pk>',RegisterViewSet.as_view({'get':'retrieve'}),name='learn_particular'),
]