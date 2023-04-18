import mock
import unittest

from on_stop.on_stop import main


class TestOnStop(unittest.TestCase):

    @unittest.skip("dummy test")
    def test_main(self):
        """Dummy test."""
        main = mock.Mock()
        main.return_value = None
        assert None is main()
