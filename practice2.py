file_obj = open('lotto999.csv', 'rt', encoding='utf-8')
lines = file_obj.readlines()
file_obj.close()

prize_list = []

def prize(input_list, num_txts_modified, num_txts_modified_modified, order):
    prize_count = 0
    bonus_count = 0

    for input in input_list:
        if input in num_txts_modified:
            prize_count += 1

    for input in input_list:
        if input in num_txts_modified_modified:
            bonus_count += 1

    if prize_count == 6:
        prize_list.append(1)        
    
    elif prize_count == 5:
        if bonus_count == 6:
            prize_list.append(2)
        elif bonus_count != 6:
            prize_list.append(3)

    elif prize_count == 4:
        prize_list.append(4)

    elif prize_count == 3:
        prize_list.append(5)

    else:
        prize_list.append('꽝')

your_number_list = []
for q in range(6):
    p = 6 - q
    print('숫자 입력 가능 횟수 :', p)
    s = input()
    your_number_list.append(int(s))

for line in lines[1:]:
    line_strip = line.strip()
    num_txts = line_strip.split(',')

    num_txts_modified = num_txts[1:7] # 1부터 6

    num_txts_modified_modified = num_txts[1:] # 보너스 넘버를 포함

    order = int(num_txts[0]) # 회자를 기록하기 위함

    nums = []
    nums_bonus = []
    
    for txt in num_txts_modified: # 1부터 6 -> 숫자만이 기록된 리스트로 변환한다
        nums.append(int(txt))

    for txt2 in num_txts_modified_modified: # 보너스 넘버를 포함 -> 숫자만이 기록된 리스트로 변환
        nums_bonus.append(int(txt2))

    prize(your_number_list, nums, nums_bonus, order)

first_prize_list = []
second_prize_list = []
third_prize_list = []
fourth_prize_list = []
fifth_prize_list = []
fail_prize_list = []

for i, ranking in enumerate(prize_list):
    v = 999 - i
    if ranking == 1:
        first_prize_list.append(v)
    
    elif ranking == 2:
        second_prize_list.append(v)

    elif ranking == 3:   
        third_prize_list.append(v)

    elif ranking == 4:
        fourth_prize_list.append(v)

    elif ranking == 5:
        fifth_prize_list.append(v)
        
    elif ranking == '꽝':
        fail_prize_list.append(v)






if len(first_prize_list) > 0:
    for a in first_prize_list:
        print(a,'회차 1등')
        break       
if len(first_prize_list) == 0 and len(second_prize_list) > 0:
    for b in second_prize_list:
        print(b,'회차 2등')

if len(first_prize_list) == 0 and len(second_prize_list) == 0 and len(third_prize_list) > 0:
    for c in third_prize_list:
        print(c,'회차 3등')

if len(first_prize_list) == 0 and len(second_prize_list) == 0 and len(third_prize_list) == 0 and len(fourth_prize_list) > 0:
    for d in fourth_prize_list:
        print(d,'회차 4등')    

if len(first_prize_list) == 0 and len(second_prize_list) == 0 and len(third_prize_list) == 0 and len(fourth_prize_list) == 0 and len(fail_prize_list) > 0:
    for e in fail_prize_list:
        print(e,'꽝')
    

    




