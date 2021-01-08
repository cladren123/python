
print("Start");
sum = 0;
#avg = 0.0; #처음 데이터타입을 선언하는게 중요하다

a = input('input number1...?');
b = input('input number1...?');
c = input('input number1...?');

try:
    a = int(a); # = 있을 땐 오른쪽에서부터 실행된다.
    b = int(b);
    c = int(c);
except:
    print("Invalid Input Data... Try Again");
    exit();

sum = a + b + c;

print(sum);
avg = sum/3;
print(round(avg,1));
print("End");

#round 함수를 많이 쓴다. format 보다. format 출력할 때 자주 사용한다.
#원데이터를 없애면 안된다.



"""
a = input("첫번째 수 입력 : ")
b = input("두번째 수 입력 : ")
c = input("세번째 수 입력 : ")

try :
    num1 = int(a)
    num2 = int(b)
    num3 = int(c)
except :
    print("숫자를 입력하세요.")
    exit()


hap = num1 + num2 + num3
pyong = round(hap / 3,1)

print("합 :", hap, "평균 : ", pyong)
"""



