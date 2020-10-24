import os

def create_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
    print("Created Directory : ", dir)
  else:
    print("Directory already existed : ", dir)
  return dir

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

for dir in data_folders:
    print("the dir is: " + dir)
    create_dir(dir)

print("DONE")
