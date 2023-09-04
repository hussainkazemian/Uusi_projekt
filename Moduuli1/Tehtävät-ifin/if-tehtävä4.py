vuosi = int(input("kirjoitta vuosi:"))
if (vuosi % 4 ==0 and vuosi % 100 != 0) or vuosi % 400 == 0:
    print("vuosi on kakausvuosi")
else:
    print(" vuosi ei ole kakausvuosi")