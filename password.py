password = 'a123456'
x = 3
while x > 0:
	key = input('請輸入密碼:')
	if key == password:
		print('登入成功')
		break
	else:
		x -= 1
		if x == 0:
			print('登入失敗')
			break
		print('密碼錯誤,您還有', x,'次機會')
