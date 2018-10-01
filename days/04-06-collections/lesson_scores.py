import pandas as pd
from collections import namedtuple, Counter


def convert_xls_into_dict(file_name):

    df = pd.read_excel(file_name, skip_blank_lines=False)

    df = df.fillna('None')

    uroks_dict = {urok[0]:[digit for digit in urok[1:-1] if type(digit) == int or ',' in digit] 
                  for urok in df.values[2:14]}
    
    uroks_dict = {urok: align_scores_in_list(raw_scores_list) for urok, raw_scores_list in uroks_dict.items()}
    
    return uroks_dict

def align_scores_in_list(raw_scores_list):
    aligned_list = []
    for score in raw_scores_list:
        if type(score) == int:
            aligned_list.append(score)
        else:
            aligned_list += [int(digit) for digit in score.split(',')]
    return aligned_list

def average_score(list_of_scores):
   try:
       return round(sum(list_of_scores)/len(list_of_scores), 1)
   except ZeroDivisionError:
       print('No scores!')

def make_report(uroks):
    Urok = namedtuple('Urok', 'Name Scores Average_score')
    for k,v in uroks.items():
        urok = Urok(Name=k, Scores=v, Average_score=average_score(v))
        print(urok.Name)
        print(urok.Scores)
        print(urok. Average_score)
        print('-'*40)

if __name__ == "__main__":
    file_name = "/home/python/Downloads/lessons.xls"
    make_report(convert_xls_into_dict(file_name))


