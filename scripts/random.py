import time

def shuffle(seq):
    control = {}
    random_seq_size = len(seq)
    max_idx = len(seq) + 2
    random_idxs = set([num for num in range(2, max_idx)])

    for idx in random_idxs:
        control[idx] = seq[idx-2]

    random_seq = []

    while len(random_seq) != random_seq_size:
        number = time.ticks_cpu()
        differ = random_idxs.difference(random_seq)

        for num in differ:
            if (number % num == 0):
                random_seq.append(num)

    return [control[num] for num in random_seq]

def choice(seq):
    return shuffle(seq)[0]

def randrange(start, stop, step=1):
    sequence = [num for num in range(start, stop, step)]
    return choice(sequence)

def random():
    return lcg_algorithm(time.ticks_cpu()) / 2147483647.

def lcg_algorithm(s, n=1):
    # ref.: http://www.uff.br/cdme/rdf/rdf-html/rdf-g-br.html
    a = 16807
    c = 0
    m = 2147483647

    def run_formula(a, c, m, s):
        return ( (a * s) + c) % m

    x = []
    for i in range(n):
        resp = run_formula(a, c, m, s)
        x.append(resp)
        s = resp

    # this is probably a technician adjustment
    if n == 1:
        x = x[0]

    return x