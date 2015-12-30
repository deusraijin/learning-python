#!/usr/bin/env python

import random
import time

def nsum(list_t):
    sum = 0.0

    if not isinstance(list_t, list):
        return False

    for item in list_t:
        if isinstance(item, list):
            sum += nsum(item)
        elif isinstance(item, float):
            sum += item
        elif isinstance(item, int):
            sum += item*1.0

    return sum

def cumsum(list_t):
    csum = []

    if not isinstance(list_t, list):
        return False

    i = 0
    for i in range(len(list_t)):
        csum += [sum(list_t[:i+1])]
        i += 1

    return csum

def middle(list_t):
    return list_t[1:-1]

def chop(list_t):
    del list_t[0]
    del list_t[-1]

def is_sorted(list_t):
    return list_t == sorted(list_t)

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def has_duplicates(list_t):
    unique_values = []

    if not isinstance(list_t, list):
        return False

    for item in list_t:
        if item in unique_values:
            return True
        unique_values.append(item)

    return False

def has_duplicates2(t):
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def birthday_simulation(n, num_trials = 1000):
    num_overlaps = num_birthdays = 0
    start_time = time.time()

    for i in range(num_trials):
        num_birthdays += n
        birthdays = []

        for j in range(n):
            birthdays.append(random.randint(1,365))

        if has_duplicates2(birthdays):
            num_overlaps += 1

    print('There were {0} total birthdays, {1} overlaps, with a percentage probability of {2} %.'.format(num_birthdays, num_overlaps, (num_overlaps * 1.0 / num_birthdays * 100)))
    print('The simulation took {0} seconds.'.format(time.time()-start_time))
