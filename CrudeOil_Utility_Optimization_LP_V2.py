# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 15:39:56 2025

@author: spinosaurus777
"""

# Import libraries

import pulp
print("PuLp current version: ", pulp.__version__)

#%%

# List for units in the process

flows =  [ f'F{i}' for i in range(1,48)]

units = [ 'T101', 'D101', 'D102', 'D103', 'R101', 'C101', 'T102', 'T103', 'T104', 
         'D104', 'D105', 'D106', 'D107', 'D108', 'D109', 'D110',
         'D111', 'D112', 'M101', 'M102', 'M103', 'M104']


# Mass flows per unit

flows_per_unit = {
    
    'IN': {
        
        'T101': ['F1', 'F2', 'F3', 'F4'],
        
        'D101': ['F5'],
        'D102': ['F6'],
        'D103': ['F7'],
        
        'R101': ['F8'],
        'C101': ['F10'],
        'T102': ['F13'],
        
        'T103': ['F9', 'F14'],
        'T104': ['F11', 'F15'],
        
        'D104': ['F17'],
        'D105': ['F18'],
        'D106': ['F19'],
        'D107': ['F20'],
        'D108': ['F21'],
        
        'D109': ['F22'],
        'D110': ['F23'],
        'D111': ['F24'],
        'D112': ['F12', 'F16'],
        
        'M101': ['F25', 'F27', 'F29', 'F31', 'F33'],
        'M102': ['F26', 'F28', 'F30', 'F32', 'F34'],
        'M103': ['F35', 'F37', 'F39', 'F41'],
        'M104': ['F36', 'F38', 'F40', 'F42'],
        },
    
    'OUT': {
        
        'T101': ['F5', 'F6', 'F7'],
        
        'D101': ['F8', 'F9'],
        'D102': ['F10', 'F11'],
        'D103': ['F12', 'F13'],
        
        'R101': ['F14'],
        'C101': ['F15'],
        'T102': ['F16','F47'],
        
        'T103': ['F17', 'F18', 'F19', 'F20'],
        'T104': ['F21', 'F22', 'F23', 'F24'],
        
        'D104': ['F25', 'F26'],
        'D105': ['F27', 'F28'],
        'D106': ['F29', 'F30'],
        'D107': ['F31', 'F32'],
        'D108': ['F33', 'F34'],
        
        'D109': ['F35', 'F36'],
        'D110': ['F37', 'F38'],
        'D111': ['F39', 'F40'],
        'D112': ['F41', 'F42'],
        
        'M101': ['F43'],
        'M102': ['F44'],
        'M103': ['F45'],
        'M104': ['F46'],
        
        }
    }

# Component per flow

component_per_flow = {
    
    'F1': ['C1'],
    'F2': ['C2'],
    'F3': ['C3'],
    'F4': ['C4'],
    
    'F5': ['LN', 'MN', 'HN'],
    'F6': ['LO', 'HO'],
    'F7': ['R'],
    
    'F8': ['LN', 'MN', 'HN'],
    'F9': ['LN', 'MN', 'HN'],
    'F10': ['LO', 'HO'],
    'F11': ['LO', 'HO'],
    'F12': ['R'],
    'F13': ['R'],
    
    'F14': ['RG', 'LN', 'MN', 'HN'],
    'F15': ['CG', 'CO', 'LO', 'HO'],
    
    'F16': ['R'],
    
    'F17': ['LN'],
    'F18': ['MN'],
    'F19': ['HN'],
    'F20': ['RG'],
    'F21': ['CG'],
    
    'F22': ['LO'],
    'F23': ['HO'],
    'F24': ['CO'],
    
    'F25': ['LN'],
    'F26': ['LN'],
    'F27': ['MN'],
    'F28': ['MN'],
    'F29': ['HN'],
    'F30': ['HN'],
    'F31': ['RG'],
    'F32': ['RG'],
    'F33': ['CG'],
    'F34': ['CG'],
    
    'F35': ['LO'],
    'F36': ['LO'],
    'F37': ['HO'],
    'F38': ['HO'],
    'F39': ['CO'],
    'F40': ['CO'],
    'F41': ['R'],
    'F42': ['R'],
    
    'F43': ['PrG'],
    'F44': ['ReG'],
    'F45': ['JF'],
    'F46': ['FO'],
    'F47': ['EL']
    
    }

# Entrt Flows

entry_total_flows = ['F1', 'F2', 'F3', 'F4']

# Out flows

out_total_flows = ['F43', 'F44', 'F45', 'F46', 'F47']
# List final productos

final_products = ['PrG', 'ReG', 'JF', 'FO', 'EL']

# List of Naftas

naftas = ['LN', 'MN', 'HN']

# List of oils

oils = ['LO', 'HO']

# List of middle gases

middle_gas = ['RG', 'CG']

# List of middle oils

middle_oil = ['CO']

# List of entry crudes

entry_crudes = ['C1', 'C2', 'C3', 'C4']

ing_JF = ['LO','HO','CO','R']
ing_PrG = ['LN','MN','HN','RG','CG']
ing_ReG = ['LN','MN','HN','RG','CG']

#%%

# Creates de Flows per Component List:
    
flows_per_component=[]

for key in component_per_flow:
    for comp in component_per_flow[key]:
        flows_per_component.append(f'{key}_{comp}')

#%%

# PARAMETERS

# ENTRY COMPOSITIONS OF THE CRUDES

# Dctionary for Light Nafta (NL) composition in each crude [-]

crudes_composition = {
    
    'C1': {'LN': 0.1,
           'MN': 0.2,
           'HN': 0.2,
           'LO': 0.12,
           'HO': 0.2,
           'R': 0.13
                },
    
    'C2': {'LN': 0.15,
           'MN': 0.25,
           'HN': 0.18,
           'LO': 0.08,
           'HO': 0.19,
           'R': 0.12
                },
    
    'C3': {'LN': 0.15,
           'MN': 0.1,
           'HN': 0.2,
           'LO': 0.2,
           'HO': 0.1,
           'R': 0.05
                },
    
    'C4': {'LN': 0.25,
           'MN': 0.2,
           'HN': 0.15,
           'LO': 0.05,
           'HO': 0.15,
           'R': 0.05
                }
    }


# CONVERSTON RATE - REFORMING

# A dictionary for conversion rates in the reforming unit [-]


conversion = {
    
    'R101': {
        'RG': { 
            'LN': 0.6,
            'MN': 0.52,
            'HN': 0.45
            }
        },
    
    'C101': {
        
        'CO': {
            'LO': 0.68,
            'HO': 0.75
            },
        
        'CG': {
            'LO': 0.28,
            'HO': 0.2
            },
        },
        
    'T102': {
        'EL': {
            'R': 0.5
            }
        }
    }
    

# MIXING - VAPOUR PRESSURE

# A dictionary for vapur pressures in the mixing unit [kg/cm2]

mixing_vapour_pressure = {
    
    'LO': 1,
    'HO': 0.6,
    'CO': 1.5,
    'R': 0.05
    
    }


# MIXING - FUELOIL PROPORTION

FO_proportion = {
    
    'LO': 0.55,
    'CO': 0.24,
    'HO': 0.16,
    'R': 0.05
    
    }

# RATIO BETWEEN REGULAR GAS AND PREMIUM GAS

min_r_ReG_PrG = 0.4


# COSTS - ENTRY CRUDES

# A dictionary for  costs for in each crude [$/barrel]

costs_crudes = {
    
    'C1': 200,
    'C2': 300,
    'C3': 250,
    'C4': 350
    
    }

# OCTANE

# Dictionary for octane values [Octane]

octane_values = {
    
    'LN': 90,
    'MN':80,
    'HN':70,
    'RG':115,
    'CG': 105
    
    }

# SALE PRICES - FINAL PRODUCTOS

# A dictionary for sale prices for each final product [$/barrel]

prices_final_products= {
    
    'PrG': 700, 
    'ReG': 600, 
    'JF': 400, 
    'FO': 350,
    'EL':150
    
    }



#%%

# INEQULAITY CONTRAINS PARAMETERS

# Dictionary for crude avaliability


crude_avaliabity = {
    
    'C1': 20000,
    'C2': 30000,
    'C3': 15000,
    'C4': 25000
    
    }

units_capacity = {
    
    'T101': 55000,
    'R101': 15000,
    'C101': 12000
    
    }

range_for_EL_production = [500, 1500]

max_JF_vpresure = 1

min_oct_ReG = 84
min_oct_PrG = 94

#%%

    

#%%

# CREATION OF MODEL

# Create the variable to contain the porblem data

model = pulp.LpProblem('Crude_Oil_Utiliy_model', pulp.LpMaximize)


#%%

# VARIABLES

# Create the variables for the modellem

# Dictionary for Total Mass Flows in each fcurrent  (Mass_Flows_F#)

flows_vars = pulp.LpVariable.dicts(
    'Mass_Flows', flows, lowBound=0, cat='Continuous')

# Dictionary for Composition Flow in each current (Mass_Flow_F#_Component):

flows_per_component_vars = pulp.LpVariable.dicts(
    'Mass_Flows_Comp', flows_per_component, lowBound=0, cat='Continuous')

# Total of 109 variables. We have 16 GL (Grados de Libertidad):
#   - 4 flows entrys: F1, F2, F3, F4
#   - 12 flows for each divisor

# We then, must have 93 equality constrains.

# Some varaibles may seen redundant (and they are), specifically, those that only have one component in their
# current, ie. F1 = F1_C1, and such eqqualities must be added to the equality constrains.
# This implies the expansion of the porblem, and, logically, a need of more computational
# resources. However, in order to codify the model in the most clear but also the most contained way,
# including such variables becomes necesarry to be ables of, first, matain a consistent
# formating of the variables and avoid confussion, and second, to allow the use
# of complete cycles for contrain creation instead of making a cycle for each unit or flow.

# The expansion of the problem is of 30 additional variables. Around half of the
# original problem. That is to say, the solution I am showing here today is 147.62%
# bigger than the original problem. I would consider this a important porblem of size
# if we were dealing with non-linear models, as their complexity, resources and 
# solution time increase in almost all cases exponentaully with the increase of size.
# But as I am modeling the process plant as a lineal problem with convertions and ratios
# calculated from historial prodcuction data, and lineal problems optimizations
# are so powerful and effcient, the consequences of the increase in size in this particular case 
# is almost impercetable, difference in the solutions times betweeen the two scenaros
# running in the nano seconds. 


#%%

# EQUALITY CONSTRAINS

# GENERAL MASS BALANCE (1)
model += ((pulp.lpSum([flows_vars[flow] for flow in entry_total_flows])) 
          - (pulp.lpSum([flows_vars[flow] for flow in out_total_flows]))) == 0, 'General_Mass_Balance'

# MASS BALANCE PER UNIT
# Total Mass Balance (This is useful for all units) (21)

#for unit in units:
#    model += ((pulp.lpSum([flows_vars[flow] for flow in flows_per_unit['IN'][unit]])) 
#          - (pulp.lpSum([flows_vars[flow] for flow in flows_per_unit['OUT'][unit]]))) == 0, f'Total_Mass_Balance_for_{unit}'


# SUM OF COMPONENTS IN EACH FLOW
# Sum of all component flows in a current (47)
for flow in component_per_flow:
    model += (flows_vars[flow] 
              - (pulp.lpSum([flows_per_component_vars[f'{flow}_{component}'] for component in component_per_flow[flow]]))) == 0, f'Sum_of_component_flows_for_{flow}'



# COMPONENT MASS BALANCE UN UNITS WITHOUT CONVERSION

divisors = ['D101', 'D102', 'D103', 'D104', 'D105', 'D106', 'D107', 'D108',
                       'D109', 'D110', 'D111', 'D112']

# !!! 
# Divisors ar working like destilation towers.
for unit in divisors:
    list_comp_unit = []
    for flow_in in flows_per_unit['IN'][unit]:
        for comp in component_per_flow[flow_in]:
            if comp not in list_comp_unit:
                list_comp_unit.append(comp)
    for comp in list_comp_unit:
        model += (pulp.lpSum([flows_per_component_vars[f'{flow_out}_{comp}'] for flow_out in flows_per_unit['OUT'][unit]]) 
                  - pulp.lpSum([flows_per_component_vars[f'{flow_in}_{comp}'] for flow_in in flows_per_unit['IN'][unit]])) == 0, f'Mass_Balance_for_{comp}_in_{unit}'
  

dividing_towers = ['T103', 'T104']

for unit in dividing_towers:
    
    list_comp_unit = []
    for flow_out in flows_per_unit['OUT'][unit]:
        for comp in component_per_flow[flow_out]:
            if comp not in list_comp_unit:
                list_comp_unit.append(comp)
                
    for comp in list_comp_unit:
        list_in_flows = []
        list_out_flows = []
        for flow_in in flows_per_unit['IN'][unit]:
            if comp in component_per_flow[flow_in]:
                list_in_flows.append(flow_in)
        for flow_out in flows_per_unit['OUT'][unit]:
            if comp in component_per_flow[flow_out]:
                list_out_flows.append(flow_out)
        model += (pulp.lpSum([flows_per_component_vars[f'{flow_out}_{comp}'] for flow_out in list_out_flows]) 
                  - pulp.lpSum([flows_per_component_vars[f'{flow_in}_{comp}'] for flow_in in list_in_flows])) == 0, f'Mass_Balance_for_{comp}_in_{unit}'
    

          
        
# MASS BALANCE FOR UNIT WITH CONVERSIONS

# T101 (6)
for flow_out in flows_per_unit['OUT']['T101']:
    print(flow_out)
    for comp_out in component_per_flow[flow_out]:
        print(comp_out)
        vector_conversions = []
        for flow_in in flows_per_unit['IN']['T101'] :
            for comp_in in component_per_flow[flow_in]:
                conv = crudes_composition[comp_in][comp_out]
                vector_conversions.append(conv*flows_per_component_vars[f'{flow_in}_{comp_in}'])
        print(flow_out, comp_out)
        model += (flows_per_component_vars[f'{flow_out}_{comp_out}']
                                           - (pulp.lpSum(vector_conversions))) == 0, f'Mass_Balance_for_{comp_out}_in_{flow_out}_in_T101'
        print("finshed :", flow_out, comp_out)
        

# R101 (4)
for flow_out in flows_per_unit['OUT']['R101']:
    for comp_out in component_per_flow[flow_out]:
        vector_conversions = []
        for flow_in in flows_per_unit['IN']['R101'] :
            for comp_in in component_per_flow[flow_in]:
                try:
                    conv = conversion['R101'][comp_out][comp_in]
                except KeyError:
                    products = conversion['R101'].keys()
                    if comp_in == comp_out:
                        conv = 1 - (pulp.lpSum([conversion['R101'][prod][comp_in] for prod in products]))
                    else:
                        conv = 0
                vector_conversions.append(conv*flows_per_component_vars[f'{flow_in}_{comp_in}'])
        model += (flows_per_component_vars[f'{flow_out}_{comp_out}']
                                           - (pulp.lpSum(vector_conversions))) == 0, f'Mass_Balance_for_{comp_out}_in_{flow_out}_in_R101'
        

# C101 (4)
for flow_out in flows_per_unit['OUT']['C101']:
    for comp_out in component_per_flow[flow_out]:
        vector_conversions = []
        for flow_in in flows_per_unit['IN']['C101'] :
            for comp_in in component_per_flow[flow_in]:
                try:
                    conv = conversion['C101'][comp_out][comp_in]
                except KeyError:
                    products = conversion['C101'].keys()
                    if comp_in == comp_out:
                        conv = 1 - (pulp.lpSum([conversion['C101'][prod][comp_in] for prod in products]))
                    else:
                        conv = 0
                vector_conversions.append(conv*flows_per_component_vars[f'{flow_in}_{comp_in}'])
        model += (flows_per_component_vars[f'{flow_out}_{comp_out}']
                                           - (pulp.lpSum(vector_conversions))) == 0, f'Mass_Balance_for_{comp_out}_in_{flow_out}_in_C101'
        
               
# T102 (2)
for flow_out in flows_per_unit['OUT']['T102']:
    for comp_out in component_per_flow[flow_out]:
        vector_conversions = []
        for flow_in in flows_per_unit['IN']['T102'] :
            for comp_in in component_per_flow[flow_in]:
                try:
                    conv = conversion['T102'][comp_out][comp_in]
                except KeyError:
                    products = conversion['T102'].keys()
                    if comp_in == comp_out:
                        conv = 1 - (pulp.lpSum([conversion['T102'][prod][comp_in] for prod in products]))
                    else:
                        conv = 0
                vector_conversions.append(conv*flows_per_component_vars[f'{flow_in}_{comp_in}'])
        model += (flows_per_component_vars[f'{flow_out}_{comp_out}']
                                          - (pulp.lpSum(vector_conversions))) == 0, f'Mass_Balance_for_{comp_out}_in_{flow_out}_in_T102'

# FUELOIL PROPORTION

# M104 (4)
comp_FO = []
for flow in flows_per_unit['IN']['M104']:
    for comp in component_per_flow[flow]:
        if comp not in comp_FO:
            comp_FO.append(comp)
        
total_sum_out_El = pulp.lpSum([flows_per_component_vars[f'{flow_out}_FO'] for flow_out in flows_per_unit['OUT']['M104']])
# Careful.The prortion calculation must be done in a linar way.
for comp in comp_FO: 
    list_comp_flow = []
    for flow_in in flows_per_unit['IN']['M104']:
        if comp in component_per_flow[flow_in]:
            list_comp_flow.append(flows_per_component_vars[f'{flow_in}_{comp}'])
    print(list_comp_flow)
    model += total_sum_out_El*FO_proportion[comp] -  pulp.lpSum(list_comp_flow) == 0, f'Proportion of {comp} in Fueloil mixing'
    
#%%

# INEQUALITY CONSTRAINS

# CRUDES DISPONIBILITY

for crude in entry_crudes:
    list_crude_flow = []
    for flow_in in flows_per_unit['IN']['T101']:
        if crude in component_per_flow[flow_in]:
            list_crude_flow.append(flows_per_component_vars[f'{flow_in}_{crude}'])
    model += (pulp.lpSum(list_crude_flow)) <=  crude_avaliabity[crude], f'Avaliability for {crude}'      


# UNITS CAPACITY
for unit in units_capacity:
    model += (pulp.lpSum([flows_vars[flows_out] for flows_out in flows_per_unit['OUT'][unit]])) <= units_capacity[unit], f'Capacity for {unit}'
    
# RANGE FOR EL PRODUCTION

model += flows_per_component_vars['F47_EL'] <= range_for_EL_production[1], 'Maximum EL production'
model += flows_per_component_vars['F47_EL'] >= range_for_EL_production[0], 'Minimum EL production'

# MAX VAPOUR PRESSURE FOR JET FUEL           
model += (pulp.lpSum([mixing_vapour_pressure[ing]*flows_per_component_vars[f'{flow}_{ing}'] 
                      for ing,flow in zip(ing_JF, flows_per_unit['IN']['M103'])])) <= max_JF_vpresure*flows_per_component_vars['F45_JF'], 'Maximun vapour pressure of JF'
                      

# MIN OCTANE FOR PREMIUM GAS           
model += (pulp.lpSum([octane_values[ing]*flows_per_component_vars[f'{flow}_{ing}'] 
                      for ing,flow in zip(ing_PrG, flows_per_unit['IN']['M101'])])) >= min_oct_PrG*flows_per_component_vars['F43_PrG'],'Minimun_octane_for_PrG'
                      
# MIN OCTANE FOR REGULAR GAS  

model += (pulp.lpSum([octane_values[ing]*flows_per_component_vars[f'{flow}_{ing}'] 
                      for ing,flow in zip(ing_ReG, flows_per_unit['IN']['M102'])])) >= min_oct_ReG*flows_per_component_vars['F44_ReG'], 'Minimun_octane_for_ReG'
        
# MIN RATIO BETWEEN PrG AND ReG

model += flows_per_component_vars['F43_PrG'] - (min_r_ReG_PrG*flows_per_component_vars['F44_ReG']) <= 0, 'Ratio PrG and ReG'
                        

#%%

# OBJECTIVE FUNCTION

model += (
    pulp.lpSum([prices_final_products[prod]*flows_vars[f_prod] for prod,f_prod in zip(final_products,out_total_flows)]
               ) -
    pulp.lpSum([costs_crudes[crude]*flows_vars[f_crude] for crude,f_crude in zip(entry_crudes,entry_total_flows)]),
    "Utilitily - Crude Processing",
    )


#%%

# SOLVER

model.writeLP("Crude_Optimization_model.lp")

model.solve()

# The status of the solution is printed to the screen
print("Status:", pulp.LpStatus[model.status])

# Each of the variables is printed with it's resolved optimum value
for v in model.variables():
    print(v.name, "=", v.varValue)


# The optimised objective function value is printed to the screen
print("Total Opereation Utility = ", pulp.value(model.objective))
