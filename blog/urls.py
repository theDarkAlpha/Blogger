from django.urls import path
from .views import HomePage, BlogPage
urlpatterns = [
    path('', HomePage.as_view(), name="Home"),
    path('post/<int:pk>/', BlogPage.as_view(), name="BlogPage"),

]