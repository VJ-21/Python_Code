""" OS_module used to navigate operating system"""
import os

# os.chdir('/users/dummypath') chdir used to change directory 


# delete the folder 
os.rmdir("very_new") # used to delete top level directory
os.removedirs("OS-Demo-2/sub-level")# will delete top level directory plus inside folders as well

print(os.listdir())# prints the list of directories present in the current path  



