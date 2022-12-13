print("---dict---")
device={"이미폰":5, "아이패드":10, "윈도우":20}
print(type(device))
print(device)
#디버깅할때 중단점(Break point)
for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

#검색
print(device["아이폰"])
#입력
device["맵북"]=15
#수정
device["아이폰"]=6
device
#삭제
del device["아이폰"]
device
