import json


# python 的字典，字串可以用 "" 但為了示範 json 的轉換，故意用 ''
keywords = { '萬海': 3, '長榮': 1 }
# print(json.dumps(keywords)) # 中文會顯 unicode
print(json.dumps(keywords, ensure_ascii=False))

# Json概述以及python對json的相關操作
# http://kuma-uni.blogspot.com/2012/06/jsonpythonjson.html
# JSON 是 JavaScript Object Notation
# 所以 true, false, null 都是小寫。Python 對應則是 True, False 

