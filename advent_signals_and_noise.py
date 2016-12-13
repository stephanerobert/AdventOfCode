from collections import Counter
from unittest import TestCase


class TestSignalsNoise(TestCase):
    input =['eedadn',
            'drvtee',
            'eandsr',
            'raavrd',
            'atevrs',
            'tsrnev',
            'sdttsa',
            'rasrtv',
            'nssdts',
            'ntnada',
            'svetve',
            'tesnvt',
            'vntsnd',
            'vrdear',
            'dvrsen',
            'enarar']

    def test_signal(self):
        sn = SignalNoise(self.input)
        signal = sn.find(reverse=True)
        print(signal)
        assert(signal == "easter")

    def test_signal_least_frequent(self):
        sn = SignalNoise(self.input)
        signal = sn.find(reverse=False)
        print(signal)
        assert(signal == "advent")



class SignalNoise:
    def __init__(self, input):
        self.input = input

    def find(self, reverse):
        answer = ''
        for i in zip(*self.input):
            c = Counter(i)
            answer = answer + sorted(c.keys(), key=c.__getitem__, reverse=reverse)[0]
        return answer

if __name__ == '__main__':
    with open('signal_noise_input.txt', 'r') as f:
        print(SignalNoise(f.readlines()).find(reverse=False))
