import os
import pandas as pd

# hardcode the folder names
#CHANGE
data_folders = ['all',
 'bed',
 'before',
 'black',
 'blue',
 'book',
 'bowling',
 'can',
 'candy',
 'chair',
 'clothes',
 'computer',
 'cool',
 'cousin',
 'deaf'
 'dog',
 'drink',
 'family',
 'fine',
 'finish',
 'fish',
 'go',
 'graduate',
 'like',
 'hat',
 'hearing',
 'help',
 'hot',
 'kiss',
 'language',
 'later',
 'like',
 'man',
 'many',
 'mother',
 'no',
 'now',
 'orange',
 'table',
 'thanksgiving',
 'thin',
 'walk',
 'what',
 'who',
 'woman',
 'year',
 'yes'
 ]


data_folders = ['all',
 'bed']

# array of arrays, containing the list files, grouped by folder
filenames = [os.listdir(f) for f in data_folders]
print(filenames)
# [print(f[1]) for f in filenames]
# [len(f) for f in filenames]
print("DONE")

files_dict = dict(zip(data_folders, filenames))

# CHANGE
# base_gcs_path = 'gs://cloudml-demo-vcm/chairs_table_bike/'
base_gcs_path = 'gs://asl_video2'


# What we want:
# gs://cloudml-demo-vcm/chairs_table_bike/chair_black/chair_black157.jpg, 'chair_black'
# base_gcs_path + dict_key + '/' + filename

data_array = []

for (dict_key, files_list) in files_dict.items():
    for filename in files_list:
#         print(base_gcs_path + dict_key + '/' + filename)
        if '.mp4' not in filename:
            continue # don't include non-photos

        label = dict_key
#         label = 'chair' if 'chair' in dict_key else dict_key # for grouping all chairs as one label

        data_array.append((base_gcs_path + dict_key + '/' + filename , label))

print(data_array)
dataframe = pd.DataFrame(data_array)
dataframe.to_csv('all_data.csv', index=False, header=False)
# gsutil cp all_data.csv gs://asl_video2
