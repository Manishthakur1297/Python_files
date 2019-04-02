import numpy as np;
import pandas as pd;

df = pd.read_csv(r'C:/Users/768940.CTS/Desktop/Python/employeeDetails.csv',
                 names=["Id","Name","Age","Salary", "Designation", "Department", "Project Id", "Project Name", "Manager", "City", "State"])

#print(df['Designation'])

df['Designation'] = df['Designation'].fillna("Employee")

#print(df['Designation'])

##print("--------Eldest-------------")
##
##mx_age = df[df['Age'].max()==df['Age']]
##print(mx_age)
##
##
##
##print("\n--------Youngest-------------")
##mn_age = df[df['Age'].min()==df['Age']]
##print(mn_age)
##
##
##print("\n--------2nd highest paid-------------")
##lar = list(df['Salary'].nlargest(2))
##print(lar[1])
##
##
##
##print("\n--------Cost Department Wise-------------")
##dept = pd.DataFrame(df.groupby('Department')['Salary'].sum()).reset_index()
##print(dept)
##print("\n")
##
##
##
##print("\n--------Cost Project Wise-------------")
##proj = pd.DataFrame(df.groupby('Project Name')['Salary'].sum()).reset_index()
##print(proj)
##print("\n")
##
##
##print("\n--------Employee Based on Manager-------------")
##manager = dict(list(df.groupby('Manager')))
##
##for key, value in manager.items():
##    print(key)
##    print(value)
##    print("\n")
##
##print("\n--------Employee Based on Project ID-------------")
##
##project_id = dict(list(df.groupby('Project Id')))
##
##for key, value in project_id.items():
##    print(key)
##    print(value)
##    print("\n")


print("\n--------Mean Age Department Wise-------------")
age = pd.DataFrame(df.groupby('Department')['Age'].mean()).reset_index()
print(age)
row,col = age.shape
for i in range(row):
    print("In Case of "+age.iloc[i][0]+" Department, Types of Employees are mostly : ",end=" ")
    if(age.iloc[i][1]>45):
        print("Elderly........")
    else:
        print("Younger........")
print("\n")
