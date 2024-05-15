"""rock == rock
paper == paper
scissors == scissors



rock #User input : scissors #Computer throw
scissors : paper
paper : rock




if UserThrow == ComputerThrow   #In the case that your choice ties with the computer
    return "tie"
elif ComputerThrow is in our beatable  #In the case that your choice beats the computer
    return "you win!"
elif  #In the case that your choice loses to the computer
    return "womp womp"
"""
import typing
# import random
#
# def gameDict
#     rock = "rock"
#     paper = "paper"
#     scissors = "scissors"
#
#     winTable = {"rock" : "scissors", "scissors" : "paper", "paper" : "rock"}
#
# #Get player throw
# def playerThrow
#
#
#
# #Get computer throw
# def computerThrow
#     #random number generator where throws == numbers

def findWinner(gameDict:typing.Dict[str, typing.List[str]], computerThrow:str, playerThrow:str) -> str:
    if playerThrow == computerThrow:
        return "tie"
    if computerThrow not in gameDict:
        print("Computer threw an invalid option")
    if playerThrow not in gameDict:
        print("Player threw an invalid option")
    if computerThrow in gameDict[playerThrow]:
        return "player wins"
    else:
        return "computer wins"


#start game