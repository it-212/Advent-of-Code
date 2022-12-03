import os
import os.path
import sys

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    return file_text

def calculateCharPriority(char):
    char_priority = ord(char)
    if((char_priority - ord("a")) >= 0 and (char_priority - ord("a")) <= 26):
        return 1 + (char_priority - ord("a"))
    else:
        return 27 + (char_priority - ord("A"))

def calculatePriority(input_text):
    priority = 0

    for line in input_text:
        compartment_size = len(line)//2
        
        compartment_1 = line[:compartment_size]
        compartment_2 = line[compartment_size:]

        for char in compartment_1:
            if(char in compartment_2):
                priority += calculateCharPriority(char)
                break
    
    return priority

def findGroupBadge(input_text):
    priority = 0

    for i in range(0,len(input_text), 3):
        elf_1 = input_text[i]
        elf_2 = input_text[i+1]
        elf_3 = input_text[i+2]
        for char in elf_1:
            if(char in elf_2 and char in elf_3):
                priority += calculateCharPriority(char)
                break
        
    return priority

def main():
    # input_file_name = "input_data_demo.txt"
    input_file_name = "input_data.txt"
    input = takeInputData(input_file_name)
    

    solution_part_one = calculatePriority(input)
    print(f"Part one: {solution_part_one}")

    solution_part_two = findGroupBadge(input)
    print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()