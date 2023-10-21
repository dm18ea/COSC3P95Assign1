# python code for question 2
# from terminal be in the correct working directory as question2.py
# ensure python3 is installed (up-to-date) before running
# invoke "python3 question2.py"
# this code will initially produce 10 iterations of random list generation
# which will be organized in ascending order using insertion sort

# import and initialize random instance with given student number seed
import random
seed = 5550
random.seed(seed)
print("Seed: " + str(seed) + "\n")


# procedure to replicate random test case generation with insertion sort algorithm
def testing():
    total_tests = 10    # total_tests can be modified to desired number of tests
    for x in range(1, total_tests):
        insertion_algo()
        print("ITERATION PASSED")

    print("\ntesting finished")


# insertion sort procedure to organize list produced from random_test_gen()
def insertion_algo():
    arg = random_test_gen()     # copies random list to arg variable

    print("Executing insertion sort")
    # loop to iterate through each item in list
    for i in range(1, len(arg)):
        key = arg[i]    # copy value of current position to variable key
        j = i - 1       # copy position of key'd value to variable j

        # loop through sorted list until end reached or key > sorted position in list
        while j >= 0 and arg[j] > key:
            arg[j + 1] = arg[j]     # shifts value of sorted item right 1 cell
            j -= 1      # decrement to smaller item in list

        arg[j + 1] = key        # position for key placed in correct position

    print(arg)


# function to generate random list of integers ranging from mini-maxi
def random_test_gen():
    mini = 1
    maxi = 20
    length = random.randint(mini, maxi)

    print("\nInitializing list of " + str(length) + " items")
    array = [0]*length
    print(array)

    print("Filled with random integers from 1-" + str(maxi))
    for x in range(length):
        array[x] = random.randint(mini, maxi)

    print(array)
    return array


# execution of random generation and insertion sort algorithm
testing()

