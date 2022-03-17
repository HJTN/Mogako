from xmlrpc.client import MAXINT


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_elt = MAXINT
        # 최솟값 탐색
        for idx in range(i,len(arr)):
            if min_elt > arr[idx]:
                min_elt = arr[idx]
                min_idx = idx
        #print(min_elt, min_idx)
        # 최솟값과 배열의 i번째 데이터와 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # 현재 배열 상태 출력
        print(f'Current Array: {arr}')

arr = [9,6,7,3,5]
selection_sort(arr)