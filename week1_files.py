

with open('week1_files.txt', 'w') as file:
    file.write("Line 1: Hello, World!\n")
    file.write("Line 2: Welcome to Week 1 of the AI Bootcamp.\n")
    file.write("Line 3: Today, we will learn about file handling in Python.\n")
    file.write("Line 4: Let's get started!\n")

with open('week1_files.txt', 'r') as file:
    print(file.read())