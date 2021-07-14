#password is 'a1234567890'
i = 3
password = 'a1234567890'
while True:
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功！！！')
		break
	else:
		i = i - 1
		print('密碼錯誤, ' , i,'次機會')
		if i == 0:
			print('登入失敗')
			break
			
