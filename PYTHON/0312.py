
# 자료형 중에서
"""
1. 숫자형 
   - 정수형 integer, int
a = 123    
   
   
   
   
   
   - 실수형 (소수형) float



"""

a = 123   # 등호는 등호가 아니다. 등호는 ==
b = 100
print(a+b)
## assignment 할당한다 

type(a)

c = 100.0
type(c)

a+c

# 정수형으로 바꾸기
int(a+c)

# 실수형으로 바꾸기
b = 100
float(b)

float("100")
float("100")

int("100")
int("Hello")

"100" + "10"

a = "100"
b = "10"
a+b

### 16진법

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 
# A(10), B(11), C(12), D(13), E(14), F(15) # 알파벳은 10부터 세면 됨.

# 0x1A  > 1*16 + A (10)  > A 는 10
# 0x2A  > 2*16 + A (10)
# 0x22A > 2*16*16 + 2*16 + A (10)

# 0xFF  > 15*16 + 15
### 16진법에서 F는 15


# 연산기호
2*3
2**3

23 % 10
# 23을 10으로 나눈 나머지 값이 출력 됨 > 나머지 기호는 %

a = 100
a = a + 1

a += 1    # 할 때 마다 1 만큼 증가
a

a = a - 1
a

a *= 2
a


"""
문자, 문자열 : string
"""

a = "Hello"
print(a)

a = """
    Life is too short
    You need Python
    Life is too short
    You need Python
    """

a = """
life is too short
you need python
life is too short
you need python
"""

a = '"python is easy" he says'
print(a)

a = """
    life is too short
    you need python
    life is too short
    you need python
    """








# 역슬래시 escape charcter  - 눈에 보이는 대로 출력

a = "he's diamond"
print(a)

a = 'he\'s diamond' 
print(a)

a = 'he\\s diamond' 
print(a)

a = 'he\ns diamond' 
print(a)

a = 'he\ns diamond' 
print(a)

### \n > new line


a = "Life is too short. \nYou need Python"
print(a)

a = "Life is too short. \tYou need Python"
print(a)


a = '100'
b = '10'

a + b # 문자열에서 + 는 더하기가 아니라 이어붙이기 concatenate (concat)
a - b
a * b
a / b

a = "Hello"
b = "Good Morning"

a + b
a * 10 

print("="*30)
print("\t\t안녕하세요.")
print("="*30)
# 문자열은 빼기 곱하기 나누기는 안되지만
# 뒤에 숫자가 있을 때 위처럼 곱하기 사용하기는 가능하다.

print("="*30)
print("\n안\n녕\n하\n세\n요.")
print("="*30)


a = "Hello"  
len(a)
# length < - long 길이 = 크기 = 갯수

a = "Good Morning"
len(a)
# 스페이스 바도 포함

# indexing 인덱싱
a[0]
# index 로 맨 앞 철자만 출력하기

a[1]
a[2]
a[3]
a[4]

a[-1]
a[-2]
# -2는 뒤에서 두번째

## Slicing 슬라이싱

# "Good" 인덱싱으로 출력해주세요. 
a[0:4]

# "Monring" 인덱싱으로 출력해주세요
a[5:12]
a[5:  ] # morning
# 블랭크는 끝까지의 표현

a[  :4]
a[  : ]
a[-7: ] # morning

weather = "20260312shiny"

(weather[:4])      # 2026
(weather[4:8])     # 0312
(weather[8:])      # shiny

변수
variable
varios

a = "I ate 3 apples. So I have sicked two days"
print(a)


# 변수로 알려주는 방법

numbers = 3
days = "two"

# 방법 1. 
a = "I ate %d apples. So I have sicked %s days" %(numbers, days)
print(a)


# 방법 2. formatting
a = "I ate {} apples. So I have sicked {} days".format(numbers, days)
print(a)

a = "I ate {0} apples. So I have sicked {1} days".format(numbers, days)
print(a)

a = "I ate {1} apples. So I have sicked {0} days".format(numbers, days)
print(a)

a = "I ate {0} apples. So I have sicked {0} days".format(numbers, days)
print(a)


a = "I ate {0}{1} apples. So I have sicked {0} days".format(numbers, days)
print(a)


# 방법 3. f-string
numbers = 3
days = "two"

a = f"I ate {numbers} apples. So I have sicked {days} days".format(numbers, days)
print(a)

a = '"Python is very difficult." That\'s what she says.'
print('"Python is very difficult." \nThat\'s what she says')


a = "Good Morning everyone"

# 인덱싱을 활용하여 "everyone" 만 출력해보자.

a[13:]

a = "Have A Nice Day"
a[7:11]

a = 105
105 % 2

0/

