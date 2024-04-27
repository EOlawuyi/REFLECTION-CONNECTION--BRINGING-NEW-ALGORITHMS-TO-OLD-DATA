from PIL import Image as im
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys
import numpy as np
import imageio.v3 as iio
import ipympl
import matplotlib.pyplot as plt
import skimage as ski
import skimage.feature
import pandas as pd
import scipy.stats as stats
from scipy.stats import entropy
from skimage import feature, measure
from skimage.measure import label, regionprops, regionprops_table
import pyarrow.parquet as pa
import string
from openpyxl import load_workbook
from openpyxl import Workbook
import openpyxl
import csv
import cv2
import json

#This is the code that belongs to Olorogun Engineer Enoch O. Ejofodomi in his Collaboration with Shell Onward.
#This code also belongs to Engineer Francis Olawuyi in his collaboration with Shell Onward.
#The code also belongs to the following people
#1. Esther Olawuyi
#2. Michael Olawuyi.
#3. Joshua Olawuyi
#4. Joseph Olawuyi
#5. Onome Ejofodomi
#6. Efejera Ejofodomi
#7. Deborah Olawuyi
#8. Isi Omiyi
#9. Kome Odu
#10. Sunday Damilola Olawuyi
#11. Godswill Ofualagba
#12. Matthew Olawuyi
#13. Jason Zara
#14. Vesna Zderic
#15. Ahmed Jendoubi
#16. Mohammed Chouikha
#17. Shani Ross
#18. Nicholas Monyenye
#19. Ochamuke Ejofodomi
#20. 
# MARCH 3, 2024.

