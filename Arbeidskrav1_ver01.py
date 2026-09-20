#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 09:29:11 2026

@author: linnvinje
"""
#%% Årlige kostnader for elbil
Forsikring = 5000.0
Trafikkforsikring = 8.38*365.0
Drivstoff = 0.2*2.00*10_000.0
Bomavgift = 0.1*10_000.0
Årlige_kostnader_elbil = Forsikring + Trafikkforsikring + Drivstoff + Bomavgift
print('årlige kostnader for elbil er:', Årlige_kostnader_elbil, 'kr')

#%% Årlige kostnader for bensinbil
Forsikring = 7500.0
Trafikkforsikring = 8.38 *365.0
Drivstoff = 1.0* 10_000.0
Bomavgifter = 3.0*10_000.0 
Årlige_kostnader_bensinbil = Forsikring + Trafikkforsikring + Drivstoff + Bomavgift
print('årlige kostnader for bensinbil er:', Årlige_kostnader_bensinbil, 'kr')

#%% kostnadsdifferanse mellom bensinbil og elbil
Kostnadsdifferanse = Årlige_kostnader_bensinbil - Årlige_kostnader_elbil
print('kostnadsdifferanse mellom bensinbil og elbil er:', Kostnadsdifferanse, 'kr')

