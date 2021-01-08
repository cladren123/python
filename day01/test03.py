#100.0이 나오는 이유? 실수는 큰 범위의 숫자를 표현
#정수 * 실수, 실수가 더 큰 범위이므로 결과는 실수

a = input('input numer1..?');
b = input('input numer2..?');

result = int(a) * int(b);

print(a,b, sep="*", end ="=" + str(result));












