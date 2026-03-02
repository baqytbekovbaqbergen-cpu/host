from django.test import TestCase, Client
from django.urls import reverse
from .models import ContactMessage
from .forms import ContactForm


class ContactMessageModelTest(TestCase):
    def test_create_message(self):
        message= ContactMessage.objects.create(
            name = "Ayat",
            email = "ayatikepashel@shymkent.com",
            message="AYYY AYYY AYYYY"

        )
        self.assertEqual(str(message), "Ayat ayatikepashel@shymkent.com")
        self.assertIsNotNone(message.created_at)

    def test_str_representation(self):
        message= ContactMessage.objects.create(
            name="Dimash",
            email="dimasik@ponosik.com",
            message="nice message"
        )
        self.assertEqual(str(message), "Dimash dimasik@ponosik.com")
# Create your tests here.
