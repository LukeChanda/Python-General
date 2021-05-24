# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:31:19 2021

@author: Luke
"""

import math

def mersenne_number(p):
    return 2**p - 1


def is_prime(number): # Helper function to check is a given number is prime
    if number <= 1: # ensures 0 will not be included as a prime
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True


# The first optimization takes advantage of the fact that two is the only even 
# prime.  Thus we can check if a number is even and as long as its greater 
# than 2, we know that it is not prime.
def is_prime_fast(n):
    if n <= 1: # ensures 0 will not be included as a prime
        return False
    elif n % 2 == 0 and n > 2: # 2 is the only even prime
        return False # number is even
    else:
        # only check odd factors up to root n
        b = int(math.sqrt(n)) + 1
        for factor in range(3, b, 2):
            if n % factor == 0:
                return False
            
    return True
    

def get_primes(n_start, n_end):
    primes = []
    for x in range(n_start, n_end):
        if is_prime(x):
            primes.append(x)           
    return primes


def get_primes_fast(n):
    primes = []
    for x in range(n):
        if is_prime_fast(x):
            primes.append(x)           
    return primes


def lucas_lehmer(p):
    seq = []
    if p < 2:
        raise 'Exponent less than 2'
    else:
        s = 4
        seq.append(s)
        m = 2**p - 1
        for _ in range(p - 2): # repeat p - 2 iterations
            s = (s * s - 2) % m
            seq.append(s)
    
    return seq
    

def ll_prime(p):
    if is_prime(p):
        if lucas_lehmer(p)[-1] == 0:
            return 1 # corresponding Mersenne number is prime
    return 0

list_of_primes = get_primes(3, 65)
        
test = [ll_prime(p) for p in list_of_primes]

mersenne_primes = list(zip(list_of_primes, test))

# Sieve of Eratosthenes

# a list of true values of length  𝑛+1  where the first two values are false
def list_true(n):
    values = [True]*(n + 1)
    values[0] = False
    values[1] = False
    return values


def mark_false(bool_list, p):
    for i in range(p * 2, len(bool_list), p):
        print(i)
        bool_list[i] = False
    return bool_list


def find_next(bool_list,  p):
    for i in range(p + 1, len(bool_list)):
        if bool_list[i]:
            return i


def prime_from_list(bool_list):
    indices = []
    for i in range(len(bool_list)):
        if bool_list[i]:
            indices.append(i)
    return indices

primes = list_true(6)

mark_false(primes, 2)

find_next(primes, 2)

P = prime_from_list(primes)

print(P)



























