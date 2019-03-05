import sys
def func3():
    global i
    i = 7
    if __name__ == '__main__':
        print('1111')
    else:
        print('2222')


print(func3())
print(i)
print(sys.platform)
a = sys.stdin
print(a)

if __name__ == '__main__':
    print('1111')
else:
    print('2222')

dir(sys)
