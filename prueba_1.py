# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 05:43:30 2020

@author: FPer15
"""
import csv 
#Se obtienen las rutas
rutas  =[]
export =[]
with open("synergy_logistics_database.csv") as archivo:
    lector = csv.DictReader(archivo)
    for i in lector:
        rutas.append(i["destination"])
    r=set(rutas)
print(r)

Exportaciones = [3529000000,3766779000,
16412451000,
1841219000,
1901000,
16917409000,
7321668000,
3516000000,
344000000,
13099380000,
840346000,
7508016000,
5850549000,
1147123000,
1673000,
37209015000,
13831992000,
5934191000,
4860036000,
1446000000,
6109329000,
14605152000,
8885119000]

totales  =[]

with open("synergy_logistics_database.csv","r") as archivo:
    lector = csv.DictReader(archivo)
    for linea in lector:
        totales.append(int(linea["total_value"]))
total = sum(totales)
total = total/1000
print("Total de embarques: ",total)

for ex in Exportaciones:
    ex=ex/1000
    totales.append(ex)
    print(ex,".......", "%",(100*ex)/total)

Exportaciones.sort(reverse=True)
indice = 0
for i in Exportaciones:
    indice+=1
    print(indice,i)
    
transportes=[]
with open("synergy_logistics_database.csv","r") as archivo:
    lector = csv.DictReader(archivo)
    
    for i in lector:
        transportes.append(i["transport_mode"])
    trans=set(transportes)
print(trans)

trans = list(trans)
print(trans)
ttransport=[]
with open("synergy_logistics_database.csv","r") as archivo:
    lector = csv.DictReader(archivo)
    for i in lector:
        ttransport.append(i["transport_mode"])
#print(ttransport)

top_transporte=[]


count = ttransport.count("Sea")
count1 = ttransport.count("Road")
count2 = ttransport.count("Air")
count3 = ttransport.count("Rail")
print("Uso de aire: ",count2,"\n","Uso de Tierra: ",count1,"\n","Uso de agua: ",count,"\n","Uso de vías: ",count3)
        
        

        
    
    
    