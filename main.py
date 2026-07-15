def world_cup_predictor(team_1 = "Argentina", team_2 = "England"):
    print('world cup predictor')
    print(team_1, "will win against", team_2, "vamos!")

team_1 = input("Which team do you predict will win: ")
team_2 = input("Which team do you predict will lose: ") 
world_cup_predictor(team_1, team_2)