import os
import os.path
import sys

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    return file_text

def getRange(elf):
    range = []
    bottom = elf.split("-")[0]
    top = elf.split("-")[1]

    range.append(int(bottom))
    range.append(int(top))

    return range

def fullyContains(input_text):
    counter = 0

    for line in input_text:
        first_elf = line.strip().split(",")[0]
        second_elf = line.strip().split(",")[1]

        first_range = getRange(first_elf)
        second_range = getRange(second_elf)

        if(first_range[0] <= second_range[0] and first_range[1] >= second_range[1] or
           first_range[0] >= second_range[0] and first_range[1] <= second_range[1] ):
           counter += 1
    
    return counter

def overlap(input_text):
    counter = 0

    for line in input_text:
        first_elf = line.strip().split(",")[0]
        second_elf = line.strip().split(",")[1]

        first_range = getRange(first_elf)
        second_range = getRange(second_elf)

        if(first_range[0] <= second_range[0] and first_range[1] >= second_range[1] or
           first_range[0] >= second_range[0] and first_range[1] <= second_range[1] or
           first_range[0] <= second_range[0] and first_range[1] >= second_range[0] or
           first_range[0] <= second_range[1] and first_range[1] >= second_range[1] or
           second_range[0] <= first_range[0] and second_range[1] >= first_range[0] or
           second_range[0] <= first_range[1] and second_range[1] >= first_range[1]):
           counter += 1




    return counter


def main():
    # input_file_name = "input_data_demo.txt"
    input_file_name = "input_data.txt"
    input = takeInputData(input_file_name)
    

    solution_part_one = fullyContains(input)
    print(f"Part one: {solution_part_one}")

    solution_part_two = overlap(input)
    print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()