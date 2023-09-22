marks = [90, 45, 64, 9, 17, 29]
result = []
for mark in marks:
    if mark >=71:
        print("A입니다")
        result.append("A")
    elif mark >=41:
        print("B입니다")
        result.append("B")
    elif mark >=11:
        print("C입니다")
        result.append("C")
    elif mark <=10:
        print("D입니다")
        result.append("D")
print(result)