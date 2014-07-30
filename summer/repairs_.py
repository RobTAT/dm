__author__ = 'yuafan'

Data_Directory = '/Users/yuafan/Desktop/Course/datamining/dm-data-all/'
Save_Directory = '/Users/yuafan/Desktop/Course/datamining/Save/'

File_Specification = Data_Directory + '_specifications.csv'
File_Repair = Data_Directory + '_repairs_all.csv'

SpecificationTypes = ['Model', 'ADAPTIVE CRUISE CONTROL', 'AIR INTAKE', 'ANTILOCK BRAKE SYST.', 'AXLE ARRANGEMENT', 'BATTERY CAPACITY', 'BRAKE SYSTEM', 'CAB VERSION', 'CHASSIS TYPE', 'CLUTCH TYPE', 'COMPRESSOR CAPACITY', 'CONCEPT', 'DYNAFLEET ONLINE SUBCRIPTION', 'ENGINE APPLICATION', 'ENGINE BRAKE ASSISTANCE', 'ENGINE GENERATION', 'ENGINE MANUFACTURER', 'ENGINE PTO TORQUE CAPACITY', 'ENGINE TYPE', 'ENGINE VERSION', 'FINAL ASSEMBLY PLANT', 'FRONT AXLE LOAD', 'GEAR SHIFTING SYSTEM', 'GROSS COMBINATION WEIGHT', 'INSTRUMENTATION LEVEL', 'LOW BEAM', 'MARKET _ AREA', 'PRODUCT CLASS', 'PRODUCT TYPE', 'REAR AXLE ARRANGEMENT', 'REAR AXLE LOAD', 'RETARDER', 'TIRE DIMENSION DRIVE', 'TIRE DIMENSION FRONT', 'TIRE DIMENSION TRAILING', 'TRANSMISSION TYPE', 'TRANSPORT CYCLE', 'VEHICLE HEIGHT', 'VEHICLE PROFILE', 'VEHICLE VERSION', 'VEHICLE WIDTH', 'VERSION']

class ErrorType_Rep(object):

    def __init__(self, code_):
        # id_1
        self.code = code_ # Error names

        # id_1
        self.cnt = 0 # Number of Occurrence

        # id_2
        self.veh_nr = [] # Vehicle List
        self.cnt_veh = [] # Number of Occurrence List

        #self.date = [] # date... implement later

        # id_3
        # Number of Occurrence
        #self.BusSpecificationTypes = ['Model', 'ADAPTIVE CRUISE CONTROL', 'AIR INTAKE', 'ANTILOCK BRAKE SYST.', 'AXLE ARRANGEMENT', 'BATTERY CAPACITY', 'BRAKE SYSTEM', 'CAB VERSION', 'CHASSIS TYPE', 'CLUTCH TYPE', 'COMPRESSOR CAPACITY', 'CONCEPT', 'DYNAFLEET ONLINE SUBCRIPTION', 'ENGINE APPLICATION', 'ENGINE BRAKE ASSISTANCE', 'ENGINE GENERATION', 'ENGINE MANUFACTURER', 'ENGINE PTO TORQUE CAPACITY', 'ENGINE TYPE', 'ENGINE VERSION', 'FINAL ASSEMBLY PLANT', 'FRONT AXLE LOAD', 'GEAR SHIFTING SYSTEM', 'GROSS COMBINATION WEIGHT', 'INSTRUMENTATION LEVEL', 'LOW BEAM', 'MARKET _ AREA', 'PRODUCT CLASS', 'PRODUCT TYPE', 'REAR AXLE ARRANGEMENT', 'REAR AXLE LOAD', 'RETARDER', 'TIRE DIMENSION DRIVE', 'TIRE DIMENSION FRONT', 'TIRE DIMENSION TRAILING', 'TRANSMISSION TYPE', 'TRANSPORT CYCLE', 'VEHICLE HEIGHT', 'VEHICLE PROFILE', 'VEHICLE VERSION', 'VEHICLE WIDTH', 'VERSION']
        self.SpecificationList_item = [[] for x in xrange(len(SpecificationTypes)+1)]
        self.SpecificationList_cnt = [[] for x in xrange(len(SpecificationTypes)+1)]

        # id_4
        # Number of Vehicles
        self.SpecificationList_item_Veh = [[] for x in xrange(len(SpecificationTypes)+1)]
        self.SpecificationList_cnt_Veh = [[] for x in xrange(len(SpecificationTypes)+1)]

    def update(self, info_):

        veh_nr_ = info_[0]
        # id_1
        self.cnt += 1

        # id_2
        if veh_nr_ in self.veh_nr:
            old = True
            self.cnt_veh[self.veh_nr.index(veh_nr_)] += 1
        else:
            self.veh_nr.append(veh_nr_)
            self.cnt_veh.append(1)
            old = False

        # id_3
        for nCol in range(1, len(info_)):
            if info_[nCol] in self.SpecificationList_item[nCol]:
                self.SpecificationList_cnt[nCol][self.SpecificationList_item[nCol].index(info_[nCol])] += 1
            else:
                self.SpecificationList_item[nCol].append(info_[nCol])
                self.SpecificationList_cnt[nCol].append(1)

            if old == False:
                if info_[nCol] in self.SpecificationList_item_Veh[nCol]:
                    self.SpecificationList_cnt_Veh[nCol][self.SpecificationList_item_Veh[nCol].index(info_[nCol])] += 1
                else:
                    self.SpecificationList_item_Veh[nCol].append(info_[nCol])
                    self.SpecificationList_cnt_Veh[nCol].append(1)


