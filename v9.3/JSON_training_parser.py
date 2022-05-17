import json
import os
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
from iteration_utilities import deepflatten

# v7.6
path1 = "./training_data.json"
path2 = "./testing_data.json"
json_path = os.path.abspath(path2)
with open(json_path) as json_file:
    json = json.load(json_file)

predictions1 = [0.0000,0.7000,0.2980,0.3699,0.3284,0.4391,0.3167,0.4579,0.1883,0.4558]
predictions2 = [0.0000,0.1130,0.2755,0.4302,0.3900,0.5641,0.4793,0.4273,0.5165,0.5595]
predictions3 = [0.0000,0.0000,0.0000,0.0000,0.8000,0.0000,0.0000,0.7000,0.0757,0.0000]
predictions4 = [0.0000,0.4385,0.5378,0.6123,0.6969,0.6381,0.7267,0.5644,0.7000,0.3707]
predictions5 = [0.0000,0.0000,0.0000,0.4464,0.1803,0.5126,0.4626,0.3457,0.3986,0.3519]
predictions6 = [0.0000,0.2005,0.3503,0.4548,0.5636,0.5413,0.5041,0.5522,0.5635,0.5642]
predictions = np.array([predictions1,predictions2,
                       predictions3,predictions4,
                       predictions5,predictions6])
for i in range(len(predictions)):
    predictions[i] = [items * 100 for items in predictions[i]]

col_means = predictions.mean(axis=0)
row_means = predictions.mean(axis=1)

prediction_ids = ['excavator','dump_truck','mobile_crane','helmet','human','upper body','w/,vest']

print('predictions=',predictions)
'''
#area_rng = [[2 ** 2, 4 ** 2], [4 ** 2, 8 ** 2], [8 ** 2, 16 ** 2],[16 ** 2, 32 ** 2], [32 ** 2, 48 ** 2],  [48 ** 2, 64 ** 2]]
area_rng = [#[0 ** 2, 1e5 ** 2], [0 ** 2, 32 ** 2],
                        [0 ** 2, 2 ** 2], [2 ** 2, 4 ** 2],[4 ** 2, 6 ** 2],[6 ** 2, 8 ** 2],
                        [8 ** 2, 10 ** 2], [10 ** 2, 12 ** 2],[12 ** 2, 14 ** 2],[14 ** 2, 16 ** 2],
                        [16 ** 2, 18 ** 2],[18 ** 2, 20 ** 2],[20 ** 2, 22 ** 2],[22 ** 2, 24 ** 2],
                        [24 ** 2, 26 ** 2],[26 ** 2, 28 ** 2],[28 ** 2, 30 ** 2],[30 ** 2, 32 ** 2],
                        
                        #[32 ** 2, 96 ** 2],
                        [32 ** 2, 48 ** 2], [48 ** 2, 64 ** 2], [64 ** 2, 80 ** 2],[80 ** 2, 96 ** 2],
                        #[96 ** 2, 1e5 ** 2],
                        [96 ** 2, 112 ** 2], [112 ** 2, 128 ** 2], [128 ** 2, 144 ** 2], [144 ** 2, 160 ** 2],[160 ** 2, 1e5 ** 2]]
'''
area_rng = [#[0 ** 2, 1e5 ** 2], [0 ** 2, 32 ** 2],
                        [0 ** 2, 16 ** 2], [16 ** 2, 32 ** 2],
                        #[32 ** 2, 96 ** 2],
                        [32 ** 2, 48 ** 2], [48 ** 2, 64 ** 2], [64 ** 2, 80 ** 2],[80 ** 2, 96 ** 2],
                        #[96 ** 2, 1e5 ** 2],
                        [96 ** 2, 112 ** 2], [112 ** 2, 128 ** 2], [128 ** 2, 144 ** 2], [144 ** 2, 160 ** 2],[160 ** 2, 1e5 ** 2]]
'''
        #[64 ** 2, 80 ** 2], [80 ** 2, 96 ** 2],
        #[96 ** 2, 1e5 ** 2],
        #[96 ** 2, 112 ** 2], [112 ** 2, 128 ** 2],[128 ** 2, 144 ** 2],[144 ** 2, 160 ** 2]]

area_rng_custom = [[0 ** 2, 1e5 ** 2],
        [0 ** 2, 32 ** 2],
        [32 ** 2, 96 ** 2],
        [96 ** 2, 1e5 ** 2]]

        [96 ** 2, (96 + 32 * 1) ** 2],
        [(96 + 32 * 1) ** 2, (96 + 32 * 2) ** 2],
        [(96 + 32 * 2) ** 2, (96 + 32 * 3) ** 2],
        [(96 + 32 * 3) ** 2, (96 + 32 * 4) ** 2],
        [(96 + 32 * 4) ** 2, (96 + 32 * 5) ** 2],
        [(96 + 32 * 5) ** 2, (96 + 32 * 6) ** 2],
        [(96 + 32 * 6) ** 2, 1e5 ** 2]]
'''
rng_id = ['all',
       'small', 'small16', 'small32',
       'medium', 'medium48','medium64','medium80','medium96',
       'large','large112','large128','large144','large160','largerer160']

rng_id_custom = ['all', 'small16', 'small32',
                 'medium48','medium64','medium80','medium96',
                 'large112','large128','large144','large160']

area_main_list = []
for i in range(1,7,1):
    areas = []
    for key in json["annotations"]:
        if key["category_id"] == i:
            area = key["area"]
            areas.append(area)
    areas.sort()
    #print(i,np.sqrt(areas[0]), np.sqrt(areas[-1]))
    area_main_list.append(areas)