mainwindow = tk.Tk()
mainwindow.geometry("1400x700")

            
#Load 362 Images
Imagefile = ["acsqx.png", "aczgx.png", "adgvs.png", "afbaz.png",
             "ahwgp.png", "aiwyk.png", "ajaeu.png", "alfit.png",
             "amkyl.png", "amndm.png", "amtqn.png", "aoord.png",
             "aoyfq.png", "asbph.png" ,"axbvm.png", "axkpq.png",
             "axlnb.png", "ayhzq.png", "aynif.png", "bacnt.png",
             "bbhlb.png", "befgl.png", "bftqz.png", "bfxqg.png",
             "bltzi.png", "bnekx.png", "bobqs.png", "bqtqq.png",
             "bwbxa.png", "bztqu.png", "cdrfy.png", "ceauj.png",
             "cgbsp.png", "chzzg.png", "ckhfg.png", "ckhfg.png",
             "clezu.png", "csart.png", "csfya.png", "cspaf.png",
             "cwkhh.png", "cxpbs.png", "cypbk.png", "cyvmv.png",
             "daevy.png", "dargb.png", "dbqkm.png", "dbtew.png",
             "dclnx.png", "dczms.png", "dfgwi.png", "dfquc.png",
             "dhlga.png", "dhzch.png", "dihoj.png", "dilfz.png",
             "ditcx.png", "dngdx.png", "dpvji.png", "dqusm.png",
             "druas.png", "dsdyo.png", "duuce.png", "dyfjv.png",
             "dzywf.png", "dzzss.png", "ebmly.png", "egfzl.png",
             "egwmu.png", "eikpr.png", "eiokv.png", "elhve.png",
             "emfvp.png", "emmli.png", "epjdp.png", "epmbn.png",
             "eprmh.png", "evfkm.png", "fatax.png", "fbipc.png",
             "fdmjk.png", "fhlth.png", "fjqis.png", "fpnhq.png",
             "fpnhq(1).png","frebw.png","ftgsk.png","fuywp.png",
             "fyfsj.png", "gdddd.png", "gdnxh.png", "gdqra.png",
             "gdubx.png", "gfeks.png", "ghdbs.png", "ghdbs.png",
             "ghsxi.png", "ghxop.png", "gjzbf.png", "gkdcz.png",
             "glryw.png", "gofcl.png", "gqjcs.png", "gruig.png",
             "gvyio.png", "gxxrp.png", "gymtn.png", "heluk.png",
             "hgwhe.png", "hhche.png", "hhjig.png", "hkkxj.png",
             "hltcq.png", "hmufa.png", "hnzkw.png", "hpzpi.png",
             "hsbqt.png", "hsdoe.png", "hwdxe.png", "hwjrn.png",
             "hxtrd.png", "hxumt.png", "hylpl.png", "hzpml.png",
             "hzsdg.png", "iboti.png", "icbgc.png", "idedg.png",
             "ifikv.png", "igcvk.png", "igmvu.png", "ihwbl.png",
             "ilzgg.png", "iozhn.png", "irnzi.png", "itfgi.png",
             "ivybj.png", "iwuia.png", "jfqdk.png", "jfqqr.png",
             "jhkxm.png", "jicdt.png", "jijvv.png", "jkixj.png",
             "jmfyt.png", "jmjbr.png", "jqoel.png", "jropv.png",
             "jvobj.png", "jxcxs.png", "jxcxs.png", "jxgym.png",
             "jyfzu.png", "jzbjj.png", "kajhl.png", "kajrz.png",
             "kcrci.png", "kdasb.png", "kfrfd.png", "khpie.png",
             "kifsj.png", "kjrlw.png", "kkbul.png", "klluc.png",
             "kporq.png", "kqmdc.png", "krxde.png", "ksznk.png",
             "kzeyp.png", "kzpqe.png", "kzuuj.png", "lbqnl.png",
             "lftpk.png", "lftpk.png", "lhvce.png", "likzy.png",
             "llavy.png", "lldcs.png", "lljfv.png", "lmqor.png",
             "lmqor.png", "lmqor.png", "lmrqi.png", "loomz.png",
             "lsqfx.png", "lvxts.png", "lwfvv.png", "lwlvx.png",
             "lwswb.png", "mibki.png", "mjhgp.png", "mlgjg.png",
             "msjfv.png", "msumu.png", "muodd.png", "mvqck.png",
             "mxcyl.png", "myaoo.png", "myhpk.png", "myoac.png",
             "mzegh.png", "nglks.png", "niyos.png", "nlggw.png",
             "nnjhu.png", "nokyy.png", "nruwf.png", "ntama.png",
             "nvomd.png", "nwgfk.png", "nwgwo.png", "nzhkt.png",
             "oaibj.png", "obdyy.png", "odirc.png", "odlgb.png",
             "oetim.png", "oewlp.png", "oexuy.png", "ofusu.png",
             "ofycm.png", "ohbxb.png", "oiohf.png", "oizmu.png",
             "ojztv.png", "olivu.png", "onoca(1).png", "ooaav.png",
             "ouakr.png", "ouivw.png", "oxahm.png", "ozkrh.png",
             "pdhgb.png", "pdigu.png", "peath.png", "piwyi.png",
             "pmtfj.png", "povvx.png", "ppcwe.png", "prkww.png",
             "prnfq.png", "prpzr.png", "prqau.png", "pshmt.png",
             "puwde.png", "pvjpb.png", "pvmcz.png", "pvydw.png",
             "pvygv.png", "pyxfz.png", "qamjq.png", "qawor.png",
             "qgaqz.png", "qjgjj.png", "qmbzv.png", "qmufw.png.",
             "qqnzu.png", "qtivt.png", "qzgnv.png", "rakgg.png",
             "rbyle.png", "reulr.png", "rfxjq.png", "rguoz.png",
             "rjagw.png", "rkucz.png", "rkxit.png", "rluvv.png",
             "rponj.png", "rsxvy.png", "ruoqv.png", "sbpih.png",
             "sgubo.png", "shhym.png", "sipfs.png", "sjgqy.png",
             "sjsdw.png", "sknty.png", "snpgy.png", "sqwmg.png",
             "syeoq.png", "syfkj.png", "szrol.png", "tacje.png",
             "tesdi.png", "tffbk.png", "thqir.png", "tiopk.png",
             "tmfcx.png", "tmklm.png", "tpiau.png", "tvrdz.png",
             "tvsqf.png", "tvsqf.png", "twmud.png", "udcwt.png",
             "ufgie.png", "ufxyu.png", "ugvoa.png", "ulanu.png",
             "umhwv.png", "upipm.png", "uqkmp.png", "uuuzn.png",
             "uvdrh.png", "uxdaj.png", "uygnt.png", "vdctq.png",
             "vdqqb.png", "vetzn.png", "vfvqv.png", "viihy.png",
             "vjywg.png", "vmhje.png", "vqnnc.png", "vqygp.png",
             "vqysg.png", "vsvko.png", "vvzxj.png", "vwthi.png",
             "vzcjf.png", "wameh.png", "wcrkg.png", "wddyc.png",
             "wfbmp.png", "wfhws.png", "wgfpj.png", "whqbs.png",
             "wjkdu.png", "wmket.png", "wsfyp.png", "wtcqz.png",
             "wttsx.png", "wyybi.png", "xbkio.png", "xfuhc.png",
             "xhvrg.png", "xiugj.png", "xmeyu.png", "xoerq.png",
             "xrufl.png", "yabqs.png", "ygcbq.png", "ygnud.png",
             "yhjcv.png", "yhllr.png", "yiyxs.png", "ylwsl.png",
             "ytivk.png", "yuohz.png", "yvgvn.png", "yvwbc.png",
             "zadtg.png", "zjffk.png", "zkcvn.png", "zlcwr.png",
             "zmbzo.png", "zncas.png", "zndih.png", "zolkh.png",
             "ztgqp.png", "ztnkk.png", "zudvm.png", "zukbo.png",
             "zwbgs.png", "zwjjm.png", "zxsoj.png"

             ]
         


