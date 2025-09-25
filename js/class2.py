# student number  chinese english maths


class Student :
    def __init__(self, name, number, chinese, english, maths):
        self.name = name
        self.number = number
        self.chinese = chinese
        self.english = english
        self.maths = maths
        
    def info(self):
        print(f'姓名：{self.name}学号：{self.number}语文：{self.chinese}数学：{self.maths}英语：{self.english}')
        
        
        
a = Student('张逸', '93', '68', '74', '59')

a.info()

l = list()
print(l)