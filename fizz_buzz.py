def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    return number


for i in range(1, 31):
    print(fizz_buzz(i))

