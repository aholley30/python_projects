import pandas as pd
import re
from matplotlib import pyplot as plt

# Input data manually from linkedIn
def skill_clarity():
  df = pd.read_csv("skills.csv", names=['Skills', 'Freq'], index_col=0)
  skills = dict(zip(list(df.index), list(df['Freq'])))
  while True:
    user_input = input("Enter skill(s) or q to quit: ")
    if user_input == 'q':
      break
    # attempt to reduce duplicates
    user_input = user_input.lower()

    # remove spaces, turn into array
    user_input = user_input.replace(' ', '')
    user_input = user_input.split(',')
    for i in user_input:
      #i = re.sub(r'\W+', '', i)
      if i == 'js':
        i = 'javascript'
      if i in skills:
        skills[i] += 1
      else:
        skills[i] = 1

  df = pd.DataFrame.from_dict(skills, orient='index')
  df.to_csv('skills.csv')
  # df.plot(kind="bar", title="What Should I Learn?")
  # plt.xticks(rotation=30, horizontalalignment="center")
  # plt.xlabel("Skills")
  # plt.ylabel("Frequency")
  # plt.show()
    
skill_clarity()

def clean_data():
  df = pd.read_csv("skills.csv", names=['Skills', 'Freq'], index_col=0)
  df.drop(df.loc[df['Freq']<=1].index, inplace=True)
  df.sort_values(by=["Freq"], inplace = True)
  df.plot(kind="bar", title="What Should I Learn?")
  #plt.xticks(rotation=30, horizontalalignment="center")
  plt.xlabel("Skills")
  plt.ylabel("Frequency")
  plt.show()

clean_data()