class Specification_stat(object):

    def __init__(self):
        self.SpecificationList_item = [[] for x in xrange(len(SpecificationTypes)+1)]
        self.SpecificationList_cnt = [[] for x in xrange(len(SpecificationTypes)+1)]

    def update(self, info_):

        for nCol in range(1, len(info_)):
            if info_[nCol] in self.SpecificationList_item[nCol]:
                self.SpecificationList_cnt[nCol][self.SpecificationList_item[nCol].index(info_[nCol])] += 1
            else:
                self.SpecificationList_item[nCol].append(info_[nCol])
                self.SpecificationList_cnt[nCol].append(1)


class error_stats_(object):
    def __init__(self, code):
        self.code = code
        self.SpecificationList_item = []
        self.SpecificationList_error_cnt = []
        self.SpecificationList_total_cnt = [[] for x in xrange(len(SpecificationTypes)+1)]
        self.SpecificationList_rate = [[] for x in xrange(len(SpecificationTypes)+1)]

    def update(self, error_, stat_):
        self.SpecificationList_item = error_.SpecificationList_item_Veh
        self.SpecificationList_error_cnt = error_.SpecificationList_cnt_Veh
        #self.SpecificationList_total_cnt = stat_.SpecificationList_cnt

        '''
        for nClass in range(1, len(error_.SpecificationList_item_Veh)):
            for nelem in range(len(error_.SpecificationList_item_Veh[nClass])):
                self.SpecificationList_total_cnt[nClass].append(stat_.SpecificationList_cnt[nClass][stat_.SpecificationList_item[nClass].index(error_.SpecificationList_item_Veh[nClass][nelem])])
        '''

        for nClass in range(1, len(error_.SpecificationList_item_Veh)):
            for nelem in range(len(error_.SpecificationList_item_Veh[nClass])):
                self.SpecificationList_total_cnt[nClass].append(stat_.SpecificationList_cnt[nClass][stat_.SpecificationList_item[nClass].index(error_.SpecificationList_item_Veh[nClass][nelem])])
                self.SpecificationList_rate[nClass].append(float(self.SpecificationList_error_cnt[nClass][nelem])/float(self.SpecificationList_total_cnt[nClass][nelem]))








'''

error1 = ErrorType_Rep('test')
error1.update('111')
error1.update('111')
error1.update('1113')
error1.update('1112')

print(error1.veh_nr)
print(error1.cnt_veh)

'''



'''

    def append_specList(self, type_):
        self.SpecificationList_cnt[1].append([type_, 1])

    def densityofOccurrence_Date(self):
        pass

    def densityofOccurrenceDate_Specification(self, Specification_Code):
        pass


error1 = ErrorType_Rep('test')

print(error1.BusSpecificationTypes_cnt)
print(len(error1.BusSpecificationTypes_cnt))
print(len(error1.BusSpecificationTypes))

error1.initialize_TypeList()
print(error1.SpecificationList_cnt)
#error1.append_specList('hihihi')
#error1.append_specList('hihihi')
print(error1.SpecificationList_cnt)

list_ = []

list_.append(ErrorType_Rep('104'))
list_.append(ErrorType_Rep('104'))
list_.append(ErrorType_Rep('104'))

print(list_)

print(len(list_))
'''