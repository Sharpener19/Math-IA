import pandas as pd

# Program 2

pgn = pd.read_csv("Raw_Data_IA_game_info.csv")

column_list = ['game_id','game_order','event','site','round','eco','termination','time_control','utc_date','utc_time','variant','ply_count','date_created','file_name'
               ,'winner','winner_elo','loser','loser_elo','winner_loser_elo_diff','white','black','white_rating_diff','black_rating_diff','white_title','black_title']

count = 0

for category in column_list:
    pgn = pgn.drop(category,axis=1)

pgn.to_csv("Parsed_Data.csv")

