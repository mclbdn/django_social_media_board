from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.

class SocialMediaBoardTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='password'
        )

        self.post = Post.objects.create(
            body="My content.",
            author=self.user
        )

    def test_string_representation(self):
        post = Post(body="A sample body")
        self.assertEqual(str(post), post.body)

    def test_post_content(self):
        self.assertEqual(f'{self.post.body}', 'My content.')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_posts_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My content.')
        self.assertTemplateUsed(response, 'home.html')