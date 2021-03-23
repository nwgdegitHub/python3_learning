for i in range(1, 10):
    # print(i)  # 1-9 没有10
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='&')
        # 在python3.X里，你想不让一个输出结束就用： end='' 这里如果没有end=''，那么就会换行
    print("#%……&") # 恢复一条print()另起一行

