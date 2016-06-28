#! /usr/bin/env python

import math

def mult(n, k, l, p, q):
    value = combination(n, k) * combination(n-k, l)
    value *= math.pow(p, k) * math.pow(q, l) * math.pow(1-p-q, n-k-l)
    return value

def bin(n, k, p):
    return combination(n, k) * math.pow(p, k) * math.pow(1-p, n-k)

def combination(n, k):
    value = 1;
    for i in xrange(k):
        value *= (n-i) / float(k-i);
    return value;

n = 10
epsilon = 0.01

aa = bin(n, 1, 1-epsilon) * 1/6.0;
ag = mult(n, 1, 1, 1/2.0 * (1-2/3.0*epsilon), 1/2.0*(1-2/3.0*epsilon))*1/6.0

print "A/A: " + str(aa)
print "A/G: " + str(ag)

