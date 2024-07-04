# hello_world= "엄마가 말했다. '밥 먹었니?'"
# print(hello_world)

# name="김진수"
# money=100
# print("안녕하세요."+name+"님, 반갑습니다.")
# print("입력하신 금액은",money,"원 입니다.")

#데이터 출력 시, %기호 사용하는 방법
name="김진수"
print("안녕하세요. 저의 이름은 %s입니다."%name)
money=10000
print("입력하신 금액은 %d원 입니다."%money)

#alt+shift+e
a=7
b=3
result=a+b
print(result)

#문자열 길이 구하기
hello_world= "엄마가 말했다. '밥 먹었니?'"
print(len(hello_world))

#문자열 슬라이싱
자유로운_문자열="왜 아직도 집에 도착하지 못한걸까."
print(len(자유로운_문자열))
자유로운_문자열[2:5]

#문자열 치환
date="2024.07.04"
print("바꾸기 전의 데이터:",date)
date=date.replace("." , "-")
print("바꾼후의 데이터:",date)

#연습문제 6
알파벳=("abcd")
알파벳=알파벳.replace("a","A")
print(알파벳)

#연습문제 5.
#1. 주어진 변수 및 데이터를 할당
문자열="Python"
new=문자열[5]+문자열[4]+문자열[3]+문자열[2]+문자열[1]+문자열[0]
print(new)

#문자열 여러 줄 출력하기
자유로운_문자열="왜 아직도 집에 도착하지 못한걸까.\n그런데 저는 더이상 지하철을 타고 싶지 않아요."
print(자유로운_문자열)

