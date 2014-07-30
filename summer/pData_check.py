__author__ = 'yuafan'

import repairs_ as re
import csv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import scipy.io
import time

Data_Directory = '/Users/yuafan/Desktop/Course/datamining/dm-data-all/'
Save_Directory = '/Users/yuafan/Desktop/Course/datamining/Save/'
backup_Directory = '/Users/yuafan/Desktop/Course/datamining/Save/backup/'
Test_Directory = '/Users/yuafan/Desktop/Course/datamining/test_data/'

File_Specification = Data_Directory + '_specifications.csv'
File_Repair = Data_Directory + '_repairs_all.csv'
Test_Repair = Test_Directory + '_repairs_all.csv'

SpecificationTypes = ['Model', 'ADAPTIVE CRUISE CONTROL', 'AIR INTAKE', 'ANTILOCK BRAKE SYST.', 'AXLE ARRANGEMENT', 'BATTERY CAPACITY', 'BRAKE SYSTEM', 'CAB VERSION', 'CHASSIS TYPE', 'CLUTCH TYPE', 'COMPRESSOR CAPACITY', 'CONCEPT', 'DYNAFLEET ONLINE SUBCRIPTION', 'ENGINE APPLICATION', 'ENGINE BRAKE ASSISTANCE', 'ENGINE GENERATION', 'ENGINE MANUFACTURER', 'ENGINE PTO TORQUE CAPACITY', 'ENGINE TYPE', 'ENGINE VERSION', 'FINAL ASSEMBLY PLANT', 'FRONT AXLE LOAD', 'GEAR SHIFTING SYSTEM', 'GROSS COMBINATION WEIGHT', 'INSTRUMENTATION LEVEL', 'LOW BEAM', 'MARKET _ AREA', 'PRODUCT CLASS', 'PRODUCT TYPE', 'REAR AXLE ARRANGEMENT', 'REAR AXLE LOAD', 'RETARDER', 'TIRE DIMENSION DRIVE', 'TIRE DIMENSION FRONT', 'TIRE DIMENSION TRAILING', 'TRANSMISSION TYPE', 'TRANSPORT CYCLE', 'VEHICLE HEIGHT', 'VEHICLE PROFILE', 'VEHICLE VERSION', 'VEHICLE WIDTH', 'VERSION']



import pickle
import ulti_fileIO as u_sio

ET_list = u_sio.loadPickle(backup_Directory + 'ET_list')
Shadow_ET = u_sio.loadPickle(backup_Directory + 'ET_shadow')
stat_ = u_sio.loadPickle(backup_Directory + 'stat_')

print('------------ Information ------------')
print('Number of errors: ', len(ET_list))
print('One of the Error', ET_list[0] )

print(ET_list[0].code)
print(ET_list[0].SpecificationList_item)
print(len(ET_list[0].SpecificationList_item))
print(ET_list[0].SpecificationList_cnt)
print(len(ET_list[0].SpecificationList_cnt))

print(ET_list[0].SpecificationList_item_Veh)
print(ET_list[0].SpecificationList_cnt_Veh)

print(ET_list[0].cnt)
print(ET_list[0].veh_nr)
print(ET_list[0].cnt_veh)

print(stat_.SpecificationList_item)
print(stat_.SpecificationList_cnt)

print('------------ Error Rate Calculation ------------')

errList = []

ctr_n = 0

ctimeS = time.time()

for err_ in ET_list:

    print(ctr_n)
    ctr_n += 1

    er = re.error_stats_(err_.code)
    er.update(err_, stat_)
    errList.append(er)

    '''
    if er.code == '286':
        print('found it')
        print(er.code)
        print(er.SpecificationList_item)
        print(er.SpecificationList_rate)
    '''


ctimeE = time.time()
print('Loading done, we lost: ' + str(ctimeE-ctimeS) + ' s')


#    del er



print(errList[0].code)
print(errList[0].SpecificationList_item)
print(errList[0].SpecificationList_rate)









