import random
import os

grid = [[random.choice([0, 2, 4]) for _ in range(4)] for _ in range(4)]

def move_left():
    global score
    tmp = []
    for row in range(4):
        for num in grid[row]:
            if num:
                if tmp and tmp[-1] == num:
                    tmp[-1] *= -2
                    score += num * 2  # 해당 타일이 합쳐져서 점수를 증가시킴
                else:
                    tmp.append(num)

        tmp = [abs(x) for x in tmp]
        tmp += [0] * (4 - len(tmp))
        grid[row] = tmp
        tmp = []

def move_right():
    global score
    for row in grid:
        row.reverse()

    move_left()

    for row in grid:
        row.reverse()

def move_up():
    global score
    global grid
    grid = list(map(list, zip(*grid)))
    move_left()
    grid = list(map(list, zip(*grid)))

def move_down():
    global score
    global grid
    grid = list(map(list, zip(*grid)))
    move_right()
    grid = list(map(list, zip(*grid)))

 # clear screen
os.system('cls' if os.name == 'nt' else 'clear')

print('[Welcome to 2048!]')
print()
print('Enter X to exit')
print()

score = 0

while True:
    print("Score:", score)
    print()
    for row in grid:
        for num in row:
            print(f'{num:4}', end=' ')
        print()
    print()
    direction = input("Enter the direction(A, S, D, W): ")

    if direction in 'Aa':
        move_left()
    elif direction in 'Dd':
        move_right()
    elif direction in 'Ww':
        move_up()
    elif direction in 'Ss':
        move_down()
    elif direction in 'Xx':
        print('\nGoodbye\n')
        break
    else:
        print('Invalid direction')

    empty = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                empty.append((i, j))

    if empty:
        i, j = random.choice(empty)
        grid[i][j] = random.choice([2, 4])
    else:
        print('Game Over')
        break

    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
