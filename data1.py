import pandas as pd
import matplotlib.pyplot as plt

airlines = pd.read_csv('C:/Users/Oscar/OneDrive/Documents/GitHub/hack23/data/airlines.csv')
country = pd.read_csv('C:/Users/Oscar/OneDrive/Documents/GitHub/hack23/data/country.csv')
covid = pd.read_csv('C:/Users/Oscar/OneDrive/Documents/GitHub/hack23/data/covid.csv')
lfd = pd.read_csv('C:/Users/Oscar/OneDrive/Documents/GitHub/hack23/data/load_factor_data.csv')
seats = pd.read_csv('C:/Users/Oscar/OneDrive/Documents/GitHub/hack23/data/seats.csv')
submission = pd.read_csv('C:/Users/Oscar/OneDrive/Documents/GitHub/hack23/data/submission.csv')
validation = pd.read_csv('C:/Users/Oscar/OneDrive/Documents/GitHub/hack23/data/validation.csv')

# print(airlines)
# print(country)
# print(covid)
# print(lfd)
# print(seats)
# print(submission)
# print(validation)

# print(airlines['airline_code_iata'].nunique())
# print(airlines['airline_type'].nunique())

# print(lfd['organization_code_iata'].nunique())

# print(submission['organization_code_iata'].nunique())


countryX = 'United Kingdom'
covidcountry = covid[covid['location'] == countryX]
# print(covidcountry)

covidcountry['stringency_index'].plot()
# plt.show()

df = pd.DataFrame()

df['airline'] = seats['operating_airline'].unique()
# print(df)

airline_list = df['airline'].tolist()
print(airline_list)

# count the number of times each color appears for rows where 'operating_airline' is '2L'
valuecountA = seats.loc[seats['operating_airline'] == '2L', 'departure_country_iata'].value_counts()
valuecountB = seats.loc[seats['operating_airline'] == '2L', 'arrival_country_iata'].value_counts()
valuecounts = valuecountA + valuecountB
# print(valuecounts)

# get the most common value
most_common_value = valuecounts.idxmax()
# print(most_common_value)


for value in airline_list:
    valuecountA = seats.loc[seats['operating_airline'] == value, 'departure_country_iata'].value_counts()
    valuecountB = seats.loc[seats['operating_airline'] == value, 'arrival_country_iata'].value_counts()
    
    valuecounts = valuecountA + valuecountB
    most_common_value = valuecounts.idxmax()
    # print(f"The most common value for {value} is {most_common_value}")

df['country'] = df['airline'].map(most_common_value)

# countryX = 'United Kingdom'
# covidcountry = covid[covid['location'] == countryX]
# # print(covidcountry)

# Now, I want to iterate through a list and calculate valuecount for each 

# covidcountry['stringency_index'].plot()