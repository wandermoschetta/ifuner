from django.urls import path
from ifuner.website import views as v

urlpatterns = [
    path('', v.index, name='index'),
]