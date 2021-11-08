import constants as const 
import statistics as stats
import copy 

player_data = copy.deepcopy(const.PLAYERS)

def avg_height(team_name):
    player_height = []
    for player in team_name:
        player_height.append(player['height'])
    return round(stats.mean(player_height), 1)

def clean_data():

    for data in player_data: 
        for key, value in data.items(): 
            if key == 'height':
                data['height'] = int(value.split()[0])
            elif key == 'experience':
                if value == 'NO': 
                    data['experience'] = False 
                elif value == 'YES': 
                    data['experience'] = True
            elif key == 'guardians':
                data['guardians'] = value.split(" and ")

PANTHERS, BANDITS, WARRIORS = [], [], []
all_teams = [PANTHERS, BANDITS, WARRIORS]

def balance_teams(team_name):
    
    num_players_team = len(const.PLAYERS) / len(const.TEAMS)
    total_experienced = num_players_team / 2
    total_inexperienced = num_players_team / 2 
    
    for team in all_teams:

        exp_count = 0
        inexp_count = 0
        while len(team) < num_players_team:

            for player in player_data: 
                if player['experience'] == True and exp_count < (total_experienced):
                    team.append(player)
                    player_data.remove(player)
                    exp_count += 1
                    continue
                elif player['experience'] == False and inexp_count < (total_inexperienced):
                    team.append(player)
                    inexp_count += 1
                    player_data.remove(player)
                    continue
                else:
                    break
    
    team_name = sorted(team_name, key=lambda x: x.get('height')) #sorting function syntax found at https://www.programiz.com/python-programming/methods/list/sort
    team_players = ''
    player_guardians = []
    for player in team_name:
        if player != team_name[-1]:
            team_players += (player['name'] + ', ')
            player_guardians.extend(player['guardians']) 
        elif player == team_name[-1]:
            team_players += player['name']
            player_guardians.extend(player['guardians'])
    guardian_string = ", ".join(player_guardians) 
 
    print(f"Total Players: {len(team_name)}\nTotal experienced: {int(total_experienced)}\nTotal inexperienced: {int(total_inexperienced)}\nAverage Height: {avg_height(team_name)}\n")
    print(f"Players on this team (in order of ascending height): {team_players}")
    print(f"Guardians on this team: {guardian_string}\n")
    
    team_stats = {'total inexperienced' : total_inexperienced, 'total experienced' : total_experienced, 'average height' : avg_height(team_name)}
    team_name.append(team_stats)
    
def tool_start():
    
    clean_data()

    while True:
        print('BASKETBALL TEAM STATS TOOL\n---- MENU ----')
        continue_ = input("Here are your choices: \nA) Display Team Stats\nB) Quit\n\nEnter an option: ")
        if continue_.lower() == 'a'.lower():
            team_name = input("Please choose a team:\nA) Panthers\nB) Bandits\nC) Warriors\n\nEnter an option: ")
            if team_name.lower() == 'a'.lower():
                balance_teams(PANTHERS)
                continue
            elif team_name.lower() == 'b'.lower():
                balance_teams(BANDITS)
                continue
            elif team_name.lower() == 'c'.lower():
                balance_teams(WARRIORS)
                continue
        elif continue_.lower() == 'b'.lower():
            print("You have quit the stats tool. See you next time!")
            break
        else: 
            print("That is not an option. Please select either 'A' or 'B'")
            continue 

                 
                    
if __name__ == '__main__':
    tool_start()
