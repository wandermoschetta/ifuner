from django.urls import path
from ifuner.core import views as v
from ifuner.website import views as site
app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('login', v.login, name='login'),
    path('site', site.index, name='index'),
]