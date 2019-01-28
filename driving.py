country = input('请输入你的国家：')
age = input('请输入你的年龄：')
age = int(age)
if country == '中国':
	if age >= 18:
		print('你可以考驾照了')
	else :
		print('你还不能考驾照')	
elif country == '美国':
	if age >= 18:
		print('你可以考驾照了')
	else :
		print('你还不能考驾照')	