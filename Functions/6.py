#Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

sample_input = 17
if is_prime(sample_input):
    print(f"{sample_input} is a prime number.")
else:
    print(f"{sample_input} is not a prime number.")