import os
import os.path
import sys

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    return file_text
        
def calculateCalories(input_text):
    elves = []
    calories = 0
    for line in input_text:
        if(line == '' or line == '\n'):
            elves.append(calories)
            calories = 0
        else:
            calories += int(line.strip())

    return elves

def calculateMax(elves):
    max = 0
    for elf in elves:
        if(elf > max):
            max = elf
    return max

def calculateThreeMax(elves):
    max = [0, 0, 0]
    for elf in elves:
        if(elf > max[0]): 
            max[2] = max[1]
            max[1] = max[0]   
            max[0] = elf
        elif(elf > max[1]):
            max[2] = max[1]
            max[1] = elf
        elif(elf > max[2]):
            max[2] = elf
    return max[0]+max[1]+max[2]

def main():
    input_file_name = "input_data.txt"
    # input_file_name = "input_data.txt"
    input = takeInputData(input_file_name)
    elves = calculateCalories(input)

    solution_part_one = calculateMax(elves)
    print(f"Part one: {solution_part_one}")

    solution_part_two = calculateThreeMax(elves)
    print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()