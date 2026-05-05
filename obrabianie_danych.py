import pandas as pd
import math
#[
# przystanek,miasto,ludność, 
# liczba pociągów opóźnionych od 6 min x12 miesiecy,
# liczba wszystkich zatrzymań pociągów x12 miesiecy,
# wielkość opóźnień (w min) dla pociągów opóźnionych od 6 min x12 miesiecy
#]

"""
Poradnik używania:
    -jak chcesz dane z 2019 to robisz najpierw coś=clean_2019(), z 2020 analogicznie
    -miesieczne funkcje daja ci wartosci względem miesiąca(tabela o długości 12)
    -roczne funkcje dają ci wartości roczne w słowniku
    --wyjątek na funkcje z "wszystkie", one dają tylko jedną wartość
"""


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
    out=out/((len(list)-1)*(standard_deviation(list)**3)+0.0001)
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

miesiace=["styczeń","luty","marzec","kwiecień","maj","czerwiec","lipiec","sierpień","wrzesień","październik","listopad","grudzień"]
    

def clear_2019():
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
    return plik_2019
def clear_2020():
    to_drop=[]
    plik_2020=pd.read_excel("./merged_2020.ods",header=0,index_col=0)
    for i in plik_2020.index:
        if str(plik_2020["Miasto"][i])=="nan":
            to_drop.append(i)
    miesiace=["styczeń","luty","marzec","kwiecień","maj","czerwiec","lipiec","sierpień","wrzesień","październik","listopad","grudzień"]
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
    return plik_2020


