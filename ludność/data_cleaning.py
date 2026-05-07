import pandas as pd

data = pd.read_csv('ludnosc_wg_miast.csv', delimiter=';')
# delating the () and the text inside
data['nazwa'] = data['nazwa'].str.replace(r'\s*\([^)]*\)\s*$', '', regex=True)

data.rename(columns={'20192': '2019_2', '20203': '2020_2'}, inplace=True)

# changing data types into numeric (number of people)
data['2019'] = data['2019'].str.replace(r'\s+', '', regex=True)
data['2020'] = data['2020'].str.replace(r'\s+', '', regex=True)
data['2019_2'] = data['2019_2'].str.replace(r'\s+', '', regex=True)
data['2020_2'] = data['2020_2'].str.replace(r'\s+', '', regex=True)
data['2019'] = pd.to_numeric(data['2019'], errors='coerce')
data['2020'] = pd.to_numeric(data['2020'], errors='coerce')
data['2019_2'] = pd.to_numeric(data['2019_2'], errors='coerce')
data['2020_2'] = pd.to_numeric(data['2020_2'], errors='coerce')

# method used to clean that particular dataset (bolesławiec(1), bolesławiec(2) -> bolesławiec) and sum the values of the same cities together
cols_to_sum = ['2019', '2020', '2019_2', '2020_2']
data = data.groupby("nazwa", sort=False)[cols_to_sum].sum().reset_index()
print(data.head(30))

# we are not interested in powiat and wojewodztwo level data
mask_powiat = data['nazwa'].str.contains('powiat', case=False, na=False)
mask_wojewodztwo = data['nazwa'].str.isupper()
data = data[~(mask_powiat | mask_wojewodztwo)]
data["nazwa"] = data["nazwa"].str.strip()
# we exclude the distinction between miasto and obszar wiejski
mask_only_dist = data['nazwa'].str.contains(' - miasto| - obszar wiejski', case=False, na=False)  # Keep only the first word of the city name
data = data[~mask_only_dist]
print(data.head(30))

duplicates = data['nazwa'].duplicated().any()
print(f"Czy są duplikaty? {duplicates}")

data.loc[data['2019'] == 0, '2019'] = data['2019_2']
data.loc[data['2020'] == 0, '2020'] = data['2020_2']
# we want to have all population data in one column
print((data['2019'] == 0).any())
print((data['2020'] == 0).any())
print(data[data["nazwa"]=="Legnica"])

data.drop(columns=['2019_2', '2020_2'], inplace=True)
data.to_csv('cleaned_ludnosc_wg_miast.csv', index=False, encoding='utf-8-sig')
data.at["M.st.Warszawa od 2002", 'nazwa'] = "Warszawa"
print(data.head(30))
print(data[data["nazwa"]=="Warszawa"])

print()