text = open("Employeedata.csv", "r")
text = ' '. join([i for i in text])
text = text.replace("helpinghands.cm", "handsinhands.org")
x=open("UpdatedCsv.csv", "w")
x.writelines(text)
x.close