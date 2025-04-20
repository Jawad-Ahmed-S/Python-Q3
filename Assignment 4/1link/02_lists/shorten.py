MAX_LENGTH:int  = 5
list = [4,5,6,7,8,9,4,6,7]
def shorten(list):
    while len(list)>MAX_LENGTH:
        print(list[-1])
        list.pop(-1)

shorten(list)
print(list);