# Name: Case Buckmaster
# Lab: 4.16
# Description: Prints a triangle based on user input for height and what characters it's made of.

# Variables
# Input for the character the triangle will be composed of.
triangle_char = input("Enter a character:\n") + " "

# Input for the height of the triangle.
triangle_height = int(input("Enter triangle height:\n\n"))

# Iterate based on the height input given to build the triangle.
for row in range(1, triangle_height + 1):
    print((triangle_char * row))
