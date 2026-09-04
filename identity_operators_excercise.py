a=[1,2,3]
b=a
result =b is a
print("result of b is a is : ",result)

c=[1,2,3]
d=[1,2,3]
result = c is d
print("result of c is d is : ",result)

#identity operators
j=20#is operators
result=j>10 and j<30
print("result of",j,">10 and <",j,"<30 is:",result)
g=25
result=g>30 and g<40
print("result of",g,">30 and <",g,"<40 is:",result)

#is not operator
k=25
result=not(k>30)
print("result of not(",k,">30) is:",result)
l=35
result=not(l<40)
print("result of not(",l,"<40) is:",result)