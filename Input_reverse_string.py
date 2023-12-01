
def reverse_string(input_string):
    return input_string[::-1]

# Get user input
user_input = input("Enter a string: ")

# Reverse the string
reversed_user_input = reverse_string(user_input)

# Output
print("Original String:", user_input)
print("Reversed String:", reversed_user_input)
