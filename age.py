driver = input("請問你有沒開過車:")
if driver != "有" and driver != "沒有":
	print("只能輸入有或沒有")
age = input("請問你的年齡:")
age = int(age)
if driver == "有":
	if age >= 18:
		print("你通過測驗了")
	if age <= 18:
		print("奇怪 你怎麼有開過車")
elif driver == "沒有":
	if age >= 18:
		print("你可以去考駕照了")
	if age <= 18:
		print("再過幾年你就能考駕照了")
