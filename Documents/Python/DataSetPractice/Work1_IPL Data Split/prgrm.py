#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:48:57 2019

@author: akki
"""
import pandas as pd

data= pd.read_csv('matches.csv')
    

for dt in data['season'].unique():
    main_data=data.where((data.season==dt) & (data.winner==data.toss_winner))
    main_data=data[main_data.id.notnull()]
    main_data.to_csv(str(dt)+'.csv')
            
    



    
