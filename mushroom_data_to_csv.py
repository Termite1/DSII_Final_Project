# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:08:06 2024

@author: samda
"""
import csv
  

file = 'agaricus-lepiota.data'

#number of categories for each column
numCats = {0: 2,
            1: 6,
            2: 4,
            3: 10,
            4: 2,
            5: 9,
            6: 4,
            7: 3, 
            8: 2,
            9: 12,
            10: 2,
            11: 7,
            12: 4,
            13: 4,
            14: 9,
            15: 9,
            16: 2,
            17: 4,
            18: 3, 
            19: 8,
            20: 9,
            21: 6,
            22: 7}

#column titles
col_dict = {0: "edible",
            1: "cap-shape",
            2: "cap-surface",
            3: "cap-color",
            4: "bruises",
            5: "odor",
            6: "gill-attachment",
            7: "gill-spacing", 
            8: "gill-size",
            9: "gill-color",
            10: "stalk-shape",
            11: "stalk-root",
            12: "stalk-surface-above-ring",
            13: "stalk-surface-below-ring",
            14: "stalk-color-above-ring",
            15: "stalk-color-below-ring",
            16: "veil-type",
            17: "veil-color",
            18: "ring-number", 
            19: "ring-type",
            20: "spore-print-color",
            21: "population",
            22: "habitat"}

output = []

data_dictionary = [None] * 23

#Generates seperate dictionaries. Otherwise changes to one dictionary would change them all
for h in range(len(data_dictionary)):
    data_dictionary[h] = {}

data_dictionary[0].update({'e': 0, 'p': 1})

#opens file as openfile object
with open(file, 'r') as openfile:
    #runs for each line in the file
    for line in openfile:
        #splits line into indevidual characters in a list
        current_line = line.split(",")
        #Shouldn't matter,  but this removes the newline character from the last attribute
        current_line[-1] = current_line[-1][0] 
        
        length = len(current_line)
        
        data_line = [0] *  length
        
        #Makes list appropriate size with sublists of appropriate size for each category
        for i in range(length):
            data_line[i] = [0] * (numCats[i] - 1)
        
        #Runs through each line
        for j in range(length):
            #Checks if entry is in dictionary
            if current_line[j] in data_dictionary[j]:
                #If entry is 0 (base value) continues since all values are 0 by default, indicateing the base value
                if data_dictionary[j][current_line[j]] == 0: continue
                else:
                    #Otherwise the appropriate entry is marked with a 1
                    #temp_col is used to aquire the correct column from the dictionary.
                    temp_col = data_dictionary[j][current_line[j]] - 1
                    data_line[j][temp_col] = 1
            #Adds to dictionary then updates if newest item isn't in the dictionary
            else:
                data_dictionary[j].update({current_line[j]: len(data_dictionary[j])})
                if data_dictionary[j][current_line[j]] == 0: continue
                else: 
                    temp_col = data_dictionary[j][current_line[j]] - 1    
                    data_line[j][temp_col] = 1
        
        #used to build list that is added to the output
        temp_line = []
        for category in data_line:
            temp_line = temp_line + category
        
        #adds line to output
        output.append(temp_line)
        
    #used to build header
    header = []
    
    #Turns dictionaries into lists of their values so indexies can be extracted
    data_dict_list = [None] * length
    for d in range(length):
        data_dict_list[d] = list(data_dictionary[d].keys())
    
    #Constructs header line
    #repeates for each column
    for k in range(length):
        #repeats for each category in each column
        for l in range(len(data_dictionary[k]) - 1):            
            temp_header = col_dict[k] + ": " + data_dict_list[k][l + 1]
            header.append(temp_header)    

    output.insert(0, header)  

    
    #open file to write into
    out_file = open('mushroom_data.csv', 'w+', newline='')
    
    # writing the data into the file
    with out_file:    
        write = csv.writer(out_file)
        write.writerows(output)
        