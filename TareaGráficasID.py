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
es_ID = fronteras["State"] == "ID"



#--------------------------------------------------------------------

#Creamos el DataFrame de IDPVP, IDPV Para el ESTADO DE ID
frameDePerIDPV = fronteras[es_2019 & es_Canada & es_PerVeh & es_ID]
DataFrameIDPV = pd.DataFrame(frameDePerIDPV)
#print(frameDePerIDPV)
frameDePerIDPVP = fronteras[es_2019 & es_Canada & es_PerVehPas & es_ID]
DataFrameIDPVP = pd.DataFrame(frameDePerIDPVP)
#print(frameDePerIDPVP)






#-------------------------------------------------------------------------

#Cremos el data frame de Pedestrians
frameDeIDPD = fronteras[es_2019 & es_Canada & es_PD  & es_ID]
DataFrameIDPD = pd.DataFrame(frameDeIDPD)
#print(DataFrameIDPD)




#--------------------------------------------------------------------------


#Gráfica de lineas por estado sin detalles de puertas, que muestra el movimiento de Personal Vehicles
#xIDPV=DataFrameIDPV['Date']
#yIDPV=DataFrameIDPV['Value']
#plt.plot(xIDPV,yIDPV)
#plt.show()




#-------------------------------------------------------------------------------------------------------

#Hacer Gráfica de puntos que muestre el comportamiento de "Pedestrians". Que sea una gráfica
#por cada estado y con detalle de puertas en la horizontal
#xIDPD=frameDePerIDPD['Port Name']
#yIDPD=frameDePerIDPD['Value']
#plt.scatter(xIDPD,yIDPD)
#plt.show()



#--------------------------------------------------------------------------------------------------------


#Creamos  los data frames con la condición de PV y PVP Por estado
idPV= DataFrameIDPV[DataFrameIDPV['Measure']=='Personal Vehicles']
idPVP= DataFrameIDPVP[DataFrameIDPVP['Measure']=='Personal Vehicle Passengers']
dfidPV= pd.DataFrame(idPV)
dfidPVP= pd.DataFrame(idPVP)
sumaIDPV  = dfidPV.groupby('Port Name')['Value'].sum()
sumaIDPVP = dfidPVP.groupby('Port Name')['Value'].sum()
dfsumaIDPV= pd.DataFrame(sumaIDPV)
dfsumaIDPVP= pd.DataFrame(sumaIDPVP)






#print(dfsumaIDPV)
#print(dfsumaIDPVP)
#---------------------------------------------------------------------------------------


#Unimos PV y PVP POR CADA ESTADO dentro de un mismo data frame
JuntosID= pd.merge(dfsumaIDPV,dfsumaIDPVP,on='Port Name')
dfJuntosID=pd.DataFrame(JuntosID)



#print(dfJuntosID)
#-----------------------------------------------------------------------------------------


#Graficamos por estado las dos barras en una gráfica
#JuntosIDx = dfJuntosID[['Value_x','Value_y']]
#JuntosIDx.plot.bar()
#plt.show()


#-----------------------------------------------------------------------------------------


#Histograma de Buss pasengers para todos los estados

es_BP = fronteras["Measure"] == "Bus Passengers"
frameDeBP = fronteras[es_2019 & es_Canada & es_BP ]
DataFrameBP = pd.DataFrame(frameDeBP)
#print(DataFrameBP)

#xBP=DataFrameBP['Value']
#yBP=DataFrameBP[]
#plt.hist(xBP)
#plt.show()

#DataFrameBP['Value'].plot.hist()
#plt.show()
