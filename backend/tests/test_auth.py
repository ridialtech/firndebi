import unittest
from backend import auth

class AuthTestCase(unittest.TestCase):
    def test_authenticate_success(self):
        self.assertTrue(auth.authenticate("admin", "secret"))

    def test_authenticate_failure(self):
        self.assertFalse(auth.authenticate("user", "pass"))

if __name__ == "__main__":
    unittest.main()
