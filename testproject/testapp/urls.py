from django.urls import path
from . import views  # точна говорит что из этой же директорий импортируй views

urlpatterns = [
    path('', views.home_page)
]
