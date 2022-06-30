import random
from statistics import stdev
#designate number of simulation trials at 0 for start
trials = 0
#designate the number of simulations of the nfl playoffs through which you would like to run
trial_num = 1
#designate a counter variable for any trials that result in ties
tie_count = 0

#set number of times each player has won = 0 and create a dictionary of player information
mom_wins = 0
dad_wins = 0
clay_wins = 0
will_wins = 0
player_dictionary = {0:["Mom",mom_wins],1:["Dad",dad_wins], 2:["Clay",clay_wins], 3:["Will",will_wins]}

#designate an empty bracket accuracy dictionary into which you will put all bracket accuracy percentages
bracket_accuracy_dict = {0: ["Mom", []], 1: ["Dad",[]], 2: ["Clay", []], 3: ["Will",[]]}

#run through n = 5000 simulations of the NFL playoffs
while trials <= trial_num - 1: 
	#simulate the nfc playoff bracket
	nfc_playoffs = {1:['Green Bay Packers', (1/3.8)], 2:['Tampa Bay Bucaneers', (1/8)], 3:['Dallas Cowboys', (1/12)], 4:['Los Angeles Rams',(1/10)], 5:['Arizona Cardinals',(1/25)], 6:['San Fransisco 49ers',(1/20)],7:['Philadelphia Eagles',(1/65)]}
	nfc_seeds = list(nfc_playoffs.keys())
	nfc_wildcard_seeds = nfc_seeds[1:]
	nfc_wild_card_teams = [nfc_playoffs[i] for i in nfc_wildcard_seeds]
	nfc_wild_card_games = {}
	match_num = 0
	while len(nfc_wildcard_seeds) > 0:
		match_num += 1
		match_list = []
		teams_list = [nfc_playoffs[min(nfc_wildcard_seeds)], nfc_playoffs[max(nfc_wildcard_seeds)]]
		for team in teams_list:
			match_list.append(team)
			nfc_wildcard_seeds.remove(list(nfc_playoffs.values()).index(team) + 1)
		nfc_wild_card_games["Match " + str(match_num)] = match_list
	nfc_wild_card_winners = {}
	for matchlabel in list(nfc_wild_card_games.keys()):
		teams_list = [nfc_wild_card_games[matchlabel][i][0] for i in list(range(0,len(nfc_wild_card_games[matchlabel])))]
		odds_list = [nfc_wild_card_games[matchlabel][i][1] for i in list(range(0,len(nfc_wild_card_games[matchlabel])))]
		matchup_winner = random.choices(teams_list,odds_list,k=1)[0]
		for team_info in list(nfc_playoffs.values()):
			if matchup_winner in team_info:
				matchup_winner_seed = list(nfc_playoffs.keys())[list(nfc_playoffs.values()).index(team_info)]
				nfc_wild_card_winners[matchup_winner_seed] = team_info
	nfc_wild_card_winners[list(nfc_playoffs.keys())[0]] = list(nfc_playoffs.values())[0]
	# print("NFC Wildcard: " + str(nfc_wild_card_winners))
	nfc_divisional_seeds = list(nfc_wild_card_winners.keys())
	nfc_divisional_teams = [nfc_playoffs[i] for i in nfc_divisional_seeds]
	nfc_divisional_games = {}
	match_num = 0
	while len(nfc_divisional_seeds) > 0:
		match_num += 1
		match_list = []
		teams_list = [nfc_playoffs[min(nfc_divisional_seeds)], nfc_playoffs[max(nfc_divisional_seeds)]]
		for team in teams_list:
			match_list.append(team)
			nfc_divisional_seeds.remove(list(nfc_playoffs.values()).index(team) + 1)
		nfc_divisional_games["Match " + str(match_num)] = match_list
	nfc_divisional_winners = {}
	for matchlabel in list(nfc_divisional_games.keys()):
		teams_list = [nfc_divisional_games[matchlabel][i][0] for i in list(range(0,len(nfc_divisional_games[matchlabel])))]
		odds_list = [nfc_divisional_games[matchlabel][i][1] for i in list(range(0,len(nfc_divisional_games[matchlabel])))]
		matchup_winner = random.choices(teams_list,odds_list,k=1)[0]
		for team_info in list(nfc_playoffs.values()):
			if matchup_winner in team_info:
				matchup_winner_seed = list(nfc_playoffs.keys())[list(nfc_playoffs.values()).index(team_info)]
				nfc_divisional_winners[matchup_winner_seed] = team_info
	# print("NFC Divisional: " + str(nfc_divisional_winners))
	nfc_championship_seeds = list(nfc_divisional_winners.keys())
	nfc_championship_teams = [nfc_playoffs[i] for i in nfc_championship_seeds]
	nfc_championship_game = {}
	match_num = 0
	while len(nfc_championship_seeds) > 0:
		match_num += 1
		match_list = []
		teams_list = [nfc_playoffs[min(nfc_championship_seeds)], nfc_playoffs[max(nfc_championship_seeds)]]
		for team in teams_list:
			match_list.append(team)
			nfc_championship_seeds.remove(list(nfc_playoffs.values()).index(team) + 1)
		nfc_championship_game["Match " + str(match_num)] = match_list
	nfc_championship_winner = {}
	for matchlabel in list(nfc_championship_game.keys()):
		teams_list = [nfc_championship_game[matchlabel][i][0] for i in list(range(0,len(nfc_championship_game[matchlabel])))]
		odds_list = [nfc_championship_game[matchlabel][i][1] for i in list(range(0,len(nfc_championship_game[matchlabel])))]
		matchup_winner = random.choices(teams_list,odds_list,k=1)[0]
		for team_info in list(nfc_playoffs.values()):
			if matchup_winner in team_info:
				matchup_winner_seed = list(nfc_playoffs.keys())[list(nfc_playoffs.values()).index(team_info)]
				nfc_championship_winner[matchup_winner_seed] = team_info
	# print("NFC Championship: " + str(nfc_championship_winner))

	#simulate the afc playoff bracket
	afc_playoffs = {1:['Tennessee Titans',(1/8.5)], 2:['Kansas City Chiefs',(1/4.5)], 3:['Buffalo Bills',(1/5)], 4:['Cincinnati Bengals',(1/12)], 5:['Las Vegas Raiders',(1/60)], 6:['New England Patriots',(1/25)],7:['Pittsburgh Steelers',(1/80)]}
	afc_seeds = list(afc_playoffs.keys())
	afc_wildcard_seeds = afc_seeds[1:]
	afc_wild_card_teams = [afc_playoffs[i] for i in afc_wildcard_seeds]
	afc_wild_card_games = {}
	match_num = 0
	while len(afc_wildcard_seeds) > 0:
		match_num += 1
		match_list = []
		teams_list = [afc_playoffs[min(afc_wildcard_seeds)], afc_playoffs[max(afc_wildcard_seeds)]]
		for team in teams_list:
			match_list.append(team)
			afc_wildcard_seeds.remove(list(afc_playoffs.values()).index(team) + 1)
		afc_wild_card_games["Match " + str(match_num)] = match_list
	afc_wild_card_winners = {}
	for matchlabel in list(afc_wild_card_games.keys()):
		teams_list = [afc_wild_card_games[matchlabel][i][0] for i in list(range(0,len(afc_wild_card_games[matchlabel])))]
		odds_list = [afc_wild_card_games[matchlabel][i][1] for i in list(range(0,len(afc_wild_card_games[matchlabel])))]
		matchup_winner = random.choices(teams_list,odds_list,k=1)[0]
		for team_info in list(afc_playoffs.values()): 
			if matchup_winner in team_info:
				matchup_winner_seed = list(afc_playoffs.keys())[list(afc_playoffs.values()).index(team_info)]
				afc_wild_card_winners[matchup_winner_seed] = team_info
	afc_wild_card_winners[list(afc_playoffs.keys())[0]] = list(afc_playoffs.values())[0]
	# print("AFC Wildcard: " + str(afc_wild_card_winners))
	afc_divisional_seeds = list(afc_wild_card_winners.keys())
	afc_divisional_teams = [afc_playoffs[i] for i in afc_divisional_seeds]
	afc_divisional_games = {}
	match_num = 0
	while len(afc_divisional_seeds) > 0:
		match_num += 1
		match_list = []
		teams_list = [afc_playoffs[min(afc_divisional_seeds)], afc_playoffs[max(afc_divisional_seeds)]]
		for team in teams_list:
			match_list.append(team)
			afc_divisional_seeds.remove(list(afc_playoffs.values()).index(team) + 1)
		afc_divisional_games["Match " + str(match_num)] = match_list
	afc_divisional_winners = {}
	for matchlabel in list(afc_divisional_games.keys()):
		teams_list = [afc_divisional_games[matchlabel][i][0] for i in list(range(0,len(afc_divisional_games[matchlabel])))]
		odds_list = [afc_divisional_games[matchlabel][i][1] for i in list(range(0,len(afc_divisional_games[matchlabel])))]
		matchup_winner = random.choices(teams_list,odds_list,k=1)[0]
		for team_info in list(afc_playoffs.values()):
			if matchup_winner in team_info:
				matchup_winner_seed = list(afc_playoffs.keys())[list(afc_playoffs.values()).index(team_info)]
				afc_divisional_winners[matchup_winner_seed] = team_info
	# print("AFC Divisional: " + str(afc_divisional_winners))
	afc_championship_seeds = list(afc_divisional_winners.keys())
	afc_championship_teams = [afc_playoffs[i] for i in afc_championship_seeds]
	afc_championship_game = {}
	match_num = 0
	while len(afc_championship_seeds) > 0:
		match_num += 1
		match_list = []
		teams_list = [afc_playoffs[min(afc_championship_seeds)], afc_playoffs[max(afc_championship_seeds)]]
		for team in teams_list:
			match_list.append(team)
			afc_championship_seeds.remove(list(afc_playoffs.values()).index(team) + 1)
		afc_championship_game["Match " + str(match_num)] = match_list
	afc_championship_winner = {}
	for matchlabel in list(afc_championship_game.keys()):
		teams_list = [afc_championship_game[matchlabel][i][0] for i in list(range(0,len(afc_championship_game[matchlabel])))]
		odds_list = [afc_championship_game[matchlabel][i][1] for i in list(range(0,len(afc_championship_game[matchlabel])))]
		matchup_winner = random.choices(teams_list,odds_list,k=1)[0]
		for team_info in list(afc_playoffs.values()):
			if matchup_winner in team_info:
				matchup_winner_seed = list(afc_playoffs.keys())[list(afc_playoffs.values()).index(team_info)]
				afc_championship_winner[matchup_winner_seed] = team_info
	# print("AFC Championship: " + str(afc_championship_winner))

	#simulate the super bowl
	super_bowl_teams_list = [list(nfc_championship_winner.values())[0][0],list(afc_championship_winner.values())[0][0]]
	super_bowl_odds_list = [list(nfc_championship_winner.values())[0][1],list(afc_championship_winner.values())[0][1]]
	super_bowl_winner = random.choices(super_bowl_teams_list,super_bowl_odds_list,k=1)
	# print(super_bowl_teams_list)
	# print("Super Bowl: " + str(super_bowl_winner))

	#store each player's picks for the wild card, divisional, conference championship, and superbowl
	mom_picks = {'NFC':{'NFC Wildcard':{2: ['Tampa Bay Bucaneers', 0.125], 3: ['Dallas Cowboys', 0.08333333333333333], 5: ['Arizona Cardinals', 0.04], 1: ['Green Bay Packers', 0.2631578947368421]},
	'NFC Divisional':{1: ['Green Bay Packers', 0.2631578947368421], 3: ['Dallas Cowboys', 0.08333333333333333]},'NFC Championship':{1: ['Green Bay Packers', 0.2631578947368421]}},
	'AFC':{'AFC Wildcard':{2: ['Kansas City Chiefs', 0.2222222222222222], 6: ['New England Patriots', 0.04], 4: ['Cincinnati Bengals', 0.08333333333333333], 1: ['Tennessee Titans', 0.11764705882352941]},
	'AFC Divisional':{1: ['Tennessee Titans', 0.11764705882352941], 4: ['Cincinnati Bengals', 0.08333333333333333]},'AFC Championship':{1: ['Tennessee Titans', 0.11764705882352941]}},"Super Bowl": ['Green Bay Packers']}
	mom_points = 0

	dad_picks = {'NFC':{'NFC Wildcard':{2: ['Tampa Bay Bucaneers', 0.125], 3: ['Dallas Cowboys', 0.08333333333333333], 4: ['Los Angeles Rams', 0.1], 1: ['Green Bay Packers', 0.2631578947368421]},
	'NFC Divisional':{1: ['Green Bay Packers', 0.2631578947368421], 2: ['Tampa Bay Bucaneers', 0.125]},'NFC Championship':{1: ['Green Bay Packers', 0.2631578947368421]}},
	'AFC':{'AFC Wildcard':{2: ['Kansas City Chiefs', 0.2222222222222222], 3: ['Buffalo Bills', 0.2], 4: ['Cincinnati Bengals', 0.08333333333333333], 1: ['Tennessee Titans', 0.11764705882352941]},
	'AFC Divisional':{4: ['Cincinnati Bengals', 0.08333333333333333], 3: ['Buffalo Bills', 0.2]},'AFC Championship':{3: ['Buffalo Bills', 0.2]}},"Super Bowl": ['Green Bay Packers']}
	dad_points = 0

	clay_picks = {'NFC':{'NFC Wildcard':{2: ['Tampa Bay Bucaneers', 0.125], 3: ['Dallas Cowboys', 0.08333333333333333], 4: ['Los Angeles Rams', 0.1], 1: ['Green Bay Packers', 0.2631578947368421]},
	'NFC Divisional':{4: ['Los Angeles Rams', 0.1], 2: ['Tampa Bay Bucaneers', 0.125]},'NFC Championship':{4: ['Los Angeles Rams', 0.1]}},
	'AFC':{'AFC Wildcard':{2: ['Kansas City Chiefs', 0.2222222222222222], 3: ['Buffalo Bills', 0.2], 4: ['Cincinnati Bengals', 0.08333333333333333], 1: ['Tennessee Titans', 0.11764705882352941]},
	'AFC Divisional':{1: ['Tennessee Titans', 0.11764705882352941], 2: ['Kansas City Chiefs', 0.2222222222222222]},'AFC Championship':{1: ['Tennessee Titans', 0.11764705882352941]}},"Super Bowl": ['Tennessee Titans']}
	clay_points = 0

	will_picks = {'NFC':{'NFC Wildcard':{2: ['Tampa Bay Bucaneers', 0.125], 3: ['Dallas Cowboys', 0.08333333333333333], 4: ['Los Angeles Rams', 0.1], 1: ['Green Bay Packers', 0.2631578947368421]},
	'NFC Divisional':{1: ['Green Bay Packers', 0.2631578947368421], 2: ['Tampa Bay Bucaneers', 0.125]},'NFC Championship':{1: ['Green Bay Packers', 0.2631578947368421]}},
	'AFC':{'AFC Wildcard':{2: ['Kansas City Chiefs', 0.2222222222222222], 3: ['Buffalo Bills', 0.2], 4: ['Cincinnati Bengals', 0.08333333333333333], 1: ['Tennessee Titans', 0.11764705882352941]},
	'AFC Divisional':{1: ['Tennessee Titans', 0.11764705882352941], 3: ['Buffalo Bills', 0.2]},'AFC Championship':{1: ['Tennessee Titans', 0.11764705882352941]}},"Super Bowl": ['Tennessee Titans']}
	will_points = 0

	#store info for family picks, and store simulated picks into a separate dictionary for comparison
	family_picks = [[mom_picks,mom_points],[dad_picks,dad_points],[clay_picks,clay_points],[will_picks,will_points]]
	actual_picks = {'NFC':{'NFC Wildcard': nfc_wild_card_winners, 'NFC Divisional': nfc_divisional_winners, 'NFC Championship': nfc_championship_winner},
	'AFC':{'AFC Wildcard': afc_wild_card_winners, 'AFC Divisional': afc_divisional_winners, 'AFC Championship': afc_championship_winner}, "Super Bowl": super_bowl_winner}
	# print(afc_wild_card_winners)
	nfl_playoff_result = {'NFC':{'NFC Wildcard':{2: ['Tampa Bay Bucaneers', 0.125], 6:['San Fransisco 49ers',(1/20)], 4: ['Los Angeles Rams', 0.1], 1: ['Green Bay Packers', 0.2631578947368421]},
	'NFC Divisional':{4: ['Los Angeles Rams', 0.1], 6:['San Fransisco 49ers',(1/20)]},'NFC Championship':{4: ['Los Angeles Rams', 0.1]}},
	'AFC':{'AFC Wildcard':{2: ['Kansas City Chiefs', 0.2222222222222222], 3: ['Buffalo Bills', 0.2], 4: ['Cincinnati Bengals', 0.08333333333333333], 1: ['Tennessee Titans', 0.11764705882352941]},
	'AFC Divisional':{4: ['Cincinnati Bengals', 0.08333333333333333], 2: ['Kansas City Chiefs', 0.2222222222222222]},'AFC Championship':{4: ['Cincinnati Bengals', 0.08333333333333333]}},"Super Bowl": ['Los Angeles Rams']}

	#determine the number of points each player receives based off of his or her bracket accuracy
	for i in list(range(0,len(family_picks))):
		point_count = family_picks[i][1] #this is equivalent to the variable representing the total points accrued for each family member
		#gather points for the wild card winners
		for team_info in list(family_picks[i][0]['NFC']['NFC Wildcard'].values()):
			if team_info in list(nfl_playoff_result['NFC']['NFC Wildcard'].values()):
			# if team_info in list(actual_picks['NFC']['NFC Wildcard'].values()):
				point_count += 3 #gather points for correct nfc wild card round winners

		for team_info in list(family_picks[i][0]['NFC']['NFC Divisional'].values()):
			if team_info in list(nfl_playoff_result['NFC']['NFC Divisional'].values()):
			# if team_info in list(actual_picks['NFC']['NFC Divisional'].values()):
				point_count += 5 #gather points for correct nfc divisional round winners

		for team_info in list(family_picks[i][0]['NFC']['NFC Championship'].values()):
			if team_info in list(nfl_playoff_result['NFC']['NFC Championship'].values()):
			# if team_info in list(actual_picks['NFC']['NFC Championship'].values()):
				point_count += 9 #gather points for the correct nfc championship winner
		
		for team_info in list(family_picks[i][0]['AFC']['AFC Wildcard'].values()):
			if team_info in list(nfl_playoff_result['AFC']['AFC Wildcard'].values()):
			# if team_info in list(actual_picks['AFC']['AFC Wildcard'].values()):
				point_count += 3 #gather points for correct afc wild card round winners
		
		for team_info in list(family_picks[i][0]['AFC']['AFC Divisional'].values()):
			if team_info in list(nfl_playoff_result['AFC']['AFC Divisional'].values()):
			# if team_info in list(actual_picks['AFC']['AFC Divisional'].values()):
				point_count += 5 #gather points for correct afc divisional round winners

		for team_info in list(family_picks[i][0]['AFC']['AFC Championship'].values()):
			if team_info in list(nfl_playoff_result['AFC']['AFC Championship'].values()):
			# if team_info in list(actual_picks['AFC']['AFC Championship'].values()):
				point_count += 9 #gather points for correct afc championship winner
		
		if family_picks[i][0]["Super Bowl"][0] in nfl_playoff_result["Super Bowl"]:		
		# if family_picks[i][0]["Super Bowl"][0] in actual_picks["Super Bowl"]:
			point_count += 17
		
		family_picks[i][1] = point_count

	#designate number that represents a perfect nfl playoff bracket in points according to point logic
	maxpoints = 79 

	#gather a list of bracket accuracies as a fraction of the max number of points for each family member
	bracket_accuracy_list = [family_picks[i][1]/maxpoints for i in list(range(0, len(family_picks)))]
	
	#add the bracket accuracy fraction to the player's list of n percentages equivalent in length to the n number of trials in the simulation
	for i in list(range(0,len(bracket_accuracy_list))):
		bracket_accuracy_dict[i][1].append(bracket_accuracy_list[i])

	#tally the winner for each trial number in the simulation
	acc_count = 0
	max_acc = max(bracket_accuracy_list)
	for acc in bracket_accuracy_list: #validate that there is not a tie for the maximum bracket accuracy percentage for this trial
		if acc == max_acc:
			acc_count +=1
	if acc_count == 1:
		for i in list(player_dictionary.keys()):
			if bracket_accuracy_list[i] == max(bracket_accuracy_list):
				player_dictionary[i][1] += 1
	else:
		tie_count += 1
	trials += 1

