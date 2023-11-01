#!/usr/bin/env python3
import pandas as pd
import regex as re
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
import argparse
import re, os
import itertools
from collections import Counter
from wordfreq import zipf_frequency

def parse_args():
    parser = argparse.ArgumentParser(description='Create a dataset.')
    parser.add_argument('-f', '--file', help='filename', required=True, type=str)
    args = parser.parse_args()
    return(args)

if __name__== "__main__" :
    args = parse_args()

    #if not os.path.isdir(args.out):
        #os.mkdir(args.out)
    
    file = args.file

    df = pd.read_json(file, lines=True)

    wano = df.drop(columns = ['channel', 'photo', 'heart', 'time_parsed'])
    wano ['text'] = wano ['text'].astype('string')

    def jelly (str): 
       return str.lower()

    wano ['text'] = wano ['text'].apply(jelly)
    wano ['len'] = wano ['text'].apply(len)
    momo = wano
    momo['text'] = \
    momo['text'].map(lambda x: re.sub('[,\.!?&#]', '', x))
    def jelly (str): 
        return str.lower()
    momo ['text'] = momo['text'].apply(jelly)
    momo['len'] = momo['text'].apply(len)
    momo.sort_values(by = ['len'])
    kuni = momo[momo['len'] >11]
    kuni.sort_values(by = ['len'])

    def tokenize(tea):
        return nltk.tokenize.word_tokenize(tea)
    kuni['tokens'] = kuni['text'].apply(tokenize)

    def garp (list):
        lista = [i for i in list if i.isalpha() == True]
        liste = [i for i in lista if len(i) > 1]
        return [i for i in liste if i not in stopwords.words('english')]
    kuni ['tony'] = kuni['tokens'].apply(garp)
   
    kuni.to_csv(f'{file}oops.tsv', sep='\t', header=True, index=False)