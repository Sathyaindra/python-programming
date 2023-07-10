numbers = input("Enter the list of numbers (separated by spaces): ").split()

# Convert the numbers to integers
numbers = [int(x) for x in numbers]

try:
    # Get the index from the user
    index = int(input("Enter the index: "))
    
    # Access the element at the given index and print it
    element = numbers[index]
    print("Element at index", index, ":", element)

except IndexError:
    print("Error: Index is out of range")
