# parser.py
# coding: utf-8
# name: Weijian Zheng

# This program is used to tanaslate an tokenized FQL statement 
# into a list of keywords, 

# semantic: used to do semantic analysis of the code
# parse: combine the lexical analyzer and the semantic analyzer  

from fql_lang import * 

# semantic analyzer: input is the tokenized string
def semantic(result, stn_type):
    # num_check is used to measure how many CHECKs in our FQL statement
    num_check = 0
    
    # A list of tuples for keywords
    list_keywords = []
    # List of tuples for AND/OR relationship, now most cases are OR 
    list_andOrs = []
    # List of feature names
    list_features = ()
    # List to show the file extension to search for each feature, 
    # now support different files
    list_searchFile = []

    # A flag to tell program what is the category of next phrase 
    # 0 is the default value, 
    # 1 means it is a keyword
    # 2 means it is a reserved keyword 
    # 3 means it is the first file extension
    # 4 means it is a feature name 
    # 5 means it is another file extension	
    next_word = 0
    # j here is just used to debug and check whether  
    # we have visited all words in a statement
    j = 0
    for i in range (0, len(result)):
        j = j + 1
        #handle 1st phrase in FQL
        if(stn_type != 0 and i == 0):
            next_word = 2
            continue
        #find a CHECK keyword
        if(result[i] == check_ and (next_word == 2 or stn_type == 0)):
            # create a temp tuple for later add keywords 
            temp = ()
            next_word = 1
            #create a temp tuple for logic relationship between keywords
            temp_andOr = ()
            num_check += 1
            continue
        #find a keyword to search
        if(next_word == 1):
            temp = temp + (result[i],)
            next_word = 2
            # get to the last keyword    
            if(result[i+1] != or_ and result[i+1] != and_):
                list_keywords.append(temp)
                list_andOrs.append(temp_andOr)
            continue
        #find a logic relationship description
        if(result[i] == or_ or result[i] == and_ and next_word == 2):
            temp_andOr = temp_andOr + (result[i],)
            next_word = 1
            continue
        #now we find a WHERE keyword
        if(result[i] == where_ and next_word == 2):
            temp = ()
            next_word = 3
            continue
        #now we come to a file extension description
        if(next_word == 3):
            #print(result[i])
            temp = temp + (result[i],)
            if(i+1 >= len(result)):
                list_searchFile.append(temp)
                continue
            if(result[i+1] != ","):
                list_searchFile.append(temp)
                next_word = 2
                #print(str(len(list_searchFile)))
            if(result[i+1] == "," and result[i+2] != as_ \
                    and result[i+2] != check_):
                next_word = 5
            continue 
        # find a AS keyword
        if(result[i] == as_ and next_word == 2):
            next_word = 4
            continue
        # add feature name
        if(next_word == 4):
            list_features = list_features + (result[i],)
            next_word = 2
            continue
        # prepare to do another CHECK sentence
        if(result[i] == dot_ and next_word == 2):
            next_word = 2
            continue
        # prepare to parse another file extension
        if(next_word == 5):
            next_word = 3
            continue
    
    return (num_check, list_features, list_searchFile, list_keywords, list_andOrs) 

# combine lexical analyzer and semantic analyzer
def parse(FQL_str):
    try:
        # check type of the statement first:
        stn_type = check_type(FQL_str)
	# two steps here: 
        # first step is to tokenize (with the help of pyparsing)
        if(stn_type > 0):
            result = fql_adv.parseString(FQL_str)
        else:
            result = fql_reg.parseString(FQL_str)
        # second step here is to do semantic analysis
        (num_check, list_features, list_searchFile, list_keywords, \
                list_andOrs) = semantic(result, stn_type)
    except Exception:
        print("parse error")
        return (0, (), (), (), (), (), 0)   

    return (num_check, list_features, list_searchFile, list_keywords, \
            list_andOrs, result, stn_type)

# test whether newly added query follow the grammar of FQL
def parse_test(test_str):

    try:
        # check type of the statement first:
        stn_type = check_type(test_str)
	# two steps here: 
        # first step is to tokenize (with the help of pyparsing)
        if(stn_type > 0):
            result = fql_adv.parseString(test_str)
        else:
            result = fql_reg.parseString(test_str)
        # second step here is to do semantic analysis
        (num_check, list_features, list_searchFile, list_keywords, \
                list_andOrs) = semantic(result, stn_type)
        print("it was tested correctly")
        return True
    except Exception:
        print("New query is not follow the format!")
        return False 


