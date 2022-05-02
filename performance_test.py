from recursive_floyd import recursivepaths
from imperative_floyd import imperativepaths
import datetime
import timeit

"""Performance tests using both brute force and timeit library
on both the imperative and recusrive implementation of Floyd's
algorithm.
"""

# Run performance tests on recursion using internal datetime
print("Recursion timing using brute force.")
start_time = datetime.datetime.now()
recursivepaths()
end_time = datetime.datetime.now()
print("Recursion brute force timing: " + str(end_time - start_time))

# Run performance tests on imperative using internal datetime
print("\n\nImperative timing using brute force.")
start_time = datetime.datetime.now()
imperativepaths()
end_time = datetime.datetime.now()
print("Imperative brute force timing: " + str(end_time - start_time))

# Run performance tests on recursion using timeit
print("\n\nRecusion timing using timeit library.")
print("Recursion timeit timing: " + str(timeit.timeit(
    setup="from recursive_floyd import recursivepaths",
    stmt="recursivepaths()",
    number=10)))

# Run performance tests on imperative using timeit
print("\n\nImperative timing using timeit library.")
print("Imperative timeit timing: " + str(timeit.timeit(
    setup="from imperative_floyd import imperativepaths",
    stmt="imperativepaths()",
    number=10)))
