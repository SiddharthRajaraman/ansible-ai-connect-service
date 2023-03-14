from http import HTTPStatus

from ai.api.tests.test_views import WisdomServiceAPITestCaseBase
from django.urls import reverse


class TestMiddleware(WisdomServiceAPITestCaseBase):
    def test_users(self):
        self.client.force_authenticate(user=self.user)
        r = self.client.get(reverse('me'))
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertTrue('username' in r.data)

    def test_home_view(self):
        self.login()
        r = self.client.get(reverse('home'))
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertIn(f'You are signed in as {self.username} ({self.email}).', str(r.content))

    def test_home_view_without_login(self):
        r = self.client.get(reverse('home'))
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertIn('You are not signed in.', str(r.content))