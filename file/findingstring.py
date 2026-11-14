
def check_for_list():
    word="third"
    data=True
    line_no=1
    with open("test.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no = line_no+1
    return -1
check_for_list()

