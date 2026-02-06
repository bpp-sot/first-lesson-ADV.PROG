name = input("Enter your name: ")
print(f"Welcome, {name}!")

with open("greeting.txt", "w") as f:
    f.write(f"User {name} accessed this environment.\n")

print("Greeting saved to file.")