#Variable to hold image size
xycoordinates = np.zeros((362,2))

#Array Variable to hold Average Intensity of all Image Corpus Images
AverageIntensity = np.zeros((362,1))

#Array Variable to hold Color Homogeneity Percentage
HomogeneityPercent = np.zeros((362,1))


#Array Variable to hold Number of Lines Detected
TotalLines = np.zeros((362,1))

#Array Variable to hold Mean PSD of Images
PSDMean = np.zeros((362,1))

#Array Variable to hold Entropy Mean of Images
EntropyMean = np.zeros((362,1))

#Array Variable to hold All One Shot Algorithm Development
OneShotAlgorithm = np.zeros((362,5))

#Array to Hold String Variable for file
StringFile = "{"

#One Shot Algorithm Development
#Average Intensity Value across the Image
#Color Homogeneity (for grayscale)
#Edge Filtration  of line detection(such as Canny Edge)
#Power Spectrum Density Cross Correlation across the Image
#Entropy across the Image


#for l in range(0,362):
    #Read in Image Corpus Image
for i in range(0,362):
   datab = cv2.imread(Imagefile[i])

   #Convert Image from RGB to Gray
   gray = cv2.cvtColor(datab, cv2.COLOR_BGR2GRAY)
   
   # Get the shape of the image [Row x Column] and save values
   #as row and colum variables
   [xycoordinates[i,0], xycoordinates[i,1]]= gray.shape
   row = int(xycoordinates[i,0])
   column = int(xycoordinates[i,1])

   #PROCESS 1: AVERAGE INTENSITY
   #Variable to hold Sum of Intensity across an Entire Image
   SumIntensity = 0
   
   #Nested Loop to Extract Average Intensity from the Image
   for j in range(0,row):
      for k in range(0,column):
         #Obtain Pixel Intensity
         test = gray[j,k]
         
         #Add Pixel Value to Sum of Intensity)
         SumIntensity = SumIntensity + test

   #Get the Average Intensity Value of the Grayscale Image
   AvIntensity = ((SumIntensity/row)/column)
   
   #Store the Average Intensity Value of the Grayscale Image in
   #the Average Intensity Array
   AverageIntensity[i] = AvIntensity 

       
   #PROCESS 2: COLOR HOMOGENEITY

   #Variable to Count Homogeneous Pixels
   HomogeneousCount = 0
   #Nested Loop to Extract Homogeneous Pixels
   for j in range(1,row-1):
      for k in range(1,column-1):
         #Obtain Homogeneous Value
         hv = (gray[j,k]+gray[j-1,k]+gray[j+1,k]+gray[j,k+1]+gray[j-1,k+1]+gray[j+1,k+1]+gray[j,k-1]+gray[j-1,k-1]+gray[j+1,k-1])
         hv2 = hv/9
         if((abs(gray[j,k] - hv2)) < 30):
            HomogeneousCount = HomogeneousCount + 1
   #Store Homogeneity Percent in Homogeneity Array
   HomogeneityPercent[i] = ((HomogeneousCount * 100)/(row * column))
         


   #PROCESS 3: LINE DETECTION

   #Variable to Count Line Detection
   line = 0
   lineimage = gray

   #Grayscale Thresholding to extract lines in Image
   for j in range(1,row-1):
       for k in range(1,column-1):
           #if( ( gray[j,k] > 50) &  (gray[j,k] < 80)):
           if( ( gray[j,k] > 180)):
              lineimage[j,k] = 255
           else:
              lineimage[j,k] = 0   

   #perform Region Props on Thresholded Image
   lineimagecc = np.array(lineimage)
   #Select Pixels Greater than 100 with a mask
   mask = lineimagecc > 100
   labels = measure.label(mask)

   #Segment out Regions
   regions = measure.regionprops(labels, lineimagecc)
   numlabels = len(regions)
   regions = regionprops_table(labels, properties=('area', 'coords'))
   #print(regions)
   pd.DataFrame(regions)
   y = pd.DataFrame(regions)
   #Get Shape and Size of Regions
   [a1,b1] = y.shape

   #Select Only Regions Greater than 500 Pixels and Get their Line Count
   linecount = 0

   for j in range(0,a1):
       if(y.values[j,0] > 200):
          linecount = linecount + 1


   #Store LineCounts in Total Line Array
   TotalLines[i] = linecount



   #PROCESS 4 POWER SPECTRUM DENSITY (PSD)

   #Variable to Hold PSD
   psd = 0
   psdimage = gray
   psdsum = 0

   #Get PSD
   fourier_image = np.fft.fftn(gray)
   fs = 1000.0 #1 kHz sampling frequency
   #signal = grayscale image
   signal = gray
   (S,f) = plt.psd(signal, Fs=fs)
   #f contains the frequency components
   #S is the PSD
   #plt.semilogy(f,S)
   #plt.xlim([0,100])
   #plt.xlabel('frequency [Hz]')
   #plt.ylabel('PSD [V**22222Hz]')
   #plt.show()

   #Size of the PSD
   psd =S.size

   #Get Average PSD
   for j in range(0,psd):
      psdsum = psdsum + S[j]

   #Store Average PSD in PSDMean Variable
   PSDMean[i] = psdsum/psd


   
   #PROCESS 5 ENTROPY

   #Variable to Hold Entropy
   entropyimage = gray
   entropysum = 0
   entropy1 = np.array(entropyimage)

   #Get Entropy Value
   entropy2 = entropy(entropy1, base=10)

   #Get Size of Entropy
   entropysize =entropy2.size

   #Find Entropy Mean
   for j in range(0,entropysize):
      entropysum = entropysum + entropy2[j]

   #Store Average Entropy in EntropyMean Variable
   EntropyMean[i] = entropysum/entropysize

   
