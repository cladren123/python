#값을 넣을 때 변수타입이 결정된다.
#메모리에 들어가서 동작이 된다.
a = 10; # 10이라는 숫자가 메모리에 들어가는게 아니라 2진수로 들어간다.
b = "";

a = 100.2;
b = "abc"; #unicode 값이 들어간다. 메모리에

print(a);
print(type(a))
print(type(b))


#del(a);

a = input();
num = 0;

#중요한 예외 처리
try :
    num = int(a);
except :
    print("invalid input number.. try again");
    exit();


