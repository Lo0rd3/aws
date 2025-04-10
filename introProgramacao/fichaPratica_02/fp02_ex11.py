#ask user to input a number
num=int(input("Input a number:"))

#define ranges
r0025=0
r2650=0
r5175=0
r76100=0
#function to see in which range the num falls into
while num >=0:
    if num >=0 and num<=25:
        r0025+=1
        num=int(input("Input a number:"))
        if num<0:
            break
    elif num>=26 and num<=50:
        r2650+=1
        num=int(input("Input a number:"))
        if num<0:
            break
    elif num>=51 and num<=75:
        r5175+=1
        num=int(input("Input a number:"))
        if num<0:
            break
    elif num>=76 and num<=100:
        r76100+=1
        num=int(input("Input a number:"))
        if num<0:
            break
print(f">[00<->25]: {r0025}\n>[26<->50]: {r2650}\n>[51<->75]: {r5175}\n>[75<>100]: {r76100}")
