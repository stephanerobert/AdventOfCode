from collections import Counter

import re
from unittest import TestCase

class TestDisplay(TestCase):
    def setUp(self):
        self.display = Display(7, 3)

    def test_rectangle_2(self):
        result =[['#', '#', ' ', ' ', ' ', ' ', ' '],
                 ['#', '#', ' ', ' ', ' ', ' ', ' '],
                 ['#', '#', ' ', ' ', ' ', ' ', ' ']]

        answer = self.display.rect(2, 3)
        assert(answer == result)

    def test_rectangle(self):
        result =[['#', '#', '#', '#', ' ', ' ', ' '],
                 ['#', '#', '#', '#', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        answer = self.display.rect(4, 2)
        assert(answer == result)

    def test_rectangle_3(self):
        result =[['#', '#', '#', '#', ' ', ' ', ' '],
                 ['#', '#', '#', '#', ' ', ' ', ' '],
                 ['#', '#', '#', '#', ' ', ' ', ' ']]

        answer = self.display.rect(4, 3)
        assert(answer == result)

    def test_rotate_row(self):
        result =[['#', '#', ' ', ' ', ' ', '#', '#'],
                 ['#', '#', '#', '#', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.test_rectangle()
        answer = self.display.rotate_row(0, 5)
        assert(answer == result)

    def test_rotate_row2(self):
        result =[['#', '#', '#', '#', ' ', ' ', ' '],
                 ['#', '#', ' ', ' ', ' ', '#', '#'],
                 ['#', '#', '#', '#', ' ', ' ', ' ']]

        self.test_rectangle_3()
        answer = self.display.rotate_row(1, 5)
        assert(answer == result)

    def test_rotate_row3(self):
        result =[['#', '#', '#', '#', ' ', ' ', ' '],
                 ['#', '#', '#', '#', ' ', ' ', ' '],
                 ['#', '#', ' ', ' ', ' ', '#', '#']]

        self.test_rectangle_3()
        answer = self.display.rotate_row(2, 5)
        assert(answer == result)

    def test_rotate_column(self):
        result =[['#', '#', '#', '#', ' ', ' ', ' '],
                 [' ', '#', '#', '#', ' ', ' ', ' '],
                 ['#', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.test_rectangle()
        answer = self.display.rotate_column(0, 2)
        assert(answer == result)

    def test_rotate_column_2(self):
        result =[['#', '#', '#', '#', ' ', ' ', '#'],
                 ['#', '#', ' ', ' ', ' ', '#', ' '],
                 ['#', '#', '#', '#', ' ', ' ', ' ']]

        self.test_rotate_row2()
        answer = self.display.rotate_column(6, 2)
        assert(answer == result)



class Display:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.display = []
        for i in range(y):
            self.display.append([])
            self.display[i] = [' '] * x

    def rect(self, x, y):
        print('rect %sx%s' % (x,y))

        for i in range(y):
            self.display[i][0:x] = '#'*x
        return self.display

    def rotate_row(self, row, by):
        print('rotate row y=%s by %s' % (row, by))

        self.display[row] = self.display[row][-by:] + self.display[row][:-by]
        return self.display

    def rotate_column(self, col, by):
        print('rotate column y=%s by %s' % (col, by))

        c = [self.display[i][col] for i in range(self.y)]
        c = c[-by:] + c[:-by]
        for i in range(self.y):
            self.display[i][col] = c[i]
        return self.display


if __name__ == '__main__':
    d = Display(50, 6)
    with open('display_input.txt', 'r') as f:
        for i in f.readlines():
            if 'rect' in i:
                match = re.match(r'.* (\d+)x(\d+)', i)
                d.rect(int(match.group(1)), int(match.group(2)))
            elif 'rotate row' in i:
                match = re.match(r'.*=(\d+) by (\d+)', i)
                d.rotate_row(int(match.group(1)), int(match.group(2)))
            elif 'rotate column' in i:
                match = re.match(r'.*=(\d+) by (\d+)', i)
                d.rotate_column(int(match.group(1)), int(match.group(2)))

    c = Counter()
    for i in d.display:
        c = c + Counter(i)
        print(''.join(i))
    print(c)
