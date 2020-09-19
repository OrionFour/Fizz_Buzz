fizz_buzz = [number if number % 3 and number % 5 else 'Buzz' if number % 3 else 'Fizz' if number % 5 else 'FizzBuzz' for number in range(1, 16)]
print(fizz_buzz)