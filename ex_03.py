# --------------------------
# 파이썬 객체와 변수
# -------------------------

#여러 개의 데이터를 저장하는 리스트 생성
[10,4.3,"Happy",True]

# 메모리에 존재하는 리스트 객체에 접근
# 객체 주소 저장(참조)하는 변수
data = [10,4.3,"Happy",True]
print(id(data),data)
data = 12                         # int 객체 주소를 담고 있는 변수
data = "happy"                    # str 객체 주소 담고 있는 변수
data = {'name' : "hong", "age" : 12}  # dict 객체 주소 담고 있는 변수
print(data['name'])

import keyword
print("Keyword\n",keyword.kwlist)
a = 10
b = 12
print("a+b = %d"%(a+b))
print("a+b = %d a*b = %d"%(a+b,a*b))

