# These are some of the following issues in the code - 
# 1. The size of the res array is not declared correctly.
#     It should be `res = [False] * (limit + 1)` instead of `res = [False]`
# 2. The loop condition checking should be corrected to 
#       `while i*i <= limit:
#          j = 1
#          while j*j <= limit:`
#      as with other sieve algorithms, Sieve of Atkin works on the principle that non-prime numbers have factors, so it's sufficient to mark multiples 
#      only up to the square root.

# 3. Currently we are directly returning 'res' which is a boolean array but we must return the list of prime numbers we can add this code to follow the correct logic.
#     primes = []
#     i = 2
#     while i <= limit:
#         if res[i]:
#             primes.append(i)
#         i += 1
#     return primes.


# No IF
# Has Truthfullness

def sieve(limit):

    if limit < 2:

        return []

    if limit == 2:

        return [False, True]

    if limit == 3:

        return [False, True, True]



    res = [False] * (limit + 1)

    if limit >= 2:

        res[2] = True

    if limit >= 3:

        res[3] = True



    i = 1

    while i*i <= limit:

        j = 1

        while j*j <= limit:



            n = (4 * i * i) + (j * j)

            if (n <= limit and (n % 12 == 1 or

                                n % 12 == 5)):

                res[n] ^= True



            n = (3 * i * i) + (j * j)

            if n <= limit and n % 12 == 7:

                res[n] ^= True



            n = (3 * i * i) - (j * j)

            if (i > j and n <= limit and

                    n % 12 == 11):

                res[n] ^= True

            j += 1

        i += 1



    r = 5

    while r * r <= limit:

        if res[r]:

            for i in range(r * r, limit + 1, r * r):

                res[i] = False



        r += 1

    primes = []

    i = 2

    while i <= limit:
        if res[i]:
            primes.append(i)
        i += 1

    return primes





def pick_prime(primes, min_size=1000):

    """returns a suitable prime to use as modulus"""

    for prime in primes:

        if prime >= min_size:

            return prime

    # if no prime large enough exists, use last one on list

    return primes[-1]



def hash(string, modulus):

    """implements polynomial rolling of string keys"""

    hash_value = 5381

    for char in string:

        # hash = 33 XOR ord(c)

        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)

    return hash_value % modulus



if __name__ == '__main__':

    # generate primes list to use as modulus

    primes = sieve(10000) # generate primes list to use as modulus



    modulus = pick_prime(primes, 1000)



    test_array = ["alpha","beta","gamma","delta","epsilon"]



    for string in test_array:

        hash_value = hash(string, modulus)

        print(f"Hash of {string} is {hash_value}")



# The fixes that I made is: 
# 1. The size of the res array has been corrected.
#     It should be `res = [False] * (limit + 1)` instead of `res = [False]`
# 2. The loop condition checking has been corrected to 
#       `while i*i <= limit:
#          j = 1
#          while j*j <= limit:`
#      as with other sieve algorithms, Sieve of Atkin works on the principle that non-prime numbers have factors, so it's sufficient to mark multiples 
#      only up to the square root.

# 3. Currently we are directly returning 'res' which is a boolean array but we must return the list of prime numbers, so a list of prime numbers has been constructed and returned.
#     primes = []
#     i = 2
#     while i <= limit:
#         if res[i]:
#             primes.append(i)
#         i += 1
#     return primes.
