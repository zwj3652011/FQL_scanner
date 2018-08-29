# scanner.py
# coding: utf-8
# name: Weijian Zheng

# lexical scanner (helped by pyparsing). 
# This program is used to define the format of the FQL statement
# Also, type of the statement can be decided based on tokenized statement

# check_type: check the type of statement, three types now. 

# firstly define the format of our FQL using pyparsing
# Three layers: phrase -> clause -> statement
# Two types of statement: 
# fql_adv: will summarize the information from different CHECK clauses
# fql_reg: without the AS clause

from pyparsing import CaselessKeyword, Combine, Literal, Optional, Word, alphanums, alphas, nums, oneOf, Suppress, OneOrMore 

# First layer: phrases in FQL 
CHECK_KEYWORD = "CHECK"
WHERE_KEYWORD = "WHERE"
AS_KEYWORD = "AS"
LIST_KEYWORD = "LIST"
MAX_KEYWORD = "MAX"
AND_KEYWORD = "AND" # used for hybrid detect
# add HERE if new type statement is needed

check_ = CaselessKeyword(CHECK_KEYWORD)
where_ = CaselessKeyword(WHERE_KEYWORD)
as_ = CaselessKeyword(AS_KEYWORD)
list_ = CaselessKeyword(LIST_KEYWORD)
max_ = CaselessKeyword(MAX_KEYWORD)
and__ = CaselessKeyword(AND_KEYWORD)
# add HERE if new type of statement is needed

underline_ = Literal("_")
space_ = Literal(" ")
or_ = Literal("||")
and_ = Literal("&&")
star_ = Literal("*")
leftb_ = Literal("(")
rightb_ = Literal(")")
leftB_ = Literal("[")
rightB_ = Literal("]")
comma_ = Literal(",")
dot_ = Literal(".")
hashtag_ = Literal("#")
slash_ = Literal("-")
equal_ = Literal("=")

# format of version number for AS clause
version_ = Combine(OneOrMore(Optional(dot_) + Word(nums)))
# format of feature name for AS clause
feature_ = Combine(OneOrMore(Word(alphanums) \
        + Optional(OneOrMore(underline_^space_))))
# this is for the keywords to search 
keyword_ = Optional(OneOrMore(underline_^leftb_^hashtag_^space_^dot_^slash_\
        ^equal_)) + Word(alphanums) + Optional(OneOrMore(underline_^leftb_\
        ^dot_^slash_^equal_))
keywords_ = OneOrMore(Combine(OneOrMore(keyword_)) \
        + Optional(space_) + Optional(or_^and_) + Optional(space_))

# Clauses in FQL
# CHECK clause
check = check_ + Optional(space_) + Suppress(leftb_) + Optional(space_) \
        + keywords_ + Optional(space_) + Suppress(rightb_)
# this is one WHERE clause
file_ext_ = Combine(Literal(".") + Word(alphanums))
where = where_ + Optional(space_) + Suppress(leftb_) + Optional(space_) \
        + OneOrMore(star_^file_ext_ + Optional(comma_)) + Optional(space_) \
        + Suppress(rightb_)
# this is one AS sentence clause
as_s = as_ + Optional(space_) + Suppress(leftb_) + Optional(space_) \
        + OneOrMore(feature_^version_) + Optional(space_) + Suppress(rightb_)
# this is one check clause
check_s = check + Optional(space_) + where + Optional(space_) \
        + Optional(as_s) + Optional(space_)

# Third layer: define the statement, two types of statement here
fql_max = max_ + Suppress(leftb_) + OneOrMore(check_s + Optional(comma_)) \
        + Optional(space_) + Suppress(rightb_) 
fql_adv = OneOrMore(max_^list_^and__) + Suppress(leftb_) + OneOrMore(check_s \
        + Optional(comma_)) + Optional(space_) + Suppress(rightb_)  
fql_reg = Optional(space_) + OneOrMore(check_s + Optional(comma_)) \
        + Optional(space_)

# this function is used to tell user the type of the query
# 0 means it is just a regular CHECK query
# 1 means it is a LIST, 2 means it is a MAX, 
# 3 means it is a AND (used to detect hybrid usage) 
# we will add more later when we have more types
def check_type(stn):
    
    str_test = stn.split(" ") 
    stn_type = 0
    if(str_test[0] == "LIST"):
        stn_type = 1
    if(str_test[0] == "MAX"):
        stn_type = 2
    if(str_test[0] == "AND"):
        stn_type = 3
    
    return stn_type
