import os
import os.path
import sys

global opponent_plays
opponent_plays = {"A": "Rock", "B": "Paper", "C": "Scissors"}

global i_play
i_play = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

global game_outcome_win
game_outcome_win = {"Rock" : "Y", "Paper": "Z", "Scissors": "X"}

global game_outcome_draw
game_outcome_draw = {"Rock" : "X", "Paper": "Y", "Scissors": "Z"}

global game_outcome_lose
game_outcome_lose = {"Rock" : "Z", "Paper": "X", "Scissors": "Y"}

global my_points
my_points = {"X": 1, "Y": 2, "Z": 3}

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    return file_text

def calculateRoundOutcome(opponents_move, my_move):
    if(opponents_move == my_move):
        return 3
    elif(opponents_move == "Rock" and my_move == "Paper" or 
        opponents_move == "Paper" and my_move == "Scissors" or
        opponents_move == "Scissors" and my_move == "Rock"):
        return 6
    return 0

def calculateScore(input_text):
    global opponent_plays, i_play, my_points
    score = 0

    for line in input_text:
        round_score = 0
        opponents_move_letter = line.strip().split(" ")[0]
        my_move_letter = line.strip().split(" ")[1]

        opponents_move = opponent_plays[opponents_move_letter]
        my_move = i_play[my_move_letter]

        round_score += calculateRoundOutcome(opponents_move, my_move)
        round_score += my_points[my_move_letter]

        score += round_score

    return score


def calculateScorePart2(input_text):
    global opponent_plays, game_outcome_win, game_outcome_draw, game_outcome_lose, my_points
    score = 0
    
    for line in input_text:
        round_score = 0
        opponents_move_letter = line.strip().split(" ")[0]
        opponents_move = opponent_plays[opponents_move_letter]

        game = line.strip().split(" ")[1]


        if(game == "X"): #I lose
            i_play = game_outcome_lose[opponents_move]
            round_score += 0
        elif(game == "Z"): #I win
            i_play = game_outcome_win[opponents_move]
            round_score += 6
        else:
            i_play = game_outcome_draw[opponents_move]
            round_score += 3

        round_score += my_points[i_play]
        score += round_score

    return score

def main():
    # input_file_name = "input_data_demo.txt"
    input_file_name = "input_data.txt"
    input = takeInputData(input_file_name)
    

    solution_part_one = calculateScore(input)
    print(f"Part one: {solution_part_one}")

    solution_part_two = calculateScorePart2(input)
    print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()