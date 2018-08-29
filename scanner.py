# x_ray.py
# coding: utf-8
# name: Weijian Zheng

# This is the main function

import math
import sys
import subprocess

import scan_all as pre
import parser as parser
import searcher as searcher
import utility as uti
import report as report

# count the number of questions
num_lis = sum(1 for line in open("question.txt"))
num_qns = math.ceil(num_lis/3)

# ask user to enter the path want to search
path = input("Please enter the path want to search: ")
# call cloc first to show some basic info
retcode = subprocess.call(["perl","./cloc-1.76.pl", path])
if retcode == 0:
    print("Passed!")
else:
    print("Failed!")

# read the questions from the text file 
fh = open("question.txt", "r")
(list_qns, list_qrs) = uti.read_questions(num_qns, fh)
fh.close()

# next we need to pre-answer some questions and print results
pre_res = pre.search_all(14, list_qns, list_qrs, path)
report.print_result_all(pre_res)

# variable to count how many queries have been executed
qry_count = 0

while True:

    # Two ways for user to enter a new query: one is to modify the 
    # questions.txt directly, another is to add it from terminal.
    fh = open("question.txt", "r")
    
    # update number of questions 
    num_lis = sum(1 for line in open("question.txt"))
    num_qns = math.ceil(num_lis/3)

    (list_qns, list_qrs) = uti.read_questions(num_qns, fh)
    fh.close()

    if(qry_count == 0):
        report.print_questions(list_qns, list_qrs, num_qns)
            
    qry_count += 1
 
    tmp_input = input("Please enter a number from 1 to " \
            + str(num_qns) + " to select one \
            \n (Quit or Q for exit, ADD or A for adding a new question, LIST or L for list questions): ")
   
    if(tmp_input.lower() == "q" or tmp_input.lower() == "quit"):
        break

    if(tmp_input.lower() == "l" or tmp_input.lower() == "list"):
        report.print_questions(list_qns, list_qrs, num_qns)
        continue

    if(tmp_input.lower() != "a" and tmp_input.lower() != "add"):

        qns_index = int(tmp_input) - 1

        if(qns_index > num_qns or qns_index < 0):
            print("Please enter another correct index number")
            continue

        #next is show user our list of questions and let user select one:
        statement = uti.select_question(list_qns, list_qrs\
                , qns_index)
        #call parser first to parse the FQL query
        (num_fea, list_fea, list_searchFile, list_keywords, \
                list_andOrs, result, stn_type) = parser.parse(statement)

        if(num_fea == 0):
            print("Query is not correct")
            continue

        #call searcher next to find the keywords
        list_true = searcher.find_features(list_fea, list_keywords, \
                num_fea, list_andOrs, path, list_searchFile)

        #prepare to present the result based on types of the sentence
        list_res = uti.return_result(list_true, list_fea, \
                num_fea, stn_type)

        #print result
        num_feature_name = len(list_fea)
        report.print_result(stn_type, list_res, list_true, list_fea)
 
    else:

        uti.add_question()
        

