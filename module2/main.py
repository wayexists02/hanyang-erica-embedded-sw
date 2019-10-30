#!/usr/bin/env python3

from algorithm import *
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import TouchSensor

def main():
    begin, end, board = scan()
    
    for row in board:
        for col in row:
            if col is None:
                print(0, end="")
            elif col is begin:
                print(2, end='')
            elif col is end:
                print(3, end='')
            else:
                print(1, end='')
        print('')

    path = bfs(begin, end)
    for node in path:
        x = node.x
        y = node.y
        print(x, y)
    print("")

    print("wait for pressed")
    touch = TouchSensor(INPUT_4)
    touch.wait_for_pressed()
    print("go")

    follow_path(path)

def test():
    with open("z.txt", "r") as f:
        lines = f.readlines()

    begin, end, board = scan_test(lines)

    for row in board:
        line = ""
        for col in row:
            if col is None:
                line = line + "0"
            elif col is begin:
                line = line + "2"
            elif col is end:
                line = line + "3"
            else:
                line = line + "1"
        print(line)

    path = bfs(begin, end)

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    for node in path:
        print(node.x, node.y)
        board[node.y][node.x] = 1

    print("")
    for l in board:
        print(l)


if __name__ == "__main__":
    main()
    #test()