def podziel_miasta(plik,prog):
    data1={}
    data1["Ludność"]=[]
    data1["Miasto"]=[]
    data1["Ludność"]=[]

    data1["styczeń"]=[]
    data1["luty"]=[]
    data1["marzec"]=[]
    data1["kwiecień"]=[]
    data1["maj"]=[]
    data1["czerwiec"]=[]
    data1["lipiec"]=[]
    data1["sierpień"]=[]
    data1["wrzesień"]=[]
    data1["październik"]=[]
    data1["listopad"]=[]
    data1["grudzień"]=[]

    data1["styczeń.1"]=[]
    data1["luty.1"]=[]
    data1["marzec.1"]=[]
    data1["kwiecień.1"]=[]
    data1["maj.1"]=[]
    data1["czerwiec.1"]=[]
    data1["lipiec.1"]=[]
    data1["sierpień.1"]=[]
    data1["wrzesień.1"]=[]
    data1["październik.1"]=[]
    data1["listopad.1"]=[]
    data1["grudzień.1"]=[]

    data1["styczeń.2"]=[]
    data1["luty.2"]=[]
    data1["marzec.2"]=[]
    data1["kwiecień.2"]=[]
    data1["maj.2"]=[]
    data1["czerwiec.2"]=[]
    data1["lipiec.2"]=[]
    data1["sierpień.2"]=[]
    data1["wrzesień.2"]=[]
    data1["październik.2"]=[]
    data1["listopad.2"]=[]
    data1["grudzień.2"]=[]



    index1=[]
    data2={}
    data2["Ludność"]=[]
    data2["Miasto"]=[]
    data2["Ludność"]=[]
    data2["styczeń"]=[]
    data2["luty"]=[]
    data2["marzec"]=[]
    data2["kwiecień"]=[]
    data2["maj"]=[]
    data2["czerwiec"]=[]
    data2["lipiec"]=[]
    data2["sierpień"]=[]
    data2["wrzesień"]=[]
    data2["październik"]=[]
    data2["listopad"]=[]
    data2["grudzień"]=[]
    data2["styczeń.1"]=[]
    data2["luty.1"]=[]
    data2["marzec.1"]=[]
    data2["kwiecień.1"]=[]
    data2["maj.1"]=[]
    data2["czerwiec.1"]=[]
    data2["lipiec.1"]=[]
    data2["sierpień.1"]=[]
    data2["wrzesień.1"]=[]
    data2["październik.1"]=[]
    data2["listopad.1"]=[]
    data2["grudzień.1"]=[]
    data2["styczeń.2"]=[]
    data2["luty.2"]=[]
    data2["marzec.2"]=[]
    data2["kwiecień.2"]=[]
    data2["maj.2"]=[]
    data2["czerwiec.2"]=[]
    data2["lipiec.2"]=[]
    data2["sierpień.2"]=[]
    data2["wrzesień.2"]=[]
    data2["październik.2"]=[]
    data2["listopad.2"]=[]
    data2["grudzień.2"]=[]
    index2=[]

    for j in plik.index:
        if int(plik.loc[j,"Ludność"])>prog:
            data1["Miasto"].append(plik.loc[j,"Miasto"])
            data1["Ludność"].append(plik.loc[j,"Ludność"])

            data1["styczeń"].append(plik.loc[j,"styczeń"])
            data1["luty"].append(plik.loc[j,"luty"])
            data1["marzec"].append(plik.loc[j,"marzec"])
            data1["kwiecień"].append(plik.loc[j,"kwiecień"])
            data1["maj"].append(plik.loc[j,"maj"])
            data1["czerwiec"].append(plik.loc[j,"czerwiec"])
            data1["lipiec"].append(plik.loc[j,"lipiec"])
            data1["sierpień"].append(plik.loc[j,"sierpień"])
            data1["wrzesień"].append(plik.loc[j,"wrzesień"])
            data1["październik"].append(plik.loc[j,"październik"])
            data1["listopad"].append(plik.loc[j,"listopad"])
            data1["grudzień"].append(plik.loc[j,"grudzień"])

            data1["styczeń.1"].append(plik.loc[j,"styczeń.1"])
            data1["luty.1"].append(plik.loc[j,"luty.1"])
            data1["marzec.1"].append(plik.loc[j,"marzec.1"])
            data1["kwiecień.1"].append(plik.loc[j,"kwiecień.1"])
            data1["maj.1"].append(plik.loc[j,"maj.1"])
            data1["czerwiec.1"].append(plik.loc[j,"czerwiec.1"])
            data1["lipiec.1"].append(plik.loc[j,"lipiec.1"])
            data1["sierpień.1"].append(plik.loc[j,"sierpień.1"])
            data1["wrzesień.1"].append(plik.loc[j,"wrzesień.1"])
            data1["październik.1"].append(plik.loc[j,"październik.1"])
            data1["listopad.1"].append(plik.loc[j,"listopad.1"])
            data1["grudzień.1"].append(plik.loc[j,"grudzień.1"])

            data1["styczeń.2"].append(plik.loc[j,"styczeń.2"])
            data1["luty.2"].append(plik.loc[j,"luty.2"])
            data1["marzec.2"].append(plik.loc[j,"marzec.2"])
            data1["kwiecień.2"].append(plik.loc[j,"kwiecień.2"])
            data1["maj.2"].append(plik.loc[j,"maj.2"])
            data1["czerwiec.2"].append(plik.loc[j,"czerwiec.2"])
            data1["lipiec.2"].append(plik.loc[j,"lipiec.2"])
            data1["sierpień.2"].append(plik.loc[j,"sierpień.2"])
            data1["wrzesień.2"].append(plik.loc[j,"wrzesień.2"])
            data1["październik.2"].append(plik.loc[j,"październik.2"])
            data1["listopad.2"].append(plik.loc[j,"listopad.2"])
            data1["grudzień.2"].append(plik.loc[j,"grudzień.2"])
            index1.append(j)
        else:
            data2["Miasto"].append(plik.loc[j,"Miasto"])
            data2["Ludność"].append(plik.loc[j,"Ludność"])

            data2["styczeń"].append(plik.loc[j,"styczeń"])
            data2["luty"].append(plik.loc[j,"luty"])
            data2["marzec"].append(plik.loc[j,"marzec"])
            data2["kwiecień"].append(plik.loc[j,"kwiecień"])
            data2["maj"].append(plik.loc[j,"maj"])
            data2["czerwiec"].append(plik.loc[j,"czerwiec"])
            data2["lipiec"].append(plik.loc[j,"lipiec"])
            data2["sierpień"].append(plik.loc[j,"sierpień"])
            data2["wrzesień"].append(plik.loc[j,"wrzesień"])
            data2["październik"].append(plik.loc[j,"październik"])
            data2["listopad"].append(plik.loc[j,"listopad"])
            data2["grudzień"].append(plik.loc[j,"grudzień"])

            data2["styczeń.1"].append(plik.loc[j,"styczeń.1"])
            data2["luty.1"].append(plik.loc[j,"luty.1"])
            data2["marzec.1"].append(plik.loc[j,"marzec.1"])
            data2["kwiecień.1"].append(plik.loc[j,"kwiecień.1"])
            data2["maj.1"].append(plik.loc[j,"maj.1"])
            data2["czerwiec.1"].append(plik.loc[j,"czerwiec.1"])
            data2["lipiec.1"].append(plik.loc[j,"lipiec.1"])
            data2["sierpień.1"].append(plik.loc[j,"sierpień.1"])
            data2["wrzesień.1"].append(plik.loc[j,"wrzesień.1"])
            data2["październik.1"].append(plik.loc[j,"październik.1"])
            data2["listopad.1"].append(plik.loc[j,"listopad.1"])
            data2["grudzień.1"].append(plik.loc[j,"grudzień.1"])

            data2["styczeń.2"].append(plik.loc[j,"styczeń.2"])
            data2["luty.2"].append(plik.loc[j,"luty.2"])
            data2["marzec.2"].append(plik.loc[j,"marzec.2"])
            data2["kwiecień.2"].append(plik.loc[j,"kwiecień.2"])
            data2["maj.2"].append(plik.loc[j,"maj.2"])
            data2["czerwiec.2"].append(plik.loc[j,"czerwiec.2"])
            data2["lipiec.2"].append(plik.loc[j,"lipiec.2"])
            data2["sierpień.2"].append(plik.loc[j,"sierpień.2"])
            data2["wrzesień.2"].append(plik.loc[j,"wrzesień.2"])
            data2["październik.2"].append(plik.loc[j,"październik.2"])
            data2["listopad.2"].append(plik.loc[j,"listopad.2"])
            data2["grudzień.2"].append(plik.loc[j,"grudzień.2"])
            index2.append(j)
    df1=pd.DataFrame(data1,index=index1)
    df2=pd.DataFrame(data2,index=index2)
    return[df1,df2]



