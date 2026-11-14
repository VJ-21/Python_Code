import os 

os.chdir('C:\\Users\\VigneshJitendra\\Downloads\\test_purpose')

for f in os.listdir():
    var =os.path.splitext(f) #splitext is the python function to split the file name and its extension
    
    sub_var= var[0].split()
    
    final_val=(f"{sub_var[2]} {sub_var[0]} {sub_var[1]}")
    # print(final_val)
    os.rename(f,final_val)
   

