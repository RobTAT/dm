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
Test_Directory = '/Users/yuafan/Desktop/Course/datamining/test_data/'

File_Specification = Data_Directory + '_specifications.csv'
File_Repair = Data_Directory + '_repairs_all.csv'
Test_Repair = Test_Directory + '_repairs_all.csv'


SpecificationTypes = ['Model', 'ADAPTIVE CRUISE CONTROL', 'AIR INTAKE', 'ANTILOCK BRAKE SYST.', 'AXLE ARRANGEMENT', 'BATTERY CAPACITY', 'BRAKE SYSTEM', 'CAB VERSION', 'CHASSIS TYPE', 'CLUTCH TYPE', 'COMPRESSOR CAPACITY', 'CONCEPT', 'DYNAFLEET ONLINE SUBCRIPTION', 'ENGINE APPLICATION', 'ENGINE BRAKE ASSISTANCE', 'ENGINE GENERATION', 'ENGINE MANUFACTURER', 'ENGINE PTO TORQUE CAPACITY', 'ENGINE TYPE', 'ENGINE VERSION', 'FINAL ASSEMBLY PLANT', 'FRONT AXLE LOAD', 'GEAR SHIFTING SYSTEM', 'GROSS COMBINATION WEIGHT', 'INSTRUMENTATION LEVEL', 'LOW BEAM', 'MARKET _ AREA', 'PRODUCT CLASS', 'PRODUCT TYPE', 'REAR AXLE ARRANGEMENT', 'REAR AXLE LOAD', 'RETARDER', 'TIRE DIMENSION DRIVE', 'TIRE DIMENSION FRONT', 'TIRE DIMENSION TRAILING', 'TRANSMISSION TYPE', 'TRANSPORT CYCLE', 'VEHICLE HEIGHT', 'VEHICLE PROFILE', 'VEHICLE VERSION', 'VEHICLE WIDTH', 'VERSION']


# Read Data, Specification cost 0.19s

ctimeS = time.time()


# Chage test or formal files here

csvReader_Repair = csv.reader(open(File_Repair, 'rb'), delimiter=';', quotechar='|')
#csvReader_Repair = csv.reader(open(Test_Repair, 'rb'), delimiter=';', quotechar='|')
data1 = list(csvReader_Repair)

csvReader_Spec = csv.reader(open(File_Specification, 'rb'), delimiter=';', quotechar='|')
data2 = list(csvReader_Spec)

ctimeE = time.time()
print('Loading done, we lost: ' + str(ctimeE-ctimeS) + ' s')


ctimeS = time.time()

# Sort list cost 0.02 sec_

from operator import itemgetter
data2_sorted = sorted(data2, key=itemgetter(0))

ctimeE = time.time()
print('Loading done, we lost: ' + str(ctimeE-ctimeS) + ' s')

#print('Last', data2_sorted[-1])
#print('Last5Char', int(data2_sorted[-1][0][-5:]))

del data2
del data1[0]
del data2_sorted[0]

# Go through all the Repair file
# Create a Error type for each new type
# Update stuff in the class
# 1. Increase ctr
# 2. Bus Number
# 3. Record timeStamp
# 4. add Specification


# Casual and Crappy initialization
Shadow_ET = []
ET_list = []

Shadow_ET.append(data1[0][2])

ET_list.append(re.ErrorType_Rep(data1[0][2]))
ET_list[0].update(data2_sorted[int(data1[0][0][-5:])])

print(ET_list[0].code)
print(ET_list[0].SpecificationList_item)
print(len(ET_list[0].SpecificationList_item))
print(ET_list[0].SpecificationList_cnt)
print(len(ET_list[0].SpecificationList_cnt))

# = =why



ctimeS = time.time()

for cRow_rep in range(1, len(data1)):

    if cRow_rep % 10000 == 0:
        print('Row: '+ str(cRow_rep))
        print('total: ' + str(len(data1)) +'  ' + 'Per: ' + str(float(cRow_rep/float(len(data1)))))

    if data1[cRow_rep][2] in Shadow_ET:
        #print('index: ' + data1[cRow_rep][0][-5:])
        #print('index2: ' + data1[cRow_rep][2])
        #print('index3: ' + str(Shadow_ET.index(data1[cRow_rep][2])))

        #print(data2_sorted[int(data1[cRow_rep][0][-5:])])
        ET_list[Shadow_ET.index(data1[cRow_rep][2])].update(data2_sorted[int(data1[cRow_rep][0][-5:])])
    else:
        Shadow_ET.append(data1[cRow_rep][2])
        ET_list.append(re.ErrorType_Rep(data1[cRow_rep][2]))
        ET_list[Shadow_ET.index(data1[cRow_rep][2])].update(data2_sorted[int(data1[cRow_rep][0][-5:])])

ctimeE = time.time()
print('Loading done, we lost: ' + str(ctimeE-ctimeS) + ' s')


print('------------ Information ------------')
print('Number of errors: ', len(ET_list))
print('One of the Error', ET_list[0] )

print(ET_list[0].code)
print(ET_list[0].SpecificationList_item)
print(len(ET_list[0].SpecificationList_item))
print(ET_list[0].SpecificationList_cnt)
print(len(ET_list[0].SpecificationList_cnt))
print(len(ET_list[0].SpecificationList_cnt_Veh))

print(ET_list[0].cnt)
print(ET_list[0].veh_nr)
print(ET_list[0].cnt_veh)


print('------------ Save Information ------------')

import ulti_fileIO as u_sio

u_sio.savePickle(Save_Directory + 'ET_list', ET_list)
u_sio.savePickle(Save_Directory + 'ET_shadow', Shadow_ET)
u_sio.savePickle(Save_Directory + '305', ET_list[0])
u_sio.savePickle(Save_Directory + 'sec', ET_list[1])




'''

# Create stat_...

stat_ = re.Specification_stat()

for cRow_rep in range(0, len(data2_sorted)):

    if cRow_rep % 1000 == 0:
        print(cRow_rep)

    stat_.update((data2_sorted[cRow_rep]))

print(stat_.SpecificationList_item)
print(stat_.SpecificationList_cnt)

import ulti_fileIO as u_sio

u_sio.savePickle(Save_Directory + 'stat_', stat_)

'''




