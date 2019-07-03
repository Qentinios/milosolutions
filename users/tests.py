from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from users.templatetags.user_custom_tags import eligibletag, bizzfuzztag
from .models import MiloUser


class MiloUserListViewTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        for user_id in range(5):
            MiloUser.objects.create(username=f'test {user_id}', password='zaq1@WSX', is_superuser=False,
                                    is_active=False, first_name=f'Jan {user_id}', last_name=f'Kowalski {user_id}',
                                    email=f'jan{user_id}@kowalski.com', is_staff=False, birthday=date.today())

    def test_list_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_by_name(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)

    def test_list_length(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(len(response.context['object_list']), 5)


class MiloUserDetailViewTest(TestCase):
    def setUp(self):
        MiloUser.objects.create(username='test', password='zaq1@WSX', is_superuser=False, is_active=False,
                                first_name='Jan', last_name='Kowalski', email='jan@kowalski.com', is_staff=False,
                                birthday=date.today())

    def test_view_by_url(self):
        response = self.client.get('/view/1')
        self.assertEqual(response.status_code, 200)

    def test_view_by_name(self):
        response = self.client.get(reverse('user_view', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_view(self):
        response = self.client.get(reverse('user_view', args=(1,)))
        self.assertEqual(response.context['object'].username, 'test')


class MiloUserDeleteViewTest(TestCase):
    def setUp(self):
        MiloUser.objects.create(username='test', password='zaq1@WSX', is_superuser=False, is_active=False,
                                first_name='Jan', last_name='Kowalski', email='jan@kowalski.com', is_staff=False,
                                birthday=date.today())

    def test_delete_by_url(self):
        response = self.client.get('/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_by_name(self):
        response = self.client.get(reverse('user_delete', args=(1,)))
        self.assertEqual(response.status_code, 200)


class MiloUserNewViewTest(TestCase):
    def setUp(self):
        MiloUser.objects.create(username='test', password='zaq1@WSX', is_superuser=False, is_active=False,
                                first_name='Jan', last_name='Kowalski', email='jan@kowalski.com', is_staff=False,
                                birthday=date.today())

    def test_form_new_by_url(self):
        response = self.client.get('/new')
        self.assertEqual(response.status_code, 200)

    def test_form_new_by_name(self):
        response = self.client.get(reverse('user_new'))
        self.assertEqual(response.status_code, 200)


class MiloUserEditViewTest(TestCase):
    def setUp(self):
        MiloUser.objects.create(username='test', password='zaq1@WSX', is_superuser=False, is_active=False,
                                first_name='Jan', last_name='Kowalski', email='jan@kowalski.com', is_staff=False,
                                birthday=date.today())

    def test_form_edit_by_url(self):
        response = self.client.get('/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_form_edit_by_name(self):
        response = self.client.get(reverse('user_edit', args=(1,)))
        self.assertEqual(response.status_code, 200)


class CustomTagsTest(TestCase):
    def test_eligibletag_blocked(self):
        blocked_eligibletag = date.today()
        blocked_eligibletag2 = date.today()-timedelta(days=365 * 10)
        self.assertEqual(eligibletag(blocked_eligibletag), 'blocked')
        self.assertEqual(eligibletag(blocked_eligibletag2), 'blocked')

    def test_eligibletag_allowed(self):
        allowed_eligibletag = date.today()-timedelta(days=365 * 22)
        allowed_eligibletag2 = date.today()-timedelta(days=365 * 14 + 5)
        self.assertEqual(eligibletag(allowed_eligibletag), 'allowed')
        self.assertEqual(eligibletag(allowed_eligibletag2), 'allowed')

    def test_bizzfuzztag_none(self):
        self.assertEqual(bizzfuzztag(37), '')
        self.assertEqual(bizzfuzztag(2), '')

    def test_bizzfuzztag_bizz(self):
        self.assertEqual(bizzfuzztag(3), 'Bizz')
        self.assertEqual(bizzfuzztag(33), 'Bizz')

    def test_bizzfuzztag_fuzz(self):
        self.assertEqual(bizzfuzztag(5), 'Fuzz')
        self.assertEqual(bizzfuzztag(55), 'Fuzz')

    def test_bizzfuzztag_bizzfuzz(self):
        self.assertEqual(bizzfuzztag(30), 'BizzFuzz')
        self.assertEqual(bizzfuzztag(60), 'BizzFuzz')

