data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 = 0
			print(len(data))
print('檔案讀取完成, 共有' , len(data), 筆)

sun_len = 0
for d in data:
		len(d)
		sum_len = sum_len + len(d)
print('每筆平均長度為',sum_len/len(data))



