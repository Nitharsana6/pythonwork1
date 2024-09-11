#Q1
a=6
result= "a is Even number" if a % 2 == 0 else "a is a Odd number"

print(result)  


#Q2
def check_age_category(age):
    if age < 18:
        return "Minor"
    elif 18 <= age <= 64:
        return "Adult"
    else:
        return "Senior"

print(check_age_category(25))  


#Q3
def temperature_advice(temp):
    if temp > 30:
        return "Hot"
    elif 15 <= temp <= 30:
        return "Warm"
    else:
        return "Cold"

print(temperature_advice(20))  


#Q4
def evaluate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(evaluate_grade(85))  


#Q5
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))  


#Q6
def print_multiples(n):
    for i in range(1, 11):
        print(n * i)

print_multiples(3)  


#Q7
def reverse_string(string):
    return string[::-1]

print(reverse_string("hello")) 


#Q8
def count_vowels(string):
    vowels = 'aeiou'
    count = sum(1 for char in string.lower() if char in vowels)
    return count

print(count_vowels("hello world"))  


#Q9
def countdown(n):
    while n > 0:
        print(n)
        n -= 1

countdown(5)  


#Q10
import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    while True:
        guess = int(input("Guess the number: ")) 
        if guess == number_to_guess:
            print("Congratulations! You guessed the number.")
            break
        elif guess < number_to_guess:
            print("Try a higher number.")
        else:
            print("Try a lower number.")




#Q11
def calculate_factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(calculate_factorial(5))  


#Q12
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci_sequence(10)  


#Q13
def to_uppercase(string):
    return string.upper()

print(to_uppercase("hello world"))  


#Q14
def square_number(n):
    return n ** 2

print(square_number(4)) 


#Q15
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("madam"))  


#Q16
def find_maximum(numbers):
    return max(numbers)

print(find_maximum([1, 2, 3, 4, 5]))  
