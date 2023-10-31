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

    taglist = kuni['tony']

    def devilfruit(x):
        zoro = list (itertools.product(x, repeat = 2))
        return zoro
    sanji = [devilfruit(x) for x in taglist]
    def nami(m): 
        return [i for r in m for i in r ]
    usopp = nami(sanji)

    bepo = [i for i in usopp if i[0] != i[1]]
    c = Counter (zip(bepo))

    brook = pd.DataFrame.from_dict(c, orient = 'index').reset_index()
    brook.columns = ['pairs', 'count']
    brook ['pairs'] = brook ['pairs'].astype('string')
    def robin(s): 
        return s[1:-2]
    brook ['pairs'] = brook ['pairs'].apply(robin)

    def franky (s):
        return s.split(',')[0]

    def chopper (s): 
        return s.split(',')[1]

    brook ['Source'] = brook ['pairs'].apply(franky)
    brook ['Target'] = brook ['pairs'].apply(chopper)

    def rubber(s): 
        return s[2:-1]
    def man (s): 
        return s[2:-2]

    brook ['Source'] = brook ['Source'].apply(rubber)
    brook ['Target'] = brook ['Target'].apply(man)

    stopwords = ['people', 'like', 'would', 'even', 'think', 'get', 'one', 'also', 'br', 'said', 'say', 'thing', 'still', 'could', 'something', 'actually', 'go', 'though', 'anyone']
    strawhat = brook[~brook['Source'].isin (stopwords)]
    mugiwara = strawhat[~strawhat['Target'].isin(stopwords)]
    def iceberg (r): 
        return round (zipf_frequency(r, 'en'),2) 
    mugiwara ['SourceFreq'] = mugiwara ['Source'].apply(iceberg)
    mugiwara ['TargetFreq'] = mugiwara ['Target'].apply(iceberg)
    mugiwara ['freqsum'] = mugiwara['SourceFreq'] + mugiwara['TargetFreq']
    mugiwara.sort_values(by = ['freqsum'])
    array = pd.concat([brook['Source'], brook ['Target']]).unique()
    dc = pd.DataFrame (array).reset_index()
    dc.columns = ['Id', 'Label']
    mydict = dict(map(lambda i,j: (i,j), dc['Label'], dc['Id']))
    def switch (m):
        return mydict[m]
    mugiwara ['SourceId'] = mugiwara ['Source'].apply(switch)
    mugiwara ['TargetId'] = mugiwara ['Target'].apply(switch)
    mugiwara ['Identity'] = file

    mugiwara.to_csv(f'{file}.tsv', sep='\t', header=True, index=False)