# Input names and ages
name1 = input("Enter first name: ")
age1 = int(input("Enter first age: "))
name2 = input("Enter second name: ")
age2 = int(input("Enter second age: "))

# Swap ages
age1, age2 = age2, age1

# Display results
print(f"{name1} is now {age1} years old.")
print(f"{name2} is now {age2} years old.")
