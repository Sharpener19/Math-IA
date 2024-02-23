import pandas as pd
from csv import writer

# Program 4

result = pd.read_csv('empty_columns_removed.csv')

sorted_rd = result.sort_values(['rating_diff_W-B'],axis=0,ascending=[False])

print(sorted_rd)

for i, row in sorted_rd.iterrows():
    new = row['rating_diff_W-B']
    game_result = 'blank'
    if row['result_num_W'] == 1.0:
        game_result = row['result_num_W']
    elif row['result_num_D'] == 0.5:
        game_result = row['result_num_D']
    elif row['result_num_B'] == 0.0:
        game_result = row['result_num_B']
    else:
        print('not working!')
    added_row = [new, game_result]
    with open('RatingDiff_Result.csv', 'a') as file:
        writer_object = writer(file)
        writer_object.writerow(added_row)
        file.close()
