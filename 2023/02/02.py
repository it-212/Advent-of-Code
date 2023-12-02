import os.path

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    file.close()
    return file_text

def getPossibleGames(input):
    bag = {"red" : 12,  "green" : 13, "blue" : 14}
    sum = 0
    for line in input:
        possible = True
        line = line[4:].strip()
        if(line == ""):
            continue
        game_id, games = line.split(": ")
        games = games.split(";")
        for game in games:
            rounds = game.strip().split(", ")
            for one_round in rounds:
                value, color = one_round.strip().split(" ")
                if(int(value) > bag[color]):
                    possible = False
                    break
        if(possible == True):
            sum += int(game_id)                  
    
    return sum


def getMinimalPossibleGames(input):    
    sum = 0
    for line in input:
        bag = {"red" : 0,  "green" : 0, "blue" : 0}
        line = line[4:].strip()
        if(line == ""):
            continue
        game_id, games = line.split(": ")
        games = games.split(";")
        for game in games:
            rounds = game.strip().split(", ")
            for one_round in rounds:
                value, color = one_round.strip().split(" ")
                if(int(value) > bag[color]):
                    bag[color] = int(value)
        
        game_power = 1
        for color, value in bag.items():
            game_power *= value
            
        sum += game_power
    
    return sum
                
def main():
    # input_file_name = "input_data_demo.txt"
    input_file_name = "input_data.txt"
    input = takeInputData(input_file_name)
    
    solution_part_one = getPossibleGames(input)
    print(f"Part one: {solution_part_one}")

    solution_part_two = getMinimalPossibleGames(input)
    print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()