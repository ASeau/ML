import json
import os
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
# v7.6
json_path = os.path.abspath("./testing_data.json")
with open(json_path) as json_file:
    json = json.load(json_file)

#area_rng_custom = [[0 ** 2, 1e5 ** 2],
                        #[0 ** 2, 32 ** 2], [0 ** 2, 16 ** 2], [16 ** 2, 32 ** 2],
                        #[32 ** 2, 96 ** 2], [32 ** 2, 48 ** 2], [48 ** 2, 64 ** 2], [64 ** 2, 80 ** 2],
                        #[80 ** 2, 96 ** 2],
                        #[96 ** 2, 1e5 ** 2], [96 ** 2, 112 ** 2], [112 ** 2, 128 ** 2], [128 ** 2, 144 ** 2],
                        #[144 ** 2, 160 ** 2],[160 ** 2, 1e5 ** 2]]

area_rng_custom = [#[0 ** 2, 1e5 ** 2], [0 ** 2, 32 ** 2],
                        [0 ** 2, 16 ** 2], [16 ** 2, 32 ** 2], [32 ** 2, 48 ** 2], [48 ** 2, 64 ** 2], [64 ** 2, 80 ** 2],[80 ** 2, 96 ** 2],[96 ** 2, 112 ** 2], [112 ** 2, 128 ** 2], [128 ** 2, 144 ** 2], [144 ** 2, 160 ** 2],[160 ** 2, 1e5 ** 2]]

rng_id_custom = ['all',
       'small', 'small16', 'small32',
       'medium', 'medium48','medium64','medium80','medium96',
       'large','large112','large128','large144','large160','largerer160']



area_main_list = []
for i in range(1,7,1):
    areas = []
    for key in json["annotations"]:
        if key["category_id"] == i:
            area = key["area"]
            areas.append(area)
    areas.sort()
    area_main_list.append(areas)

area_main_list = [np.sqrt(x) for x in area_main_list]
for index,item in enumerate(area_main_list):
    print(len(item), 'mean=',stat.mean(item),'median=',stat.median(item))
    print(item[0],item[-1])
    #plt.hist(item, edgecolor="red", bins=range(int(item[0]),int(item[-1])))
    #plt.title(f'{index},mean_,{stat.mean(item)},median_,{stat.median(item)}')
    #plt.show()

area_key_list = [[] for _ in range(len(area_main_list))]

for i in range(len(area_main_list)):
    area_key = [[] for _ in range(len(area_rng_custom))]
    for ob in area_main_list[i]:
        #print(area_rng_custom)
        for index, item in enumerate(area_rng_custom):
            if item[0] <= ob <= item[1]:
                print(f'{item[0]} <= {ob} <= {item[1]}')
                area_key[index].append(ob)
                #area_main_list.pop(ob)
                #print(area_key[index])
    area_key_list[i] = area_key

area_count = [[[] for _ in range(len(area_rng_custom))] for _ in range(len(area_key_list))]

for i in range(len(area_key_list)):
    for j in range(len(area_rng_custom)):
        area_count[i][j] = len(area_key_list[i][j])

for i in range(len(area_count)):
    print(f'{i+1}: {area_count[i]},{sum(area_count[i][1:])}')

print(rng_id_custom)
print("1: excavator, 2:dump_truck, 3:mobile_crane,4:helmet,5:human,6:upper body w/ vest")
print("v9.3,tsmc_helmet*0.08, vest*0.08, human*0.04, mobile_crane, dump_truck, excavator")
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