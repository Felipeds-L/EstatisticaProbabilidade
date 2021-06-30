import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

archive = open("ranked.csv", "r")
listy = []
list_games = []
list_gold_blue_size = []
count = 0

for line in archive:
    if(count <= 1000):
        value = line.split(' , ')
        listy.append(value[0])
        count += 1
        
for v in listy:
    list_games.append(v.split(','))


for e in list_games:
    list_gold_blue_size.append(int(e[12]))




# Here we'll use a list of European's highelo League of Legends games. 
# The datas analized here will be the Accumulated gold from the blue side team at the firts 10 minutes.
# Let's group the datas in 4 classes

num_c = 4

highest = max(list_gold_blue_size)
lowest = min(list_gold_blue_size)
amplitude = highest - lowest

class_amplitude = round(amplitude/num_c)

print("Class amplitude:", class_amplitude)

lower_limit = [lowest]
for x in range(num_c):
    lower_limit.append(lower_limit[x]+class_amplitude)

print("List of lower limit of every class: ", lower_limit)

# Until now we have some informations like the highest and lowest value of accumulated gold by all blue teams side at the first 10 minutes, we discored the amplitude, 
# and the class amplitude. Yet was defined all the lower limits from every class created;

# The next step is count and agrupade all the accumulated gold's values

goldAccumulated = {'class1':0,'class2':0,'class3':0,'class4':0}

for gold in list_gold_blue_size:
    if gold < lower_limit[1]:
        goldAccumulated['class1'] += 1
    elif gold < lower_limit[2]:
        goldAccumulated['class2'] += 1
    elif gold < lower_limit[3]:
        goldAccumulated['class3'] += 1
    else:
        goldAccumulated['class4'] += 1

print("Agroupped Accumulated gold from every class:", goldAccumulated)

# As we can see, most os teams have in the firts 10 minutes something between 15394 and 18040 of gold in the sum of all 5 players, 
# There's many other that have less than 15393, and only a small group have more than 23335;


plt.hist(list_gold_blue_size,4)
plt.xlabel("Class")
plt.ylabel("Num teams")
plt.title("Accumulated Gold")
plt.show()


# What we've done above was create a graphc representations of the datas analized

avg_accumulated_gold = sum(list_gold_blue_size)/len(list_gold_blue_size)
list_gold_blue_size = sorted(list_gold_blue_size)

print("The average of accumulated gold is: ", np.mean(list_gold_blue_size), " while the median is:", np.median(list_gold_blue_size), " and the moda: ", stats.mode(list_gold_blue_size))
archive.close()

# Before we had showed the average, the median and the mode. We saw that all the 3 results are really similar, after we'll observate the variance and the standart deviation

print("The varience and the standart deviation are:", np.var(list_gold_blue_size), " and ", np.std(list_gold_blue_size))

