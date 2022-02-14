m=int(input("Enter the month:"))
if m in [3,4,5]:
   print("Season:Spring")
elif m in [6,7,8]:
   print("Season:Summer")
elif m in [9,10,11]:
   print("Season:Autumn")
elif m in [12,1,2]:
   print("Season:Winter")
else:
   print("Invalid month")