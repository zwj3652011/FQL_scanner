# searcher.py
# coding: utf-8
# name: Weijian Zheng

# This program is generally used for intermediate results generator parts 

# list_files: used to list files recursively
# search_words: used to search keyword in a file
# find_features: combine list_files and search_words to find features

from glob import glob
import os

# given a path, this function is used to return a list files that we need to search
def list_files(path, list_searchFile, feature_index):
    #create a list of files in the current folder
    files_list = []
    
    if(len(list_searchFile[feature_index]) == 1 \
            and list_searchFile[feature_index][0] == '*'):
        #print(feature_index)
        for filename in glob(path + '/**/*', recursive=True):       
            if(os.path.isfile(filename)):
                files_list.append(filename)
    else:
        num_ext = len(list_searchFile[feature_index])
        for i in range (0, num_ext):
            for filename in glob(path + '/**/*' \
                    + list_searchFile[feature_index][i], recursive=True):       
                if(os.path.isfile(filename)):
                    files_list.append(filename)
    
    return files_list 

# search the keyword in a file
def search_words(read_file, search_word):
    count = 0
    with open(read_file, encoding = "ISO-8859-1") as f:
        for line in f.readlines():
            check_line = line.lower()
            search_keyword = search_word.lower()
            if search_keyword in check_line:
                count += 1
		#break here is used to accelerate the search process
                break 
                   
    return count

# combine the listing file and the keyword searching function
def find_features(list_features, list_keywords, num_features, \
        list_andOrs, path, list_searchFile):
    
    #print ("There are " + str(len(list_features)) + " features")
    list_true = [False] * num_features

    #find keyword in each file 
    #here used a slow way
    for i in range(0, num_features):
        #first step is to list all files
        files_list = list_files(path, list_searchFile, i)
        #second step is to search keyword in files
        for files in files_list:
            for j in range(0, len(list_keywords[i])):
                #print("search keywords: " + list_keywords[i][j] \
                        #+ " for feature " + list_features[i])
                count = search_words(files, list_keywords[i][j])
                #after search, return its value
                if(count > 0):
                    list_true[i] = True
                    continue
    
    return list_true
