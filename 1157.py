word = input().upper()
word_list = list(set(word))
count_list = [] #count_list는 [1.1]

for i in word_list: #(zza라고 하면 word_list는 ['a','z']
    count = word.count(i) #word의 각각 알파벳 갯수가 몇 개 인지 센다
    count_list.append(count) #cnt

if count_list.count(max(count_list)) >= 2: #max의 개수를 count했는데 1보다 크면
    print("?")
else:
    max_index = count_list.index(max(count_list)) #max_index를 구하고 index값을 출력한다다
    print(word_list[max_index].upper())

