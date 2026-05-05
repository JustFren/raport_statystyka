import pandas as pd
import math
#[
# przystanek,miasto,ludność, 
# liczba pociągów opóźnionych od 6 min x12 miesiecy,
# liczba wszystkich zatrzymań pociągów x12 miesiecy,
# wielkość opóźnień (w min) dla pociągów opóźnionych od 6 min x12 miesiecy
#]
def arythm_mean(list):
    sum=0
    n=len(list)
    for i in range(n):
        sum+=list[i]
    return sum/n
def variance(t):
    if len(t)<2:
        raise Exception()
    sum=0
    x_dash=arythm_mean(t)
    for i in range(len(t)):
        sum+=(t[i]-x_dash)**2
    return (1/(len(t)-1))*sum    
def standard_deviation(t):
    return math.sqrt(variance(t))
def skewness(list):
    out=0
    mean=arythm_mean(list)
    for i in range(len(list)):
        out+=(list[i]-mean)**3
    out=out/((len(list)-1)*(standard_deviation**3))
    return out
def kurtosis(list):
    sum1=0
    sum2=0
    n=len(list)
    mean=arythm_mean(list)
    for i in range(n):
        sum1+=(list[i]-mean)**4
        sum2+=(list[i]-mean)**2
    return (1/n)*(sum1)/(((1/n)*sum2)**2)    



plik_2019=pd.read_excel("./merged_2019.ods",header=0,index_col=0)
to_drop=[]


for i in plik_2019.index:
    if str(plik_2019["Miasto"][i])=="nan":
        to_drop.append(i)

plik_2019.drop(to_drop,inplace=True)   
to_drop=[]

miesiace=["styczeń","luty","marzec","kwiecień","maj","czerwiec","lipiec","sierpień","wrzesień","październik","listopad","grudzień"]

for i in range(12):
    for j in plik_2019.index:
        if str(plik_2019[miesiace[i]][j])=="nan":
            plik_2019.loc[j,miesiace[i]]=0
    for j in plik_2019.index:
        if str(plik_2019[miesiace[i]+".1"][j])=="nan":
            plik_2019.loc[j,miesiace[i]+".1"]=0
    for j in plik_2019.index:
        if str(plik_2019[miesiace[i]+".2"][j])=="nan":
            plik_2019.loc[j,miesiace[i]+".2"]=0
#===========
#plik_2019 wyczyszczony z nan
#===========
plik_2020=pd.read_excel("./merged_2020.ods",header=0,index_col=0)
for i in plik_2020.index:
    if str(plik_2020["Miasto"][i])=="nan":
        to_drop.append(i)

plik_2020.drop(to_drop,inplace=True)   

for i in range(12):
    for j in plik_2020.index:
        if str(plik_2020[miesiace[i]][j])=="nan":
            plik_2020.loc[j,miesiace[i]]=0
    for j in plik_2020.index:
        if str(plik_2020[miesiace[i]+".1"][j])=="nan":
            plik_2020.loc[j,miesiace[i]+".1"]=0
    for j in plik_2020.index:
        if str(plik_2020[miesiace[i]+".2"][j])=="nan":
            plik_2020.loc[j,miesiace[i]+".2"]=0
#===========
#plik_2020 wyczyszczony z nan
#===========
data={}

def roczna_srednia_ile_pociag(plik):
    srednia={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".1"])
        srednia[j]=int(arythm_mean(temp))
    return srednia    


def roczna_srednia_ile_spoznia(plik):
    srednia={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]])
        srednia[j]=int(arythm_mean(temp))
    return srednia  

def roczna_srednia_ile_spoznienia(plik):  
    srednia={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"])
        srednia[j]=int(arythm_mean(temp))
    return srednia 

def roczna_srednia_ile_spoznienia_na_pociag(plik):  
    srednia={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"]/(plik.loc[j,miesiace[i]]+1))
        srednia[j]=int(arythm_mean(temp))
    return srednia 

def roczna_wariancja_ile_pociag(plik):
    srednia={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".1"])
        srednia[j]=variance(temp)
    return srednia

def roczna_wariancja_ile_spoznia(plik):
    srednia={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]])
        srednia[j]=variance(temp)
    return srednia  

def roczna_wariancja_ile_spoznienia(plik):  
    srednia={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"])
        srednia[j]=variance(temp)
    return srednia 

def roczna_srednia_ile_spoznienia_na_pociag(plik):  
    srednia={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"]/(plik.loc[j,miesiace[i]]+1))
        srednia[j]=variance(temp)
    return srednia 