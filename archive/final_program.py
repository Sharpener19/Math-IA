import pandas as pd
import numpy as np

# Final Program 6

input_csv = pd.read_csv('RD_R_Clear.csv')
list = []

rating_diff = 100000
result_sum = 0.0
duplicate_count = 1
avg_score = 0.5
previous_rating_diff = 100000000.0
previous_result = -1000000.0
# arbitrary values

for i, row in input_csv.iterrows():
    if previous_rating_diff == row['rating_diff_W-B']:
        result_sum += previous_result
        previous_result = row['result']
        duplicate_count += 1
        if i == len(input_csv) - 1:
            result_sum += previous_result
            avg_score = result_sum / duplicate_count
            rating_diff = previous_rating_diff
            list.append([rating_diff, avg_score])
    else:
        if duplicate_count > 1:
            result_sum += previous_result
            avg_score = result_sum / duplicate_count
            rating_diff = previous_rating_diff
            list.append([rating_diff, avg_score])
            duplicate_count = 1
            result_sum = 0.0
        elif i > 0:
            list.append([previous_rating_diff, previous_result])

        previous_rating_diff = row['rating_diff_W-B']
        previous_result = row['result']

        if i == len(input_csv) - 1:
            list.append([previous_rating_diff, previous_result])

np.savetxt('SampleOutput.csv', list, delimiter=',', fmt='% s')