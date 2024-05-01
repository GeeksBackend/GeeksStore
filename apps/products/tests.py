from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

# Create your tests here.
class ProductTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Создаем пользователя и его токен
        self.user = User.objects.create_user(username='testing', password='geeks2024')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_products(self):
        response = self.client.get('/api/products/products/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_products(self):
        image_path = r'C:\Users\admin\Desktop\geek_store\codex.jpg'
        image = SimpleUploadedFile(name='codex.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        data = {
            "title": "Hello World",
            "description": "Geeks",
            "price": 12000,
            'image': image
        }
        response = self.client.post('/api/products/products/', data=data, format='multipart')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)