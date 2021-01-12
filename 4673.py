num = set(range(1, 10001))
generated_num = set()

for i in num:
    for n in str(i):
        i += int(n)
    generated_num.add(i)

self_num = num - generated_num
for j in sorted(self_num):
    print(j)