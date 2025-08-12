import random

def rock_paper_scissors() -> str:
    moves = ('rock', 'paper', 'scissors')
    return moves[random.randint(0, 2)]

if __name__ == '__main__':
    move = rock_paper_scissors()
    print(f'For this demo, my rock paper scissors move is \'{move}\'!')