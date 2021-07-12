In [44]:
import pandas as pd
import numpy as np

file_path = 'multiple_choice_responses_2019.csv'
df = pd.read_csv(file_path, usecols = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5','Q10','Q15'])
header = ['Age', 'Gender', 'Country', 'Formal_Education','Position', 'Salary','Years_Coding']
df = df[1:]
df.columns = header
#df = df[(df['Country'] == 'United States of America')].dropna()
df = df[['Age', 'Gender', 'Country', 'Formal_Education', 'Position','Years_Coding','Salary']].dropna()
df.head()
Out[44]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
1	22-24	Male	France	Master’s degree	Software Engineer	1-2 years	30,000-39,999
2	40-44	Male	India	Professional degree	Software Engineer	I have never written code	5,000-7,499
4	40-44	Male	Australia	Master’s degree	Other	1-2 years	250,000-299,999
5	22-24	Male	India	Bachelor’s degree	Other	< 1 years	4,000-4,999
6	50-54	Male	France	Master’s degree	Data Scientist	20+ years	60,000-69,999
In [45]:
# Check Type
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 11422 entries, 1 to 19717
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Age               11422 non-null  object
 1   Gender            11422 non-null  object
 2   Country           11422 non-null  object
 3   Formal_Education  11422 non-null  object
 4   Position          11422 non-null  object
 5   Years_Coding      11422 non-null  object
 6   Salary            11422 non-null  object
dtypes: object(7)
memory usage: 713.9+ KB
In [46]:
# Turn Each Value to String
df['Age'] = df['Age'].astype('string')
df['Gender'] = df['Gender'].astype('string')
df['Country'] = df['Country'].astype('string')
df['Formal_Education'] = df['Formal_Education'].astype('string')
df['Position'] = df['Position'].astype('string')
df['Years_Coding'] = df['Years_Coding'].astype('string')
df['Salary'] = df['Salary'].astype('string')
In [47]:
# Check Type
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 11422 entries, 1 to 19717
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Age               11422 non-null  string
 1   Gender            11422 non-null  string
 2   Country           11422 non-null  string
 3   Formal_Education  11422 non-null  string
 4   Position          11422 non-null  string
 5   Years_Coding      11422 non-null  string
 6   Salary            11422 non-null  string
dtypes: string(7)
memory usage: 713.9 KB
In [48]:
# Strip away second set of ages
first_age = df['Age'].str[:-3]
first_age
Out[48]:
1        22
2        40
4        40
5        22
6        50
         ..
19664    25
19685    30
19691    25
19714    18
19717    50
Name: Age, Length: 11422, dtype: string
In [49]:
# Strip away first set of ages
second_age = df['Age'].str[3:]
second_age
Out[49]:
1        24
2        44
4        44
5        24
6        54
         ..
19664    29
19685    34
19691    29
19714    21
19717    54
Name: Age, Length: 11422, dtype: string
In [50]:
# Get the average age
first_age = pd.to_numeric(first_age, errors = 'coerce')
second_age = pd.to_numeric(second_age, errors = 'coerce')
avg = (first_age + second_age)/2
In [51]:
df['Age'] = avg
df.head()
Out[51]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
1	23.0	Male	France	Master’s degree	Software Engineer	1-2 years	30,000-39,999
2	42.0	Male	India	Professional degree	Software Engineer	I have never written code	5,000-7,499
4	42.0	Male	Australia	Master’s degree	Other	1-2 years	250,000-299,999
5	23.0	Male	India	Bachelor’s degree	Other	< 1 years	4,000-4,999
6	52.0	Male	France	Master’s degree	Data Scientist	20+ years	60,000-69,999
In [52]:
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 11422 entries, 1 to 19717
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Age               11360 non-null  float64
 1   Gender            11422 non-null  string 
 2   Country           11422 non-null  string 
 3   Formal_Education  11422 non-null  string 
 4   Position          11422 non-null  string 
 5   Years_Coding      11422 non-null  string 
 6   Salary            11422 non-null  string 
dtypes: float64(1), string(6)
memory usage: 713.9 KB
In [53]:
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
Out[53]:
1          30000 
2            5000
4        250000  
5            4000
6          60000 
           ...   
19664      20000 
19685        7500
19691      60000 
19714            
19717      60000 
Name: Salary, Length: 11422, dtype: object
In [54]:
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
Out[54]:
1           39999
2            7499
4          299999
5            4999
6           69999
           ...   
19664       24999
19685        9999
19691       69999
19714            
19717       69999
Name: Salary, Length: 11422, dtype: object
In [55]:
# Change low from object to float
low_sal = pd.to_numeric(low, errors = 'coerce')
low_sal
Out[55]:
1         30000.0
2          5000.0
4        250000.0
5          4000.0
6         60000.0
           ...   
19664     20000.0
19685      7500.0
19691     60000.0
19714         NaN
19717     60000.0
Name: Salary, Length: 11422, dtype: float64
In [56]:
# Change hight from object to float
high_sal = pd.to_numeric(high, errors = 'coerce')
high_sal
Out[56]:
1         39999.0
2          7499.0
4        299999.0
5          4999.0
6         69999.0
           ...   
19664     24999.0
19685      9999.0
19691     69999.0
19714         NaN
19717     69999.0
Name: Salary, Length: 11422, dtype: float64
In [57]:
# Get the average Salary 
avg = (low_sal + high_sal)/2
avg
Out[57]:
1         34999.5
2          6249.5
4        274999.5
5          4499.5
6         64999.5
           ...   
19664     22499.5
19685      8749.5
19691     64999.5
19714         NaN
19717     64999.5
Name: Salary, Length: 11422, dtype: float64
In [58]:
# Replace the column in the dataframe
df['Salary'] = avg
df.head()
Out[58]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
1	23.0	Male	France	Master’s degree	Software Engineer	1-2 years	34999.5
2	42.0	Male	India	Professional degree	Software Engineer	I have never written code	6249.5
4	42.0	Male	Australia	Master’s degree	Other	1-2 years	274999.5
5	23.0	Male	India	Bachelor’s degree	Other	< 1 years	4499.5
6	52.0	Male	France	Master’s degree	Data Scientist	20+ years	64999.5
In [59]:
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 11422 entries, 1 to 19717
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Age               11360 non-null  float64
 1   Gender            11422 non-null  string 
 2   Country           11422 non-null  string 
 3   Formal_Education  11422 non-null  string 
 4   Position          11422 non-null  string 
 5   Years_Coding      11422 non-null  string 
 6   Salary            10073 non-null  float64
dtypes: float64(2), string(5)
memory usage: 713.9 KB
In [60]:
# Remove years from Years Coding 
df['Years_Coding'] = df['Years_Coding'].str[:-6]
df.head()
Out[60]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
1	23.0	Male	France	Master’s degree	Software Engineer	1-2	34999.5
2	42.0	Male	India	Professional degree	Software Engineer	I have never writte	6249.5
4	42.0	Male	Australia	Master’s degree	Other	1-2	274999.5
5	23.0	Male	India	Bachelor’s degree	Other	< 1	4499.5
6	52.0	Male	France	Master’s degree	Data Scientist	20+	64999.5
In [61]:
# Remove hyphen
exp_space = []
for x in df['Years_Coding']:
    exp_space.append(x.replace('-',' '))
df['Years_Coding'] = exp_space    

# Remove <
exp_tick = []
for x in df['Years_Coding']:
    exp_tick.append(x.replace('<','0'))
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
Out[61]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
1	23.0	Male	France	Master’s degree	Software Engineer	1 2	34999.5
2	42.0	Male	India	Professional degree	Software Engineer	000	6249.5
4	42.0	Male	Australia	Master’s degree	Other	1 2	274999.5
5	23.0	Male	India	Bachelor’s degree	Other	0 1	4499.5
6	52.0	Male	France	Master’s degree	Data Scientist	0020	64999.5
In [62]:
# Grab the higher years
exp_max = df['Years_Coding'].str[2:]
exp_max.head()
Out[62]:
1     2
2     0
4     2
5     1
6    20
Name: Years_Coding, dtype: object
In [63]:
#Object to float
exp_max = pd.to_numeric(exp_max, errors = 'coerce')
In [64]:
# Place in the dataframe
df['Years_Coding'] = exp_max
df.head()
Out[64]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
1	23.0	Male	France	Master’s degree	Software Engineer	2	34999.5
2	42.0	Male	India	Professional degree	Software Engineer	0	6249.5
4	42.0	Male	Australia	Master’s degree	Other	2	274999.5
5	23.0	Male	India	Bachelor’s degree	Other	1	4499.5
6	52.0	Male	France	Master’s degree	Data Scientist	20	64999.5
In [65]:
df.dropna( how='any', inplace=True)
df.head()
Out[65]:
Age	Gender	Country	Formal_Education	Position	Years_Coding	Salary
1	23.0	Male	France	Master’s degree	Software Engineer	2	34999.5
2	42.0	Male	India	Professional degree	Software Engineer	0	6249.5
4	42.0	Male	Australia	Master’s degree	Other	2	274999.5
5	23.0	Male	India	Bachelor’s degree	Other	1	4499.5
6	52.0	Male	France	Master’s degree	Data Scientist	20	64999.5
In [66]:
df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 10022 entries, 1 to 19717
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Age               10022 non-null  float64
 1   Gender            10022 non-null  string 
 2   Country           10022 non-null  string 
 3   Formal_Education  10022 non-null  string 
 4   Position          10022 non-null  string 
 5   Years_Coding      10022 non-null  int64  
 6   Salary            10022 non-null  float64
dtypes: float64(2), int64(1), string(4)
memory usage: 626.4 KB
In [67]:
df.to_csv(r'Cleaned_Kaggle_2019.csv', index = False)
In [ ]:
