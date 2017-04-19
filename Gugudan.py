print("## 구구단 출력 프로그램 ##")

dan   = 2
count = 1

print("%d단" %dan)
while count < 10:
    print("%d * " %dan)
    print("%d = " %count)
    print("%d" %count*dan) 
    count =count + 1
