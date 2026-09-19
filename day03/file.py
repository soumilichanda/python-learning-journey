# 1. Take user input for Name, College, and Branch
name = input("Enter Name: ")
college = input("Enter College: ")
branch = input("Enter Branch: ")

# 2. Store the details into 'notes.txt' using write ('w') mode
with open("notes.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"College: {college}\n")
    file.write(f"Branch: {branch}\n")

print("\n✅ Details saved to notes.txt successfully!\n")

# 3. Read and print the contents of 'notes.txt'
print("--- Reading from notes.txt ---")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)