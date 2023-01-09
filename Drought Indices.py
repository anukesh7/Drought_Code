import arcpy, os, sys, numpy as np

from arcpy import env
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
EVI = r'D:\DROUGHT_INDEX_UP_FINAL\SMCI'
##LST = r'J:\LST_2000_2017_INDIA_CROP_AREA_UP'
##VSWI=r'J:\VSWI'

arcpy.env.pyramid = "NONE"
arcpy.env.overwriteOutput=True
arcpy.env.workspace=EVI
rasters=arcpy.ListRasters()
arcpy.env.scratchWorkspace = r'D:\HDF'
OUT = r'D:\DROUGHT_INDEX_UP\VCI'
out1=r'D:\DROUGHT_INDEX_UP\TCI'
out2=r'D:\DROUGHT_INDEX_UP\VHI'
out3=r'D:\DROUGHT_INDEX_UP\NVSWI'
out4=r'D:\DROUGHT_INDEX_UP\MTCI'
out5=r'L:\DROUGHT_INDEX_STATE_WISE\MTCI_VCI'
out6 = r'L:\DROUGHT_INDEX_STATE_WISE\SMCI'
##
##out8=r'D:\DROUGHT_INDEX_UP_FINAL\VCI'
##out7=r'D:\DROUGHT_INDEX_UP_FINAL\MTCI'

out9=r'L:\DROUGHT_INDEX_STATE_WISE\SMADI'
out10=r'L:\DROUGHT_INDEX_STATE_WISE\SMCI'

EVI_MAX=Raster(r'D:\EVIM_EVIMX_LSTm_LSTMX_FINAL\MAX_EVI_2000_2017.tif')
EVI_MAX=SetNull(EVI_MAX,EVI_MAX,"Value = 0")
EVI_MIN=Raster(r'D:\EVIM_EVIMX_LSTm_LSTMX_FINAL\MIN_EVI_2000_2017.tif')
EVI_MIN=SetNull(EVI_MIN,EVI_MIN,"Value = 0")
LST_MAX=Raster(r'D:\EVIM_EVIMX_LSTm_LSTMX_FINAL\MAX_LST_2000_2017.tif')
LST_MAX=SetNull(LST_MAX,LST_MAX,"Value = 0")
LST_MIN=Raster(r'D:\EVIM_EVIMX_LSTm_LSTMX_FINAL\MIN_LST_2000_2017.tif')
LST_MIN=SetNull(LST_MIN,LST_MIN,"Value = 0")
VSWI_MAX=Raster(r'D:\EVIM_EVIMX_LSTm_LSTMX_FINAL\MAX_VSWI_2000_2017.tif')
VSWI_MAX=SetNull(VSWI_MAX,VSWI_MAX,"Value = 0")
VSWI_MIN=Raster(r'D:\EVIM_EVIMX_LSTm_LSTMX_FINAL\MIN_VSWI_2000_2017.tif')
VSWI_MIN=SetNull(VSWI_MIN,VSWI_MIN,"Value = 0")

SSM_MAX=Raster(r'E:\GLEAM\FINAL_MAX_MIN_GLEAM_SOIL_250M\MAX_SOIL_2000_2017_STACK.tif')
SSM_MAX=SetNull(SSM_MAX,SSM_MAX,"Value = 0")
SSM_MIN=Raster(r'E:\GLEAM\FINAL_MAX_MIN_GLEAM_SOIL_250M\MIN_SOIL_2000_2017_STACK.tif')
SSM_MIN=SetNull(SSM_MIN,SSM_MIN,"Value = 0")


for i in np.arange(0,np.size(rasters)):
    EVI_R=(os.path.join(EVI,rasters[i]))
    EVI_R=Raster(EVI_R)
    EVI_R=SetNull(EVI_R,EVI_R,"Value = 0")
    ##VCI
    VCI=((Minus(EVI_R,EVI_MIN))/(Minus(EVI_MAX,EVI_MIN)))*100
    vci_nme=os.path.join(OUT,('VCI'+rasters[i][3:len(rasters[i])]))
    VCI.save(os.path.join(OUT,('VCI'+rasters[i][3:len(rasters[i])])))