print("Homogeneity% : ")
print(HomogeneityPercent)  
print("Array Final Average Intensity: ")
print(AverageIntensity)
print("Total Line Count: ")
print(TotalLines)
print("PSD Mean: ")
print(PSDMean)
print("Entropy Mean: ")
print(EntropyMean)


#insert the 5 Oneshot Algorithm Features into the OneShotAlgorithm Array Variable
OneShotAlgorithm[:,0] = HomogeneityPercent[:,0]
OneShotAlgorithm[:,1] = AverageIntensity[:,0]
OneShotAlgorithm[:,2] = TotalLines[:,0]
OneShotAlgorithm[:,3] = PSDMean[:,0]
OneShotAlgorithm[:,4] = EntropyMean[:,0]

#Print the OneshotAlgorithm Array Variable
print("OneshotAlgorithm : ")
print(OneShotAlgorithm)

#Access Oneshot Algorithm Array Variable Shape and Size
OneShotAlgorithm.shape
OneShotAlgorithm.size
        
print("XY Coordinates: ")     
print(xycoordinates)


#Upload Images to be used as Test Data
#Load 50 Images
ImageTestData = ["aogst.png", "bbqxg.png", "cwrzg.png", "dbxmq.png",
             "eckdo.png", "engqt.png", "ezuen.png", "fhnts.png",
             "gdchp.png", "hqfll.png", "iiqot.png", "ijdzo.png",
             "itzis.png", "iwiev.png" ,"iyphf.png", "jggsc.png",
             "jjvxo.png", "klxxh.png", "kthks.png", "lvoiu.png",
             "lzwdh.png", "mfros.png", "miufj.png", "mzwjh.png",
             "nfnmb.png", "ngxvb.png", "nojtp.png", "pijkw.png",
             "qemqk.png", "qsiio.png", "qtudi.png", "siisg.png",
             "sjplt.png", "skjpp.png", "skqhg.png", "uciie.png",
             "ukwfg.png", "uyjad.png", "vcnst.png", "wakcc.png",
             "wtdvm.png", "wvbsi.png", "xvhbx.png", "yjglq.png",
             "yracw.png", "yzaxb.png", "zivsv.png", "zjxrd.png",
             "zluym.png", "zqqan.png",

             ]


