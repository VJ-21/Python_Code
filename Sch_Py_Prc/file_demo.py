with open('dummy_file.txt','r') as rf:
    with open('dummy_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)
