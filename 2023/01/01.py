import os.path

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    file.close()
    return file_text

def calculateSum(input):
    numbers = "0123456789"
    sum = 0
    for line in input:
        first_number = ""
        last_number = ""
        for letter in line:
            if(letter in numbers):
                if(first_number == ""):
                    first_number = letter
                last_number = letter
        if(first_number == ""):
            continue
        sum += (int(first_number)*10 + int(last_number))

    return sum
 
def calculateSum2(input):
    sum = 0
    numbers = "0123456789"
    numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    new_input = []
    
    
    for line in input:
        new_line = line
        added_chars = 0
        for k in range(len(line)):            
            for i in range(len(numbers_str)):
                num = numbers_str[i]
                if(num[0] != new_line[k+added_chars]):
                    continue            
                if(new_line[k+added_chars:k+added_chars+len(num)] == num):
                    new_line = new_line[:k+added_chars] + str(i+1) + new_line[k+added_chars:]
                    added_chars += 1
                    k += 2
                    break
                    
        new_input.append(new_line)
        
    sum = calculateSum(new_input)
    
    return sum
                
def main():
    # input_file_name = "input_data_demo.txt"
    input_file_name = "input_data.txt"
    input = takeInputData(input_file_name)
    solution_part_one = calculateSum(input)
    print(f"Part one: {solution_part_one}")

    solution_part_two = calculateSum2(input)
    print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()