#Variable to hold image size of all Test Images
xycoordinatestest = np.zeros((50,2))

#Array Variable to hold Average Intensity of all Test Images
AverageIntensitytest = np.zeros((50,1))

#Array Variable to hold Color Homogeneity Percentages of all Test Images
HomogeneityPercenttest = np.zeros((50,1))


#Array Variable to hold Number of Lines Detected in all Test Images
TotalLinestest = np.zeros((50,1))

#Array Variable to hold Mean PSD of all Test Images
PSDMeantest = np.zeros((50,1))

#Array Variable to hold Entropy Mean of all Test Images
EntropyMeantest = np.zeros((50,1))

#Array Variable to hold All One Shot Algorithm Development of all Test Images
OneShotAlgorithmtest = np.zeros((50,5))

#for l in range(0,50):
    #Read in Test Images
for i in range(0,50):
   datac = cv2.imread(ImageTestData[i])

   #Convert Image from RGB to Gray
   graytest = cv2.cvtColor(datac, cv2.COLOR_BGR2GRAY)
   
   # Get the shape of the image [Row x Column] and save values
   #as row and colum variables
   [xycoordinatestest[i,0], xycoordinatestest[i,1]]= graytest.shape
   rowtest = int(xycoordinatestest[i,0])
   columntest = int(xycoordinatestest[i,1])

   #PROCESS 1: AVERAGE INTENSITY
   #Variable to hold Sum of Intensity across an Entire Test Image
   SumIntensitytest = 0
   
   #Nested Loop to Extract Average Intensity from the Test Image
   for j in range(0,rowtest):
      for k in range(0,columntest):
         #Obtain Pixel Intensity
         testtest = graytest[j,k]
         
         #Add Pixel Value to Sum of Intensity)
         SumIntensitytest = SumIntensitytest + testtest

   #Get the Average Intensity Value of the Grayscale Test Image
   AvIntensitytest = ((SumIntensitytest/rowtest)/columntest)
   
   #Store the Average Intensity Value of the Grayscale Test Image in
   #the Average Intensity Array
   AverageIntensitytest[i] = AvIntensitytest 

       
   #PROCESS 2: COLOR HOMOGENEITY

   #Variable to Count Homogeneous Pixels
   HomogeneousCounttest = 0
   #Nested Loop to Extract Homogeneous Pixels
   for j in range(1,rowtest-1):
      for k in range(1,columntest-1):
         #Obtain Homogeneous Value
         hvtest = (graytest[j,k]+graytest[j-1,k]+graytest[j+1,k]+graytest[j,k+1]+graytest[j-1,k+1]+graytest[j+1,k+1]+graytest[j,k-1]+graytest[j-1,k-1]+graytest[j+1,k-1])
         hv2test = hvtest/9
         if((abs(graytest[j,k] - hv2test)) < 30):
            HomogeneousCounttest = HomogeneousCounttest + 1
   #Store Homogeneity Percent in Homogeneity Array
   HomogeneityPercenttest[i] = ((HomogeneousCounttest * 100)/(rowtest * columntest))
         


   #PROCESS 3: LINE DETECTION

   #Variable to Count Line Detection
   linetest = 0
   lineimagetest = graytest

   #Grayscale Thresholding to extract lines in Test Image
   for j in range(1,rowtest-1):
       for k in range(1,columntest-1):
           #if( ( gray[j,k] > 50) &  (gray[j,k] < 80)):
           if( ( graytest[j,k] > 180)):
              lineimagetest[j,k] = 255
           else:
              lineimagetest[j,k] = 0   

   #perform Region Props on Thresholded Test Image
   lineimagecctest = np.array(lineimagetest)
   #Select Pixels Greater than 100 with a mask
   masktest = lineimagecctest > 100
   labelstest = measure.label(masktest)

   #Segment out Regions
   regionstest = measure.regionprops(labelstest, lineimagecctest)
   numlabelstest = len(regionstest)
   regionstest = regionprops_table(labelstest, properties=('area', 'coords'))
   #print(regions)
   pd.DataFrame(regionstest)
   y = pd.DataFrame(regionstest)
   #Get Shape and Size of Regions
   [a1,b1] = y.shape

   #Select Only Regions Greater than 500 Pixels and Get their Line Count
   linecounttest = 0

   for j in range(0,a1):
       if(y.values[j,0] > 200):
          linecounttest = linecounttest + 1


   #Store LineCounts in Total Line Array
   TotalLinestest[i] = linecounttest



   #PROCESS 4 POWER SPECTRUM DENSITY (PSD)

   #Variable to Hold PSD
   psdtest = 0
   psdimagetest = graytest
   psdsumtest = 0

   #Get PSD
   fourier_imagetest = np.fft.fftn(graytest)
   fstest = 1000.0 #1 kHz sampling frequency
   #signaltest = grayscale image
   signaltest = graytest
   (S,f) = plt.psd(signaltest, Fs=fstest)
   #f contains the frequency components
   #S is the PSD
   #plt.semilogy(f,S)
   #plt.xlim([0,100])
   #plt.xlabel('frequency [Hz]')
   #plt.ylabel('PSD [V**22222Hz]')
   #plt.show()

   #Size of the PSD
   psdtest =S.size

   #Get Average PSD
   for j in range(0,psdtest):
      psdsumtest = psdsumtest + S[j]

   #Store Average PSD in PSDMean Variable
   PSDMeantest[i] = psdsumtest/psdtest


   
   #PROCESS 5 ENTROPY

   #Variable to Hold Entropy
   entropyimagetest = graytest
   entropysumtest = 0
   entropy1test = np.array(entropyimagetest)

   #Get Entropy Value
   entropy2test = entropy(entropy1test, base=10)

   #Get Size of Entropy
   entropysizetest =entropy2test.size

   #Find Entropy Mean
   for j in range(0,entropysizetest):
      entropysumtest = entropysumtest + entropy2test[j]

   #Store Average Entropy in EntropyMean Variable
   EntropyMeantest[i] = entropysumtest/entropysizetest

   
   print("Homogeneity% for Test Image : ")
   print(HomogeneityPercenttest)  
   print("Array Final Average Intensity for Test Image: ")
   print(AverageIntensitytest)
   print("Total Line Count for Test Image: ")
   print(TotalLinestest)
   print("PSD Mean for Test Image: ")
   print(PSDMeantest)
   print("Entropy Mean for Test Image: ")
   print(EntropyMeantest)

   #insert the 5 Oneshot Algorithm Features into the OneShotAlgorithm Array Variable
   OneShotAlgorithmtest[:,0] = HomogeneityPercenttest[:,0]
   OneShotAlgorithmtest[:,1] = AverageIntensitytest[:,0]
   OneShotAlgorithmtest[:,2] = TotalLinestest[:,0]
   OneShotAlgorithmtest[:,3] = PSDMeantest[:,0]
   OneShotAlgorithmtest[:,4] = EntropyMeantest[:,0]

   #Print the OneshotAlgorithm Array Variable
   print("OneshotAlgorithm for Test Image: ")
   print(OneShotAlgorithmtest)

   #Access Oneshot Algorithm Array Variable Shape and Size
   OneShotAlgorithmtest.shape
   OneShotAlgorithmtest.size
           
   print("XY Coordinates for Test Image: ")     
   print(xycoordinatestest)
   print("Done for now")

   #Match Test Image against the 362 Images in Corpus Image and Extract the
   #Top Three (3) Best Fits

   #Array Variable to hold Matching Data per Test Image
   Fit = np.zeros((362,5))
   for j in range(0,362):
      Fit[j,0] = abs(OneShotAlgorithm[j,0] - OneShotAlgorithmtest[i,0])
      Fit[j,1] = abs(OneShotAlgorithm[j,1] - OneShotAlgorithmtest[i,1])
      Fit[j,2] = abs(OneShotAlgorithm[j,2] - OneShotAlgorithmtest[i,2])
      Fit[j,3] = abs(OneShotAlgorithm[j,3] - OneShotAlgorithmtest[i,3])
      Fit[j,4] = abs(OneShotAlgorithm[j,4] - OneShotAlgorithmtest[i,4])
        
   print("Fit to Oneshot Algorithm: ")     
   print(Fit)
   print("Done for now") 

     
   #Sum Fit to Oneshot Algorithm to find the Lowest three rows (best 3 fits)
   SumFit = np.zeros((362,1))
   TestSumFit = np.zeros((362,1))
   for j in range(0,362):
      SumFit[j,0] = sum(Fit[j,:])
      TestSumFit[j,0] = sum(Fit[j,:])    
   print("SumFit for Oneshot Algorithm: ")     
   print(SumFit)
   print("Done for now")
   
   MaxSumFit = max(TestSumFit)
   print("MaxSumFit")
   print(MaxSumFit)
   
   #Check for Lowest Three sum rows and ir confidences
   RowIndexSum = np.zeros((3,1))
   Match1 = min(TestSumFit)
   MatchConfidence = np.zeros((3,1))
   FitRow = 0
   for j in range(0,362):
      if(TestSumFit[j] == Match1):
         RowIndexSum[0] = j
         FitRow = j
   print("FitRow 1: ")
   print(FitRow)
   TestSumFit[FitRow] = 1000
   
   Match2 = min(TestSumFit)
   for j in range(0,362):
      if(TestSumFit[j] == Match2):
         RowIndexSum[1] = j
         FitRow = j
   TestSumFit[FitRow] = 1000
   print("FitRow 2: ")
   print(FitRow)
   
   Match3 = min(TestSumFit)
   for j in range(0,362):
      if(TestSumFit[j] == Match3):
         RowIndexSum[2] = j
         FitRow = j
   print("FitRow 3: ")
   print(FitRow)
   TestSumFit[FitRow] = 1000


   print("Three Rows: ")     
   print(RowIndexSum)
   print("The Three Rows: ")     
   print(SumFit[int(RowIndexSum[0])])
   print(SumFit[int(RowIndexSum[1])])
   print(SumFit[int(RowIndexSum[2])])

   MatchConfidence[0] = 1.0
   MatchConfidence[1] = (1 - ((SumFit[int(RowIndexSum[1])]) / MaxSumFit))
   MatchConfidence[2] = (1 - ((SumFit[int(RowIndexSum[2])]) / MaxSumFit))

   print("Match Confidences: ")     
    
   print(MatchConfidence[0])
   print(MatchConfidence[1])
   print(MatchConfidence[2])


   #Get confidence level for three images using the SumFit[int(RowIndexSum[2])])
   #data above tomorrow
   
   
   print("Selected Three Images: ")     
   print(Imagefile[int(RowIndexSum[0])])
   print(Imagefile[int(RowIndexSum[1])])
   print(Imagefile[int(RowIndexSum[2])])

   StringFile = StringFile + "'" + ImageTestData[i] + "': [{'label': '" + str(Imagefile[int(RowIndexSum[0])]) + "', 'confidence': 1.0}, {'label': '" + str(Imagefile[int(RowIndexSum[1])]) + "', 'confidence':" + str(MatchConfidence[1]) + "}, {'label': '" + str(Imagefile[int(RowIndexSum[2])]) + "', 'confidence':" + str(MatchConfidence[2]) + "}], "
   
   print("Addded String File")
   print(StringFile)

   conf1 = str(MatchConfidence[0])
   conf2 = str(MatchConfidence[1])
   conf3 = str(MatchConfidence[2])

   
   print("String Confidences :")
   print(conf1)
   print(conf2)
   print(conf3)
   #Store Selection in an Array String Variable to be concatenated for the
   # 50 Test Images
   
   print("Done for Matching Images Singular")     

StringFile = StringFile + "}"
print("Final String: ")
print(StringFile)
np.save('Onward3start.txt',StringFile)
