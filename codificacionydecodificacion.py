# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:53:26 2021

@author: sigri
"""

def RLE(data):

  if len(data) == 0:

    return []

  index = 1

  while index < len(data) and data[index] == data[index - 1]:

    index = index + 1

  encoded_data = [data[0],index]

  return encoded_data + RLE(data[index:len(data)])
s = "AAAABBBBABBBBAAA"

print(RLE(s))

# decofica una lista

index = 0

decoded_list = []



def RLD(lista):

  if index == len(lista):

    return decoded_list

  for i in range(lista[index + 1]):

      decoded_list.append(lista[index])    

  return RLD(lista[index + 2:len(lista)])





encoded_list = ["A",8,"B",4,"A",1,"B",3]

print(encoded_list)

print(RLD(encoded_list))
    