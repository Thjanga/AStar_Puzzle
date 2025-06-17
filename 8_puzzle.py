import cv2
import random
import matplotlib.pyplot as plt
import pyautogui
import numpy as np
import copy

start1 = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
goal = [['1', '2', '3'], ['4', '5', '6'], ['8', '7', '0']]
oper = ['up', 'down', 'right', 'left']

def checkZero(puzzle):
    x, y = 0, 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == '0':
                x, y = i, j
    return x, y

def movePuzzle(puzzle, x, y, oper):
    global cur
    if(oper == 'up'):
        if(x - 1 < 0):
            return None
        else:
            tmp = puzzle[x][y]
            puzzle[x][y] = puzzle[x-1][y]
            puzzle[x-1][y] = tmp

            return puzzle

    elif(oper == 'down'):
        if (x + 1 >= 3):
            return None
        else:
            tmp = puzzle[x][y]
            puzzle[x][y] = puzzle[x + 1][y]
            puzzle[x + 1][y] = tmp

            return puzzle

    elif(oper == 'right'):
        if (y + 1 >= 3):
            return None
        else:
            tmp = puzzle[x][y]
            puzzle[x][y] = puzzle[x][y + 1]
            puzzle[x][y + 1] = tmp

            return puzzle

    elif(oper == 'left'):
        if (y - 1 < 0):
            return None
        else:
            tmp = puzzle[x][y]
            puzzle[x][y] = puzzle[x][y - 1]
            puzzle[x][y - 1] = tmp

            return puzzle

def shufflePuzzle(state, moves):
    puzzle = copy.deepcopy(state) 
    x, y = checkZero(puzzle)

    for i in range(moves):
        valid_ops = []
        if x > 0: valid_ops.append('up')
        if x < 2: valid_ops.append('down')
        if y > 0: valid_ops.append('left')
        if y < 2: valid_ops.append('right')

        move = random.choice(valid_ops)
        new_state = movePuzzle(puzzle, x, y, move)
        if new_state:
            puzzle = new_state
            x, y = checkZero(puzzle)

    return puzzle

cur = shufflePuzzle(goal, 50)

