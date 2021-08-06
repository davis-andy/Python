import RPSMod

player = RPSMod.collectStringInput()
computer = RPSMod.generateIntegerValue()
computer_choice = RPSMod.convertIntegerToRPS(computer)
print()
print("Computer's selection:",computer_choice)
print()
RPSMod.evaluateWinning(player, computer_choice)
