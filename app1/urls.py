from app1.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('chamu/',chamu,name='chamu')
]