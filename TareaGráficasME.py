import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

#Estabelcemos el data frame para la fecha
print("\nPrograma de perros con Pandas :D\n")
fronteras = pd.read_csv('frontera.csv')
fronteras["Date"] = pd.to_datetime(fronteras["Date"], format="%m/%d/%Y")
es_2019 = fronteras["Date"].dt.strftime("%Y") == "2019"
#-------------------------------------------------------------------

#Establecemos el data frame de que estamos en la frontera de Canada
es_Canada = fronteras["Border"] == "US-Canada Border"
frontCanada = fronteras[es_Canada & es_2019]
#------------------------------------------------------------------

#Creamos el data frame con ubicarnos en canada y sea el año 2019
DataFrameCanada = pd.DataFrame(frontCanada)
cols_to_subset = ["Port Name", "State", "Date", "Measure", "Value"]
filtroFinal = DataFrameCanada[cols_to_subset]
DataFrameFiltro = pd.DataFrame(filtroFinal)
#print(filtroFinal)
#--------------------------------------------------------------------

#Creamos las condiciones de PVP y PV
es_PerVehPas = fronteras["Measure"] == "Personal Vehicle Passengers"
es_PerVeh = fronteras["Measure"] == "Personal Vehicles"
#--------------------------------------------------------------------

#Creamos las condiciones de PD
es_PD = fronteras["Measure"] == "Pedestrians"


#---------------------------------------------------------------------


#Creación de la ubicación de los estados
es_ME = fronteras["State"] == "ME"



#--------------------------------------------------------------------

#Creamos el DataFrame de MEPVP, MEPV Para el ESTADO DE ME
frameDePerMEPV = fronteras[es_2019 & es_Canada & es_PerVeh & es_ME]
DataFrameMEPV = pd.DataFrame(frameDePerMEPV)
#print(frameDePerMEPV)
frameDePerMEPVP = fronteras[es_2019 & es_Canada & es_PerVehPas & es_ME]
DataFrameMEPVP = pd.DataFrame(frameDePerMEPVP)
#print(frameDePerMEPVP)






#-------------------------------------------------------------------------

#Cremos el data frame de Pedestrians
frameDeMEPD = fronteras[es_2019 & es_Canada & es_PD  & es_ME]
DataFrameMEPD = pd.DataFrame(frameDeMEPD)
#print(DataFrameMEPD)




#--------------------------------------------------------------------------


#Gráfica de lineas por estado sin detalles de puertas, que muestra el movimiento de Personal Vehicles
#xMEPV=DataFrameMEPV['Date']
#yMEPV=DataFrameMEPV['Value']
#plt.plot(xMEPV,yMEPV)
#plt.show()




#-------------------------------------------------------------------------------------------------------

#Hacer Gráfica de puntos que muestre el comportamiento de "Pedestrians". Que sea una gráfica
#por cada estado y con detalle de puertas en la horizontal
#xMEPD=frameDeMEPD['Port Name']
#yMEPD=frameDeMEPD['Value']
#plt.scatter(xMEPD,yMEPD)
#plt.show()



#--------------------------------------------------------------------------------------------------------


#Creamos  los data frames con la condición de PV y PVP Por estado
mePV= DataFrameMEPV[DataFrameMEPV['Measure']=='Personal Vehicles']
mePVP= DataFrameMEPVP[DataFrameMEPVP['Measure']=='Personal Vehicle Passengers']
dfmePV= pd.DataFrame(mePV)
dfmePVP= pd.DataFrame(mePVP)
sumaMEPV  = dfmePV.groupby('Port Name')['Value'].sum()
sumaMEPVP = dfmePVP.groupby('Port Name')['Value'].sum()
dfsumaMEPV= pd.DataFrame(sumaMEPV)
dfsumaMEPVP= pd.DataFrame(sumaMEPVP)






#print(dfsumaMEPV)
#print(dfsumaMEPVP)
#---------------------------------------------------------------------------------------


#Unimos PV y PVP POR CADA ESTADO dentro de un mismo data frame
JuntosME= pd.merge(dfsumaMEPV,dfsumaMEPVP,on='Port Name')
dfJuntosME=pd.DataFrame(JuntosME)



#print(dfJuntosME)
#-----------------------------------------------------------------------------------------


#Graficamos por estado las dos barras en una gráfica
#JuntosMEx = dfJuntosME[['Value_x','Value_y']]
#JuntosMEx.plot.bar()
#plt.show()


#-----------------------------------------------------------------------------------------


#Histograma de Buss pasengers para todos los estados

es_BP = fronteras["Measure"] == "Bus Passengers"
frameDeBP = fronteras[es_2019 & es_Canada & es_BP ]
DataFrameBP = pd.DataFrame(frameDeBP)
#print(DataFrameBP)

xBP=DataFrameBP['Value']
#yBP=DataFrameBP[]
plt.hist(xBP)
plt.show()

#DataFrameBP['Value'].plot.hist()
#plt.show()
