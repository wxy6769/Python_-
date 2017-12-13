import collections
import jieba

#-------------------------
stops_file = open('stops_cn.txt', 'r', encoding = 'UTF-8')
stops_txt = stops_file.read()
stops_words = stops_txt.split('\n')

#-------------------------
with open('text_cn.txt', 'r', encoding = 'UTF-8') as file:
  text = file.read()
  
  print(text)
  print('-'*30)
  
  #-------------------------以外掛模組進行中文分詞
  words = jieba.cut(text)
  
  #-------------------------開始進行詞彙計數
  co = collections.Counter()
  
  for k in words:
    if k not in stops_words:
      co[k] = co[k] + 1
  
  print(co.most_common(10))
  print('-'*30)  
  
  #-------------------------