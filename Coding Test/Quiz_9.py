import queue

task_num = int(input())
task = queue.Queue()

for i in range(task_num):
    cust_id, task_time = input().split(' ')
    task.put([int(cust_id), int(task_time)])

def answer(task):
    print('-- 처리한 고객의 아이디 --')
    total_time = 0
    work_time = 50
    cust_list = []
    while(task.qsize() > 0):
        cust_id, task_time = task.get()
        if task_time > work_time:
            print(cust_list)
            cust_list.clear()
            total_time += 10
            work_time = 50
        cust_list.append(cust_id)
        total_time += task_time
        work_time -= task_time
    print(cust_list)

    print(f'\n총 소요시간: {total_time}분')

answer(task)