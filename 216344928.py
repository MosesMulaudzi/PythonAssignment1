
#problem 1
s = 'fullstackslp'

# printing f 
print(s[0])

#printing p
print(s[-1])

#printing stack
print(s[4:9])

#printing slp
print(s[9:])

#printing cks
print(s[7:10])

# use indexing to reverse
print(s[-1]+s[-2]+s[-3]+s[-4]+s[-5]+s[-6]+s[-7]+s[-8]+s[-9]+s[-10]+s[-11]+s[-12])
#---------------------------------------------------------------------------------------

#problem 2
l = [3,7,[5,[1,4,'helo']]]

#reassigning
l[2][1][2] = 'goodbye'

#displaying
print(l)

#---------------------------------------------------------------------------------------

#problem 3
d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
#---------------------------------------------------------------------------------------

#problem 4
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
new_set = set(mylist)
print(new_set)
#---------------------------------------------------------------------------------------

#problem 5
age = 45
name = "kyle"
print("Hello my dog's name is {} and he looks {} yeas old".format(name,age))
      





