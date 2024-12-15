# Advent of Code Day 13-1
# Button A: 94x + 22y = Distance X 8400
# Buton B: 34x + 67y = Distance y 5400
# 6298x 1474y = 562800
# 748x + 1474y =118800
# 5550x = 444000
# x = 80
# y = 5400-2720/67
# y = 40

# 
#
import re

prize_lines = []

def solve_prize(prize_number: int, prizes: list):
    print(f"Solution {prize_number}")
    button_a = prizes[prize_number]
    button_b = prizes[prize_number+1]
    prize = prizes[prize_number+2]

    button_a = button_a.split(",")
    button_a_x = int(button_a[0].split("+")[1])
    button_a_y = int(button_a[1].split("+")[1].strip("\n"))
    
    button_b = button_b.split(",")
    button_b_x = int(button_b[0].split("+")[1])
    button_b_y = int(button_b[1].split("+")[1].strip("\n"))

    prize = prize.split(",")
    prize_x = int(prize[0].split("=")[1])
    prize_y = int(prize[1].split("=")[1].strip("\n"))

    print(f"Button A x:{button_a_x} y:{button_a_y}")
    print(f"Button B x:{button_b_x} y:{button_b_y}")
    print(f"Prize x:{prize_x} y:{prize_y}")

    ax = button_a_x*button_b_y
    # ay = button_a_y*button_b_y
    bx = button_b_x * button_a_y
    aprize = prize_x * button_b_y
    bprize = prize_y * button_a_y
    x_solution = (aprize -bprize)/(ax - bx)
    print(f"solution for X: {x_solution}")

with open("input13-1.txt") as f:
    for line in f:
        prize_lines.append(line)

for idx,prize_line in enumerate(prize_lines):
    if "Button A" in prize_line:
        solve_prize(idx, prize_lines)
