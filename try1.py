# try1.py
#함수정의
def divide(a,b):
    return a/b
#에러처리
try:
    #함수호출
    result = divide(5,2)

except ZeroDivisionError:
    print("0으로 나누면 안됨")
except TypeError:
    print("숫자여야")
else:
    print("결과:{0}".format(result))
finally:
    print("한번도 체크(이중체크")

print("종료")