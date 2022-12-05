import os
import os.path
import sys

def takeInputData(file_name):
    file = open(file_name, "r")
    file_text = file.readlines()
    return file_text

class Move:
    def __init__(self, number, stack_num_1, stack_num_2):
        self.from_stack = stack_num_1
        self.to_stack = stack_num_2
        self.number_of_boxes = number

    def moveBoxes(self, box_stacks):
        for i in range(self.number_of_boxes):
            removed_box = box_stacks[self.from_stack].pop()
            box_stacks[self.to_stack].append(removed_box)
        return box_stacks

    def moveBoxes2(self, box_stacks):
        removed_boxes = []
        for i in range(self.number_of_boxes):
            if(box_stacks[self.from_stack] != []):
                removed_boxes.append(box_stacks[self.from_stack].pop())
        removed_boxes.reverse()
        for box in removed_boxes:
            box_stacks[self.to_stack].append(box)
        return box_stacks


    def __str__(self):
        return str(self.number_of_boxes) + " " + str(self.from_stack) + " " + str(self.to_stack) 


def getStacks(stack_text):
    stacks = []

    for j in range(len(stack_text[0])):
        box_stack = []
        for i in range(len(stack_text)-1):
            if(j >= len(stack_text[i])):
                break
            if(stack_text[i][j] == "[" or stack_text[i][j] == "]" or stack_text[i][j] == "\n"):
                break
            if(stack_text[i][j] != "" and stack_text[i][j] != " "):
                box_stack.append(stack_text[i][j])
        if(box_stack != []):
            box_stack.reverse()
            stacks.append(box_stack)

    return stacks

def getMoves(moves_text):
    moves = []

    for line in moves_text:
        separate_line = line.strip().split(" ")
        number = separate_line[1]
        stack_from = separate_line[3]
        stack_to = separate_line[5]
        move = Move(int(number), int(stack_from)-1, int(stack_to)-1)
        moves.append(move)

    return moves

def doMoves(stacks, moves):
    for move in moves:
        # print(move)
        stacks = move.moveBoxes(stacks)
        # print(stacks)
    
    return stacks

def doMoves2(stacks, moves):
    for move in moves:
        stacks = move.moveBoxes2(stacks)
    
    return stacks

def solution(input_text, partOne):

    stack_text = []
    moves_text = []
    break_line = False

    for line in input_text:
        if(line == "\n"):
            break_line = True
        elif(break_line == False):
            stack_text.append(line)
        else:
            moves_text.append(line)

    stacks = getStacks(stack_text)
    moves = getMoves(moves_text)

    
    if(partOne == True):
        new_stacks = doMoves(stacks, moves)
    else:
        new_stacks = doMoves2(stacks, moves)

    top_boxes = ""
    for stack in new_stacks:
        top_boxes+=stack[-1]

    return top_boxes

def main():
    # input_file_name = "input_data_demo.txt"
    input_file_name = "input_data.txt"
    input = takeInputData(input_file_name) 

    solution_part_one = solution(input, True)
    print(f"Part one: {solution_part_one}")

    solution_part_two = solution(input, False)
    print(f"Part two: {solution_part_two}")


if __name__ == '__main__':
    main()