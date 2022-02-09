import numpy as np
import matplotlib.pyplot as plt

file_obj = open('lotto999.csv', 'rt', encoding='utf-8')
lines = file_obj.readlines()
file_obj.close()
counter_dict = {}
key_list = []
value_list = []

for line in lines[1:]:
    line_strip = line.strip()
    num_txts = line_strip.split(',')
    num_txts_modified = num_txts[1:7]

    nums = []
    for txt in num_txts_modified:
        nums.append(int(txt))
    for num in nums:
        counter_dict[num] = counter_dict.get(num, 0) + 1

s_counter_dict = sorted(counter_dict.items())      
for key, value in s_counter_dict:
    print(key, ':', value)
    key_list.append(key)
    value_list.append(value)

max_v = np.amax(value_list)
index_max = np.argmax(value_list)   # 33
# max_k = key_list.index(index_max) # 32
max_k = key_list[index_max]         # 34


min_v = np.amin(value_list)
index_min = np.argmin(value_list)   # 8
# min_k = key_list.index(index_min) # 7
min_k = key_list[index_min]         # 9


print(f'가장 많이 나온 공: {max_k} 번공,  횟수: {max_v} 회')
print(f'가장 적게 나온 공: {min_k} 번공,  횟수: {min_v} 회')
        
plt.style.use('seaborn')

plt.bar(key_list, value_list)   

plt.xlim(0, 46)
plt.ylim(0, 200)
plt.text(min_k, min_v, f'Min:(#{min_k}, {min_v})', horizontalalignment='center', color='red', size='large', fontweight='bold')
plt.text(max_k, max_v, f'Max:(#{max_k}, {max_v})', horizontalalignment='center', color='red', size='large', fontweight='bold')
plt.show()
        