# %% 입력한 숫자들로 평균 계산하기
total = 0 # 총합
count = 0 # 개수
numbers = input('Enter a number: ')
while numbers != "":
    try:
        x = float(numbers)
        count += 1
        total += x
    except ValueError:
        print('NOT a number!')
    
    numbers = input('Enter a number: ')

avg = total / count
print('\n average is ', avg)



# %% 입력한 숫자들로 배열 만들기
def numbers():
    X = [] # 빈 리스트
    while 1:
        number = input('Enter a number: ')
        while number != '':
            try:
                x = float(number)
                X.append(x)
            except ValueError:
                print('>>> NOT a number!')
            number = input('Enter a number: ')

        if len(X) > 1: # 저장된 숫자가 2개 이상일 때만 리턴
            return X

X = numbers()
print('X: ', X)



# %%
'''
파이썬 리스트는 동적 배열(Dynamic Array)이다.
임의의 데이터 타입을 담을 수 있는 가변적 연속열(Sequence)형
    ex. C처럼 처음 배열 변수 만들 때 원소 개수 지정 안 해도 됨
'''



# %% list와 array의 차이를 알아보자
import array as arr

# list
mylist = [1, 2, 3]
print(type(mylist))

mylist.append('4')
print(mylist)

mylist.insert(1, 5)
print(mylist)

# array
myarray = arr.array('i', [1, 2, 3])
print(type(myarray))

#myarray.append('4')
print(myarray)

myarray.insert(1, 5)
print(myarray)


'''
array를 사용하기 위해서는 import 해줘야 하구나 (built-int이 아님)
array는 연속된 메모리 공간에 배치되므로, 모든 element들이 동일한 크기/타입 가져야 함
list 안에서는 다른 타입의 자료형 허용된다.
'''



# %% 리스트를 이용해 시그마 표현
total = 0.0
for i in range(len(X)):
    total += X[i]
mean = total / len(X)

print('sum of X: ', total)



# %% 중앙값
def median(nums):
    nums.sort() # sort함수로 리스트 정렬
    size = len(nums)
    p = size // 2   # 몫 구하기

    if size % 2 == 0: # 리스트 개수 짝수일 때
        pr = p
        pl = p-1
        mid = float((nums[pl] + nums[pr]) / 2)
    else:
        mid = nums[p] # 홀수는 중앙값이 존재하니까!
    
    return mid

print('X: ', X)
median(X)

'''
ex. 먄약 size가 6이라면 pr=3, pl=2
-> mid는 이 둘의 평균
'''



# %% 평균
def means(nums):
    total = 0.0
    for i in range(len(nums)):
        total += nums[i]
    
    return total / len(nums)

means(X)




# %% 표준편차
avg = means(X)

def std_dev(nums, avg):
    texp = 0.0
    for i in range(len(nums)):
        texp += (nums[i] - avg) ** 2 # 각 수와 평균의 차이 제곱 더하기
    
    return (texp / len(nums)) ** 0.5 # 루트 취해주기

std_dev(X, avg)



# %% numpy - ndarray 만들기
import numpy as np

# A, B는 결과적으로 같은 ndarray 객체를 생성함
A = np.arange(5)
B = np.array([0, 1, 2, 3, 4]) # 리스트를 numpy ndarray로 변환

C = np.array([0, 1, 2, 3, '4'])

# D도 A, B와 같지만 B의 방법을 권장함
D = np.ndarray((5,), np.int64, np.array([0, 1, 2, 3, 4]))

print(A)
print(type(A))
print('---------------------')
print(B)
print(type(B))
print('---------------------')
print(C)
print(type(C))
print('---------------------')
print(D)
print(type(D))

'''
C도 문자열로 바꼈다.
-> 문자열을 모두 숫자로 바꿀 순 없지만, 숫자는 모두 문자여롤 바꿀 수 있음
-> ndarray에 문자열이 들어가면 몯느 숫자를 문자열로 해석해 array의 요건 맞춰줌!
'''



# %% 행렬
A = np.arange(10).reshape(2, 5) # 2x5 행렬

print(A)
print('행렬의 모양: ', A.shape)
print('행렬 축 개수: ', A.ndim) # axis 개수
print('행렬 내 원소 개수: ', A.size)



# %%
A = np.arange(10)
print('A: ', A)

B = np.arange(10).reshape(2, 5)
print('B: ', B)

# 3x3은 모양, 원소 개수가 맞지 않으므로 에러가 남
# C = np.arange(10).reshape(3, 3)
# print('C: ', C)



# %%
'''
Numpy: numpy, array, dtype
파이썬: type()

- dtype: 행렬의 '원소'의 데이터 타입 반환
- type(): 행렬A의 자료형 반환
'''



# %% 이런 ndarray은?
D = np.array([0, 1, 2, 3, [4, 5], 6])
print(D)
print(D.dtype)
print(type(D))



# %% 단위 행렬
np.eye(3)



# %% 0 행렬
np.zeros([2, 3])



# %% 1 행렬
np.ones([3, 3])



# %% 브로드캐스트(broadcast) 연산
A = np.arange(9).reshape(3, 3)
print(A)
print(A*2)
print(A+2)



# %% 3x3에 1x3 더하기
A = np.arange(9).reshape(3, 3)
B = np.array([1, 2, 3])