#search for the winner based off of the fraction of times he or she won out of "n" total trials
player_count_list = [list(player_dictionary.values())[i][1] for i in list(range(0, len(list(player_dictionary.values()))))]
player_key_list = list(player_dictionary.keys())

#display each player and fraction of simulations that he or she won
# counter = 0
# while counter < len(list(player_dictionary.keys())):
# 	for player in player_key_list:
# 		player_wins_count = list(player_dictionary.values())[player][1]
# 		if player_wins_count == max(player_count_list):
# 			print(str(counter + 1) + ": " + list(player_dictionary.values())[player][0] +  " won " + str(list(player_dictionary.values())[player][1]/sum([player[1] for player in list(player_dictionary.values())])) + " of the simulation trials that did not result in a tie.")
# 			player_count_list.remove(player_wins_count)
# 			player_key_list.remove(player)
# 			counter += 1
# print('\n')

#display each player and the average of each of his or her bracket accuracy percentages
for key in list(bracket_accuracy_dict.keys()):
	print(bracket_accuracy_dict[key][0] + "'s bracket accuracy is " + str(sum(bracket_accuracy_dict[key][1])/(trials)) + "!")
	if key == max(list(bracket_accuracy_dict.keys())):
		print("\n")
for bracket_accuracy in [str(sum(bracket_accuracy_dict[key][1])/(trials)) for key in list(bracket_accuracy_dict.keys())]:
	if bracket_accuracy == max([str(sum(bracket_accuracy_dict[key][1])/(trials)) for key in list(bracket_accuracy_dict.keys())]):
		print(bracket_accuracy_dict[[str(sum(bracket_accuracy_dict[key][1])/(trials)) for key in list(bracket_accuracy_dict.keys())].index(bracket_accuracy)][0] + " is the bracket challenge champion!")
#display each player and the standard deviation of each of his or her bracket accuracy percentages 
# for key in list(bracket_accuracy_dict.keys()):
# 	print("The standard deviation of " + bracket_accuracy_dict[key][0] + "'s  bracket accuracy percentage is " + str(stdev(bracket_accuracy_dict[key][1])) + "!")
	