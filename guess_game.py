from random import randint

def run_guess(answer, guess):
    if 0 < guess < 11:
        if guess == answer:
            print('GREAT!!!')
            return True
        else:
            print(f'Nope, it is {answer}. Try again.')
    else:
        print('Yo, I said 1-10...')

answer = randint(1, 10)

if __name__ == '__main__':
    while True:
        try:
            guess = int(input('Guess a number between 1-10!:     '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('Please enter a number.')
            continue