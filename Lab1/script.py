# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:49:21 2020

@author: delli
"""
import numpy as np
f = open("DataSet/Text0300.txt", "r")
text1 = f.read().replace('\n', '').replace('\t','').replace('  ', ' ')
f = open("DataSet/Text0342.txt", "r")
text2 = f.read().replace('\n', '').replace('\t','').replace('  ', ' ')
f = open("DataSet/Text0300-1.txt", "r")
text3 = f.read().replace('\n', '').replace('\t','').replace('  ', ' ')


def shingling(text, k):
    shin = set()
    for i in range(len(text)):
        shin.add(hash(text[i:i+k]))
    return shin
"""
def convertToInt(sets):
    union = sets[0]
    
    new_sets = []
    for s in sets:
        union |= s
        
    d = {ni: indi for indi, ni in enumerate(set(union))}
    
    for s in sets:
        numbers = [d[ni] for ni in s]
        new_sets.append(set(numbers))
    return new_sets
"""

def compareSets(set1, set2):
    intersection = set1.intersection(set2)
    union = set1 | set2
    js = len(intersection) / len(union) 
    return js

def hash1(x):
    return (2*x +1) % 619
def hash2(x):
    return (3*x +2) % 619
def hash3(x):
    return (5*x +3) % 619

def MinHasing(sets, union):
    
    k = [hash1, hash2, hash3]
    M = np.zeros((len(union), len(sets)))
    for i,u in enumerate(union):
        for j,s  in enumerate(sets):
            M[i,j] = 1 * (u in s)
            
    C  = np.ones((len(k), len(sets))) * np.inf
    
    print(M.shape)
    
    
    for i in range(M.shape[1]):
        S = M[:,i]
        for idx, x in enumerate(S):
            if x == 1:
                for j in  range(len(k)):
                    h = k[j](idx)
                    if(h < C[j][i]):
                        C[j][i] = h
             
    return C
                    
    
        

    




k = 3

set1 = shingling(text1, k)
set2 = shingling(text2, k)
set3 = shingling(text3, k)
"""
sets = [set1,set2,set3]
set1, set2, set3 = convertToInt(sets)
"""
dist = compareSets(set1,set2)
print("set1 - set2", dist)
dist = compareSets(set1,set3)
print("set1 - set3",dist)

print("After Hashing")
union = set1 | set2
sets = [set1,set2]
C= MinHasing(sets, union)
dist = compareSets(set(C[:,0]), set(C[:,1]))
print("set1 - set2", dist)

union = set1 | set3
sets = [set1,set3]
C= MinHasing(sets, union)
dist = compareSets(set(C[:,0]), set(C[:,1]))
print("set1 - set3",dist)