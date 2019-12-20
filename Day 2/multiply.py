num1 = '123'
num2 = '3'

lastanswer = ''
sign=0
if num1[0] == '-':
    sign=1
    num1 = num1[1:]
    if num2[0] == '-':
        sign = 0
        num2 = num2[1:]
else:
    if num2[0] == '-':
        sign = 1
        num2 = num2[1:]


for j in range (len(num2)-1,-1,-1):
    mult = 0
    answer = ''
    carry = 0
    for i in range (len(num1)-1, -1,-1):
        mult = (int(num1[i]) * int(num2[j])) + carry

        if mult // 10 != 0:
            carry = mult//10
            answer += str(mult % 10)

        else:
            answer += str(mult)
            carry = 0

    lastanswer += answer[::-1] +','
answerList = lastanswer.split(',')
arrayLength = len(answerList)
firstElement=answerList[0]
summation=int(firstElement)
for i in range(1,arrayLength):
    zeroelement=''
    for j in range(0,i):
        zeroelement +='0'
    answerList[i] +=zeroelement
    summation +=int(answerList[i])
if sign == 1 :
    summation*=-1
print(str(num1)+' * '+str(num2) +' = '+ str(summation))


