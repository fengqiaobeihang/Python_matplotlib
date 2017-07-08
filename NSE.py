# -*- coding: utf-8 -*-
#Author:shaodonghang
#Date:2017-03-26
#state:Error calculation code
import numpy             as np
import xlrd
import matplotlib
import matplotlib.pyplot as plt
from   matplotlib.colors import *
from   scipy.stats       import gaussian_kde
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter

data  = xlrd.open_workbook('C:\Users\sdh\Desktop\WRF_verify\SNOW_ALBEDO.xlsx')
sheet = data.sheets()[0]
# Generate fake data
simulation_data   = sheet.col_values(1)[1:]
observation_data  = sheet.col_values(2)[1:]
nrows_simulation  = sheet.row(1)
nrows_observation = sheet.row(2)
ncols_simulation  = sheet.col(1)
ncols_observation = sheet.col(2)
nrows = sheet.nrows
ncols = sheet.ncols
# print 'nrows_simulation=',nrows_simulation
# print 'ncols_simulation=',ncols_simulation
print 'nrows=',nrows
print 'ncols=',ncols
#Where average_observation is the mean of observed discharges
#And simulation_data is modeled discharge at time t 
#Observation_data is observed discharge at time t
simulation_data    = np.array(simulation_data)
observation_data   = np.array(observation_data)
#print 'simulation_data=',simulation_data
average_simulation  = np.average(simulation_data)
average_observation = np.average(observation_data)
print 'average_simulation=',average_simulation
print 'average_observation=',average_observation
QT = (observation_data-simulation_data)**2 
QO = (observation_data-average_observation)**2
SUM_QT = np.sum(QT)
SUM_QO = np.sum(QO)
#NSE=Nash–Sutcliffe model efficiency coefficient
NSE = 1-SUM_QT/SUM_QO
#########MAE#########
MAE = np.sum(np.abs(simulation_data-observation_data))/(nrows-1)
print 'MAE=',MAE
#########MAE#########
#########RMSE########
RMSE=(np.sum(QT)/(nrows-1))**0.5
print 'RMSE=',RMSE
#########RMSE########
########Pearson correlation coefficient:R########
simulation_SD  = (np.sum((simulation_data-average_simulation)**2)/(nrows-1))**0.5
observation_SD = (np.sum((observation_data-average_observation)**2)/(nrows-1))**0.5
print 'simulation_SD=', simulation_SD
print 'observation_SD=',observation_SD
R = np.sum(((simulation_data-average_simulation)/simulation_SD)*((observation_data-average_observation)/observation_SD))/(nrows-2)
print 'R=',R
########Pearson correlation coefficient:R########
########coefficient of determination#############
R2=R**2
print 'R2=',R2
########coefficient of determination#############
print 'NSE=',NSE
print 'end'
#Nash–Sutcliffe efficiency can range from −∞ to 1. 
#An efficiency of 1 (E = 1) corresponds to a perfect match of modeled discharge to the observed data. 
#An efficiency of 0 (E = 0) indicates that the model predictions are as accurate as the mean of the observed data, 
#whereas an efficiency less than zero (E < 0) occurs when the observed mean is a better predictor than the model.