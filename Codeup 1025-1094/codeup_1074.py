aa = int(input())
bbb = aa -1

def count_down (num):

    if num < 0 :
        return

    print (num)

    count_down(num-1)

count_down(bbb)