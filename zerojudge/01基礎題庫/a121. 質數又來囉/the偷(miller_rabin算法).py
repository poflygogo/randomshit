import random

# n >= 5
def miller_rabin(n, k):

  r, s = 0, n - 1
  while s % 2 == 0:
    r += 1 
    s //= 2
    for _ in range(k):
      a = random.randrange(2, n - 2)
      x = pow(a, s, n)
      if x == 1 or x == n - 1:
        continue
      for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
          break
      else:
        return False
    return True

def getRandomPrimeByBitLength(length, isnot=[]):
  return getRandomPrime((2**length)/2, 2**length)

def getRandomPrime(start, stop, isnot=[]):
  prime = 2
  while not miller_rabin(prime, 40) or prime in isnot:
    prime = random.randrange(start, stop)

  return prime

if __name__ == "__main__":
  #print("{:08b}".format(prime))

  print(getRandomPrimeByBitLength(32))
