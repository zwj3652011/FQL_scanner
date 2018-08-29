# scan_all.py
# coding: utf-8
# name: Weijian Zheng

# This program is used for the first scan

import parser as parser
import searcher as searcher
import utility as uti

# scan code for all features listed in question.txt
def search_all(num_questions, list_questions, list_queries, path):
    
    query_count = 0
    pre_result = []     

    for i in range (0, num_questions):
        #print (str(i+1) + ": " + list_questions[i])

        #then we need to return the query         
        statement = list_queries[i] 
        query_count += 1

        #call parser first to parse the FQL query
        (num_features, list_features, list_searchFile, list_keywords, \
                list_andOrs, result, stn_type) = parser.parse(statement)

        if(num_features == 0):
            print("Query is not correct")
            pre_result.append()
            continue

        #call searcher next to find the keywords
        list_true = searcher.find_features(list_features, list_keywords, \
            num_features, list_andOrs, path, list_searchFile)

        #prepare to present the result based on types of the sentence
        list_result = uti.return_result(list_true, list_features, \
            num_features, stn_type)

        pre_result.append(list_result) 
     
    return pre_result 
