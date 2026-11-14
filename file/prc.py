with open("test.txt","r") as f:
    data=f.read()

updated_data=data.replace("second","fifth")
print(updated_data)

with open("test.txt","w") as f:
    f.write(updated_data)

