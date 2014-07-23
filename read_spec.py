__author__ = 'yuafan'

DirectoryData = '/Users/yuafan/Desktop/Course/datamining/dm-data-all/'

file = DirectoryData + '_specifications.csv'

N = 28760 + 1

import csv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import scipy.io

csvReader = csv.reader(open(file, 'rb'), delimiter=';', quotechar='|')

data = list(csvReader)

print(data[0][0])
print(data[1][0])

print(data[0])
print(data[1])

print(len(data[0]))
print(len(data[1]))

# Sort according to sub list
#zip(*sorted(zip(*a), key=lambda x: -x[1]))

FeatureList = data[0]
print('Features: ', FeatureList)

FeaturesEntities = [[] for x in xrange(len(FeatureList))]
#AmountofEntities =  [[0] for x in xrange(len(FeatureList))]

print(FeaturesEntities)
print('len: ', len(FeaturesEntities))

#print(AmountofEntities)
#print('len: ', len(AmountofEntities))

del data[0]

print(data[0])

for elem in range(N):
    #print(data[elem])

    if elem % 1000 == 1:
        print(elem)

    for ele, ele_cnt in zip(data[elem], range(len(data[elem]))):
        #print([FeaturesEntities[ele_cnt][x][0] for x in range(len( FeaturesEntities[ele_cnt])) if [FeaturesEntities[ele_cnt][x] != []]])
        #print(ele, ele_cnt)

        if ele_cnt == 0:
            continue

        if ele not in [FeaturesEntities[ele_cnt][x][0] for x in range(len( FeaturesEntities[ele_cnt])) if [FeaturesEntities[ele_cnt][x] != []]]:
            FeaturesEntities[ele_cnt].append([ele, int(1)])
        else:
            #a.index(names)
            #print(FeaturesEntities[ele_cnt][1])
            for ele_ in FeaturesEntities[ele_cnt]:
                for el_ in range(len(FeaturesEntities[ele_cnt])):
                    if ele == FeaturesEntities[ele_cnt][el_][0]:
                        FeaturesEntities[ele_cnt][el_][1] += 1
                        #print(FeaturesEntities[ele_cnt][el_])

            #FeaturesEntities[ele_cnt][1] += 1

print('FE:', FeaturesEntities)

print('len: ', len(FeaturesEntities))

counts_ = [[] for x in xrange(len(FeatureList))]
labels_ = [[] for x in xrange(len(FeatureList))]

print(len(counts_))

for elem_cnt in range(1, len(FeaturesEntities)):
    for elem in FeaturesEntities[elem_cnt]:
        print(elem)
        labels_[elem_cnt].append(elem[0])
        counts_[elem_cnt].append(elem[1])

print(labels_)
print(counts_)

scipy.io.savemat('/Users/yuafan/Desktop/Course/datamining/project/_spec_PiePlot/normal/spec_', {'count': counts_, 'labels': labels_, 'Features': FeatureList})

print('------------|Demographics|------------' +'\n')

with open("/Users/yuafan/Desktop/Course/datamining/project/info_spec.txt", "a") as myfile:
    myfile.write('------------|Demographics|------------' +'\n')


for elem_cnt in range(len(FeaturesEntities)):
    print(FeatureList[elem_cnt])

    with open("/Users/yuafan/Desktop/Course/datamining/project/info_spec.txt", "a") as myfile:
        myfile.write('-------' + FeatureList[elem_cnt] + '------' +'\n')

    for ele in FeaturesEntities[elem_cnt]:
        print('ele', ele)

        with open("/Users/yuafan/Desktop/Course/datamining/project/info_spec.txt", "a") as myfile:
            if ele[0] == []:
                myfile.write(' ' +'\n')
            else:
                myfile.write(ele[0] + ':' + str(ele[1]) +'\n')




'''

for cnt in range(1, len(labels_)):
    plt.clf()
    colors = cm.rainbow(np.linspace(0, 1, len(labels_[cnt])))
    plt.pie(counts_[cnt], labels=labels_[cnt], colors=colors, autopct='%1.1f%%', shadow=True)
    plt.legend(labels_[cnt], loc=(-0.15, 0.05), shadow=True)
    plt.title(FeatureList[cnt])
    #plt.show()
    plt.savefig('/Users/yuafan/Desktop/Course/datamining/project/_spec_PiePlot/color/' +  FeatureList[cnt] + '.png')




for cnt in range(1, len(labels_)):
    plt.clf()
    #colors = cm.rainbow(np.linspace(0, 1, len(labels_[cnt])))
    plt.pie(counts_[cnt], labels=labels_[cnt], autopct='%1.1f%%', shadow=True)
    plt.legend(labels_[cnt], loc=(-0.15, 0.05), shadow=True)
    plt.title(FeatureList[cnt])
    #plt.show()
    plt.savefig('/Users/yuafan/Desktop/Course/datamining/project/_spec_PiePlot/normal/' +  FeatureList[cnt] + '.png')


'''
