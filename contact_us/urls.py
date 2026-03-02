from django.urls import path
from . import views
urlpatterns = [
    path('',views.contact_view,name = 'contact'),
    path("succes/", views.contact_success,name='contact_success')
]