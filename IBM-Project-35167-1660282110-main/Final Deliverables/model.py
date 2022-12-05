import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
import pickle
hr_df=pd.read_csv('hr.csv')
#print(hr_df)
#print(hr_df.shape)
hr_df.size
#hr_df.info()
#print(hr_df['department'].unique())
hr_df['salary'].unique()
print("hi")
s_df=pd.read_excel('employee_satisfaction_evaluation.xlsx')
print(s_df)
main_df= hr_df.set_index('employee_id').join(s_df.set_index('EMPLOYEE #'))
main_df=main_df.reset_index()
r_list=[]
for index,rows in main_df.iterrows():
    my_list=rows.department
    r_list.append(my_list)
print("departments list")
set =set()
for i in range(0,len(r_list)):
    set.add(r_list[i])
set=list(set)
print(main_df)
main_df[main_df.isnull().any(axis=1)]
main_df.isnull().sum()
main_df.describe()
main_df.fillna(main_df.mean(),inplace=True)
main_df.isnull().sum()
main_df.drop(columns='employee_id',inplace=True)
y=main_df[['department','salary']]
le=LabelEncoder()
main_df['salary']=le.fit_transform(main_df['salary'])
print("hello-----------------------------------")
print(main_df)
for i in main_df.columns:
    print(i)
print("-------------")
main_df['department']=le.fit_transform(main_df['department'])
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
for i in range(0,len(set)):
    print(set[i],"  ",main_df.loc[main_df['department']==set[i]])
print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
X=main_df.drop(['left'],axis=1)
y = main_df.left
print(main_df)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=89)
scores_dict = {}
dt=DecisionTreeClassifier()
dt.fit(X_train,y_train)
prediction_dt = dt.predict(X_test)
accuracy_dt = accuracy_score(y_test,prediction_dt)*100
print('Accuracy score : ',accuracy_dt)
scores_dict['DecisionTreeClassifier'] = accuracy_dt
print(classification_report(y_test,prediction_dt))
Catagory=['Employee will stay','Employee will Leave']
#custom_dt=[[10,500,10,6,4,0,8,0.9,0]]
#print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
#print(int(dt.predict(custom_dt)))
filename="prediction_employee"
pickle.dump(dt,open(filename,'wb'))
loadedmodel=pickle.load(open(filename,'rb'))





























