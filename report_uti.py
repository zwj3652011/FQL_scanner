# print_util.py
# coding: utf-8
# name: Weijian Zheng

# This program is used to read result and prepare for print

# read__result
# read from pre_result and return several strings

def read_mpi_result(pre_result):

    if(str(pre_result[0])!= "not_found"):
        MPI_str = "Yes"
        version_str_mpi = str(pre_result[0])
        oneSide_str_mpi = "Yes" if pre_result[1][0] == True else "No"
        topology_str_mpi = ""
        if(len(pre_result[2]) > 0):
            for i in range (0, len(pre_result[2])-1):
                topology_str_mpi += str(pre_result[2][i])
                topology_str_mpi += ", "
            topology_str_mpi += str(pre_result[2][len(pre_result[2])-1])
        else: 
            topology_str_mpi = "None"
        # IO_str here
        io_str_mpi = "Yes" if pre_result[10][0] == True else "No"
    else:
        MPI_str = "No" 
        version_str_mpi = "--"
        oneSide_str_mpi = "--"
        topology_str_mpi = "--"
        io_str_mpi = "--"

    return (MPI_str, version_str_mpi, oneSide_str_mpi, \
            topology_str_mpi, io_str_mpi)

def read_openmpi_result(pre_result):
    
    if(pre_result[3][0] == True):
        openmp_str = "Yes"
        task_const_mp = "Yes" if pre_result[5][0] == True else "No"
        schedule_str_mp = ""
        if(len(pre_result[4]) > 0):
            for i in range(0, len(pre_result[4])-1):
                schedule_str_mp += str(pre_result[4][i])
                schedule_str_mp += ", "
                schedule_str_mp += str(pre_result[4][len(pre_result[4])-1])
        else:
            schedule_str_mp = "Default"
        # add hybrid_mp_str value 
        hybrid_mp_str = "Yes"
        for i in range (0, len(pre_result[9])):
            if(pre_result[9][i] == False):
                hybrid_mp_str = "No" 
    else:  
        openmp_str = "No" 
        task_const_mp = "--"
        schedule_str_mp = "--"                      
        hybrid_mp_str = "--"

    return (openmp_str, task_const_mp, schedule_str_mp, hybrid_mp_str)

def read_cuda_result(pre_result):
   
    if(pre_result[6][0] == True):
        cuda_str = "Yes"
        multiple_str_cuda = "Yes" if pre_result[7][0] == True else "No" 
        # add single/double precision here, it is not exactly now
        precision_cuda_str = "--"
        if(len(pre_result[11]) > 0):
            if(len(pre_result[11]) == 2):
                precision_cuda_str = "Both"
            else:
                precision_cuda_str = pre_result[11][0] 
    else: 
        cuda_str = "No"
        multiple_str_cuda = "--"
        precision_cuda_str = "--"
    
    return (cuda_str, multiple_str_cuda, precision_cuda_str)


def read_acc_result(pre_result):

    if(pre_result[8][0] == True):
        acc_str = "Yes"
    else:
        acc_str = "No"

    return acc_str

def read_c_result(pre_result):
    
    ansi_c_str = "--"
    
    if(len(pre_result[12]) > 0): 
        if(str(pre_result[12]) == "110"):
            ansi_c_str = "C11"
        if(str(pre_result[12]) == "099"):
            ansi_c_str = "C99"
        if(str(pre_result[12]) == "089"):
            ansi_c_str = "C89" 

    return ansi_c_str

def read_fortran_result(pre_result):

    fortran_str = "--"

    if(len(pre_result[13]) > 0): 
        if(str(pre_result[13]) == "108"):
            fortran_str = "Fortran 2008"
        if(str(pre_result[13]) == "103"):
            fortran_str = "Fortran 2003"
        if(str(pre_result[13]) == "095"):
            fortran_str = "Fortran 95"
        if(str(pre_result[13]) == "090"):
            fortran_str = "Fortran 90"
        if(str(pre_result[13]) == "077"):
            fortran_str = "Fortran 77"
 
    return fortran_str
