if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    big = max(arr)
    while count < len(arr):
        for i in arr:
            if i == big:
                del (arr[arr.index(i)])
        count += 1
        print(max(arr))
