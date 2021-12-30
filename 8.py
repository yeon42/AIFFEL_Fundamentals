#%% for 문 잘 써보기
my_list = ['a', 'b', 'c', 'd']
for i in my_list:
    print('값 : ', i)

# %% enumerate(): 순서와 리스트 값 함께 반환
my_list = ['a', 'b', 'c', 'd']

for i, value in enumerate(my_list):
    print("순번: ", i, " , 값: ", value)


# %% 이중 for문
my_list = ['a', 'b', 'c', 'd']
result_list = []

for i in range(2):
    for j in my_list:
        result_list.append((i, j))

print(result_list)

# %% 리스트 컴프리헨션 (list Comprehension)
my_list = ['a', 'b', 'c', 'd']

result_list = [(i, j) for i in range(2) for j in my_list]

print(result_list)
# %% 제너레이터(generator)
my_list = ['a', 'b', 'c', 'd']

# 인자로 받은 리스트를 가공해 만든 데이터셋 리스트를 리턴하는 함수
def get_dataset_list(my_list):
    result_list = []
    for i in range(2):
        for j in my_list:
            result_list.append((i, j))
    print(">> {} data loaded..".format(len(result_list)))
    return result_list

for X, y in get_dataset_list(my_list):
    print(X, y)

'''
이중 for문도 다 돌아가고, 반환된 값에 대해서도 for문을 돌려야하므로,
뭔가 중복되는 느낌이 들고, 확실히 느릴 것이다.
'''



# %%
my_list = ['a', 'b', 'c', 'd']

# 인자로 받은 리스트로부터 데이터를 하나씩 가져오는 제너레이터를 리턴하는 함수
def get_dataset_generator(my_list):
    result_list = []
    for i in range(2):
        for j in my_list:
            yield (i, j) # 이전의 append 코드 대체
            print(">> 1 data loaded...")

dataset_generator = get_dataset_generator(my_list)
for X, y in dataset_generator:
    print(X, y)

'''
yield를 사용하면 처리해야 할 데이터를 1개씩 로드해서 사용할 수 있음
'''


# %% Zero Division Error
print(10/0)



# %%
a = 10
b = 0
try:
    print(a/b)
except:
    print('에러가 발생했습니다.')



# %%
a = 10
b = 1
try:
    print(a/b)
except:
    print(a/b)



# %%
a = 10
b = 0 

try:
    #실행 코드
    print(a/b)
		
except:
    print('에러가 발생했습니다.')
    b = b + 1
    print("값 수정: ", a/b)



# %%
import time
start = time.time() # 시작 시간 저장

a = 1
for i in range(10):
    a += 1

print("time: ", time.time() - start)



# %% 변수 1억 번 돌리는 코드
import time

num_list = ['p1', 'p2', 'p3', 'p4']
start = time.time()

def count(name):
    for i in range(0, 100000000):
        a = 1+2
        # pass
    
    print("finish: " + name + '\n')

for num in num_list:
    count(num)

print('time; ', time.time() - start)



# %% 병렬 처리 -> vscode에서 실행 x
from multiprocessing import *
import time

num_list = ['p1', 'p2', 'p3', 'p4']
start = time.time()

def count(name):
    for i in range(0, 100000000):
        a = 1+2
    print('finish: ' + name + '\n')

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes = 4)
    pool.map(count, num_list)
    pool.close()
    pool.join()

print('time: ', time.time() - start)

# %% 함수 사용
def function_F(input_x):
    output_x = input_x * input_x
    return output_x


# %% 최대값 구하는 코드
list_data = [10, 20, 30, 40]
list_data2 = [20, 30, 40, 50]

length = len(list_data)
max_result = list_data[0]

for i in range(length):
    if max_result < list_data[i]:
        max_result = list_data[i]

print("최댓값은: ", max_result)

length = len(list_data2)
max_result = list_data2[0]

for i in range(length):
    if max_result < list_data2[i]:
        max_result = list_data2[i]

print("최대값은: ", max_result)
# %% 최대값 구하기 - 함수 이용
list_data = [10, 20, 30, 40]
list_data2 = [20, 30, 40, 50]

def max_function(x):
    length = len(x)
    max_result = x[0]

    for i in range(length):
        if max_result < x[i]:
            max_result = x[i]
    return max_result

print("최대값은 ", max_function(list_data))
print("최대값은 ", max_function(list_data2))

# %% 함수 안에 함수
def say_something(txt):
    return txt

def send(function, count):
    for i in range(count):
        print(function)

send(say_something("안녕!"), 2)

# %% 함수 안에 함수 & 2개 이상의 return
list_data = [30, 20, 30, 40]

def minmax_function(x_list):
    def inner_min_function(x):
        length = len(x)
        min_result = x[0]
        for i in range(length):
            if min_result > x[i]:
                min_result = x[i]
        return min_result
    
    def inner_max_function(x):
        length = len(x)
        max_result = x[0]
        for i in range(length):
            if max_result < x[i]:
                max_result = x[i]
        return max_result
    
    x_min = inner_min_function(x_list)
    x_max = inner_max_function(x_list)

    minmax_list = [x_min, x_max]

    return minmax_list

print('최소값, 최대값은: ', minmax_function(list_data))
print('최소값은: ', minmax_function(list_data)[0])
print('최대값은: ', minmax_function(list_data)[1])

# %% lambda 함수
print((lambda x, y: x + y) (10, 20))



# %%
def list_mul(x):
    return x**2

result = list(map(list_mul, [1, 2, 3]))
print(result)

'''
map()의 결과는 그냥 map 객체이므로 결과 창에서 직접 
눈으로 확인할 수 있는 형태로 바꾸기 위해
list()를 사용해 리스트 형태로 반환해준다.
'''


# %%
result = list(map(lambda i: i*2, [1, 2, 3]))
print(result)



# %% 모듈 사용하기
# 'mycalculator.py'
test = 'you can use this module.'

def add(a, b):
    return a+b
def mul(a, b):
    return a*b
def sub(a, b):
    return a-b
def div(a, b):
    return a/b

class all_calc():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b
    def sub(self):
        return self.a - self.b
    def div(self):
        return self.a / self.b


'''
이렇게 저장한 뒤
'''

# %%
import mycalculator
print(mycaculator.add(4, 2))
# %%
import mycalculator as mc

print(mc.add(4, 2))
# %% 함수형 프로그래밍 (순수성이 없음)
A = 5

def impure_mul(b):
    return b * A

print(impure_mul(6))


# %% 순수서잉 있음
def pure_mul(a, b):
    return a * b

print(pure_mul(4, 6))

'''
함수 안에 함수 밖에서 바로 가져오는 함수나
or 밖에 있는 변수를 변경시키는 코드가 없음
'''

# %%
