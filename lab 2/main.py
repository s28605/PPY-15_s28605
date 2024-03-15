# 8
# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = [int(i) for i in input_numbers.split(' ')]
numbers_tuple = tuple(numbers_list)

# Manipulate List
numbers_list.append(10)

# Attempt to Modify Tuple (this will raise an error)
try:
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
f_set = {1, 2, 3, 4, 5}
s_set = {1, 2, 6, 8, 5}
# Union
set_union = f_set.union(s_set)
# Intersection
set_intersection = f_set.intersection(s_set)
# Difference
set_difference = f_set.difference(s_set)

# Dictionary Operations
numbers_dict = {"5": 25, "2": 4, "8": 64, "1": 1, "9": 81}
print("Original Dictionary:", numbers_dict)
# Add a new key-value pair
numbers_dict["3"] = 56
# Delete an existing key-value pair
del numbers_dict["5"]

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
set_to_list = list(set_union)
set_to_tuple = tuple(set_union)
dict_to_list = list(numbers_dict)
dict_to_tuple = tuple(numbers_dict)
dict_to_set = set(numbers_dict)

student_number = input("Enter your student number: ")

# Write Output to File like this:
with open('output.txt', 'w') as file:
    file.write("Student Number: " + student_number + "\n")
    file.write("Original List: " + str(numbers_list) + "\n")
    file.write("Original Tuple: " + str(numbers_tuple) + "\n")
    file.write("Original Dictionary: " + str(numbers_dict) + "\n")

    file.write("Manipulated List: " + str(numbers_list) + "\n")
    file.write("Manipulated Tuple: " + str(numbers_tuple) + "\n")
    file.write("Union of Set: " + str(set_union) + "\n")
    file.write("Intersection of Set: " + str(set_intersection) + "\n")
    file.write("Difference of Set: " + str(set_difference) + "\n")
    file.write("Updated Dictionary: " + str(numbers_dict) + "\n")

    file.write("List to Tuple: " + str(list_to_tuple) + "\n")
    file.write("List to Set: " + str(list_to_set) + "\n")
    file.write("Tuple to List: " + str(tuple_to_list) + "\n")
    file.write("Tuple to Set: " + str(tuple_to_set) + "\n")
    file.write("Set to List: " + str(set_to_list) + "\n")
    file.write("Set to Tuple: " + str(set_to_tuple) + "\n")
    file.write("Dictionary to List: " + str(dict_to_list) + "\n")
    file.write("Dictionary to Tuple: " + str(dict_to_tuple) + "\n")
    file.write("Dictionary to Set: " + str(dict_to_set) + "\n")

# print "Content of the file:"

# Perform Operations on File:
#   Count the number of lines in the file
with open('output.txt', 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)
    print(f"Number of lines in the file: {num_lines}")

#   Count the number of integers in the file
#   Add all integers in the file (sum).
def extract_integers(line):
    return [int(item) for item in line if item.isdigit()]

integer_count = 0
total_sum = 0

with open('output.txt', 'r') as file:
    for line in file:
        numbers = extract_integers(line)
        integer_count += len(numbers)
        total_sum += sum(numbers)

print(f"Total number of integers in the file: {integer_count}")
print(f"Sum of all integers in the file: {total_sum}")
#   Modify the content of the file
with open('output.txt', 'a') as file:
    file.write("This is a new line added to the file.\n")


# 9
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def extract_integer_from_line(line):
    parts = line.split(":")
    if len(parts) > 1:
        try:
            return int(parts[1].strip())
        except ValueError:
            return None
    return None

try:
    with open('output.txt', 'r') as file:
        lines = file.readlines()

    integers = [extract_integer_from_line(line) for line in lines]
    integers = [num for num in integers if num is not None]

    if not integers:
        raise ValueError("No integers found in the file.")

    largest_int = max(integers)

    prime_numbers = [i for i in range(2, largest_int + 1) if is_prime(i)]

    sum_of_primes = sum(prime_numbers)
    largest_prime = max(prime_numbers) if prime_numbers else None
    smallest_prime = min(prime_numbers) if prime_numbers else None
    is_largest_int_prime = is_prime(largest_int)

    with open('prime_numbers.txt', 'w') as file:
        file.write(f"List of prime numbers up to {largest_int}: {prime_numbers}\n")
        file.write(f"Sum of prime numbers: {sum_of_primes}\n")
        file.write(f"Largest prime number: {largest_prime}\n")
        file.write(f"Smallest prime number: {smallest_prime}\n")
        file.write(f"Is the largest integer ({largest_int}) prime: {is_largest_int_prime}\n")

    print("Prime number analysis completed successfully.")

except FileNotFoundError:
    print("Error: 'output.txt' file not found.")
except ValueError as e:
    print(f"Error: {e}")
