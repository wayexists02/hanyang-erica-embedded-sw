#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2
from ev3dev2.motor import MoveTank, MediumMotor, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

OFFSET = 10


class Node():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.is_visited = False
        self.index = 1000
        
    def add_neighbor(self, node):
        self.neighbors.append(node)
        node.neighbors.append(self)
        
        
def scan():
    board = []
    final_line = False
    
    color_sensor = ColorSensor(INPUT_2)
    sensor_motor = MediumMotor(OUTPUT_D)
    tank = MoveTank(OUTPUT_B, OUTPUT_C)
    
    begin_node = None
    end_node = None

    
    row_num = 0
    while not final_line:
        row = []
        
        for col_num in range(10):
            # input("row: %d, col: %d" % (row_num, col_num))
            node = Node(col_num, row_num)
            
            r, g, b = color_sensor.rgb
            cv = color_sensor.color
            print(r, g, b)

            if r < 50 and g >= 80 and b < 100:
                begin_node = node
            elif r >= 80 and g < 70 and b < 70:
                if row_num >= 1 and board[row_num - 1][col_num] is not None:
                    board[row_num - 1][col_num].add_neighbor(node)
                if col_num >= 1 and row[col_num - 1] is not None:
                    row[col_num - 1].add_neighbor(node)
                end_node = node
                final_line = True
            elif r > 100 and g > 100 and b > 100:
                if row_num >= 1 and board[row_num - 1][col_num] is not None:
                    board[row_num - 1][col_num].add_neighbor(node)
                if col_num >= 1 and row[col_num - 1] is not None:
                    row[col_num - 1].add_neighbor(node)
            else:
                node = None
                
            row.append(node)
            sleep(0.1)
            
            #TODO: move sensor here
            if col_num < 9:
                sensor_motor.on_for_degrees(20, 55)
                sleep(0.1)
        
        board.append(row)
        row_num += 1
        tank.on_for_degrees(10, 10, 38)
        sleep(0.1)
        sensor_motor.on_for_degrees(-20, 55*9)
        
    return begin_node, end_node, board


def scan_test(test_board):
    board = []

    begin_node = None
    end_node = None

    i = 0
    for line in test_board:
        row = []

        j = 0
        for c in line:
            node = Node(j, i)
            c = int(c)

            if c == 2:
                begin_node = node
            elif c == 3:
                if i >= 1 and board[i-1][j] is not None:
                    board[i - 1][j].add_neighbor(node)
                if j >= 1 and row[j - 1] is not None:
                    row[j - 1].add_neighbor(node)
                end_node = node
            elif c == 1:
                if i >= 1 and board[i-1][j] is not None:
                    board[i - 1][j].add_neighbor(node)
                if j >= 1 and row[j - 1] is not None:
                    row[j - 1].add_neighbor(node)

            else:
                node = None

            row.append(node)
            j += 1

            if j == 10:
                break

        board.append(row)
        i += 1

    return begin_node, end_node, board

        
def bfs(begin, end):
    children = [begin]
    
    begin.index = 0
    
    while len(children) > 0:
        node = children.pop(0)
        node.is_visited = True
        
        for neighbor in node.neighbors:
            if not neighbor.is_visited:
                neighbor.index = node.index + 1
                children.append(neighbor)
        
    node = end
    path = [end]
    
    while node is not begin:
        find = False
        for neighbor in node.neighbors:
            if neighbor.index == node.index - 1:
                node = neighbor
                path.append(node)
                find =True
                break

        if find is False:
            print("Cannot connect from begin to end")
            for n in path:
                print(n.x, n.y)

            return None
            
    path.reverse()
    return path


def follow_path(path):
    current_x = 0
    current_y = 0
    
    sensor_motor = MediumMotor(OUTPUT_D)
    tank = MoveTank(OUTPUT_B, OUTPUT_C)

    print("Length of path: " + str(len(path)))

    y_off = path[-1].y - path[0].y + 1
    tank.on_for_degrees(-10, -10, 38*y_off)

    i = 0
    for p in path:
        print(str(i) + "'th: " + str(current_x), str(current_y))

        x_off = p.x - current_x
        y_off = p.y - current_y

        if x_off > 0:
            sensor_motor.on_for_degrees(20, 55)
        elif x_off < 0:
            sensor_motor.on_for_degrees(-20, 55)

        if y_off > 0:
            tank.on_for_degrees(10, 10, 38)
        elif y_off < 0:
            tank.on_for_degrees(-10, -10, 38)

        current_x = p.x
        current_y = p.y
        i += 1

