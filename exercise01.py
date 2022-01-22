

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



# 문제 1. 반복문, 조건문을 이용하여 리스트에서 중복을 제거해 보세요.
data1_unique = []
for d in data1:
  ...

print(data1_unique)



# 문제 2. 반복문, 조건문을 이용하여 리스트를 정렬해 보세요.
#   힌트: 버블정렬의 경우 인접한 두 수를 비교하여 앞쪽이 큰 경우 서로 위치를 바꿉니다.
#        이것을 배열의 시작부터 끝까지 1회 반복하면 제일 큰 수가 맨 뒤로 가게 됩니다.
data1_sorted = data1.copy()
for stage in range(len(data1_sorted) - 1):
  ...

print(data1_sorted)



# 문제 3. 아래의 조건으로 문자열 리스트를 정렬해 보세요.
#  조건1: 문자열의 길이가 긴 것에서 짧은 순서로
#  조건2: 문자열의 길이가 같은 경우, abc 순으로
data2_sorted = data2.copy()
for stage in range(len(data2_sorted) - 1):
  ...

print(data2_sorted)

