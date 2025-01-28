def is_valid_password(password):
    if not isinstance(password, str):
        raise TypeError("Пароль має бути рядком")
    if len(password) >= 8 and not password.islower() and any(char.isdigit() for char in password) \
        and any(char in password for char in '&,.:;-^#@*(!\\/|'):
        return True
    else:
        return False
    
import unittest

class TestFunction(unittest.TestCase):
    def test_is_valid_password_basic(self):
        self.assertTrue(is_valid_password('qwErty12&@'))
        self.assertFalse(is_valid_password('Qwe2,!'))
        self.assertFalse(is_valid_password('QwErty!&)'))
        self.assertFalse(is_valid_password('1qwerty!&)'))
        self.assertFalse(is_valid_password('QwErty123'))
        self.assertFalse(is_valid_password(''))
    
    def test_is_valid_password_errors(self):
        with self.assertRaises(TypeError):
            is_valid_password(12345678)
            
        with self.assertRaises(TypeError):
            is_valid_password(None)