def binary_search(arr, start, end, target):
    if(start <= end):
        mid = (start + end) // 2
        if(arr[mid] == target):
            print(1)
        elif(arr[mid] > target):
            binary_search(arr, start, mid-1, target)
        else:
            binary_search(arr, mid+1, end, target)

arr = [1,2,3,4,5,6,7,8,9,10]
target = 9
binary_search(arr, 0, len(arr)-1, target)

#### LAN Problem ####
num_LAN = 4
LANs = []
target = 10

for idx in range(num_LAN):
    LANs.append(int(input()))
#for idx in range(len(LANs)):
#    print(LANs[idx])

global max_LAN
max_LAN = 0

def find_max_LAN(LANs, start, end, target):
    global max_LAN
    if(start <= end):
        LAN_count = 0
        mid = (start+end) // 2

        for LAN in LANs:
            LAN_count += LAN // mid
        
        if(LAN_count >= target):
            if(max_LAN < mid):
                max_LAN = mid
            find_max_LAN(LANs, mid+1, end, target)
        else:
            find_max_LAN(LANs, start, mid-1, target)

find_max_LAN(LANs, 1, max(LANs), target)
print(max_LAN)