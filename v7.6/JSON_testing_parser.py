import json
import os
# v7.6
json_path = os.path.abspath("./testing_data.json")
with open(json_path) as json_file:
    json = json.load(json_file)
'''
 "categories": [
    {
      "supercategory": "none",
      "id": 1,
      "name": "worker"
    },
    {
      "supercategory": "none",
      "id": 2,
      "name": "traffic cone"
    },
    {
      "supercategory": "none",
      "id": 3,
      "name": "backhoe_loader"
    },
    {
      "supercategory": "none",
      "id": 4,
      "name": "excavator"
    },
    {
      "supercategory": "none",
      "id": 5,
      "name": "dump_truck"
    },
    {
      "supercategory": "none",
      "id": 6,
      "name": "concrete_mixer_truck"
    },
    {
      "supercategory": "none",
      "id": 7,
      "name": "mobile_crane"
    },
    {
      "supercategory": "none",
      "id": 8,
      "name": "dozer"
    },
    {
      "supercategory": "none",
      "id": 9,
      "name": "compactor"
    },
    {
      "supercategory": "none",
      "id": 10,
      "name": "wheel_loader"
    },
    {
      "supercategory": "none",
      "id": 11,
      "name": "grader"
    },
    {
      "supercategory": "none",
      "id": 12,
      "name": "tower_crane"
    }
  ]
'''
area_rng = [[0 ** 2, 1e5 ** 2],
        [0 ** 2, 32 ** 2],  [0 ** 2, 16 ** 2], [16 ** 2, 32 ** 2],
        [32 ** 2, 96 ** 2], [32 ** 2, 48 ** 2],  [48 ** 2, 64 ** 2], [64 ** 2, 80 ** 2], [80 ** 2, 96 ** 2],
        [96 ** 2, 1e5 ** 2],[96 ** 2, 112 ** 2], [112 ** 2, 128 ** 2],[128 ** 2, 144 ** 2],[144 ** 2, 160 ** 2]]

area_rng_custom = [[0 ** 2, 1e5 ** 2],
        [0 ** 2, 16 ** 2], [16 ** 2, 32 ** 2],
        [32 ** 2, 48 ** 2],  [48 ** 2, 64 ** 2], [64 ** 2, 80 ** 2], [80 ** 2, 96 ** 2],
        [96 ** 2, 112 ** 2], [112 ** 2, 128 ** 2],[128 ** 2, 144 ** 2],[144 ** 2, 160 ** 2]]

rng_id = ['all',
       'small', 'small16', 'small32',
       'medium', 'medium48','medium64','medium80','medium96',
       'large','large112','large128','large144','large160']

rng_id_custom = ['all', 'small16', 'small32',
                 'medium48','medium64','medium80','medium96',
                 'large112','large128','large144','large160']

area_main_list = []
for i in range(1,13,1):
    areas = []
    for key in json["annotations"]:
        if key["category_id"] == i:
            area = key["area"]
            areas.append(area)
    areas.sort()
    area_main_list.append(areas)

print(len(area_main_list[0]))
print(len(area_main_list[1]))
print(len(area_main_list[2]))
#print(area_main_list[1])
#print(area_main_list[2])


area_key_list = [[] for _ in range(len(area_main_list))]

for i in range(len(area_main_list)):
    area_key = [[] for _ in range(len(area_rng_custom))]
    for ob in area_main_list[i]:
        #print(ob)
        for index, item in enumerate(area_rng_custom):
            if item[0]< ob <item[1]:
                area_key[index].append(ob)
                #print(area_key[index])
    area_key_list[i] = area_key

area_count = [[[] for _ in range(len(area_rng_custom))] for _ in range(len(area_key_list))]

for i in range(len(area_key_list)):
    for j in range(len(area_rng_custom)):
        area_count[i][j] = len(area_key_list[i][j])

for i in range(len(area_count)):
    print(f'{i+1}: {area_count[i]}')

print(rng_id_custom)
print("1: worker, 2:traffic cone, 3:backhoe_loader,4:excavator,5:dump_truck,6:concrete_mixer_truck")
print("7:mobile_crane,8:dozer,9:compactor,10:wheel_loader,11:grader, 12:tower_crane")
print("v7.6,traffic_cone_aug5,worker_aug,ACID(excavator*0.5,dump_truck*0.25)")
