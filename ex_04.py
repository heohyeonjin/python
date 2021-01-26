# ---------------------------
# 파이썬 인덱싱 & 슬라이싱
# ---------------------------

# 인덱싱(Index) : 여러 개의 데이터를 저장하는 경우
#                파이썬에서 자동으로 번호를 부여한 것
#                왼-> 오른 : 0~  / 오 -> 왼 : -1

msg = "Happy"
print(msg)         # 전체 데이터 모두 출력
print(msg[0])      # H 문자 1개 데이터만 출력
print(msg[1])      # 요소 또는 원소
print(msg[2])
print(msg[3])
print(msg[4])
print(msg[-1])

jumsu = [12,89,67,10]
print(type(jumsu),jumsu)

# 1번 요소의 점수를 출력
print(jumsu[1])
# 마지막 요소 점수 출력
print(jumsu[-1])

# 슬라이싱 (Slicing) : 데이터 일부를 추출
# [시작 인덱스 : 끝 인덱스 +1]
print(msg[0],msg[1],msg[2],msg[3],msg[4])
print(msg[0:5])
print(msg[:5])
print(msg[6:])

data = [1,2,3,4,5,6,7,8,9,10]
data[5] = "Five"
print(data)

data[5:] = ["five","six","seven","eight","nine","ten"]
print(data)

data[5:] = []
print(data)

data2 = data[:]
#문자열, 튜플은 수정 불가능