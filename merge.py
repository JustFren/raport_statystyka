import pandas as pd

def add_city_names(path, year="2020"):
    df = pd.read_excel(path, header=0, index_col=0)
    population = pd.read_csv('ludność\cleaned_ludnosc_wg_miast.csv', index_col=0, sep=';')
    print(population.head())
    print(df.head())

    if 'Miasto' not in df.columns:
        df.insert(0, 'Miasto', None)
    if 'Ludność' not in df.columns:
        df.insert(1, 'Ludność', None)

    # Dict with cities and the population 
    population_dict = population[year].to_dict()
    #print(population_dict)
    # loop throyhh the dataframe and finding the city name 
    suma = 0
    for idx in df.index:
        found = False
        city_name = idx  # Assuming the city name is the first word in the index
        if city_name in population_dict:
            df.at[idx, 'Miasto'] = city_name
            df.at[idx, 'Ludność'] = population_dict[city_name]
            found = True
        else: 
            city_name = city_name.split()  # Get the first word as the city name
            if city_name[0] in population_dict:
                df.at[idx, 'Miasto'] = city_name[0]
                df.at[idx, 'Ludność'] = population_dict[city_name[0]]
                found = True
            for i in range(1,len(city_name)):
                temp_name = city_name[0] + " " + city_name[i]  # Start with the first word
                if temp_name in population_dict:
                    df.at[idx, 'Miasto'] = temp_name
                    df.at[idx, 'Ludność'] = population_dict[temp_name]
                    found = True
                    break
        if not found:
            print(f"City not found: {idx}")
            suma += 1
    print(f"Number of cities not found: {suma}")
    print(df.head())
    df.to_excel(path, index=True)

add_city_names('wyniki\miasta_2019_mniej_niz_100k.xlsx', year="2019")
add_city_names('wyniki\miasta_2019_wiecej_niz_100k.xlsx', year="2019")
add_city_names('wyniki\miasta_2020_mniej_niz_100k.xlsx', year="2020")
add_city_names('wyniki\miasta_2020_wiecej_niz_100k.xlsx', year="2020")
add_city_names('wyniki\prawd_pociagow_2020.xlsx', year="2020")
add_city_names('wyniki\prawd_pociagow_2019.xlsx', year="2019")

