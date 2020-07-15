

import pandas as pd
import os


data=pd.read_csv('crime_data_raw.csv')


data


#Dropping some redundant columns


data=data.drop(columns=['gini_index','share_non_white','share_white_poverty','hate_crimes_per_100k_splc'])


#checking for missing values in the dataset



data.isnull().sum()


mean=data['share_non_citizen'].mean()
data['share_non_citizen']=data['share_non_citizen'].fillna(mean)


mean2=data['avg_hatecrimes_per_100k_fbi'].mean()
data['avg_hatecrimes_per_100k_fbi']=data['avg_hatecrimes_per_100k_fbi'].fillna(mean2)


data


data.isnull().sum()


#pre processing done


mean2


mean


data.to_csv('crime_data_processed.csv')
