import csv
with open('emp.csv','r') as r:
    csv_reader=csv.DictReader(r)

    with open('new_emp_1.csv','w') as w:
        fieldnames=['employee_id','name','age','department','salary','city','joining_date']
        csv_writer=csv.DictWriter(w,fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
            # print(line)