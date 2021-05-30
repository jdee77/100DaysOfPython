def prime_checker(number):
    prime = True
    for i in range(2, int(number/2)):
        if number % 2 == 0:
            prime = False
            break
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")