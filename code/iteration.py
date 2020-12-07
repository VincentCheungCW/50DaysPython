
sum = 0
for x in range(10001):
    sum = sum + x
print(sum)

for letter in 'Alexander Hamilton':
   if letter == 'i':        # 字母为 i 时直接进入下一轮循环
      continue
   print ('当前字母 :', letter)