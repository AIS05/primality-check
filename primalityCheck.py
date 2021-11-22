from random import randint

# acc, is the number of rounds of testing to perform
# it determines the accuracy of the test (higher = better)
acc = 7


def isPrime(n, k) -> bool:
    """
    This function checks if a number is prime or not.
    It uses Miller Rabin Primality Test.
    https://en.wikipedia.org/wiki/Miller–Rabin_primality_test

    It is very efficient so it is suitable for checking
    primality of very big numbers.

    I used the python implementation of this test made by Ayrx
    https://gist.github.com/Ayrx/5884790

    Parameters:

    n, The number which will be checked for primality.

    k, The number of rounds of testing to perform - determines the accuracy.

    Returns:

    boolean, True if n is prime, False if not
    """
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = randint(2, n - 1)
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


def checkUserInput() -> None:
    """
    This function takes user input and check it for primality,
    using the function above.

    No parameters required

    Does not return any values
    """
    while True:
        try:
            x = int(input("Please input a natural number > "))
            if x >= 0:
                break
            print("The input can't be negative.")

        except ValueError:
            print("The input must be an integer.")

    print("")
    print(f"'{x}' is prime.") if isPrime(x, acc) else print(f"'{x}' is NOT prime.")


if __name__ == "__main__":
    checkUserInput()
