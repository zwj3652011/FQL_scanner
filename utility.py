# utility.py
# coding: utf-8
# name: Weijian Zheng

# This program is generally include some functions to do 
# pre-processing and post-processing

# read_questions: used to read the questions from the text file
# select_question: used to let user select one question
# print_result: print the result to the user  

import math
import parser as parser

# this function is used to read questions and queries from the text file
def read_questions(num_questions, fh):
    
    list_questions = ()
    list_queries = ()

    for i in range (0, num_questions):
        
        temp_stn = fh.readline().split(" ")
        remove_temp = temp_stn[0]
        temp_stn.remove(remove_temp)
    
        temp_str = ""
        temp_str = " ".join(temp_stn)
    
        list_questions = list_questions + (temp_str,)
    
        temp_stn = fh.readline()
        temp_stn = temp_stn[5:]
        temp_stn = temp_stn[:-1]
  
        list_queries = list_queries + (temp_stn,)
        empty_line = fh.readline()
    
    return (list_questions, list_queries)

# this function is used to show user the questions we have and let user select one
def select_question(list_questions, list_queries, q_index):
    
    fh = open("question.txt", "r")
    
    # count the number of questions
    num_lines = sum(1 for line in open("question.txt"))
    num_questions = math.ceil(num_lines/3)

    fh.close() 

    list_queries[q_index]
    query = list_queries[q_index]
    
    return query

# this function is used to return the result based on types of the sentence
def return_result(list_true, list_features, num_features, stn_type):
    if(stn_type == 1):
        list_result = []
        for i in range(0, num_features):
            if(list_true[i] == True):
                list_result.append(list_features[i]) 
        return list_result
    if(stn_type == 2):
        change_or_not = 0
        newest_version = list_features[0]
        for i in range(0, num_features):
            if(list_features[i] <= newest_version):
                newest_version = list_features[i]
 
        for i in range(0, num_features):
            if(list_features[i] >= newest_version and list_true[i] == True):
                newest_version = list_features[i]
                change_or_not = 1
        
        if(change_or_not == 1):       
            return newest_version
        else: 
            return "not_found" 

    return list_true

# this function is used to add new question
def add_question():
    
    fh = open("question.txt", "a")
        
    # count the number of questions
    num_lines = sum(1 for line in open("question.txt"))
    num_questions = math.ceil(num_lines/3)

    #else here is used to add questions: 
    temp_input = input("Please enter a question: ")
    question_str = "Q" + str(num_questions+1) + ": " + temp_input + "\n"
       
    # A while loop, stop until user enter a correct query 
    follow_format = False
    while (follow_format == False):
        temp_input = input("Please enter the FQL query: (Q and Quit for quit) ")
        
        if(temp_input.lower() == "q" or temp_input.lower() == "quit"):
            fh.close()
            return

        follow_format = parser.parse_test(temp_input)
        
    query_str = "FQL: " + temp_input + "\n"

    fh.write(question_str)
    fh.write(query_str)
    fh.write("\n")

    fh.close()

