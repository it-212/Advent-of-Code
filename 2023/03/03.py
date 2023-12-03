import os.path

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    file.close()
    
    new = []
    for t in file_text:
        line = t.strip()
        new.append(line)
    return new

def checkAdjacentSimbols(input, i, j, nums):
    pairs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
    
    for pair in pairs:
        a,b = pair
        if(i+a >= 0 and i+a < len(input) and j+b >= 0 and j+b < len(input[i])):
            check_char = input[i+a][j+b]
            if(check_char not in nums and check_char != "."):
                return True    
    return False

def getPartNumSum(input):
    nums = "0123456789"
    number = 0
    part_num = False  
    sum = 0
      
    for i in range(len(input)):
        line = input[i].strip() 
        for j in range(len(line)):
            char = line[j]
            if(j == 0):
                if(part_num == True):
                    part_num = False
                    sum += number
                number = 0
            if(char in nums):
                number = number*10 + int(char)
                if(number == 485):
                    print()
                check_adjacent = checkAdjacentSimbols(input, i, j, nums)
                if(check_adjacent == True):                    
                    part_num = True                
            else:
                if(number == 0):
                    continue            
                if(part_num == True):
                    part_num = False
                    sum += number
                    print(number)
                number = 0
        # print("SUMA ", sum)
    return sum


              
def main():
    # input_file_name = "input_data_demo.txt"
    input_file_name = "input_data.txt"
    input = takeInputData(input_file_name)
    
    solution_part_one = getPartNumSum(input)
    print(f"Part one: {solution_part_one}")

    # solution_part_two = getMinimalPossibleGames(input)
    # print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()