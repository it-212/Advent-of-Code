import os.path

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    file.close()
    return file_text

def getProduct(input):
    
    times = input[0][10:].strip()
    distances = input[1][10:].strip()
    
    while("  " in times):
        times = times.replace("  ", " ")
    
    while("  " in distances):
        distances = distances.replace("  ", " ")
    
    times = times.split(" ")
    distances = distances.split(" ")
    
    product = 1
    
    for i in range(len(times)):
        beats = numberOfWaysToBeatARecord(int(times[i]), int(distances[i]))
        product *= beats

    return product

def numberOfWaysToBeatARecord(time, max_record):
    num = 0
    
    for x in range(time):
        #holding for x seconds
        #if im holding for x seconds, i have time - x time left
        remainder_time = time - x
        if(x*remainder_time>max_record):
            num+=1
    return num
            
def getProductForOne(input):            
    times = input[0][10:].strip()
    distances = input[1][10:].strip()
    
    while("  " in times):
        times = times.replace(" ", "")
    
    while("  " in distances):
        distances = distances.replace(" ", "")
    
    sol = numberOfWaysToBeatARecord(int(times), int(distances))
    
    return sol

                
def main():
    # input_file_name = "input_data_demo.txt"
    input_file_name = "input_data.txt"
    input = takeInputData(input_file_name)
    
    solution_part_one = getProduct(input)
    print(f"Part one: {solution_part_one}")

    solution_part_two = getProductForOne(input)
    print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()