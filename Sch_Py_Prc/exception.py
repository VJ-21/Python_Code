try:
    f=open('playing_csv.py','r')
except Exception as e:
    print(e)
else:
    f.close() 
    # executed close here 
finally:
    print("Finally understood the exception handling a bit ")
