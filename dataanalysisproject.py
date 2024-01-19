import pandas as pd

df = pd.read_csv('salaries.csv')

df.head(3) #yegeb mathalan awel 5 sofo to explore the data and understand it
print(df.head(3))
df.info()
df.describe() #betedini ma3lomat statistics
df.head()
# what is the average basepay
#khod balak ezay bafaltar fi pandas

df['TotalPay'].mean()
df['TotalPay'].max()
# df['TotalPay'].min()


# what is the job title of joseph

df[df['EmployeeName'] =="GARY JIMENEZ"]['JobTitle']
#khod balak faltart el data frame ezay hena

# how much gary jimenez make including benefits?
df[df['EmployeeName'] =="GARY JIMENEZ"]['TotalPayBenefits']


# what is the name of the highst paid person
#ba index men wara lama a3oz ageb el row

df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['EmployeeName']

# what was the average (mean) basepay of all employees per year? (2011-2014)?
#da sho5k time series analysis
df.groupby('Year').mean()
# elmohem lama ba3mel group by beb2a 3ashan 7astakhdem statitical fun



#how many uniqe jobtitle are there 

df['JobTitle'].unique() #nunique() begeebly 3adadhom


# what are the most top 5 common jobs

df['JobTitle'].value_counts() # beyehseb kol job title geh ad eh

# what are the most top 5 common jobs
df['JobTitle'].value_counts()[:5] # beyehseb kol job title geh ad eh
df['JobTitle'].value_counts().head(5) # heya heya
df['JobTitle'].value_counts().tail(5) #tegeb akher 5, .head 3aks .tail

# how many job titles were represented by only one person in 2013 ?

(df[df['Year'] == 2013]['JobTitle'].value_counts() == 1).sum()

def chief (str):
    if 'chief' in (str.lower()):
        return True
    else:
        return False
    

# how many people have the word cheif in theie job title?
df['JobTitle'].apply(lambda x: chief(x)).sum() # de mohema gedan leanha betkhaleny aaply fun ana 3amelha eb eidi

# is there a corriation between the len of the job title str and the salary ?

df['ntitles'] = df['JobTitle'].apply(len) # keda ana ba2olo sha5al fun len 3ala el column dah 
df['ntitles'] 

df[['ntitles', 'TotalPay']].corr() # corr finds the corelation between two columns el3elaka ben hagteen
# as the relation near to ZERO so there is no corelation here /





