def is_prime(num):
    if num<= 1:
        return False
    for i in range (2, int (num**0.5)+1) :
        if num % i == 0 :
         return False
    return True


while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")
if is_prime(number):
         print("The number is a prime number .")
else:
         print("The number is not a prime number but a composite one .")
