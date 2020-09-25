alpa = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+=-0987654321{[}]\\|"\':;<,>.?/'
out = open("out.txt", "r", encoding="utf-8").read()
check = open("check.txt", "r", encoding="utf-8").read()
passtotal = hook = ""
for en, de in zip(out, check):
	for i in alpa:
		if ((ord(i)+ord(de))%255)==ord(en):
			passtotal += i
print("Original password --> " + passtotal)
for ch in passtotal:
	hook += ch
	v = passtotal.split(hook)
	v.pop()
	if v.count("") > 1:
		print("Parsed ( correct ) password --> "+ hook)
		break
