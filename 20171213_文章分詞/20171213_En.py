# import collections
# import collections as co
from collections import Counter

with open('text.txt', 'r', encoding = 'UTF-8') as file:
  text = file.read()
  
  print(text)
  print('-'*30)
  
  #------------------------將前後空白刪除
  text = text.strip()
  
  print(text)
  print('-'*30)
  
  #------------------------將標點符號由空字串替代
  for k in '.,;()':
    text = text.replace(k , '')
    
  # text = text.replce('\n', ' ')
  print(text)
  print('-'*30)

  #------------------------以空白為基準切割字串並存至list的Instance中
  words = text.split(' ')
  
  print(words)
  print('-'*30)
  
  # #------------------------進行詞彙計數
  # counter = dict()
  
  # stops = ['a', 'is', 'as', 'for', 'and']
  
  # for k in words:
  #   m = k.lower()
  #   if m not in stops:
  #     if m in counter:
  #       counter[m] = counter[m] + 1
  #     else:
  #       counter[m] = 1
  
  # print(counter)
  # print('-'*30)
  
  # #------------------------將出現次數>=3的詞彙列出
  # for k in counter:
  #   if counter[k]>=3:
  #     print(k, counter[k])
  
  # ------------------------進行詞彙計數
  stops = ['a', 'is', 'as', 'for', 'and']
  
  # counter = collections.Counter()
  # counter = co.Counter()
  counter = Counter()
  for k in words:
    if k not in stops:
      m = k.lower()
      counter[m] += 1
    
  print(counter.most_common(10))
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  