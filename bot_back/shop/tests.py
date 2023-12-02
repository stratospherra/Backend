from django.test import TestCase
from .models import Post


class TestPostModel(TestCase):

    def test_post_has_title(self):
        post = Post.objects.create(title='Тестовый пост', content='Содержание тестового поста')
        self.assertEqual(post.title, 'Тестовый пост')

    def test_post_has_content(self):
        post = Post.objects.create(title='Тестовый пост', content='Содержание   поста')
        self.assertEqual(post.content, 'Содержание     поста')

    def test_post_str_method(self):
        post = Post.objects.create(title='Тестовый пост', content='Содержание тестового поста')
        self.assertEqual(str(post), 'Тестовый пост')