def showPuzzle():
    fig, axes = plt.subplots(3, 3, figsize=(4, 4))
    plt.cla()
    plt.close()
    imgList = [['puzzle/num_' + cur[i][j] + '.png' for j in range(3)] for i in range(3)]

    for i in range(3):
        for j in range(3):
            img = cv2.imread(imgList[i][j])
            ax = plt.subplot(3, 3, i * 3 + j + 1)
            ax.axis('off') # 축 삭제
            plt.imshow(img)
            plt.pause(0.01)

    def add_point(event):
        #if event.inaxes != ax:
        #    return
        if event.button ==1:
            fore = pyautogui.getActiveWindow()
            pos = pyautogui.position()
            x = pos.x - fore.left
            y = pos.y - fore.top
            #print("Ŭ   : ", x, ", ", y)

            if (x >= 20 and x <= 170) and (y >= 40 and y <= 190):
                move = "no"
                if cur[0][1] == '0':
                    move = 'right'
                elif cur[1][0] == '0':
                    move = 'down'
                if move != 'no':
                    next = movePuzzle(cur, 0, 0, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('1')

            if (x >= 180 and x <= 330) and (y >= 40 and y <= 190):
                move = "no"
                if cur[0][0] == '0':
                    move = 'left'
                elif cur[0][2] == '0':
                    move = 'right'
                elif cur[1][1] == '0':
                    move = 'down'
                if move != 'no':
                    next = movePuzzle(cur, 0, 1, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('2')

            if (x >= 340 and x <= 490) and (y >= 40 and y <= 190):
                move = "no"
                if cur[0][1] == '0':
                    move = 'left'
                elif cur[1][2] == '0':
                    move = 'down'
                if move != 'no':
                    next = movePuzzle(cur, 0, 2, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('3')

            if (x >= 20 and x <= 170) and (y >= 200 and y <= 350):
                move = "no"
                if cur[0][0] == '0':
                    move = 'up'
                elif cur[1][1] == '0':
                    move = 'right'
                elif cur[2][0] == '0':
                    move = 'down'
                if move != 'no':
                    next = movePuzzle(cur, 1, 0, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('4')

            if (x >= 180 and x <= 330) and (y >= 200 and y <= 350):
                move = "no"
                if cur[0][1] == '0':
                    move = 'up'
                elif cur[1][0] == '0':
                    move = 'left'
                elif cur[1][2] == '0':
                    move = 'right'
                elif cur[2][1] == '0':
                    move = 'down'
                if move != 'no':
                    next = movePuzzle(cur, 1, 1, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('5')

            if (x >= 340 and x <= 490) and (y >= 200 and y <= 350):
                move = "no"
                if cur[0][2] == '0':
                    move = 'up'
                elif cur[1][1] == '0':
                    move = 'left'
                elif cur[2][2] == '0':
                    move = 'down'
                if move != 'no':
                    next = movePuzzle(cur, 1, 2, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('6')

            if (x >= 20 and x <= 170) and (y >= 360 and y <= 510):
                move = "no"
                if cur[1][0] == '0':
                    move = 'up'
                elif cur[2][1] == '0':
                    move = 'right'
                if move != 'no':
                    next = movePuzzle(cur, 2, 0, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('7')

            if (x >= 180 and x <= 330) and (y >= 360 and y <= 510):
                move = "no"
                if cur[2][0] == '0':
                    move = 'left'
                elif cur[1][1] == '0':
                    move = 'up'
                elif cur[2][2] == '0':
                    move = 'right'
                if move != 'no':
                    next = movePuzzle(cur, 2, 1, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('8')

            if (x >= 340 and x <= 490) and (y >= 360 and y <= 510):
                move = "no"
                if cur[2][1] == '0':
                    move = 'left'
                elif cur[1][2] == '0':
                    move = 'up'
                if move != 'no':
                    next = movePuzzle(cur, 2, 2, move)
                    print(move)
                    showPuzzle()
                    plt.show()
                    if next == goal:
                        print("성공")
                print('9')

    def on_key(event):
        global cur
        if event.key == '1':
            print("수동 모드 실행")
        elif event.key == '2':
            print("자동 모드 실행")
            result = astar(copy.deepcopy(cur))
            if result == -1:
                print("해결 불가")
            else:
                for state in result:
                    cur = state
                    showPuzzle()
                    plt.pause(0.5)
                print("자동 해결 완료")

    cid = plt.connect('button_press_event', add_point)
    cid2 = plt.connect('key_press_event', on_key)
    plt.subplots_adjust(left=0.01, bottom=0.01, right=0.99, top=0.99, wspace=0.01, hspace=0.01)
    plt.show()

class Node:
    def __init__(self, data, hval, level, parent=None):
        self.data = data
        self.hval = hval
        self.level = level
        self.parent = parent

def h(puzzle, goal):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal[i][j]:
                cnt += 1
    return cnt

def f(puzzle, goal):
    return puzzle.level + h(puzzle.data, goal)

def astar(puzzle):
    visit = []
    queue = []
    start = Node(data=puzzle, hval=h(puzzle, goal), level=0, parent=None)
    queue.append(start)

    while queue:
        current = queue.pop(0)
        print(np.array(current.data))

        if h(current.data, goal) == 0:
            path = []
            while current:
                path.append(current.data)
                current = current.parent
            return path[::-1]  

        visit.append(current.data)
        x, y = checkZero(current.data)

        for op in oper:
            next_state = movePuzzle(copy.deepcopy(current.data), x, y, op)

            if next_state is not None and next_state not in visit:
                queue.append(Node(next_state, h(next_state, goal), current.level + 1, parent=current))

        queue.sort(key=lambda x: f(x, goal))

    return -1

print("1: 수동, 2: 자동")
showPuzzle()