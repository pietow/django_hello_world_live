from django.urls import path, re_path
from .views import homePageView

urlpatterns = [
    re_path(r"^\d+$", homePageView, name="home")
]
