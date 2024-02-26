# write a code to print prime number
def get_primes(limit):
   primes = []
   for num in range(2, limit + 1):
       if all(num % i != 0 for i in range(2, num)):
           primes.append(num)
   return primes


# Print the prime numbers up to 100.
print(get_primes(100))