def miesieczne_prawd_na_spoz(plik):
    prawd={}
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(float(plik.loc[j,miesiace[i]])/float(plik.loc[j,miesiace[i]+".1"]+1))
        prawd[j]=temp
    return prawd

def miesieczne_ile_wszystkich_pociagow(plik):
    suma=[]
    for i in range(12):
        s=0
        for j in plik.index:
            s+=int(plik.loc[j,miesiace[i]+".1"])
        suma.append(s)
    return suma        

def rocznie_ile_wszystkich_pociagow(plik):
    suma=0
    for i in range(12):
        for j in plik.index:
            suma+=int(plik.loc[j,miesiace[i]+".1"])
    return suma

def miesieczne_ile_wszystkich_spoznionych_pociagow(plik):
    suma=[]
    for i in range(12):
        s=0
        for j in plik.index:
            s+=int(plik.loc[j,miesiace[i]])
        suma.append(s)
    return suma        

def rocznie_ile_wszystkich_spoznionych_pociagow(plik):
    suma=0
    for i in range(12):
        for j in plik.index:
            suma+=int(plik.loc[j,miesiace[i]])
    return suma        

def roczna_srednia_ile_pociagow_starter(plik):
    srednia={}
    srednia["roczna_srednia_ile_pociagow"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".1"])
        srednia["roczna_srednia_ile_pociagow"].append(int(arythm_mean(temp)))
    return srednia

def roczna_srednia_ile_pociagow(plik):
    srednia={}
    srednia["roczna_srednia_ile_pociagow"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".1"])
        srednia["roczna_srednia_ile_pociagow"].append(int(arythm_mean(temp)))
    return srednia   

def roczna_srednia_ile_spoznionych(plik):
    srednia={}
    srednia["roczna_srednia_ile_spoznionych"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]])
        srednia["roczna_srednia_ile_spoznionych"].append(int(arythm_mean(temp)))
    return srednia

def roczna_srednia_ile_spoznienia(plik):  
    srednia={}
    srednia["roczna_srednia_ile_spoznienia"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"])
        srednia["roczna_srednia_ile_spoznienia"].append(int(arythm_mean(temp)))
    return srednia

def roczna_srednia_ile_spoznienia_na_pociag(plik):  
    srednia={}
    srednia["roczna_srednia_ile_spoznienia_na_pociag"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"]/(plik.loc[j,miesiace[i]]+1))
        srednia["roczna_srednia_ile_spoznienia_na_pociag"].append(int(arythm_mean(temp)))
    return srednia

def roczna_wariancja_ile_pociagow(plik):
    srednia={}
    srednia["roczna_wariancja_ile_pociagow"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".1"])
        srednia["roczna_wariancja_ile_pociagow"].append(variance(temp))
    return srednia

def roczna_wariancja_ile_spoznionych(plik):
    srednia={}
    srednia["roczna_wariancja_ile_spoznionych"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]])
        srednia["roczna_wariancja_ile_spoznionych"].append(variance(temp))
    return srednia

