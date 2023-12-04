import pandas as pd
import re

data = pd.DataFrame()

results_list = []

with open('input.txt') as f:
     for line in f:
        game, results = line.strip().split(':')
        game_number = int(game.split(' ')[-1])
        results = results.split(';')
        for r in results:
            green_match = re.search(r'(\d+)\s+green', r)
            red_match = re.search(r'(\d+)\s+red', r)
            blue_match = re.search(r'(\d+)\s+blue', r)
            res = {'game_number': game_number, 'green': 0, 'red': 0, 'blue': 0}
            if green_match:
                res['green'] = int(green_match.group(1))
            if red_match:
                res['red'] = int(red_match.group(1))
            if blue_match:
                res['blue'] = int(blue_match.group(1))
            
            results_list.append(res)
df = pd.DataFrame(results_list)
# 12 red cubes, 13 green cubes, and 14 blue cubes
df['passed_test'] = (df['red'] <= 12) & (df['green'] <= 13) & (df['blue'] <= 14)
df_pct = df.groupby('game_number')['passed_test'].mean().reset_index()

solution = df_pct.query('passed_test == 1')['game_number'].sum()
print(solution)

df_max = df.groupby(['game_number'])[['red', 'green', 'blue']].max()
df['power'] = df_max['red'] * df_max['green'] * df_max['blue']
pt2_solution = int(df['power'].sum())
print(pt2_solution)