for i in np.arange(0,np.size(rasters)):
    LST_R=Raster(os.path.join(LST,('LST'+rasters[i][3:len(rasters[i])])))
    ##TCI    
    TCI=((Minus(LST_MAX,LST_R))/(Minus(LST_MAX,LST_MIN)))*100
    tci_nme=os.path.join(out1,('TCI'+rasters[i][3:len(rasters[i])]))
    TCI.save(os.path.join(out1,('TCI'+rasters[i][3:len(rasters[i])])))
    ##VHI
for i in np.arange(0,np.size(rasters)):
    vci_nme=os.path.join(OUT,('VCI'+rasters[i][3:len(rasters[i])]))
    tci_nme=os.path.join(out1,('TCI'+rasters[i][3:len(rasters[i])]))
    VHI=(Plus((Raster(vci_nme)),(Raster(tci_nme))))*0.5
    VHI.save(os.path.join(out2,('VHI'+rasters[i][3:len(rasters[i])])))
    ##NVSWI
for i in np.arange(0,np.size(rasters)):
    VSWI_R=Raster(os.path.join(VSWI,('VSWI'+rasters[i][3:len(rasters[i])])))
    NVSWI=((Minus(VSWI_R,VSWI_MIN))/(Minus(VSWI_MAX,VSWI_MIN)))*100
    NVSWI.save(os.path.join(out3,('NVSWI'+rasters[i][3:len(rasters[i])])))

for i in np.arange(0,np.size(rasters)):
    LST_R=Raster(os.path.join(LST,('LST'+rasters[i][3:len(rasters[i])])))
    ##MTCI    
    TCI=((Minus(LST_R,LST_MIN))/(Minus(LST_MAX,LST_MIN)))*100
    tci_nme=os.path.join(out4,('MTCI'+rasters[i][3:len(rasters[i])]))
    TCI.save(os.path.join(out4,('MTCI'+rasters[i][3:len(rasters[i])])))
######## MTCI/VCI    
for i in np.arange(0,np.size(rasters)):
    j=i+1
    if j<np.size(rasters):
        MTCI=Raster(os.path.join(out7,('MTCI'+rasters[i][3:len(rasters[i])])))
        VCI=Raster(os.path.join(out8,('VCI'+rasters[j][3:len(rasters[j])])))
##        print ('MTCI'+rasters[i][3:len(rasters[i])]),('VCI'+rasters[j][3:len(rasters[j])])
        MTCI_VCI=MTCI/VCI
        MTCI_VCI.save(os.path.join(out5,('MTCI_VCI'+rasters[i][3:len(rasters[i])])))

############SMCI
for i in np.arange(0,np.size(rasters)):
    SSM_R=Raster(os.path.join(EVI,rasters[i]))
    ##MTCI    
    SMCI=((Minus(SSM_MAX,SSM_R))/(Minus(SSM_MAX,SSM_MIN)))*100
    SMCI.save(os.path.join(out6,rasters[i]))


###############SMADI
for i in np.arange(7,np.size(rasters)):
    SSM_R=Raster(os.path.join(out10,rasters[i]))    
    path_MTCI_VCI=os.path.join(out5,'MTCI_VCI'+rasters[i][4:len(rasters[i])])
    ##MTCI
    if os.path.exists(path_MTCI_VCI):
        MTCI_VCI=Raster(os.path.join(out5,'MTCI_VCI'+rasters[i][4:len(rasters[i])]))
        SMADI=(SSM_R/100)*MTCI_VCI
        SMADI.save(os.path.join(out9,'SMADI'+rasters[i][4:len(rasters[i])]))







    
