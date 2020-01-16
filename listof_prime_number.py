# # to print out list from prime number where limit is given by the use
num1 = int(input("enter the lower limit: "))
num2 = int(input("enter the upper limit: "))
if num1 == 1:
    num1+=1
for prime in range(num1,num2+1):
     k =0
     for i in range(2,prime//2+1):
       if (prime%i == 0):
           k = 1
     if k == 0:
         print(prime)


# r=int(input("Enter upper limit: "))
# for a in range(2,r+1):
#     k=0
#     for i in range(2,a//2+1):
#         if(a%i==0):
#             k=k+1
#     if(k<=0):
#         print(a)