def roczna_wariancja_ile_spoznienia(plik):  
    srednia={}
    srednia["roczna_wariancja_ile_spoznienia"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"])
        srednia["roczna_wariancja_ile_spoznienia"].append(variance(temp))
    return srednia

def roczna_wariancja_ile_spoznienia_na_pociag(plik):  
    srednia={}
    srednia["roczna_wariancja_ile_spoznienia_na_pociag"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"]/(plik.loc[j,miesiace[i]]+1))
        srednia["roczna_wariancja_ile_spoznienia_na_pociag"].append(variance(temp))
    return srednia

def roczna_skosnosc_ile_pociagow(plik):
    srednia={}
    srednia["roczna_skosnosc_ile_pociagow"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".1"])
        srednia["roczna_skosnosc_ile_pociagow"].append(skewness(temp))
    return srednia

def roczna_skosnosc_ile_spoznionych(plik):
    srednia={}
    srednia["roczna_skosnosc_ile_spoznionych"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]])
        srednia["roczna_skosnosc_ile_spoznionych"].append(skewness(temp))
    return srednia

def roczna_skosnosc_ile_spoznienia(plik):  
    srednia={}
    srednia["roczna_skosnosc_ile_spoznienia"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"])
        srednia["roczna_skosnosc_ile_spoznienia"].append(skewness(temp))
    return srednia

def roczna_skosnosc_ile_spoznienia_na_pociag(plik):  
    srednia={}
    srednia["roczna_skosnosc_ile_spoznienia_na_pociag"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"]/(plik.loc[j,miesiace[i]]+1))
        srednia["roczna_skosnosc_ile_spoznienia_na_pociag"].append(skewness(temp))
    return srednia

def roczna_kurtoza_ile_pociagow(plik):
    srednia={}
    srednia["roczna_kurtoza_ile_pociagow"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".1"])
        srednia["roczna_kurtoza_ile_pociagow"].append(skewness(temp))
    return srednia  

def roczna_kurtoza_ile_spoznionych(plik):
    srednia={}
    srednia["roczna_kurtoza_ile_spoznionych"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]])
        srednia["roczna_kurtoza_ile_spoznionych"].append(skewness(temp))
    return srednia

