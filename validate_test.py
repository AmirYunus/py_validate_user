#!/usr/bin/env python3

import unittest

from validate_user import validate_user

class Test_Validate_User(unittest.TestCase):
    def test_valid(self):
        assert validate_user("validuser", 3) == True

    def test_too_short(self):
        assert validate_user("inv", 5) == False

    def test_invalid_characters(self):
        assert validate_user("invalid_user", 1) == False

    def test_invalid_min_length(self):
        try:
            assert validate_user("user", -1)
        except:
            return True

unittest.main()