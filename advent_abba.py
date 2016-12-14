import re
from collections import Counter
from unittest import TestCase


class TestSignalsNoise(TestCase):
    def setUp(self):
        self.ad = AbbaDetector()

    def test_abba1(self):
        assert(self.ad.validate('abba[mnop]qrst'))

    def test_abba2(self):
        assert(self.ad.validate('abcd[bddb]xyyx') == False)

    def test_abba3(self):
        assert(self.ad.validate('aaaa[qwer]tyui') == False)

    def test_abba4(self):
        assert(self.ad.validate('ioxxoj[asdfgh]zxcvbn'))

    def test_abba3(self):
        assert(self.ad.validate('aaaa[qwer]tyui[qwer]tyabbaui[qwer]tyui'))


class AbbaDetector:

    def validate(self, input):
        valid = False
        entries = re.split(r'[\[\]]', input)
        for i, entry in enumerate(entries):
            is_palyndrome = self.is_valid(entry)
            if i%2 == 0:
                if is_palyndrome:
                    valid = True
            else:
                if is_palyndrome:
                    return False
        return valid

    def is_valid(self, entry):
        for i in range(len(entry)-3):
            palyndrome = entry[i:i+4]
            if palyndrome == palyndrome[::-1]:
                if len(Counter(palyndrome)) > 1:
                    return True
        return False


class TestSignalsNoise2(TestCase):
    def setUp(self):
        self.ad = AbaBabDetector()

    def test_abba1(self):
        assert(self.ad.validate('aba[bab]xyz'))

    def test_abba2(self):
        assert(self.ad.validate('xyx[xyx]xyx') == False)

    def test_abba3(self):
        assert(self.ad.validate('aaa[kek]eke'))


class AbaBabDetector:

    def validate(self, input):
        valid = []
        bracket = []
        entries = re.split(r'[\[\]]', input)
        for i, entry in enumerate(entries):
            p1 = self.is_valid(entry)
            if p1:
                if i%2 == 0:
                    for j in p1:
                        valid.append(j)
                else:
                    for j in p1:
                        p = j[1]+j[0]+j[1]
                        bracket.append(p)

                if len(set(valid).intersection(set(bracket))):
                    return True

        return False

    def is_valid(self, entry):
        ps=[]
        for i in range(len(entry)-2):
            palyndrome = entry[i:i+3]
            if palyndrome == palyndrome[::-1]:
                if len(Counter(palyndrome)) > 1:
                    ps.append(palyndrome)
        if ps:
            return ps
        return False


if __name__ == '__main__':
    ab = AbaBabDetector()
    count = 0
    with open('abba_input.txt', 'r') as f:
        for i in f.readlines():
            if ab.validate(i):
                count = count +1
    print(count)
