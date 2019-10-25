#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 01:13:51 2019

@author: felipe
"""

import pandas as pd

data = pd.read_csv("dados.csv",  sep=';')
data.set_index('Região', inplace=True)
df=data.transpose()
df.drop('Total', axis=0, inplace=True)
df.drop('Total', axis=1, inplace=True)

#fig, ax = plt.subplots()
#df.plot(y='1 Região Norte', use_index=True)

ax=df.plot(use_index=True)
ax.set_title("Mortalidade infantil")
ax.set_ylabel('Número de óbitos')


