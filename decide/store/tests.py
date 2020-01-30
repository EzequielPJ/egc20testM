import datetime
import random
from django.contrib.auth.models import User
from django.utils import timezone
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from .models import Vote
from .serializers import VoteSerializer
from base import mods
from base.models import Auth
from base.tests import BaseTestCase
from census.models import Census
from mixnet.models import Key
from voting.models import Question
from voting.models import Voting


class StoreTextCase(BaseTestCase):

    def tearDown(self):
        super().tearDown()
