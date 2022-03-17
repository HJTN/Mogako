def answer(n):
    prime_range = n + 1
    prime_list = [True] * prime_range

    # 0, 1 index의 prime_list를 False로 설정
    prime_list[0] = False
    prime_list[1] = False

    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        if prime_list[i]:
            for j in range(i + i, prime_range, i):
                prime_list[j] = False
    
    # Prime 값 추출
    primes = []
    for i in range(2, prime_range):
        if prime_list[i]:
            primes.append(i)

    cur_list = []
    start_idx = 0
    next_idx = 0
    while(start_idx < len(primes)):
        cur_list.append(primes[next_idx])
        if sum(cur_list) == n:
            break
        elif sum(cur_list) < n:
            if next_idx == len(primes)-1:
                cur_list.clear()
                break
            else:
                next_idx += 1
        else:
            start_idx += 1
            next_idx = start_idx
            cur_list.clear()
    
    if cur_list:
        print(f'연속된 소수{cur_list}의 합은 {n}입니다.')
    else:
        print(f'연속된 소수의 합으로 {n}을 만들 수 없습니다.')

for i in range(2, 21):
    answer(i)
