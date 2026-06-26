#output the average percentage marks obtained by a student
input_dict={"Krishna": [67,68,69], "Arjun": [70,98,63], "Malika": [52,56,60]}
stu=input("Enter the name of the student: ")
if stu in input_dict:
    marks=input_dict[stu]
    avg=sum(marks)/len(marks)
    print("Average percentage mark: ",avg)