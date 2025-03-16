P = input("Enter Prinicipal Amount (P): ")
R = input("Enter Annual Interest Rate (R in %): ")
T = input("Enter Time Period (T in years): ")
n = input("Enter Number of times interest is compounded per year: ")

A = int(P) * (1 + float(R)/ int(n)) ** (int(n) * int(T))

print(f"Compound Interest: {A}")