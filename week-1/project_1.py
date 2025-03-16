P = input("Enter Prinicipal Amount (P): ")
R = input("Enter Annual Interest Rate (R in %): ")
T = input("Enter Time Period (T in years): ")

A = int(P) * (1 + (float(R)/ 100) * int(T))

print(f"Simple Interest: {A}")