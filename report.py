# report.py
# coding: utf-8
# name: Weijian Zheng

# This program is to print out of HPC related features
# in one table

import report_uti as print_uti

def print_result_all(pre_result):
    
    (MPI_str, version_str_mpi, oneSide_str_mpi, topology_str_mpi, \
            io_str_mpi) = print_uti.read_mpi_result(pre_result)

    print("{0:<80}".\
            format("\nHPC Related Features:"))
    
    print("----------------------------------------------\
----------------------------------")

    print("{0:<14}{1:>33}{2:>33}".\
            format("MPI:","Min Version Required:","One-sided Communication:"))
       
    print("{0:<14}{1:>33}{2:>33}".\
            format(MPI_str,version_str_mpi,oneSide_str_mpi))

    print("")

    print("{0:<14}{1:>33}{2:>33}".\
            format("","MPI Process Topology:","MPI-IO:"))

    print("{0:<6}{1:>41}{2:>33}".\
            format("", topology_str_mpi, io_str_mpi))

    print("----------------------------------------------\
----------------------------------")

    print("{0:<14}{1:>33}{2:>33}".\
            format("OpenMP:","Hybrid MPI/OpenMP:","Task Programming Construct:"))

    (openmp_str, task_const_mp, schedule_str_mp, hybrid_mp_str) \
            = print_uti.read_openmpi_result(pre_result)
    
    print("{0:<14}{1:>33}{2:>33}".\
            format(openmp_str, hybrid_mp_str, task_const_mp)) 
        
    print("")

    print("{0:<6}{1:>74}".\
            format("", "Scheduling Method:"))

    print("{0:<6}{1:>74}".\
            format("", schedule_str_mp))

    print("----------------------------------------------\
----------------------------------")

    print("{0:<14}{1:>33}{2:>33}".\
            format("CUDA:","Support Multiple GPUs:","Single/Double Precision:"))

    (cuda_str, multiple_str_cuda, precision_cuda_str) \
            = print_uti.read_cuda_result(pre_result)

   
    print("{0:<14}{1:>33}{2:>33}".\
            format(cuda_str,multiple_str_cuda,precision_cuda_str))

    print("----------------------------------------------\
----------------------------------")

    print("{0:<14}{1:>33}{2:>33}".\
            format("OpenACC","",""))

    acc_str = print_uti.read_acc_result(pre_result)
    
    print("{0:<14}{1:>33}{2:>33}".\
            format(acc_str,"",""))

    print("----------------------------------------------\
----------------------------------")

    print("{0:<14}{1:>33}{2:>33}".format("C","Min C Compiler Version:",""))

    ansi_c_str = print_uti.read_c_result(pre_result)
    
    print("{0:<14}{1:>33}{2:>33}".\
        format("", ansi_c_str, ""))

    print("----------------------------------------------\
----------------------------------")
    
    fortran_str = print_uti.read_fortran_result(pre_result)
            
    print("{0:<14}{1:>33}{2:>33}".\
            format("Fortran","Fortran Standard:",""))

    print("{0:<14}{1:>33}{2:>33}".\
        format("",fortran_str,""))

    print("----------------------------------------------\
----------------------------------")

# print function here for print one question's result:
def print_result(stn_type, list_result, list_true, list_features):

    print("===================================================\
==============")

    num_features = len(list_features)

    if(stn_type == 0 and num_features > 0):
        if(list_result[0] == True):
            print ('{:<40}'.format("Feature " +  list_features[0]) \
               + '{:>25}'.format(" : Found in the code"))
        else:
            print ('{:<40}'.format("Feature " +  list_features[0]) \
               + '{:>25}'.format(" : Not found in the code"))
    elif(stn_type == 0):
        if(list_result[0] == True):
            print ('{:<40}'.format("Feature desired") \
               + '{:>25}'.format(" is Found in the code"))
        else:
            print ('{:<40}'.format("Feature desired") \
               + '{:>25}'.format(" is Not found in the code")) 
    elif(stn_type == 2 and list_result != "not_found"):
        print ('{:<40}'.format("The minimum version requirement is " \
                +  list_result))
    elif(stn_type == 3 and list_result == "not_found"):
        print ('{:<40}'.format("Feature is not found "))
    else:
        for i in range(0, num_features):
            if(list_true[i] == True):
                print ('{:<40}'.format("Feature " +  list_features[i]) \
                   + '{:>25}'.format(" : Found in the code"))
            else:
                print ('{:<40}'.format("Feature " +  list_features[i]) \
                   + '{:>25}'.format(" : Not found in the code"))
        
    print("===================================================\
==============")

# print result, used for LIST command
def print_questions(list_qns, list_qrs, num_qns):
    
    print ("\nQuestions we have now are: \n")    
    for i in range (0, num_qns):
        print (str(i+1) + ": " + list_qns[i])
