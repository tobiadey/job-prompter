from unittest import TestCase

from api.api import app


class TryTesting(TestCase):
    def test_flask_app(self):
        assert app is not None
