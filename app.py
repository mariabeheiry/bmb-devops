def add_numbers(a,b):
    return a+b

def subtract_numbers(a,b):
    return a-b

def multiply_numbers(a,b):
    return a*b

def divide_numbers(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b

if __name__ == "__main__":
    print(add_numbers(1,2))
    print(subtract_numbers(3,2))
    print(multiply_numbers(3,2))
    print(divide_numbers(10,2))
    print(divide_numbers(10,0))