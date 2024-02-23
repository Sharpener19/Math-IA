import pandas as pd
from csv import writer

# Program 3
# The for-loop converts the ratings for White and Black into one value called Rating Difference.
# Additionally, the result of the game is converted from a string into a float value that is either (1.0, 0.5, or 0.0).

reader = pd.read_csv('Parsed_Data.csv')

for i, row in reader.iterrows():
    rating_difference = int(row['white_elo'])-int(row['black_elo'])
    game_result = row['result']
    if game_result == '1-0':
        game_result = 1.0
    elif game_result == '0-1':
        game_result = 0.0
    elif game_result == '1/2-1/2':
        game_result = 0.5
    else:
        print('ERROR ERROR')
    new_row=[rating_difference,game_result]
    with open('Next_Step.csv', 'a') as file:
        writer_object = writer(file)
        writer_object.writerow(new_row)
        file.close()

file = pd.read_csv('Next_Step.csv')

# Adding a Header List to the columns

header_list = ['Rating-Diff','Score']
file.to_csv('Next_Step_2.csv', header=header_list, index=False)


new_file = pd.read_csv('Next_Step_2.csv')

# Sorts the new CSV file in descending order by rating difference.

sorted_file = new_file.sort_values(['Rating-Diff'],axis=0,ascending=[False])

sorted_file.to_csv('Next_Step_3.csv',index=False)
