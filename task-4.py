talabalar = [("Ali", 85), ("Malika", 95), ("Vali", 78)]


ozgargan = sorted(talabalar, key=lambda x: x[1], reverse=True)
print(ozgargan)
