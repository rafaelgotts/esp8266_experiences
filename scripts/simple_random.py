import time

__all__ = ["LCGRandom"]

class LCGRandom(object):
    """ Class to implement a lcg 
        algorithm for random numbers.

        formula: Xn+1 = (a * Xn + c) mod m
        a = multiplier
        Xn = seed
        c = increment
        m = modulus

        In this case, we will use timeticks
        for first seed
    """ 
    MULTIPLIER = 16807
    INCREMENT = 0
    MODULUS = 2147483647

    def __init__(self):
        self.a = MULTIPLIER
        self.c = INCREMENT
        self.m = MODULUS
        self.xn = time.ticks_cpu()

    def random(self):
        """ Get the next random 
            number in range (0.0, 1.0)
        """
        self.xn = (
            self.a * self.xn + self.c
        ) % self.m

        return self.xn / float(self.m)

    def shuffle(self, seq):
        """ Copied from python random module 
        """
        for i in reversed(xrange(1, len(seq))):
            # pick an element in seq[:i+1] with which to exchange seq[i]
            j = int(random() * (i + 1))
            seq[i], seq[j] = seq[j], seq[i]

    def choice(self, seq):
        """ Copied from python random module
        """ 
        idx = int(random() * len(seq))
        return seq[idx]

    def randrange(start, stop, step=1):
        """ Return a random number of a defined range.
        """
        sequence = [num for num in range(start, stop, step)]
        return choice(sequence)