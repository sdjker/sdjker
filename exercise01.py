

data1 = [4, 29, 41, 92, 70, 60, 43, 54, 56, 49, 77, 10, 14, 46, 52, 20, 40, 64, 93, 70, 0, 91, 20, 59, 54,
         93, 46, 89, 11, 75, 50, 16, 97, 55, 11, 32, 1, 7, 36, 55, 13, 19, 89, 96, 88, 14, 26, 2, 63, 44]

data2 = [
    'business',
    'switch',
    'letters',
    'agonizing',
    'irate',
    'strange',
    'light',
    'bone',
    'clover',
    'locket',
    'knock',
    'part',
    'throne',
    'announce',
    'mitten',
    'claim',
    'impartial',
    'structure',
    'vessel',
    'homely',
    'arrange',
    'ticket',
    'growth',
    'quarrelsome',
    'satisfying',
    'avoid',
    'panoramic',
    'perfect',
    'beautiful',
    'escape',
    'daily',
    'subtract',
    'knowledgeable',
    'argument',
    'butter',
    'invincible',
    'rhetorical',
    'overflow',
    'humor',
    'tease',
    'noxious',
    'crime',
    'truculent',
    'shake',
    'bridge',
    'bulb',
    'phobic',
    'icky',
    'immense',
    'space'
]



# 문제 1. 정렬 함수를 반복문, 조건문을 이용하여 구현하시오.
#        함수 이름의 "alg" 부분은 정렬 알고리즘 이름으로 대체 (예: bubble_sort(arr): )
def alg_sort(arr):

    return arr




# 문제 2. 리스트에서 중복을 제거하는 함수를 반복문, 조건문을 이용하여 구현하시오.
def unique(arr):
    result = []

    return result




# 문제 3. 아래의 정렬 조건으로 문자열 리스트를 정렬하는 함수를 작성하시오.
#  조건1: 문자열의 길이가 긴 것에서 짧은 순서로 정렬
#  조건2: 문자열의 길이가 같은 경우, abc 순으로 정렬
def custom_sort(arr):

    return arr




if __name__ == '__main__':

    data1_sorted = alg_sort(data1)

    print(len(data1_sorted), data1_sorted)


    data1_unique = unique(data1)

    print(len(data1_unique), data1_unique)


    data2_sorted = custom_sort(data2)

    for word in data2_sorted:
        print(word)
