from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from ..views import BoardListView
from ..models import Board

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_view_url_resolver(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={ 'pk': self.board.pk })
        self.assertContains(self.response, 'href="{}"'.format(board_topics_url))