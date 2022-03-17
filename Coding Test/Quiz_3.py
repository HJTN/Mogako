num_LAN = 4
LANs = []
target = 10

for idx in range(num_LAN):
    LANs.append(int(input()))
#for idx in range(len(LANs)):
#    print(LANs[idx])

start = 1
end = max(LANs)

while(end-start >= 0):
    LAN_count = 0
    middle = (start+end)//2
    
    for LAN in LANs:
        LAN_count += LAN//middle
    
    if(LAN_count >= target):
        start = middle+1
    else:
        end = middle-1

print(end)