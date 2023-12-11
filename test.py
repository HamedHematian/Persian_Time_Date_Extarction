import re
import json

# read test cases
with open('test_cases.txt', 'r') as f:
  data = f.read()
data = data.split('[')
data = data[1:]
test = [[] for d in range(len(data) // 2)]
for index, d in enumerate(data):
  if index % 2 == 0:
    test[int(index // 2)].append(d.split(':')[1].split(',')[0][1:-1])
  else:
    test[int(index // 2)].append(d.split(':')[1].split(',')[0][1:-1])
test = test[51:]


from time_history_extractor import history_extractor

h = history_extractor()

for i in range(len(test)):
  print('###################')
  print(h.find(test[i][0]))
  print(test[i][0])
