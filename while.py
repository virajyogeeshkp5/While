# python while loop
#1
is_failed = True
i=1
while is_failed and i<=100:
    print(f"try{i}")
    i=i+1

print("try")

# 2
is_failed = True
i=1
while is_failed:
    print(f"try{i}")
    i=i+1
    if i<100:
        break

print("give up")

#3
is_failed = True
i=1
while is_failed:
    if i%2!=0:
        i=i+1
        continue
    print(f"attempt{i}")
    i=i+1
    if i>100:
        break

print("I give up")

i=0
while i<=10:
    x=0
    while x<i:
        print("chandan")
        x+=1
    i+=1 
print("get up")        