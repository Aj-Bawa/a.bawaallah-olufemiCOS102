PMT = input("Enter Payment amount for annuity: ")
R = input("Enter Annual Interest Rate (R in %): ")
T = input("Enter Time Period (T in years): ")
n = input("Enter Number of times interest is compounded per year: ")

A = int(PMT) * ((1 + (float(R)/ int(n)) ** int(n) * int(T)) - 1) / (float(R) / int(T))

print(f"Annuity Plan: {A}")