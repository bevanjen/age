driving = input('請問你有沒有開過車 :')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('合法')
    else:
        print('不合法')
elif driving == '沒有':
    if age >= 18:
        print('你可以考駕照')
    else:
        print('等到18你就可以考了')