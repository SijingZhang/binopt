# -*- coding: utf-8 -*-

from .context import zbinner

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        """Test absolute truth and meaning."""
        assert True


if __name__ == '__main__':
    unittest.main()
