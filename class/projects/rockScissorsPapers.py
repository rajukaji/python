def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice.lower() == 'rock' and player2_choice.lower() == 'paper':
        return 'Player 2 wins'
    elif player1_choice.lower() == 'rock' and player2_choice.lower() == 'scissors':
        return 'Player 1 wins'
    elif player1_choice.lower() == 'scissors' and player2_choice.lower() == 'paper':
        return 'Player 1 wins'
    elif player1_choice.lower() == 'scissors' and player2_choice.lower() == 'rock':
        return 'Player 2 wins'
    elif player1_choice.lower() == 'paper' and player2_choice.lower() == 'rock':
        return 'Player 1 wins'
    elif player1_choice.lower() == 'paper' and player2_choice.lower() == 'scissors':
        return 'Player 2 wins'
    else:
        return "It's a tie"
    
print(rock_paper_scissors('Rock', 'PAPER'))
