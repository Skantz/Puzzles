

#https://stackoverflow.com/a/568684
def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
'''
>> filter(is_prime, range(1, 20))
  [2, 3, 5, 7, 11, 13, 17, 19]

We will get all the prime numbers upto 20 in a list. 
'''

def primes_up_to(n):
  return list(filter(is_prime, range(1, n)))
