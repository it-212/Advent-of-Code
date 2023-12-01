import os
import os.path
import sys

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    return file_text

def main():
    input_file_name = "input_data_demo.txt"
    # input_file_name = "input_data.txt"
    # input = takeInputData(input_file_name)
    # elves = calculateCalories(input)

    # solution_part_one = calculateMax(elves)
    # print(f"Part one: {solution_part_one}")

    # solution_part_two = calculateThreeMax(elves)
    # print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()