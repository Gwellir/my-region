from django.test import TestCase
from django.urls import reverse


# View tests
class TravelViewTests(TestCase):
    def test_main(self):
        """
        Tests whether main page is available.
        """

        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
