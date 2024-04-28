import numpy as np
import time
def sort_indices_without_numpy(lst):
    # Check if the input list is empty or not numerical
    if not lst:
        raise ValueError("Input list is empty")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input list contains non-numerical elements")

    # Enumerate the elements along with their indices
    indexed_list = list(enumerate(lst))

    # Sort the indexed list based on the values
    sorted_indexed_list = sorted(indexed_list, key=lambda x: x[1])

    # Extract the indices after sorting
    sorted_indices = [index for index, _ in sorted_indexed_list]

    return sorted_indices

def sort_indices_with_numpy(lst):
    # Check if the input list is empty or not numerical
    if not lst:
        raise ValueError("Input list is empty")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input list contains non-numerical elements")

    # Convert the list to a NumPy array
    arr = np.array(lst)

    # Get the indices of the sorted elements
    sorted_indices = np.argsort(arr)

    return sorted_indices

# Test the functions
list1 = [23, 104, 5, 190, 8, 7, -3]
list2 = []
list3 = np.random.randint(0, 1000000, 1000000).tolist()

try:
    start_time = time.time()
    indices1 = sort_indices_without_numpy(list1)
    print("Sorted indices without NumPy for list 1:", indices1)
    print("Time taken without NumPy for list1:", time.time() - start_time, "seconds")
except ValueError as e:
    print(e)

try:
    start_time = time.time()
    indices1 = sort_indices_with_numpy(list1)
    print("Sorted indices with NumPy for list 1:", indices1)
    print("Time taken with NumPy for list1:", time.time() - start_time, "seconds")
except ValueError as e:
    print(e)

try:
    start_time = time.time()
    indices2 = sort_indices_without_numpy(list2)
    print("Sorted indices without NumPy for list 2:", indices2)
    print("Time taken without NumPy for list2:", time.time() - start_time, "seconds")
except ValueError as e:
    print(e)

try:
    start_time = time.time()
    indices2 = sort_indices_with_numpy(list2)
    print("Sorted indices with NumPy for list 2:", indices2)
    print("Time taken with NumPy for list2:", time.time() - start_time, "seconds")
except ValueError as e:
    print(e)

try:
    start_time = time.time()
    indices3 = sort_indices_without_numpy(list3)
    #print("Sorted indices without NumPy for list 3:", indices3)
    print("Time taken without NumPy for list3:", time.time() - start_time, "seconds")
except ValueError as e:
    print(e)

try:
    start_time = time.time()
    indices3 = sort_indices_with_numpy(list3)
    #print("Sorted indices with NumPy for list 3:", indices3)
    print("Time taken with NumPy for list3:", time.time() - start_time, "seconds")
except ValueError as e:
    print(e)


