import pandas as pd

df = pd.read_excel('2020.xlsx', header=[0,1], index_col=0)
population = pd.read_csv('ludność\cleaned_ludnosc_wg_miast.csv', index_col=0, sep=';')
print(population.head())
print(df.head())

df.insert(0, ('Dane Ogólne', 'Miasto'), None)
df.insert(1, ('Dane Ogólne', 'Ludność'), None)

# Dict with cities and the population 
population_dict = population['2020'].to_dict()
#print(population_dict)
# loop throyhh the dataframe and finding the city name 
suma = 0
for idx in df.index:
    found = False
    city_name = idx  # Assuming the city name is the first word in the index
    if city_name in population_dict:
        df.at[idx, ('Dane Ogólne', 'Miasto')] = city_name
        df.at[idx, ('Dane Ogólne', 'Ludność')] = population_dict[city_name]
        found = True
    else: 
        city_name = city_name.split()  # Get the first word as the city name
        if city_name[0] in population_dict:
            df.at[idx, ('Dane Ogólne', 'Miasto')] = city_name[0]
            df.at[idx, ('Dane Ogólne', 'Ludność')] = population_dict[city_name[0]]
            found = True
        for i in range(1,len(city_name)):
            temp_name = city_name[0] + " " + city_name[i]  # Start with the first word
            if temp_name in population_dict:
                df.at[idx, ('Dane Ogólne', 'Miasto')] = temp_name
                df.at[idx, ('Dane Ogólne', 'Ludność')] = population_dict[temp_name]
                found = True
                break
    if not found:
        print(f"City not found: {idx}")
        suma += 1
print(f"Number of cities not found: {suma}")
print(df.head())
df.to_excel('merged_2020.xlsx', index=True)