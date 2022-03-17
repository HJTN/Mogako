from xmlrpc.client import MAXINT

# '{에너지 드링크 번호}: [{카페인 함량},{타우린 함량}]
drink_list = {
    '0':[100,320], 
    '1':[232,720], 
    '2':[600,103], 
    '3':[100,124], 
    '4':[730,1076],
    '5':[185,125], 
    '6':[104,600], 
    '7':[392,705], 
    '8':[33,265], 
    '9':[89,421],
}

def answer(drink_data, fix_n):
    start_idx = 0
    record_idx = 0
    total = 0 - MAXINT
    while(start_idx <= len(drink_data) - fix_n):
        cur_cal = 0
        # start 포인터부터 fix_n개 드링크의 (타우린 - 카페인) 값의 합 구하기
        for i in range(start_idx, start_idx + fix_n):
            cur_cal += drink_data[f'{i}'][1] - drink_data[f'{i}'][0]
        # {타우린 함량의 합} - {카페인 함량의 합}이 큰지 확인
        if total < cur_cal:
            total = cur_cal
            record_idx = start_idx
        # start 포인트 증가
        start_idx += 1
    # {타우린 함량의 합} - {카페인 함량의 합}이 가장 큰 연속된 3개의 에너지 드링크 출력
    tau = 0
    cafe = 0
    for i in range(record_idx, record_idx + fix_n):
        print(i, end=' ')
        tau += drink_data[f'{i}'][1]
        cafe += drink_data[f'{i}'][0]
    print(f'의 타우린 합은 {tau}, 카페인 합은 {cafe}로 가장 효과가 좋습니다.')

answer(drink_list, 3)