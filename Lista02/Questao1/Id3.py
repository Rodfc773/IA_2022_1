import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import copy

dataset = pd.read_csv('Lista02/Questao1/tennis.csv')
X = dataset.iloc[:, 1:].values
# print(X)
attribute = ['Historia de Crédito', 'Dívida', 'Garantia', 'Renda']

class Node(object):
    def __init__(self):
        self.value = None
        self.decision = None
        self.childs = None


def findEntropy(data, rows):
    Alto = 0
    Moderado = 0
    Baixo = 0
    ans = -1
    idx = len(data[0]) - 1
    entropy = 0
    for i in rows:
        if data[i][idx] == 'Alto':
            Alto = Alto + 1
        elif data[i][idx] == 'Baixo':
            Baixo = Baixo + 1
        else:
            Moderado = Moderado + 1

    x = Alto/(Alto+Baixo + Moderado)
    y = Baixo/(Alto+Baixo + Moderado)
    z = Moderado/(Alto + Baixo + Moderado)
    if x != 0 and y != 0 and z != 0:
        entropy = -1 * (x*math.log2(x) + y*math.log2(y) + z*math.log2(z))
    if x == 1:
        ans = "Alto"
    if y == 1:
        ans = "Baixo"
    if z == 1:
        ans = "Moderado"
        
    print("Resultado da Entropia(S): {}".format(entropy))

    return entropy, ans


def findMaxGain(data, rows, columns):
    maxGain = 0
    retidx = -1
    entropy, ans = findEntropy(data, rows)
    if entropy == 0:
        """if ans == 1:
            print("Yes")
        else:
            print("No")"""
        return maxGain, retidx, ans

    for j in columns:
        mydict = {}
        idx = j
        for i in rows:
            key = data[i][idx]
            if key not in mydict:
                mydict[key] = 1
            else:
                mydict[key] = mydict[key] + 1
        gain = entropy

        # print(mydict)
        for key in mydict:
            Alto = 0
            Baixo = 0
            Moderado = 0
            for k in rows:
                if data[k][j] == key:
                    if data[k][-1] == 'Alto':
                        Alto = Alto + 1
                    elif data[k][-1] == 'Moderado':
                        Moderado = Moderado + 1
                    else:
                        Baixo = Baixo + 1
            # print(yes, no)
            x = Alto/(Alto+Baixo+Moderado)
            y = Baixo/(Alto+Baixo+Moderado)
            z = Moderado/(Alto+Baixo + Moderado)
            # print(x, y)
            
            #ele faz entropia com o novo ganho reduzindo seu valor
            if x != 0 and y != 0 and z != 0:
                gain += (mydict[key] * (x*math.log2(x) + y*math.log2(y) + z*math.log2(z)))/14
        # print(gain)
        if gain > maxGain:
            # print("hello")
            maxGain = gain
            retidx = j

    return maxGain, retidx, ans


def buildTree(data, rows, columns):

    maxGain, idx, ans = findMaxGain(X, rows, columns)
    root = Node()
    root.childs = []
    # print(maxGain )
    if maxGain == 0:
        if ans == "Alto":
            root.value = 'Alto'
        elif ans == "Moderado":
            root.value = 'Moderado'
        else:
            root.value = 'Baixo'
        return root

    root.value = attribute[idx]
    mydict = {}
    for i in rows:
        key = data[i][idx]
        if key not in mydict:
            mydict[key] = 1
        else:
            mydict[key] += 1

    newcolumns = copy.deepcopy(columns)
    newcolumns.remove(idx)
    for key in mydict:
        newrows = []
        for i in rows:
            if data[i][idx] == key:
                newrows.append(i)
        # print(newrows)
        temp = buildTree(data, newrows, newcolumns)
        temp.decision = key
        root.childs.append(temp)
    return root

def traverse(root):
    print("Root: {}\n".format(root.decision))
    print("Valor: {}".format(root.value))

    # print(root.decision)
    # print(root.value)

    n = len(root.childs)
    if n > 0:
        for i in range(0, n):
            traverse(root.childs[i])

def calculate():
    rows = [i for i in range(0, 14)]
    columns = [i for i in range(0, 4)]
    root = buildTree(X, rows, columns)
    root.decision = 'Start'
    traverse(root)


calculate()
