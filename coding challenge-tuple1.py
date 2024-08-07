def count(mytuple, n):
    count = 0
    for x in mytuple:
        if(x==n):
            count += 1
    return count

mytuple = (1,2,2,2,5)
num = int(input("Enter the number to count : "))
print(f'The count of {num} in {mytuple} : {count(mytuple,num)}')