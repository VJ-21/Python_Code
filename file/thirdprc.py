with open("third_prc.txt","r") as f7:
   data= f7.read()

rep_data=data.replace("this","that")
print(rep_data)

with open("third_prc.txt","w") as f7:
    f7.write(rep_data)