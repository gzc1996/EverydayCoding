def stringCompare(str1, str2):
    if str1 in str2:
        print("yes1")


# index指str2在str1中的开始下标，为-1则证明str1中不包含str2
def stringCompare2(str1, str2):
    if str1.index(str2) > -1:
        print("yes2")


# 同样是查询str2在str1中的开始下标
def stringCompare3(str1, str2):
    if str1.find(str2) > -1:
        print("yes3")


if __name__ == '__main__':
    a = "helloworld"
    b = "world"
    stringCompare(b, a)
    stringCompare2(a, b)
    stringCompare3(a, b)