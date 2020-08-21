from django.urls import path
from . import views

app_name='safe'

urlpatterns=[
    path('userpage/',views.userpage,name='userpage'),
    path('decrypt/<int:id>/',views.decrypt,name='decrypt'),
    path('encrypt/<password>/',views.encrypt,name='encrypt'),
]