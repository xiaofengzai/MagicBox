#!/usr/bin python
import pandas as pd
import sys

def xlsx_to_csv_pd(source,target):
    """ translate Excel to csv"""
    data_xls = pd.read_excel(source, index_col=0)
    data_xls.to_csv(target, encoding='utf-8')


if __name__ == '__main__':
    source = raw_input('Enter your absolue file path:\n');
    target = raw_input('Enter your output csv name:\n'); 
    if source.strip() == '' or target.strip() == '':
        sys.exit(1)
    xlsx_to_csv_pd(source,target) 