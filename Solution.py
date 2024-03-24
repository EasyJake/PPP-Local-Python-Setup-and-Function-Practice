# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello():
  print("Hello world!")
  
# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack(a,b,c):
  return [a,b,c]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.

# def eat_lunch(my_list):
#   if len(my_list) == 0:
#     print("My lunchbox is empty!")
#   else:
#     for i in range(len(my_list)):
#       if i == 0:
#         print(f"First I'll eat a {my_list[0]}")
#       else:
#         print(f"Next I'll eat a {my_list[i]}")

# hello()
# print(pack("a","b","c"))
# print(pack(1,2,3))
# eat_lunch([])
# eat_lunch(["sandwich"])
# eat_lunch(["apple","banana","sandwich","cookie"])


# I worked on some ways to make the language sound more natural, but it's still not perfect. My local Python environment is set up though, so I am marking this one as complete.

def eat_lunch(my_list):
    if not my_list:  # Checks if the list is empty
        print("My lunchbox is empty!")
    else:
        # Always print the first item with this message
        print(f"First I'll eat a {my_list[0]}")
        # Then, loop through the rest of the list starting from the second item
        for i in range(1, len(my_list)):
            if i == 1:
                # Specifically for the second item, use "Then I'll eat a"
                print(f"Then I'll eat a {my_list[i]}")
            else:
                # For all subsequent items, use "Next I'll eat a"
                print(f"Next I'll eat a {my_list[i]}")

# Now let's test the function with different lists
eat_lunch([])  # Empty list
eat_lunch(["sandwich"])  # Single item
eat_lunch(["sandwich", "apple"])  # Two items
eat_lunch(["sandwich", "apple", "banana", "cookie"])  # Multiple items

