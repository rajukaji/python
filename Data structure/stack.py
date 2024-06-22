#stack
#LIFO last in first out

#browsers works this way too,
#  browsing differnce pages with forward and backward clicking

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
#appended in the stack

print(browsing_session)

#removing last items, 
#use pop() method

last = browsing_session.pop()
print(last)
print(browsing_session)

#print( "redirect", browsing_session[-1])
#-1 returns the last item
#when pressing the back button

#now check if empty or not
#"" [] are falsy value
if not browsing_session:
#if the browsing_session is not empty
#we'll get the item on the top of the stack
    print("disable backbutton")
    print( "redirect", browsing_session[-1])

