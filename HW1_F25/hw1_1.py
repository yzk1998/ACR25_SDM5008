import time, numpy as np

# (a)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# (b)
SList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(SList)

del_list = [0, 4, 5]
SList = np.delete(SList, del_list).tolist()

print(SList)

#(c)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp_inf(self):
        print(f"Name:{self.name}, Age:{self.age}")
        # f-string

YZK = Student("YZK", 26)

YZK.disp_inf()



