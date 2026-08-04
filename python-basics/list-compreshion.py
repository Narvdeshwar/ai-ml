# list compreheshion
num=[i**2 for i in range(6)]
print(num)

# condition check
nums=[0,1,-2,3,-4,10,5,6,7,12]
ans=[0 if val<0 else val for val in nums]
print(ans)

# string cap checker
names=['ravi','vinod','suraj']
cap_names=[val.upper() for val in names]
print(cap_names)

