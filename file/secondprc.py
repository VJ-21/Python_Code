with open("second prc","r") as f3:
    var=f3.read()

    f5=var.replace("danger","king")
    print(f5)

with open("second prc","w") as f3:
    f3.write(f5)