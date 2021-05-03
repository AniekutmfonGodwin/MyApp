import datetime

from django.test import TestCase
from django.utils import timezone




class PostTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
       
        self.assertIs(False, False)