area_main_list = [np.sqrt(x) for x in area_main_list]
percentile = [[[]for _ in range(10,110,10)] for _ in range(len(area_main_list))]
print((np.asarray(percentile)).shape)
for i in range(len(area_main_list)):
    for index, percent in enumerate(range(10,110,10)):
        percentile[i][index] = np.percentile(area_main_list[i], percent, axis=0)
percentile = [np.insert(sublist,0,0) for sublist in percentile]
print('percentile=',percentile)

for index, item in enumerate(area_main_list):
    custom_bin = [ sublist[ 1 ] for sublist in area_rng ]
    custom_bin = [ np.sqrt(x) for x in custom_bin ]
    values, bins, patches = plt.hist(item, alpha=0.1,edgecolor="red", bins=range(int(item[0]),int(custom_bin[:-1][-1])))

    values2, bins2, patches2 = plt.hist(item, alpha=0.5, edgecolor="red", bins=custom_bin[:-1])
    #values3, bins3, patches3 = plt.hist(item, color="yellow", alpha=0.25, edgecolor="blue", bins=percentile[index][:-1], range=[0, bins2[-1]])
    plt.plot(bins2,predictions[index],'go-',alpha=0.5,label='predictions',linewidth=2)
    plt.title(f'captured={int(np.sum(values2))},total={int(np.sum(values))},percentage={int(100*np.sum(values2)/np.sum(values))}')
    plt.suptitle(f'{prediction_ids[index]},mean={int(stat.mean(item))},median={int(stat.median(item))}')
    plt.bar_label(patches2)
    #plt.bar_label(patches3)
    #print('custom_values', values2)
    #print("custom_bins", bins2)
    plt.savefig(f'{json_path}{index}zoom_predict.jpg')
    plt.show()

##total_classes
area_main_list_copy = [item for sublist in area_main_list for item in sublist]
area_main_list_copy.sort()
#compute percentile
percentile = [0,]
for percent in range(10,110,10):
    percentile.append(np.percentile(area_main_list_copy, percent, axis=0))
np.insert(percentile,0,0)
print('percentile=',percentile)

#print(area_main_list_copy)
#print('falt_minmax',area_main_list_copy[0],int(area_main_list_copy[-1]))
custom_bin = [sublist[1] for sublist in area_rng]
custom_bin = [np.sqrt(x) for x in custom_bin]
values, bins, patches = plt.hist(area_main_list_copy,alpha=0.1,edgecolor="red", bins=range(int(area_main_list_copy[0]),int(custom_bin[:-1][-1])))

values2, bins2, patches2 = plt.hist(area_main_list_copy, alpha=0.5, edgecolor="red", bins=custom_bin[:-1],range=[0,custom_bin[:-1][-1]])
#values3, bins3, patches3 = plt.hist(area_main_list_copy, color="yellow", alpha=0.25, edgecolor="blue", bins=percentile[:-1],range=[0,custom_bin[:-1][-1]])
plt.plot(bins2,col_means,'go-',alpha=0.5,label='predictions',linewidth=2)
plt.title(f'captured={int(np.sum(values2))},total={int(np.sum(values))},percentage={int(100*np.sum(values2)/np.sum(values))}')
plt.suptitle(f'all_classes,mean={int(stat.mean(area_main_list_copy))},median={int(stat.median(area_main_list_copy))}')
plt.bar_label(patches2)
#plt.bar_label(patches3)
#print('custom_values', values2)
#print("custom_bins", bins2)
plt.savefig(f'{json_path}zoom_total_predict.jpg')
plt.show()

'''
area_key_list = [[] for _ in range(len(area_main_list))]

for i in range(len(area_main_list)):
    for index,item in enumerate(area_rng):
        print([len(x) for x in area_main_list])

    area_key = [[] for _ in range(len(area_rng))]
    
    for ind, ob in enumerate(area_main_list[i]):
        for index, item in enumerate(area_rng):
            print(item)

            if item[0] <= ob <= item[1]:
                print(f'{item[0]} <= {ob} <= {item[1]}')
                area_key[index].append(ob)
                #print(area_key[index])
    area_key_list[i] = area_key

area_count = [[[] for _ in range(len(area_rng))] for _ in range(len(area_key_list))]
#print(np.asarray(area_count).shape)
for i in range(len(area_key_list)):
    for j in range(len(area_rng)):
        #print(area_key_list[i][j])
        area_count[i][j] = len(area_key_list[i][j])

#print('area_count==',area_count)

for i in range(len(area_count)):
    print(f'{i+1}: {area_count[i]},{sum(area_count[i][1:])}')

print(area_rng)
print("1: excavator, 2:dump_truck, 3:mobile_crane,4:helmet,5:human,6:upper body w/ vest")
print("v9.3,tsmc_helmet*0.08, vest*0.08, human*0.04, mobile_crane, dump_truck, excavator")
'''
'''
 "categories": [
    {
      "supercategory": "none",
      "id": 1,
      "name": "excavator"
    },
    {
      "supercategory": "none",
      "id": 2,
      "name": "dump_truck"
    },
    {
      "supercategory": "none",
      "id": 3,
      "name": "mobile_crane"
    },
    {
      "supercategory": "none",
      "id": 4,
      "name": "helmet"
    },
    {
      "supercategory": "none",
      "id": 5,
      "name": "human"
    },
    {
      "supercategory": "none",
      "id": 6,
      "name": "upper body w/ vest"
    }
  ]
'''

