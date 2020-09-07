from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post

class BlogTest(TestCase):bl

    def Setup(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            password='secret',
            email='tester@gmail.com'
        )
        self.post = Post.objects.create_user(
            title='a good post',
            body='this is a test blog!!!!',
            author = self.user
        )
    def test_admin_title(self):
        post = Post(title='a sample title')
        self.assertEqual(str(post), post.title)
    def test_body_content(self):
        self.assertEqual(f'{self.post.author}', 'tester')
        self.assertEqual(f'{self.post.title}', 'a good post')
        self.assertEqual(f'{self.post.body}', 'this is a test blog!!!!')
    def test_home_page(self):
        response = self.client.get(reverse('Home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'a good post')
        self.assertTemplateUsed(response, 'home.html')
    def test_blog_page(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'a good post')
        self.assertTemplateUsed(response, 'Detail_Blog.html')
