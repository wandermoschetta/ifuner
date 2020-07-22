from django.urls import path
from ifuner.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('login', v.login, name='login'),
]