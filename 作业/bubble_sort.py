def bubble_sort(arr):
    num = len(arr)
    for i in range(0, num):
        for j in range(i+1, num):
            if(int(arr[i]) < int(arr[j]) ):
                arr[i],arr[j] = arr[j],arr[i]
    return arr
if __name__ == "__main__":
    num_str = input('请输入要排序的数字序列：')
    l = num_str.split()

   # bubble_sort(l1)
    print('排序的结果是:',bubble_sort(l))
