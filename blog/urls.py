from django.urls import path
from .views import HomePage, BlogPage, NewBlog, EditBlog
urlpatterns = [
    path('', HomePage.as_view(), name="Home"),
    path('post/<int:pk>/', BlogPage.as_view(), name="BlogPage"),
    path('post/new', NewBlog.as_view(), name='NewPage'),
    path('post/<int:pk>/edit', EditBlog.as_view(), name='EditBlog'),

]