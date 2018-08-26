name1 = input('1st Player name :')
name2 = input('2nd Player name :')
choice1 = input('P1 - What do you want to choose : paper, rock or scissors? :')
choice2 = input('P2 - What do you want to choose : paper, rock or scissors? :')


def game(choice1, choice2):
    if choice1 == 'paper' and choice2 == 'paper':
        return ('its a tie')
    elif choice1 == 'paper' and choice2 == 'rock':
        return ('{} wins'.format(name1))
    elif choice1 == 'paper' and choice2 == 'scissors':
        return ('{} wins'.format(name2))
    elif choice1 == 'rock' and choice2 == 'rock':
        return ('its a tie')
    elif choice1 == 'rock' and choice2 == 'paper':
        return ('{} wins'.format(name2))
    elif choice1 == 'rock' and choice2 == 'scissors':
        return ('{} wins'.format(name1))
    elif choice1 == 'scissors' and choice2 == 'scissors':
        return ('its a tie')
    elif choice1 == 'scissors' and choice2 == 'paper':
        return ('{} wins'.format(name1))
    elif choice1 == 'scissors' and choice2 == 'rock':
        return ('{} wins'.format(name2))
    else:
        return ('wrong choice')


print(game(choice1, choice2))
