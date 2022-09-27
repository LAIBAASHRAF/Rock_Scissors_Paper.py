player_one = input()

player_two = input()

if (player_one == 'r' and player_two == 's') or (player_one == 'r' and player_two == 'p') or (
        player_one == 'p' and player_two == 's'):
        
    print("Congrats! user one is winner", "\U0001F600")
    
if (player_one == 'r' and player_two == 'r') or (player_one == 's' and player_two == 's') or (
        player_one == 'p' and player_two == 'p'):
        
    print("Draw Game", "\U0001F608")
else:

    print("user two is winner", "\U0001F604")