def roczna_kurtoza_ile_spoznienia(plik):  
    srednia={}
    srednia["roczna_kurtoza_ile_spoznienia"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"])
        srednia["roczna_kurtoza_ile_spoznienia"].append(skewness(temp))
    return srednia

def roczna_kurtoza_ile_spoznienia_na_pociag(plik):  
    srednia={}
    srednia["roczna_kurtoza_ile_spoznienia_na_pociag"]=[]
    for j in plik.index:
        temp=[]
        for i in range(12):
            temp.append(plik.loc[j,miesiace[i]+".2"]/(plik.loc[j,miesiace[i]]+1))
        srednia["roczna_kurtoza_ile_spoznienia_na_pociag"].append(skewness(temp))
    return srednia

def obrobka_danych(plik,path):
    out=pd.DataFrame(roczna_srednia_ile_pociagow_starter(plik),index=plik.index)
    out=out.assign(**(roczna_srednia_ile_spoznionych(plik)))
    out=out.assign(**(roczna_srednia_ile_spoznienia(plik)))
    out=out.assign(**(roczna_srednia_ile_spoznienia_na_pociag(plik)))
    
    out=out.assign(**(roczna_wariancja_ile_pociagow(plik)))
    out=out.assign(**(roczna_wariancja_ile_spoznionych(plik)))
    out=out.assign(**(roczna_wariancja_ile_spoznienia(plik)))
    out=out.assign(**(roczna_wariancja_ile_spoznienia_na_pociag(plik)))
 
    out=out.assign(**(roczna_skosnosc_ile_pociagow(plik)))
    out=out.assign(**(roczna_skosnosc_ile_spoznionych(plik)))
    out=out.assign(**(roczna_skosnosc_ile_spoznienia(plik)))
    out=out.assign(**(roczna_skosnosc_ile_spoznienia_na_pociag(plik)))
 
    out=out.assign(**(roczna_kurtoza_ile_pociagow(plik)))
    out=out.assign(**(roczna_kurtoza_ile_spoznionych(plik)))
    out=out.assign(**(roczna_kurtoza_ile_spoznienia(plik)))
    out=out.assign(**(roczna_kurtoza_ile_spoznienia_na_pociag(plik)))
    out.to_excel(path)

def rocznie_ile_pociagow_spoznionych_do_wszystkich_spoznionych(plik):
    temp1=roczna_srednia_ile_spoznionych(plik)
    out={}
    temp2=rocznie_ile_wszystkich_spoznionych_pociagow(plik)
    for i in range(len(temp1["roczna_srednia_ile_spoznionych"])):
        temp1["roczna_srednia_ile_spoznionych"][i]/=temp2
    out["rocznie_ile_pociagow_spoznionych_do_wszystkich_spoznionych"]=temp1["roczna_srednia_ile_spoznionych"]    
    return out

def rocznie_prawd_na_spoz(plik):
    prawd={}
    prawd["prawdopodobienstwo_na_spoznienie_kazda_stacja_oddzielnie"]=[]
    for j in plik.index:
        temp=0
        for i in range(12):
            temp+=(float(plik.loc[j,miesiace[i]])/float(plik.loc[j,miesiace[i]+".1"]+1))
        prawd["prawdopodobienstwo_na_spoznienie_kazda_stacja_oddzielnie"].append(temp/12)
    return prawd

def to_excel_2019():
    plik=clear_2019()
    temp=podziel_miasta(plik,100_000)
    obrobka_danych(temp[0],"./wyniki/miasta_2019_wiecej_niz_100k.xlsx")
    obrobka_danych(temp[1],"./wyniki/miasta_2019_mniej_niz_100k.xlsx")
    t=pd.DataFrame(rocznie_ile_pociagow_spoznionych_do_wszystkich_spoznionych(plik),plik.index)
    t=t.assign(**(rocznie_prawd_na_spoz(plik)))
    print(t)
    t.to_excel("./wyniki/prawdopodobienstwo_pociagow_2019.xlsx")
    t=pd.DataFrame(rocznie_ile_pociagow_spoznionych_do_wszystkich_spoznionych(temp[0]),temp[0].index)
    t=t.assign(**(rocznie_prawd_na_spoz(temp[0])))
    t.to_excel("./wyniki/prawdopodobienstwo_pociagow_2019_wiecej_100k.xlsx")
    t=pd.DataFrame(rocznie_ile_pociagow_spoznionych_do_wszystkich_spoznionych(temp[1]),temp[1].index)
    t=t.assign(**(rocznie_prawd_na_spoz(temp[1])))
    t.to_excel("./wyniki/prawdopodobienstwo_pociagow_2019_mniej_100k.xlsx")

def to_excel_2020():
    plik=clear_2020()
    temp=podziel_miasta(plik,100_000)
    obrobka_danych(temp[0],"./wyniki/miasta_2020_wiecej_niz_100k.xlsx")
    obrobka_danych(temp[1],"./wyniki/miasta_2020_mniej_niz_100k.xlsx")
    t=pd.DataFrame(rocznie_ile_pociagow_spoznionych_do_wszystkich_spoznionych(plik),plik.index)
    t=t.assign(**(rocznie_prawd_na_spoz(plik)))
    t.to_excel("./wyniki/prawdopodobienstwo_pociagow_2020.xlsx")
    t=pd.DataFrame(rocznie_ile_pociagow_spoznionych_do_wszystkich_spoznionych(temp[0]),temp[0].index)
    t=t.assign(**(rocznie_prawd_na_spoz(temp[0])))
    t.to_excel("./wyniki/prawdopodobienstwo_pociagow_2020_wiecej_100k.xlsx")
    t=pd.DataFrame(rocznie_ile_pociagow_spoznionych_do_wszystkich_spoznionych(temp[1]),temp[1].index)
    t=t.assign(**(rocznie_prawd_na_spoz[1]))
    t.to_excel("./wyniki/prawdopodobienstwo_pociagow_2020_mniej_100k.xlsx")

to_excel_2019()
#to_excel_2020()