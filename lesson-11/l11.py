
#1
try:
    float(input('input a number: '))
except ValueError:
    print('not a number!')
else:
    print('success')
print()

#2
try:
    int(input('input an integer number: '))
except ValueError:
    print('not an integer number!')
else:
    print('success')
print()

#3
my_list=input('input a list: ').split()

try:
    print(my_list[int(input('input an index: '))])
except IndexError:
    print("index is out of range")
except ValueError:
    print('incorrect index input')
print()

#4
try:
    new_list=[float(i) for i in input('input a list of numbers: ').split()]
    print('average is:',sum(new_list)/len(new_list))
except ValueError:
    print('list should contain only numbers!')
except ZeroDivisionError:
    print('list is empty')
print()

#5
try:
    new_list=[float(i) for i in input('input a list of numbers: ').split()]
    res=sum(new_list)/len(new_list)
except ValueError:
    print('list should contain only numbers!')
except ZeroDivisionError:
    print('list is empty')
else:
    print('average is: ', res)
finally:
    print('end.')
print()

#6
closed=False
while not closed:
    try:
        x=float(input('input first number: '))
        y = float(input('input second number: '))
        print(f'{x}/{y}={x/y}')
    except ValueError:
        print('input must be a number, try again\n')
    except ZeroDivisionError:
        print('you cant divide by zero, try again\n')
    else:
        closed=True
print()

#7
class CustomEx(Exception):
    pass

def find_index(mylist, ind):
    if len(mylist)-1 <ind:
        raise CustomEx
    else:
        return mylist[ind]

try:
    mylist=input('input a list divided by space ').split()
    ind=int(input('input index:'))
    result=find_index(list(mylist),ind)
except ValueError:
    print('incorrect index input')
except CustomEx:
    print('index is out of range')
else:
    print(f'element number {ind} is {result}')
print()

#8
try:
    list_e=[float(i) for i in input('input a list of numbers divided bu space: ').split()]
    ind_e=int(input('input index: '))
    div=int(input(f'input the number by which you want to divide the index number {ind_e}({list_e[ind_e]}) '))
    print(f'{list_e[ind_e]}/{div}={list_e[ind_e]/div}')
except ValueError:
    print('input must be numeric')
except ZeroDivisionError:
    print('you cant divide by zero')
except IndexError:
    print('index is out of range')