print('A: ', A)
print('B: ', B)
print('\nA+B: ', A+B)



# %% 3x3에 3x1 더하기
A = np.arange(9).reshape(3, 3)
C = np.array([[1], [2], [3]])

print('A: ', A)
print('C: ', C)
print('\nA+C: ', A+C)



# %%
print([1, 2] + [3, 4])

print(np.array([1, 2]) + np.array([3, 4]))
print(np.array([1, 2]) + 3)



# %%
A = np.arange(9).reshape(3, 3)
print(A[:, 2:])
print(A[:, 1:])
print(A[:, :]) # 전체

print(A[:, -1])



# %% random
print(np.random.random())
print(np.random.randint(0, 10)) # 정수형 난수
print(np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))



# %% 무작위로 섞인 배열
print(np.random.permutation(10))
print(np.random.permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))



# %% 정규분포
print(np.random.normal(loc=0, scale=1, size=5))

''' 평균(loc), 표준편차(scale), 추출개수(size) '''



# %% 전치행렬
A = np.arange(24).reshape(2, 3, 4)
print(A)
print('-----------------------')
print(A.T)
print('-----------------------')
print(A.T.shape)



# %% transpose: 변화할 축 임의로 지정 가능
B = np.transpose(A, (2, 0, 1)) # 위와 정확히 같음
print(A)
print('-----------------------')
print(B)
print('-----------------------')
print(B.shape)



# %% numpy로 기본 통계 데이터 계산하기
import numpy as np

def numbers():
    X = []
    number = input('Enter a number: ')
    while number != '':
        try:
            x = float(number)
            X.append(x)
        except ValueError:
            print('>>> NOT a number! ')
        
        number = input('Enter a number: ')
    return X

def main():
    nums = numbers()
    num = np.array(nums) # 리스트를 array로 변경
    print('합: ', num.sum())
    print('평균값: ', num.mean())
    print('표준편차: ', num.std())
    print("표준편차", num.std())
    print("중앙값", np.median(num)) # num.median() 아님 주의

main()



# %% 해시 (Hash) - 파이썬 dict
Country_PhoneNumber = {'Korea': 82, 'America': 1, 'Swissh': 41}
Country_PhoneNumber['Korea']



# %% 물품을 보여주는 함수
treasure_box = {'rope':2, 
                'apple':10, 
                'torch': 6, 
                'gold coin': 50, 
                'knife': 1, 
                'arrow': 30}

def display_stuff(treasure_box):
    print("Congrats! you've got a treasure box")
    for k, v in treasure_box.items():
        print('you have {} {}pcs'.format(k, v))

display_stuff(treasure_box)



# %% 물품을 통해 얻을 은화를 보여주는 함수
coin_per_treasure = {'rope':1,
        'apple':2,
        'torch': 2,
        'gold coin': 5, 
        'knife': 30,
        'arrow': 1}

def total_silver(treasure_box, coin_per_treasure):
    total_coin = 0
    for treasure in treasure_box:
        coin = coin_per_treasure[treasure] * treasure_box[treasure]
        print("{}: {}coins/pcs * {}pcs = {} coins".format(
            treasure, coin_per_treasure[treasure],
            treasure_box[treasure], coin))
        total_coin += coin
    print('total_coin: ', total_coin)

total_silver(treasure_box, coin_per_treasure)



# %% 구조화된 데이터
treasure_box = {'rope': {'coin': 1, 'pcs': 2},
                'apple': {'coin': 2, 'pcs': 10},
                'torch': {'coin': 2, 'pcs': 6},
                'gold coin': {'coin': 5, 'pcs': 50},
                'knife': {'coin': 30, 'pcs': 1},
               	'arrow': {'coin': 1, 'pcs': 30}
               }
treasure_box['rope']



# %% Series: 일련의 객체를 담을 수 있음
import pandas as pd
ser = pd.Series(['a', 'b', 'c', 3])
print(ser)
print(ser.values)
print(ser.index) # RangeIndex 반환 (정수형 인덱스)




# %%
ser2 = pd.Series(['a', 'b', 'c', 3], index=['i', 'j', 'k', 'h'])
print(ser2)



# %%
ser2.index = ['John', 'Steve', 'Jack', 'Bob']
print(ser2)



# %%
Country_PhoneNumber = {'Korea': 82, 'America': 1, 'Swiss': 41, 'Italy': 39, 'Japan': 81, 'China': 86, 'Rusia': 7}
ser3 = pd.Series(Country_PhoneNumber)
ser3



# %%
ser3['Italy':]



# %% Series 객체의 이름과 인덱스 이름 설정
ser3.name = 'Country_PhoneNumber'
ser3.index.name = 'Country_Name'
ser3



# %% Series로 변환
import pandas as pd
data = {'Region' : ['Korea', 'America', 'Chaina', 'Canada', 'Italy'],
        'Sales' : [300, 200, 500, 150, 50],
        'Amount' : [90, 80, 100, 30, 10],
        'Employee' : [20, 10, 30, 5, 3]
        }
s = pd.Series(data)
s



# %% DataFrame으로 변환
d = pd.DataFrame(data)
d



# %%
print(d.columns)
print(d.index)



# %%
d.index=['one','two','three','four','five']
d.columns = ['a','b','c','d']
d



# %%
