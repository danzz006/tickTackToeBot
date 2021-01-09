''' Main starting here, players playes with a bot '''


import subprocess as sp
from bot import Bot


#grid = [[x for x in range(3)] for y in range(3)]

# print(grid)

# for x in range(len(grid)):
#     print(grid[x])


# print(
#     ' -----|-----|-----\n',
#     '-----|-----|-----\n',
#     '-----|-----|-----'
# )

# y = 1
# for x in range(3):
#     print(f'--{y}--|--{y+1}--|--{y+2}--\n')
#     y += 3 

choices = {'X': [], 'O': []}

def mark(y, choice, symbol='X'):
    if y in choices['X']:
        return 'X'
    if y in choices['O']:
        return 'O'
    if choice == y:
        choices[symbol].append(choice)
        return symbol
    return y


def reset():
    tmp = sp.call('cls', shell=True)

    choices['X'] = []
    choices['O'] = []

    y = 1
    for _ in range(3):
        print(f'--{y}--|--{y+1}--|--{y+2}--\n')
        y += 3



def state(symbol):

    # horizontal
    winsA = [1,2,3]
    winsB = [4,5,6]
    winsC = [7,8,9]
    # vertical
    winsD = [1,4,7]
    winsE = [2,5,8]
    winsF = [3,6,9]
    # diagonals
    winsG = [1,5,9]
    winsH = [3,5,7]

    wins = [winsA, winsB, winsC, winsD, winsE, winsF, winsG, winsH]
    seq = win_segments(choices[symbol])
    # print(choices[symbol])
    # print(seq)
    if seq in wins:
        return True



def win_segments(choices):
    if 1 in choices:
        if 2 in choices:
            if 3 in choices:
                return [1,2,3]
    if 4 in choices:
        if 5 in choices:
            if 6 in choices:
                return [4,5,6]
    if 7 in choices:
        if 8 in choices:
            if 9 in choices:
                return [7,8,9]
    if 1 in choices:
        if 4 in choices:
            if 7 in choices:
                return [1,4,7]
    if 2 in choices:
        if 5 in choices:
            if 8 in choices:
                return [2,5,8]
    if 3 in choices:
        if 6 in choices:
            if 9 in choices:
                return [3,6,9]
    if 1 in choices:
        if 5 in choices:
            if 9 in choices:
                return [1,5,9]
    if 3 in choices:
        if 5 in choices:
            if 7 in choices:
                return [3,5,7]


def draw():
    if len(choices['X']) == 5 or len(choices['O']) == 5:
        return True


def run(choice, symbol):
    tmp = sp.call('cls', shell=True)
    y = 1
    for _ in range(3):  #1  #1              #2   #1              #3   #1
        print(f'--{mark(y, choice, symbol)}--|--{mark(y+1, choice, symbol)}--|--{mark(y+2, choice, symbol)}--\n')
        y += 3 


if __name__ == '__main__':

    b = Bot()

    y = 1
    for _ in range(3):
        print(f'--{y}--|--{y+1}--|--{y+2}--\n')
        y += 3 


    symbol = 'X'
    running = True
    while running:
        print('PlAYER ', symbol)

        try:
            choice = int(input('ENTER CHOICE: '))


            if choice == 0:
                break
            if choice == -1:
                reset()
                b.reset_bot()

            else:
                
                if symbol == 'X':
                    run(choice, symbol)
                    if state(symbol):
                        print(f'{symbol} wins')
                        break
                    symbol = 'O'
                
                if symbol == 'O':
                    run(b.assess_choices(choices['X']), symbol)
                    if state(symbol):
                        print(f'{symbol} wins')
                        break
                    symbol = 'X'
                
                    

                # if state(symbol):
                #     print(f'{symbol} wins')
                #     break
                if draw():
                    print('DRAW\n')
                    reset_val = input('RESET ?\n')
                    if reset_val == 'y':
                        reset()
                        b.reset_bot()
                        symbol = 'X'
                    else:
                        break

                
                # if symbol == 'X':
                #     symbol = 'O'
                
                #     symbol = 'X'

        except ValueError:
            print('\nENTER SOME VALUE\n')




