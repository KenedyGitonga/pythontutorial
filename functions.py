def ken():
    print("Hello there,  welcome to function session class")

# calling a function
ken()

# adding two numbers
def add():
    num=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print(f"sum of {num} and {num2} is {num + num2}")


def check_odd_even():
    number=int(input("Enter a number:"))
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")