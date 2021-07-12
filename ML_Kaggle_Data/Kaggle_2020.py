In [16]:
import pandas as pd
import numpy as np

file_path = 'kaggle_survey_2020_responses.csv'
df = pd.read_csv(file_path, usecols = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5','Q6','Q24'])
header = ['Age', 'Gender', 'Country', 'Formal_Education','Position','Years_Coding', 'Salary']
df = df[1:]
df.columns = header
#df = df[(df['Country'] == 'United States of America')].dropna()
df = df[['Age', 'Gender', 'Country', 'Formal_Education', 'Position','Years_Coding','Salary']].dropna()
df.head()
Out[16]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
2	30-34	Man	United States of America	Master’s degree	Data Engineer	5-10 years	100,000-124,999
3	35-39	Man	Argentina	Bachelor’s degree	Software Engineer	10-20 years	15,000-19,999
4	30-34	Man	United States of America	Master’s degree	Data Scientist	5-10 years	125,000-149,999
9	35-39	Man	Germany	Doctoral degree	Data Scientist	5-10 years	70,000-79,999
12	35-39	Man	United States of America	Doctoral degree	Research Scientist	1-2 years	30,000-39,999
In [17]:
# Check Type
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 10729 entries, 2 to 20036
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Age               10729 non-null  object
 1   Gender            10729 non-null  object
 2   Country           10729 non-null  object
 3   Formal_Education  10729 non-null  object
 4   Position          10729 non-null  object
 5   Years_Coding      10729 non-null  object
 6   Salary            10729 non-null  object
dtypes: object(7)
memory usage: 670.6+ KB
In [18]:
# Turn Each Value to String
df['Age'] = df['Age'].astype('string')
df['Gender'] = df['Gender'].astype('string')
df['Country'] = df['Country'].astype('string')
df['Formal_Education'] = df['Formal_Education'].astype('string')
df['Position'] = df['Position'].astype('string')
df['Years_Coding'] = df['Years_Coding'].astype('string')
df['Salary'] = df['Salary'].astype('string')
In [19]:
# Check Type
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 10729 entries, 2 to 20036
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Age               10729 non-null  string
 1   Gender            10729 non-null  string
 2   Country           10729 non-null  string
 3   Formal_Education  10729 non-null  string
 4   Position          10729 non-null  string
 5   Years_Coding      10729 non-null  string
 6   Salary            10729 non-null  string
dtypes: string(7)
memory usage: 670.6 KB
In [20]:
# Strip away second set of ages
first_age = df['Age'].str[:-3]
first_age
Out[20]:
2        30
3        35
4        30
9        35
12       35
         ..
20025    35
20030    35
20034    30
20035    22
20036    22
Name: Age, Length: 10729, dtype: string
In [21]:
# Strip away first set of ages
second_age = df['Age'].str[3:]
second_age
Out[21]:
2        34
3        39
4        34
9        39
12       39
         ..
20025    39
20030    39
20034    34
20035    24
20036    24
Name: Age, Length: 10729, dtype: string
In [22]:
# Get the average age
first_age = pd.to_numeric(first_age, errors = 'coerce')
second_age = pd.to_numeric(second_age, errors = 'coerce')
avg = (first_age + second_age)/2
In [23]:
df['Age'] = avg
df.head()
Out[23]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
2	32.0	Man	United States of America	Master’s degree	Data Engineer	5-10 years	100,000-124,999
3	37.0	Man	Argentina	Bachelor’s degree	Software Engineer	10-20 years	15,000-19,999
4	32.0	Man	United States of America	Master’s degree	Data Scientist	5-10 years	125,000-149,999
9	37.0	Man	Germany	Doctoral degree	Data Scientist	5-10 years	70,000-79,999
12	37.0	Man	United States of America	Doctoral degree	Research Scientist	1-2 years	30,000-39,999
In [24]:
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 10729 entries, 2 to 20036
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Age               10677 non-null  float64
 1   Gender            10729 non-null  string 
 2   Country           10729 non-null  string 
 3   Formal_Education  10729 non-null  string 
 4   Position          10729 non-null  string 
 5   Years_Coding      10729 non-null  string 
 6   Salary            10729 non-null  string 
dtypes: float64(1), string(6)
memory usage: 670.6 KB
In [25]:
#Separate low from high

# Remove commas, and other characters
low_comma = []
for x in df['Salary']:
    low_comma.append(x.replace(',',''))
df['Salary'] = low_comma

# Remove $
low_char = []
for x in df['Salary']:
    low_char.append(x.replace('$',''))
df['Salary'] = low_char

# Remove >
low_tick = []
for x in df['Salary']:
    low_tick.append(x.replace('>',''))
df['Salary'] = low_tick

# Create some space 
low_space = []
for x in df['Salary']:
    low_space.append(x.replace('-', '  '))
df['Salary'] = low_space

# Grab the low side salary 
low = df['Salary'].str[:-6]
low
Out[25]:
2        100000  
3          15000 
4        125000  
9          70000 
12         30000 
           ...   
20025        2000
20030      15000 
20034            
20035            
20036            
Name: Salary, Length: 10729, dtype: object
In [26]:
# Separate high from low

# Remove commas, and other characters
high_comma = []
for x in df['Salary']:
    high_comma.append(x.replace(',',''))
df['Salary'] = high_comma

# Remove $
high_char = []
for x in df['Salary']:
    high_char.append(x.replace('$',''))
df['Salary'] = high_char

# Remove >
high_tick = []
for x in df['Salary']:
    high_tick.append(x.replace('>',''))
df['Salary'] = high_tick

# Create some space 
high_space = []
for x in df['Salary']:
    high_space.append(x.replace('-', ''))
df['Salary'] = high_space

#Grab the high side salary
high = df['Salary'].str[6:]
high
Out[26]:
2          124999
3           19999
4          149999
9           79999
12          39999
           ...   
20025        2999
20030       19999
20034            
20035            
20036            
Name: Salary, Length: 10729, dtype: object
In [27]:
# Change low from object to float
low_sal = pd.to_numeric(low, errors = 'coerce')
low_sal
Out[27]:
2        100000.0
3         15000.0
4        125000.0
9         70000.0
12        30000.0
           ...   
20025      2000.0
20030     15000.0
20034         NaN
20035         NaN
20036         NaN
Name: Salary, Length: 10729, dtype: float64
In [28]:
# Change hight from object to float
high_sal = pd.to_numeric(high, errors = 'coerce')
high_sal
Out[28]:
2        124999.0
3         19999.0
4        149999.0
9         79999.0
12        39999.0
           ...   
20025      2999.0
20030     19999.0
20034         NaN
20035         NaN
20036         NaN
Name: Salary, Length: 10729, dtype: float64
In [29]:
# Get the average Salary 
avg = (low_sal + high_sal)/2
avg
Out[29]:
2        112499.5
3         17499.5
4        137499.5
9         74999.5
12        34999.5
           ...   
20025      2499.5
20030     17499.5
20034         NaN
20035         NaN
20036         NaN
Name: Salary, Length: 10729, dtype: float64
In [30]:
# Replace the column in the dataframe
df['Salary'] = avg
df.head()
Out[30]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
2	32.0	Man	United States of America	Master’s degree	Data Engineer	5-10 years	112499.5
3	37.0	Man	Argentina	Bachelor’s degree	Software Engineer	10-20 years	17499.5
4	32.0	Man	United States of America	Master’s degree	Data Scientist	5-10 years	137499.5
9	37.0	Man	Germany	Doctoral degree	Data Scientist	5-10 years	74999.5
12	37.0	Man	United States of America	Doctoral degree	Research Scientist	1-2 years	34999.5
In [31]:
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 10729 entries, 2 to 20036
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Age               10677 non-null  float64
 1   Gender            10729 non-null  string 
 2   Country           10729 non-null  string 
 3   Formal_Education  10729 non-null  string 
 4   Position          10729 non-null  string 
 5   Years_Coding      10729 non-null  string 
 6   Salary            8551 non-null   float64
dtypes: float64(2), string(5)
memory usage: 670.6 KB
In [32]:
# Remove years from Years Coding 
df['Years_Coding'] = df['Years_Coding'].str[:-6]
df.head()
Out[32]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
2	32.0	Man	United States of America	Master’s degree	Data Engineer	5-10	112499.5
3	37.0	Man	Argentina	Bachelor’s degree	Software Engineer	10-20	17499.5
4	32.0	Man	United States of America	Master’s degree	Data Scientist	5-10	137499.5
9	37.0	Man	Germany	Doctoral degree	Data Scientist	5-10	74999.5
12	37.0	Man	United States of America	Doctoral degree	Research Scientist	1-2	34999.5
In [33]:
# Remove hyphen
exp_space = []
for x in df['Years_Coding']:
    exp_space.append(x.replace('-',' '))
df['Years_Coding'] = exp_space    

# Remove <
exp_tick = []
for x in df['Years_Coding']:
    exp_tick.append(x.replace('<',''))
df['Years_Coding'] = exp_tick

# Remove +
exp_plus = []
for x in df['Years_Coding']:
    exp_plus.append(x.replace('20+','0020'))
df['Years_Coding'] = exp_plus

# Replace (I have never writte)p with 0
exp_zero = []
for x in df['Years_Coding']:
    exp_zero.append(x.replace('I have never writte', '000'))
df['Years_Coding'] = exp_zero
df.head()
Out[33]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
2	32.0	Man	United States of America	Master’s degree	Data Engineer	5 10	112499.5
3	37.0	Man	Argentina	Bachelor’s degree	Software Engineer	10 20	17499.5
4	32.0	Man	United States of America	Master’s degree	Data Scientist	5 10	137499.5
9	37.0	Man	Germany	Doctoral degree	Data Scientist	5 10	74999.5
12	37.0	Man	United States of America	Doctoral degree	Research Scientist	1 2	34999.5
In [34]:
# Grab the higher years
exp_max = df['Years_Coding'].str[2:]
exp_max.head()
Out[34]:
2      10
3      20
4      10
9      10
12      2
Name: Years_Coding, dtype: object
In [35]:
#Object to float
exp_max = pd.to_numeric(exp_max, errors = 'coerce')
In [36]:
# Place in the dataframe
df['Years_Coding'] = exp_max
df.head()
Out[36]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
2	32.0	Man	United States of America	Master’s degree	Data Engineer	10.0	112499.5
3	37.0	Man	Argentina	Bachelor’s degree	Software Engineer	20.0	17499.5
4	32.0	Man	United States of America	Master’s degree	Data Scientist	10.0	137499.5
9	37.0	Man	Germany	Doctoral degree	Data Scientist	10.0	74999.5
12	37.0	Man	United States of America	Doctoral degree	Research Scientist	2.0	34999.5
In [37]:
df.dropna( how='any', inplace=True)
df.head()
Out[37]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
2	32.0	Man	United States of America	Master’s degree	Data Engineer	10.0	112499.5
3	37.0	Man	Argentina	Bachelor’s degree	Software Engineer	20.0	17499.5
4	32.0	Man	United States of America	Master’s degree	Data Scientist	10.0	137499.5
9	37.0	Man	Germany	Doctoral degree	Data Scientist	10.0	74999.5
12	37.0	Man	United States of America	Doctoral degree	Research Scientist	2.0	34999.5
In [38]:
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 7693 entries, 2 to 20030
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Age               7693 non-null   float64
 1   Gender            7693 non-null   string 
 2   Country           7693 non-null   string 
 3   Formal_Education  7693 non-null   string 
 4   Position          7693 non-null   string 
 5   Years_Coding      7693 non-null   float64
 6   Salary            7693 non-null   float64
dtypes: float64(3), string(4)
memory usage: 480.8 KB
In [40]:
df.to_csv(r'Cleaned_Kaggle_2020.csv', index = False)
In [ ]:
