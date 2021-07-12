In [251]:
import pandas as pd

df = pd.read_csv("multiple_choice_responses.csv", index_col=False)
df.head()
C:\Users\snkty\anaconda3\envs\PythonData\lib\site-packages\IPython\core\interactiveshell.py:3147: DtypeWarning: Columns (0,3,7,19,34,47,49,50,51,52,53,54,68,81,94,96,109,115,130,139,147,154,167,180,193,206,219,232,245) have mixed types.Specify dtype option on import or set low_memory=False.
  interactivity=interactivity, compiler=compiler, result=result)
Out[251]:
Time from Start to Finish (seconds)	Q1	Q2	Q2_OTHER_TEXT	Q3	Q4	Q5	Q5_OTHER_TEXT	Q6	Q7	...	Q34_Part_4	Q34_Part_5	Q34_Part_6	Q34_Part_7	Q34_Part_8	Q34_Part_9	Q34_Part_10	Q34_Part_11	Q34_Part_12	Q34_OTHER_TEXT
0	Duration (in seconds)	What is your age (# years)?	What is your gender? - Selected Choice	What is your gender? - Prefer to self-describe...	In which country do you currently reside?	What is the highest level of formal education ...	Select the title most similar to your current ...	Select the title most similar to your current ...	What is the size of the company where you are ...	Approximately how many individuals are respons...	...	Which of the following relational database pro...	Which of the following relational database pro...	Which of the following relational database pro...	Which of the following relational database pro...	Which of the following relational database pro...	Which of the following relational database pro...	Which of the following relational database pro...	Which of the following relational database pro...	Which of the following relational database pro...	Which of the following relational database pro...
1	510	22-24	Male	-1	France	Master’s degree	Software Engineer	-1	1000-9,999 employees	0	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	-1
2	423	40-44	Male	-1	India	Professional degree	Software Engineer	-1	> 10,000 employees	20+	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	-1
3	83	55-59	Female	-1	Germany	Professional degree	NaN	-1	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	-1
4	391	40-44	Male	-1	Australia	Master’s degree	Other	0	> 10,000 employees	20+	...	NaN	NaN	NaN	NaN	NaN	Azure SQL Database	NaN	NaN	NaN	-1
5 rows × 246 columns

In [252]:
# Way too many columns
df = df[['Q1',
         'Q2', 
         'Q3',
         'Q4', 
         'Q5', 
         'Q6',
         'Q7',
         'Q8',
         'Q9_Part_1',
         'Q9_Part_2',
         'Q9_Part_3',
         'Q9_Part_4',
         'Q9_Part_5',
         'Q9_Part_6',
         'Q9_Part_7',
         'Q9_Part_8',
         'Q10',
         'Q11',
         'Q12_Part_1',
         'Q12_Part_2',
         'Q12_Part_3',
         'Q12_Part_4',
         'Q12_Part_5',
         'Q12_Part_6',
         'Q12_Part_7',
         'Q12_Part_8',
         'Q12_Part_9',
         'Q12_Part_10',
         'Q12_Part_11',
         'Q12_Part_12',
         'Q13_Part_1',
         'Q13_Part_2',
         'Q13_Part_3',
         'Q13_Part_4',
         'Q13_Part_5',
         'Q13_Part_6',
         'Q13_Part_7',
         'Q13_Part_8',
         'Q13_Part_9',
         'Q13_Part_10',
         'Q13_Part_11',
         'Q13_Part_12',
         'Q14',
         'Q16_Part_1',
         'Q16_Part_2',
         'Q16_Part_3',
         'Q16_Part_4',
         'Q16_Part_5',
         'Q16_Part_6',
         'Q16_Part_7',
         'Q16_Part_8',
         'Q16_Part_9',
         'Q16_Part_10',
         'Q16_Part_11',
         'Q16_Part_12',
         'Q17_Part_1',
         'Q17_Part_2',
         'Q17_Part_3',
         'Q17_Part_4',
         'Q17_Part_5',
         'Q17_Part_6',
         'Q17_Part_7',
         'Q17_Part_8',
         'Q17_Part_9',
         'Q17_Part_10',
         'Q17_Part_11',
         'Q17_Part_12',
         'Q18_Part_1',
         'Q18_Part_2',
         'Q18_Part_3',
         'Q18_Part_4',
         'Q18_Part_5',
         'Q18_Part_6',
         'Q18_Part_7',
         'Q18_Part_8',
         'Q18_Part_9',
         'Q18_Part_10',
         'Q18_Part_11',
         'Q18_Part_12',
         'Q19',
         'Q20_Part_1',
         'Q20_Part_2',
         'Q20_Part_3',
         'Q20_Part_4',
         'Q20_Part_5',
         'Q20_Part_6',
         'Q20_Part_7',
         'Q20_Part_8',
         'Q20_Part_9',
         'Q20_Part_10',
         'Q20_Part_11',
         'Q20_Part_12',
         'Q23',
         'Q24_Part_1',
         'Q24_Part_2',
         'Q24_Part_3',
         'Q24_Part_4',
         'Q24_Part_5',
         'Q24_Part_6',
         'Q24_Part_7',
         'Q24_Part_8',
         'Q24_Part_9',
         'Q24_Part_10',
         'Q24_Part_11',
         'Q24_Part_12',
         'Q25_Part_1',
         'Q25_Part_2',
         'Q25_Part_3',
         'Q25_Part_4',
         'Q25_Part_5',
         'Q25_Part_6',
         'Q25_Part_7',
         'Q25_Part_8',
         'Q27_Part_1',
         'Q27_Part_2',
         'Q27_Part_3',
         'Q27_Part_4',
         'Q27_Part_5',
         'Q27_Part_6',
         'Q28_Part_1',
         'Q28_Part_2',
         'Q28_Part_3',
         'Q28_Part_4',
         'Q28_Part_5',
         'Q28_Part_6',
         'Q28_Part_7',
         'Q28_Part_8',
         'Q28_Part_9',
         'Q28_Part_10',
         'Q28_Part_11',
         'Q28_Part_12',
         'Q32_Part_1',
         'Q32_Part_2',
         'Q32_Part_3',
         'Q32_Part_4',
         'Q32_Part_5',
         'Q32_Part_6',
         'Q32_Part_7',
         'Q32_Part_8',
         'Q32_Part_9',
         'Q32_Part_10',
         'Q32_Part_11',
         'Q32_Part_12']]
In [253]:
# Rename Columns 
df.columns = ['Age',
         'Gender', 
         'Country',
         'Education', 
         'Job_Title', 
         'Company_Size',
         'Work_Load_Size',
         'Does_Compnay_Used_ML',
         'Q9_Part_1',
         'Q9_Part_2',
         'Q9_Part_3',
         'Q9_Part_4',
         'Q9_Part_5',
         'Q9_Part_6',
         'Q9_Part_7',
         'Q9_Part_8',
         'Salary',
         'Money_Spent_On_ML',
         'Q12_Part_1',
         'Q12_Part_2',
         'Q12_Part_3',
         'Q12_Part_4',
         'Q12_Part_5',
         'Q12_Part_6',
         'Q12_Part_7',
         'Q12_Part_8',
         'Q12_Part_9',
         'Q12_Part_10',
         'Q12_Part_11',
         'Q12_Part_12',
         'Q13_Part_1',
         'Q13_Part_2',
         'Q13_Part_3',
         'Q13_Part_4',
         'Q13_Part_5',
         'Q13_Part_6',
         'Q13_Part_7',
         'Q13_Part_8',
         'Q13_Part_9',
         'Q13_Part_10',
         'Q13_Part_11',
         'Q13_Part_12',
         'Primary_Analysis_Tool',
         'Q16_Part_1',
         'Q16_Part_2',
         'Q16_Part_3',
         'Q16_Part_4',
         'Q16_Part_5',
         'Q16_Part_6',
         'Q16_Part_7',
         'Q16_Part_8',
         'Q16_Part_9',
         'Q16_Part_10',
         'Q16_Part_11',
         'Q16_Part_12',
         'Q17_Part_1',
         'Q17_Part_2',
         'Q17_Part_3',
         'Q17_Part_4',
         'Q17_Part_5',
         'Q17_Part_6',
         'Q17_Part_7',
         'Q17_Part_8',
         'Q17_Part_9',
         'Q17_Part_10',
         'Q17_Part_11',
         'Q17_Part_12',
         'Q18_Part_1',
         'Q18_Part_2',
         'Q18_Part_3',
         'Q18_Part_4',
         'Q18_Part_5',
         'Q18_Part_6',
         'Q18_Part_7',
         'Q18_Part_8',
         'Q18_Part_9',
         'Q18_Part_10',
         'Q18_Part_11',
         'Q18_Part_12',
         'Programming_Language_For_First_Time_Users',
         'Q20_Part_1',
         'Q20_Part_2',
         'Q20_Part_3',
         'Q20_Part_4',
         'Q20_Part_5',
         'Q20_Part_6',
         'Q20_Part_7',
         'Q20_Part_8',
         'Q20_Part_9',
         'Q20_Part_10',
         'Q20_Part_11',
         'Q20_Part_12',
         'Years_Using_ML',
         'Q24_Part_1',
         'Q24_Part_2',
         'Q24_Part_3',
         'Q24_Part_4',
         'Q24_Part_5',
         'Q24_Part_6',
         'Q24_Part_7',
         'Q24_Part_8',
         'Q24_Part_9',
         'Q24_Part_10',
         'Q24_Part_11',
         'Q24_Part_12',
         'Q25_Part_1',
         'Q25_Part_2',
         'Q25_Part_3',
         'Q25_Part_4',
         'Q25_Part_5',
         'Q25_Part_6',
         'Q25_Part_7',
         'Q25_Part_8',
         'Q27_Part_1',
         'Q27_Part_2',
         'Q27_Part_3',
         'Q27_Part_4',
         'Q27_Part_5',
         'Q27_Part_6',
         'Q28_Part_1',
         'Q28_Part_2',
         'Q28_Part_3',
         'Q28_Part_4',
         'Q28_Part_5',
         'Q28_Part_6',
         'Q28_Part_7',
         'Q28_Part_8',
         'Q28_Part_9',
         'Q28_Part_10',
         'Q28_Part_11',
         'Q28_Part_12',
         'Q32_Part_1',
         'Q32_Part_2',
         'Q32_Part_3',
         'Q32_Part_4',
         'Q32_Part_5',
         'Q32_Part_6',
         'Q32_Part_7',
         'Q32_Part_8',
         'Q32_Part_9',
         'Q32_Part_10',
         'Q32_Part_11',
         'Q32_Part_12']

              
df
Out[253]:
Age	Gender	Country	Education	Job_Title	Company_Size	Work_Load_Size	Does_Compnay_Used_ML	Q9_Part_1	Q9_Part_2	...	Q32_Part_3	Q32_Part_4	Q32_Part_5	Q32_Part_6	Q32_Part_7	Q32_Part_8	Q32_Part_9	Q32_Part_10	Q32_Part_11	Q32_Part_12
0	What is your age (# years)?	What is your gender? - Selected Choice	In which country do you currently reside?	What is the highest level of formal education ...	Select the title most similar to your current ...	What is the size of the company where you are ...	Approximately how many individuals are respons...	Does your current employer incorporate machine...	Select any activities that make up an importan...	Select any activities that make up an importan...	...	Which of the following machine learning produc...	Which of the following machine learning produc...	Which of the following machine learning produc...	Which of the following machine learning produc...	Which of the following machine learning produc...	Which of the following machine learning produc...	Which of the following machine learning produc...	Which of the following machine learning produc...	Which of the following machine learning produc...	Which of the following machine learning produc...
1	22-24	Male	France	Master’s degree	Software Engineer	1000-9,999 employees	0	I do not know	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
2	40-44	Male	India	Professional degree	Software Engineer	> 10,000 employees	20+	We have well established ML methods (i.e., mod...	Analyze and understand data to influence produ...	Build and/or run the data infrastructure that ...	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
3	55-59	Female	Germany	Professional degree	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
4	40-44	Male	Australia	Master’s degree	Other	> 10,000 employees	20+	I do not know	NaN	NaN	...	Azure Machine Learning Studio	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
19713	50-54	Male	Japan	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
19714	18-21	Male	India	Bachelor’s degree	Other	250-999 employees	3-4	I do not know	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
19715	35-39	Male	India	Master’s degree	Student	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
19716	25-29	Male	India	Master’s degree	Statistician	50-249 employees	15-19	We recently started using ML methods (i.e., mo...	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
19717	50-54	Male	France	Bachelor’s degree	Software Engineer	> 10,000 employees	20+	We have well established ML methods (i.e., mod...	NaN	Build and/or run the data infrastructure that ...	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
19718 rows × 143 columns

In [254]:
#Combine Multiple Choice Answers in Each Column


df['Important_Role'] = df[['Q9_Part_1',
                           'Q9_Part_2',
                           'Q9_Part_3',
                           'Q9_Part_4',
                           'Q9_Part_5',
                           'Q9_Part_6',
                           'Q9_Part_7',
                           'Q9_Part_8']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)







df['Data_Science_Path'] = df[['Q13_Part_1',
                              'Q13_Part_2',
                              'Q13_Part_3',
                              'Q13_Part_4',
                              'Q13_Part_5',
                              'Q13_Part_6',
                              'Q13_Part_7',
                              'Q13_Part_8',
                              'Q13_Part_9',
                              'Q13_Part_10',
                              'Q13_Part_11',
                              'Q13_Part_12']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)



df['IDEs'] = df[['Q16_Part_1',
                 'Q16_Part_2',
                 'Q16_Part_3',
                 'Q16_Part_4',
                 'Q16_Part_5',
                 'Q16_Part_6',
                 'Q16_Part_7',
                 'Q16_Part_8',
                 'Q16_Part_9',
                 'Q16_Part_10',
                 'Q16_Part_11',
                 'Q16_Part_12']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)


df['Notebooks'] = df[['Q17_Part_1',
                      'Q17_Part_2',
                      'Q17_Part_3',
                      'Q17_Part_4',
                      'Q17_Part_5',
                      'Q17_Part_6',
                      'Q17_Part_7',
                      'Q17_Part_8',
                      'Q17_Part_9',
                      'Q17_Part_10',
                      'Q17_Part_11',
                      'Q17_Part_12']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)



df['Programmng_Languages_Used'] = df[['Q18_Part_1',
                                      'Q18_Part_2',
                                      'Q18_Part_3',
                                      'Q18_Part_4',
                                      'Q18_Part_5',
                                      'Q18_Part_6',
                                      'Q18_Part_7',
                                      'Q18_Part_8',
                                      'Q18_Part_9',
                                      'Q18_Part_10',
                                      'Q18_Part_11',
                                      'Q18_Part_12']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)


df['Data_Visualization_Tools'] = df[['Q20_Part_1',
                                     'Q20_Part_2',
                                     'Q20_Part_3',
                                     'Q20_Part_4',
                                     'Q20_Part_5',
                                     'Q20_Part_6',
                                     'Q20_Part_7',
                                     'Q20_Part_8',
                                     'Q20_Part_9',
                                     'Q20_Part_10',
                                     'Q20_Part_11',
                                     'Q20_Part_12']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)


df['ML_Alogrithms'] = df[['Q24_Part_1',
                          'Q24_Part_2',
                          'Q24_Part_3',
                          'Q24_Part_4',
                          'Q24_Part_5',
                          'Q24_Part_6',
                          'Q24_Part_7',
                          'Q24_Part_8',
                          'Q24_Part_9',
                          'Q24_Part_10',
                          'Q24_Part_11',
                          'Q24_Part_12']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)


df['ML_Tools'] = df[['Q25_Part_1',
                     'Q25_Part_2',
                     'Q25_Part_3',
                     'Q25_Part_4',
                     'Q25_Part_5',
                     'Q25_Part_6',
                     'Q25_Part_7',
                     'Q25_Part_8',]].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)


df['NLP_Language'] = df[['Q27_Part_1',
                         'Q27_Part_2',
                         'Q27_Part_3',
                         'Q27_Part_4',
                         'Q27_Part_5',
                         'Q27_Part_6',]].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)





df['ML_Frameworks'] = df[['Q28_Part_1',
                        'Q28_Part_2',
                        'Q28_Part_3',
                        'Q28_Part_4',
                        'Q28_Part_5',
                        'Q28_Part_6',
                        'Q28_Part_7',
                        'Q28_Part_8',
                        'Q28_Part_9',
                        'Q28_Part_10',
                        'Q28_Part_11',
                        'Q28_Part_12']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)



df['ML_Products'] = df[['Q32_Part_1',
                        'Q32_Part_2',
                        'Q32_Part_3',
                        'Q32_Part_4',
                        'Q32_Part_5',
                        'Q32_Part_6',
                        'Q32_Part_7',
                        'Q32_Part_8',
                        'Q32_Part_9',
                        'Q32_Part_10',
                        'Q32_Part_11',
                        'Q32_Part_12']].apply(
    lambda x: ','.join(x.astype(str).replace(['nan', 'None'], '')), axis = 1)
In [255]:
# Remove Individual Answer Columns
for col in df.columns:
    if 'Part_' in col:
        del df[col]
In [256]:
# Remove NAN Values
df = df.dropna()
In [257]:
Women_df = df[df['Gender'] == 'Female']
Women_df
Out[257]:
Age	Gender	Country	Education	Job_Title	Company_Size	Work_Load_Size	Does_Compnay_Used_ML	Salary	Money_Spent_On_ML	...	Data_Science_Path	IDEs	Notebooks	Programmng_Languages_Used	Data_Visualization_Tools	ML_Alogrithms	ML_Tools	NLP_Language	ML_Frameworks	ML_Products
8	22-24	Female	United States of America	Bachelor’s degree	Data Scientist	> 10,000 employees	20+	We recently started using ML methods (i.e., mo...	80,000-89,999	$0 (USD)	...	,,,,,,,Udemy,,University Courses (resulting in...	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	,, Microsoft Azure Notebooks ,,,,,,,AWS Notebo...	Python,,,,,,,,,,,	, Matplotlib ,,,, Plotly / Plotly Express ,,,,,,	Linear or Logistic Regression,Decision Trees o...	,,,,,,,	,,,,,	Scikit-learn , TensorFlow , Keras ,,,,,, Sp...	,,,,,,,,,,,
16	50-54	Female	United States of America	Master’s degree	Data Analyst	50-249 employees	1-2	We use ML methods for generating insights (but...	125,000-149,999	> $100,000 ($USD)	...	,Coursera,edX,,,,,Udemy,,,,Other	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	,,,,,,,,,,,	Python,R,SQL,,,,,,,,,	Ggplot / ggplot2 , Matplotlib ,,,,,, Seaborn ...	Linear or Logistic Regression,Decision Trees o...	,,,,,,,	,,,,,	Scikit-learn ,,,,,,,,,,,	,,,,,,,,,,,
21	22-24	Female	Ireland	Master’s degree	Data Analyst	1000-9,999 employees	10-14	We are exploring ML methods (and may one day p...	20,000-24,999	> $100,000 ($USD)</td> <td>...</td> <td>,,,DataCamp,,Kaggle Courses (i.e. Kaggle Learn...</td> <td>Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...</td> <td>, Google Colab ,, Google Cloud Notebook Produc...</td> <td>Python,,SQL,,,,,,,,,</td> <td>Ggplot / ggplot2 , Matplotlib ,,,,,, Seaborn ...</td> <td>Linear or Logistic Regression,Decision Trees o...</td> <td>Automated data augmentation (e.g. imgaug, albu...</td> <td>,,,,,</td> <td>Scikit-learn , TensorFlow ,, RandomForest,,...</td> <td>,,,,,,,,,,,</td> </tr> <tr> <th>29</th> <td>30-34</td> <td>Female</td> <td>Ukraine</td> <td>Doctoral degree</td> <td>Research Scientist</td> <td>1000-9,999 employees</td> <td>3-4</td> <td>No (we do not use ML methods)</td> <td>$0-999	$1-$99	...	,Coursera,,,,,,,,,,	, RStudio ,,,,,,,,,,	,,,,,, Binder / JupyterHub , IBM Watson Studio...	,R,,,,,,,,,,	Ggplot / ggplot2 ,,,,,,,,,,,	Linear or Logistic Regression,,,,,,,,,,,	,,,,,,,	,,,,,	,,,,,,,,,,,	,,,,,,,,,,,
30	25-29	Female	Pakistan	Master’s degree	Research Scientist	0-49 employees	10-14	We use ML methods for generating insights (but...	$0-999</td> <td>$0 (USD)	...	,Coursera,edX,DataCamp,,Kaggle Courses (i.e. K...	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	,,,,,,,,,,,	Python,,,,,,,,,,,	, Matplotlib ,,,,,,,,,,	,,,,,,,,,,,	,,Automated model selection (e.g. auto-sklearn...	,,,,,	Scikit-learn ,,,,,,,,,,,	,,,,,,,,,,,
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
19074	30-34	Female	China	Master’s degree	Data Scientist	50-249 employees	5-9	We recently started using ML methods (i.e., mo...	1,000-1,999	$1000-$9,999	...	Udacity,Coursera,,,,,,,,,,	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	,,,,,, Binder / JupyterHub ,,,,,	Python,,SQL,,,,,,,,,	,,,,, Plotly / Plotly Express ,,,,,,	Linear or Logistic Regression,Decision Trees o...	,Automated feature engineering/selection (e.g....	,,,,,	Scikit-learn ,,, RandomForest, Xgboost ,, Ca...	,,,,,,Google Cloud Natural Language,,,,,
19081	22-24	Female	India	Master’s degree	Data Analyst	> 10,000 employees	5-9	We recently started using ML methods (i.e., mo...	5,000-7,499	$0 (USD)</td> <td>...</td> <td>,Coursera,,,,,,,,University Courses (resulting...</td> <td>Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...</td> <td>Kaggle Notebooks (Kernels) ,,,,,,,,,,,</td> <td>Python,R,,,,,,,,,,</td> <td>, Matplotlib ,,,, Plotly / Plotly Express ,, S...</td> <td>Linear or Logistic Regression,Decision Trees o...</td> <td>,,,,,,,</td> <td>,,,,,</td> <td>Scikit-learn ,,, RandomForest,,,,,,,,</td> <td>,,,,,,,,,,,</td> </tr> <tr> <th>19124</th> <td>35-39</td> <td>Female</td> <td>Brazil</td> <td>Master’s degree</td> <td>Other</td> <td>50-249 employees</td> <td>0</td> <td>We use ML methods for generating insights (but...</td> <td>100,000-124,999</td> <td>$100-$999	...	Udacity,Coursera,,DataCamp,DataQuest,Kaggle Co...	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	Kaggle Notebooks (Kernels) ,,,,,,,,,,,	Python,,,,,,,,,,,	, Matplotlib ,,,,,, Seaborn ,,,,	Linear or Logistic Regression,Decision Trees o...	,,,,,,,	,,,,,	Scikit-learn ,,,,,,,,,,,	,,,,,,,,,,,
19465	25-29	Female	Kenya	Master’s degree	Data Analyst	> 10,000 employees	1-2	No (we do not use ML methods)	3,000-3,999	$0 (USD)	...	,,edX,,,Kaggle Courses (i.e. Kaggle Learn),,,,,,	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	Kaggle Notebooks (Kernels) ,,,,,, Binder / Ju...	Python,,SQL,,,,,,,,,	Ggplot / ggplot2 , Matplotlib ,,,,,, Seaborn ...	,,,,,,,,,,,	,,,,,,,	,,,,,	,,,,,,,,,,,	,,,,,,,,,,,
19583	22-24	Female	Other	Bachelor’s degree	Other	50-249 employees	1-2	We are exploring ML methods (and may one day p...	5,000-7,499	$100-$999	...	Udacity,Coursera,edX,,,Kaggle Courses (i.e. Ka...	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	, Google Colab ,,,,,,,,,,	Python,,,,,,,,,,,	, Matplotlib ,,,,,, Seaborn ,,,,	Linear or Logistic Regression,Decision Trees o...	,,,,Automated hyperparameter tuning (e.g. hype...	,,,,,	Scikit-learn , TensorFlow ,,,, PyTorch ,,,,,,	,,,,,,,,,,,Other
1453 rows × 24 columns

In [258]:
Men_df = df[df['Gender'] == 'Male']
Men_df
Out[258]:
Age	Gender	Country	Education	Job_Title	Company_Size	Work_Load_Size	Does_Compnay_Used_ML	Salary	Money_Spent_On_ML	...	Data_Science_Path	IDEs	Notebooks	Programmng_Languages_Used	Data_Visualization_Tools	ML_Alogrithms	ML_Tools	NLP_Language	ML_Frameworks	ML_Products
1	22-24	Male	France	Master’s degree	Software Engineer	1000-9,999 employees	0	I do not know	30,000-39,999	$0 (USD)	...	,Coursera,,DataCamp,,Kaggle Courses (i.e. Kagg...	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	,,,,,,,,,,,	Python,R,SQL,,,Java,Javascript,,,MATLAB,,	, Matplotlib ,,,,,,,,,,	Linear or Logistic Regression,,,,,,,,,,,	,,,,,,,	,,,,,	,,,,,,,,,,,	,,,,,,,,,,,
4	40-44	Male	Australia	Master’s degree	Other	> 10,000 employees	20+	I do not know	250,000-299,999	$10,000-$99,999</td> <td>...</td> <td>,Coursera,edX,DataCamp,,,,,,University Courses...</td> <td>Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...</td> <td>,, Microsoft Azure Notebooks ,,,,,,,,,</td> <td>Python,R,SQL,,,,,,Bash,,,</td> <td>Ggplot / ggplot2 , Matplotlib ,,,,,, Seaborn ...</td> <td>Linear or Logistic Regression,,,,,,Convolution...</td> <td>,,,,,Automation of full ML pipelines (e.g. Goo...</td> <td>,,,,,</td> <td>Scikit-learn , TensorFlow , Keras , RandomF...</td> <td>,,Azure Machine Learning Studio,,,,,,,,,</td> </tr> <tr> <th>5</th> <td>22-24</td> <td>Male</td> <td>India</td> <td>Bachelor’s degree</td> <td>Other</td> <td>0-49 employees</td> <td>0</td> <td>No (we do not use ML methods)</td> <td>4,000-4,999</td> <td>$0 (USD)	...	,,,,,,,,,,,Other	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	, Google Colab ,, Google Cloud Notebook Produc...	Python,,SQL,,,,,,,,,	, Matplotlib ,,,, Plotly / Plotly Express ,, S...	Linear or Logistic Regression,Decision Trees o...	,,,,,,,	,,,,,	Scikit-learn ,,, RandomForest, Xgboost ,,, L...	,,,,,,,,,,,
6	50-54	Male	France	Master’s degree	Data Scientist	0-49 employees	3-4	We have well established ML methods (i.e., mod...	60,000-69,999	$10,000-$99,999	...	,,,,,,,,,,,	, RStudio ,,,,,,,,,,Other	,,,,,,,,,,,	Python,R,,,,,,,,,,	Ggplot / ggplot2 ,,,,,,,,,,,	Linear or Logistic Regression,Decision Trees o...	,,Automated model selection (e.g. auto-sklearn...	Word embeddings/vectors (GLoVe, fastText, word...	Scikit-learn , TensorFlow , Keras , RandomF...	,,,,,,,RapidMiner,,,,
7	22-24	Male	India	Master’s degree	Data Scientist	50-249 employees	20+	We are exploring ML methods (and may one day p...	10,000-14,999	$100-$999	...	Udacity,Coursera,edX,,,Kaggle Courses (i.e. Ka...	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	Kaggle Notebooks (Kernels) , Google Colab ,,,...	Python,R,,,,,,,Bash,,,	, Matplotlib ,,,, Plotly / Plotly Express , Bo...	Linear or Logistic Regression,,,,,Dense Neural...	Automated data augmentation (e.g. imgaug, albu...	Word embeddings/vectors (GLoVe, fastText, word...	Scikit-learn , TensorFlow , Keras ,,, PyTor...	SAS,,Azure Machine Learning Studio,Google Clou...
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
19570	22-24	Male	Indonesia	Master’s degree	Research Scientist	0-49 employees	3-4	We use ML methods for generating insights (but...	$0-999</td> <td>$100-$999</td> <td>...</td> <td>Udacity,,,,,,,,,University Courses (resulting ...</td> <td>Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...</td> <td>Kaggle Notebooks (Kernels) , Google Colab ,,,...</td> <td>Python,R,,,,,Javascript,,,,,</td> <td>Ggplot / ggplot2 , Matplotlib ,, Shiny , D3.j...</td> <td>Linear or Logistic Regression,Decision Trees o...</td> <td>Automated data augmentation (e.g. imgaug, albu...</td> <td>,,,,,</td> <td>,,,,,,,,,,,</td> <td>,,,,,,,,,,,</td> </tr> <tr> <th>19604</th> <td>22-24</td> <td>Male</td> <td>Sweden</td> <td>Master’s degree</td> <td>Statistician</td> <td>1000-9,999 employees</td> <td>5-9</td> <td>No (we do not use ML methods)</td> <td>30,000-39,999</td> <td>$0 (USD)	...	,Coursera,,,,,,,,,,	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	,,,,,,,,,,,	Python,R,,,,,,,,MATLAB,,	Ggplot / ggplot2 , Matplotlib ,,,, Plotly / P...	Linear or Logistic Regression,Decision Trees o...	,,,,,,,	,,,,,	,,,,,,,,,,,	,,,,,,,,,,,
19664	25-29	Male	China	I prefer not to answer	Data Engineer	250-999 employees	5-9	We recently started using ML methods (i.e., mo...	20,000-24,999	$100-$999	...	,,,,,Kaggle Courses (i.e. Kaggle Learn),,,,,,	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	, Google Colab ,,,,,,,,,,	Python,,,,,,,,,,,	,,,,,,, Seaborn ,,,,	,,,,,Dense Neural Networks (MLPs, etc),,,Recur...	,,,,,,,	Word embeddings/vectors (GLoVe, fastText, word...	Scikit-learn , TensorFlow , Keras ,,,,,,,,,	,,,,,,,,,,,
19691	25-29	Male	Australia	Bachelor’s degree	Other	1000-9,999 employees	5-9	No (we do not use ML methods)	60,000-69,999	$10,000-$99,999	...	,Coursera,edX,,,,Fast.ai,Udemy,,,,	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	,,,,,,,,,,,	Python,,SQL,,,,,,,MATLAB,,	, Matplotlib ,,,, Plotly / Plotly Express , Bo...	Linear or Logistic Regression,Decision Trees o...	,,,,,,,	,,,,,	Scikit-learn , TensorFlow ,,,, PyTorch ,,,,,,	,,,,,,,,,,,
19717	50-54	Male	France	Bachelor’s degree	Software Engineer	> 10,000 employees	20+	We have well established ML methods (i.e., mod...	60,000-69,999	$0 (USD)	...	,Coursera,edX,,,,,Udemy,,,,	Jupyter (JupyterLab, Jupyter Notebooks, etc) ,...	,,,,,,, IBM Watson Studio ,,,,	Python,,SQL,,,Java,,,Bash,,,	, Matplotlib ,,,,,,,,,,	Linear or Logistic Regression,Decision Trees o...	,,Automated model selection (e.g. auto-sklearn...	,,,,,	Scikit-learn ,,,,,,,, Spark MLib ,,,	,,,,,,,,,,,
8936 rows × 24 columns

In [259]:
df.to_csv(r'cleaned_multiple_choice_responses2.csv')
In [ ]:
