#fizzbuzz algorithm

#takes inputs, returnds differnet results
#divisible by 3, return Fizz
#divisible by 5, return buzz
#divisible by both 3 and 5, return FizzBuzz
#any other number return the same number


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0): 
        return "FizzBuzz"#dont need an elif
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input#we dont need an else statement
    
    
print(fizz_buzz(2))