try:
    age = int(input("age: "))
    salary = 100000000
    oo = salary/age
    print(f"your age is {age}")
    print(f"oooo is {oo}")
except ValueError:
    print("Please enter a number not a text")
except ZeroDivisionError:
    print("Age Cannot be Zero")