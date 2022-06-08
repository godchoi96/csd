# lambda

x = 3.0
print(type(x))
print(x.is_integer())
"""
1.
lambda 함수를 알기 전, 함수도 객체라는 사실을 알아보자.
변수 x에 실수 3.0 이라는 객체를 참조했다. 우리가 이 type을 찍어보면 <class 'float'> 라고 나오는 것을 알 수 있다.
여기서 알 수 있는 사실은 파이썬에서 객체를 담을 때 어떤 클래스에 담아서 이를 참조하는 것이라는 의미이다.
즉, 위에서는 x 변수를 선언하면서 float라고 파이썬 내장 클래스에 저장을 시키는 것이다.
"""

def func1(x):
    return x

def func2():
    print('Hello, CSD')

print(type(func1))
print(type(func2))
"""
2.
함수 또한 마찬가지이다.
type() 모듈을 찍어보면 <class 'function'> 라고 나오는데 이 또한 파이썬 내장 클래스 function 이라는 것에 저장시키는 것이다.
따라서 정리하면 파이썬은 기본적으로 내장 클래스에 해당 객체를 담을 수 있는 클래스가 존재하고 함수 또한 예외는 아니라는 것이다.
"""

def say1():
    print('hello')

def say2():
    print('hi')

def caller(fnc):
    fnc()

caller(say1)
caller(say2)
"""
3.
say1 이라는 함수가 있고 say2 라는 함수가 있다.
say1은 hello를 출력하는 것을 객체로 참조하고 있고 say2 또한 hi를 출력하는 것을 객체로 참조하고 있다.
따라서 이 함수들의 레퍼런스 카운트는 모두 1인 상태이다. 
여기서 caller 함수의 매개변수를 fnc로 받아 이를 통해 함수를 호출하는 방식이다.
say1 함수를 파라미터로 받아 실행시키면 fnc도 참조하기 때문에 say1 함수의 레퍼런스 카운트는 2가 된다.

함수 또한 객체라는 사실이기 때문에 레퍼런스 카운트가 증가함을 알 수 있다.
"""

def fct_fac(n):
    def exam(x):
        return x ** n
    return exam

square2 = fct_fac(2)
print(type(square2))
print(square2(3))
square3 = fct_fac(3)
print(square3(3))
"""
4.
함수 안에 함수는 가능할까? 결과는 가능하다. 간단하게 입력 제곱근을 만들어내는 함수는 다음과 같다.
가장 먼저 square2 라는 변수에 fct_fac 함수 객체를 참조하게 했다. 그리고 함수 매개변수에 2를 넣는다.
square2 변수는 함수를 참조했기 때문에 함수가 된다. 현재는 인자를 넣으면 인자를 제곱해주는 함수인 셈이다.
square2(3) 이라고 해서 파라미터로 3을 넣어주면 3의 제곱이 되기 때문에 9를 반환해서 출력하게 되는 것이다.
"""

def fct_fac(n):
    def exam(x):
        return x ** n
    return exam
"""
5.
위에서 함수 안의 함수를 다시 보면 내가 exam 이라는 함수를 따로 실행시킨 적이 없었다.
변수가 fct_fac 함수를 참조하면 exam을 다시 반환했다. 따라서 매개변수 2를 넣으면 2는 exam 함수에 종속되고 변수는 함수가 되는 셈이다.

fct_fac 함수를 통해 exam 이라는 함수를 만들고 이를 반환해주는데 이것을 변수가 참조하면 변수가 그 함수가 되는 셈이다.
하지만 이 함수를 콜하거나 하는 일이 아닌 반환 목적이기 때문에 딱히 함수네임은 중요하지 않다.
이처럼 함수의 이름은 불필요한데 함수 로직을 반환하는 것이 목적인 개념을 바로 람다 함수라고 한다.
"""

square = lambda n, x: x ** n
print(square(3, 2))
"""
6.
위의 함수를 람다식으로 정리하면 다음과 같다.
lambda 다음에 매개변수, 그리고 반환할 식을 적으면 된다.
"""