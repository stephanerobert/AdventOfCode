from unittest import TestCase


class TestPassword(TestCase):
    def test_password_unordered(self):
        pc = PasswordCalculator("abc")
        assert(pc.find_unordered() == "18f47a30")

    def test_password(self):
        pc = PasswordCalculator("abc")
        password = pc.find_ordered()
        print(password)
        assert(''.join(password) == "05ace8e3")

class PasswordCalculator:
    def __init__(self, key):
        self.key = key

    def find_unordered(self):
        import hashlib
        password = ''
        for i in range(10000000):
            key = self.key+str(i)
            m = hashlib.md5(key.encode()).hexdigest()
            if m.startswith('00000'):
                password = password + m[5:6]
                if len(password) == 8:
                    return password

    def find_ordered(self):
        import hashlib
        count = 0
        password = ['-','-','-','-','-','-','-','-']
        for i in range(100000000000):
            key = self.key+str(i)
            m = hashlib.md5(key.encode()).hexdigest()
            if m.startswith('00000'):
                try:
                    if password[int(m[5:6])] == '-':
                        password[int(m[5:6])] = m[6:7]
                        count = count +1
                        if count == 8:
                            return password
                except (ValueError, Exception):
                    pass

if __name__ == '__main__':
    print(''.join(PasswordCalculator("reyedfim").find_ordered()))
