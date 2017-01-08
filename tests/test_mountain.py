from flask_testing import TestCase
from .context import slopespot
import os

from slopespot.app import app, db
from slopespot.model import Mountain

class TestMountain(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        self.db = db
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.session.commit()
        self.db.drop_all()

    def test_adding_mountain(self):
        m = Mountain(name='Whiteface')
        self.db.session.add(m)
        self.db.session.commit()
        self.assertEqual(1, len(m.query.all()))
