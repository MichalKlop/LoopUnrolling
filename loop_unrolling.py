import time
import random
import sys


def generate_array(size: int) -> list[int]:
    """Generate array of given length with random integers from 1-10"""
    array = []
    while len(array) < size:
        array.append(random.randint(1, 10))
    return array


def f(array):
    i = 0
    s = 0
    while i < len(array):
        s += array[i]
        i += 1
    return s


def unroll4(array):
    i = 0
    acc1 = 0
    acc2 = 0
    acc3 = 0
    acc4 = 0
    while i < len(array) - 3:
        acc1 += array[i]
        acc2 += array[i+1]
        acc3 += array[i+2]
        acc4 += array[i+3]
        i += 4
    s = acc1 + acc2 + acc3 + acc4
    while i < len(array):
        s += array[i]
        i += 1
    return s


def unroll8(array):
    i = 0
    acc1 = 0
    acc2 = 0
    acc3 = 0
    acc4 = 0
    acc5 = 0
    acc6 = 0
    acc7 = 0
    acc8 = 0
    while i < len(array) - 7:
        acc1 += array[i]
        acc2 += array[i+1]
        acc3 += array[i+2]
        acc4 += array[i+3]
        acc5 += array[i+4]
        acc6 += array[i+5]
        acc7 += array[i+6]
        acc8 += array[i+7]
        i += 8
    s = acc1 + acc2 + acc3 + acc4 + acc5 + acc6 + acc7 + acc8
    while i < len(array):
        s += array[i]
        i += 1
    return s


def main():
    array_size = input("Input desired array size: ")
    while not array_size.isdigit() or not int(array_size) > 0:
        array_size = input("Error: Array size must be an integer greater than 0\n"
                           "Input desired array size: ")
    array = generate_array(int(array_size))

    loop_iterations = input("Input desired number of loop iterations: ")
    while not loop_iterations.isdigit() or not int(loop_iterations) > 0:
        loop_iterations = input("Error: Loop iterations must be an integer greater than 0\n"
                                "Input desired number of loop iterations: ")
    loop_iterations = int(loop_iterations)

    # Time it takes to sum values within array w/o unrolling
    start = time.time()
    for j in range(loop_iterations):
        f(array)
    end = time.time()
    print("f: ", end - start)

    # Time it takes to sum values within array w/ 4 way loop unrolling
    start = time.time()
    for j in range(1000):
        unroll4(array)
    end = time.time()
    print("unroll4: ", end - start)

    # Time it takes to sum values within array w/ 8 way loop unrolling
    start = time.time()
    for j in range(1000):
        unroll8(array)
    end = time.time()
    print("unroll8: ", end - start)

    repeat = input("Want to change array size or loop iterations? (yes/no): ")
    while repeat.lower() != "yes" and repeat.lower() != "no":
        repeat = input("Error: Expecting 'yes' or 'no'\n"
                       "Want to change array size or loop iterations? (yes/no): ")

    if repeat.lower() == 'yes':
        main()
    print("Exiting program")
    sys.exit()


if __name__ == "__main__":
    main()
