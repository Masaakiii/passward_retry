#password
chance = 3
while chance > 0:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功!')
		break
	else: 
		chance = chance - 1
		if chance > 0:
			print('密碼錯誤! 還有', chance, '次機會')
		if chance == 0:
			print('錯誤次數過多,將封鎖帳戶30分鐘!')