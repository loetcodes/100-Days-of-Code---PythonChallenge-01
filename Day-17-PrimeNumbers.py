"""
Day 17 - Prime numbers - CodeWars

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

"""
def primeFactors(n):
    prime_factors = ""
    p, x = 2, n
    while x >= p:
        for num in range(2,p):
            if p % num == 0:
                p += 1
                break
        pows = []
        val = x
        while (val%p == 0):
            pows.append(p)
            val = val / p
        if len(pows) == 1:
            prime_factors += "(" + str(pows[0]) + ")"
        elif len(pows) > 1:
            prime_factors += "(" + str(pows[0]) + "**" + str(len(pows)) + ")"                       
        x = val
        p += 1 
    return prime_factors
