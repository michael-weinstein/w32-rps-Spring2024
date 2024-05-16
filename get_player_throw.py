def get_player_throw():
    from game_dict import rps
    throw = ""
    while throw not in rps:
        throw = input("Please enter your throw ('paper', 'scissors', or 'rock'): ")
    return throw
