# Write a program that repeatedly prompts a user for integer numbers until
#  the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it
#  with a try/except and put out an appropriate message and ignore the number.

largest = None
smallest = None
numbers = list()

# Kullanicidan sayilari al -----------
while True:
    numInp = input("Enter a number: ")
    if numInp == "done" : break

    try:
        num = float(numInp)
    except:
        print("Invalid input")
        continue

    numbers.append(num)
# -------------------------------------

for n in numbers:

    if largest is None:
        largest = n
    if smallest is None:
        smallest = n

    if n < smallest :
    	smallest = n
    if n > largest :
    	largest = n

print("Maximum", largest)
print("Minimum ", smallest)
