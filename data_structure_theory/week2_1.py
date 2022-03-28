# 1. 클래스 알아보기
class Person:
    def __init__(self, name, age):
        print("self를 프린트했을 때:", self)
        self.name = name
        self.age = age
        print("self.name을 프린트했을 때:", self.name)

    def introduce(self):
        print("###여기는 introduce 함수###")
        print("self.name을 프린트했을 때:", self.name)
        print("안녕하세요 저는", self.name, "입니다.")
        print("제 나이는", self.age, "살입니다.")
        

person1 = Person('최승대', 27)
person1.introduce()