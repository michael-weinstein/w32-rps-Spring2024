import game_dict
import gameplay
import get_player_throw


def playGame():
    game = game_dict.rps
    playerThrow = get_player_throw.get_player_throw()
    computerThrow = gameplay.getComputerThrow(game)
    print(gameplay.findWinner(game, computerThrow, playerThrow))


if __name__ == "__main__":
    playGame()