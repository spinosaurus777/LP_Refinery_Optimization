\* Crude_Oil_Utiliy_model *\
Maximize
Utilitily___Crude_Processing: - 200 Mass_Flows_F1 - 300 Mass_Flows_F2
 - 250 Mass_Flows_F3 - 350 Mass_Flows_F4 + 700 Mass_Flows_F43
 + 600 Mass_Flows_F44 + 400 Mass_Flows_F45 + 350 Mass_Flows_F46
 + 150 Mass_Flows_F47
Subject To
Avaliability_for_C1: Mass_Flows_Comp_F1_C1 <= 20000
Avaliability_for_C2: Mass_Flows_Comp_F2_C2 <= 30000
Avaliability_for_C3: Mass_Flows_Comp_F3_C3 <= 15000
Avaliability_for_C4: Mass_Flows_Comp_F4_C4 <= 25000
Capacity_for_C101: Mass_Flows_F15 <= 12000
Capacity_for_R101: Mass_Flows_F14 <= 15000
Capacity_for_T101: Mass_Flows_F5 + Mass_Flows_F6 + Mass_Flows_F7 <= 55000
General_Mass_Balance: Mass_Flows_F1 + Mass_Flows_F2 + Mass_Flows_F3
 + Mass_Flows_F4 - Mass_Flows_F43 - Mass_Flows_F44 - Mass_Flows_F45
 - Mass_Flows_F46 - Mass_Flows_F47 = 0
Mass_Balance_for_CG_in_D108: - Mass_Flows_Comp_F21_CG + Mass_Flows_Comp_F33_CG
 + Mass_Flows_Comp_F34_CG = 0
Mass_Balance_for_CG_in_F15_in_C101: - 0.2 Mass_Flows_Comp_F10_HO
 - 0.28 Mass_Flows_Comp_F10_LO + Mass_Flows_Comp_F15_CG = 0
Mass_Balance_for_CG_in_T104: - Mass_Flows_Comp_F15_CG + Mass_Flows_Comp_F21_CG
 = 0
Mass_Balance_for_CO_in_D111: - Mass_Flows_Comp_F24_CO + Mass_Flows_Comp_F39_CO
 + Mass_Flows_Comp_F40_CO = 0
Mass_Balance_for_CO_in_F15_in_C101: - 0.75 Mass_Flows_Comp_F10_HO
 - 0.68 Mass_Flows_Comp_F10_LO + Mass_Flows_Comp_F15_CO = 0
Mass_Balance_for_CO_in_T104: - Mass_Flows_Comp_F15_CO + Mass_Flows_Comp_F24_CO
 = 0
Mass_Balance_for_EL_in_F47_in_T102: - 0.5 Mass_Flows_Comp_F13_R
 + Mass_Flows_Comp_F47_EL = 0
Mass_Balance_for_HN_in_D101: - Mass_Flows_Comp_F5_HN + Mass_Flows_Comp_F8_HN
 + Mass_Flows_Comp_F9_HN = 0
Mass_Balance_for_HN_in_D106: - Mass_Flows_Comp_F19_HN + Mass_Flows_Comp_F29_HN
 + Mass_Flows_Comp_F30_HN = 0
Mass_Balance_for_HN_in_F14_in_R101: Mass_Flows_Comp_F14_HN
 - 0.55 Mass_Flows_Comp_F8_HN = 0
Mass_Balance_for_HN_in_F5_in_T101: - 0.2 Mass_Flows_Comp_F1_C1
 - 0.18 Mass_Flows_Comp_F2_C2 - 0.2 Mass_Flows_Comp_F3_C3
 - 0.15 Mass_Flows_Comp_F4_C4 + Mass_Flows_Comp_F5_HN = 0
Mass_Balance_for_HN_in_T103: - Mass_Flows_Comp_F14_HN + Mass_Flows_Comp_F19_HN
 - Mass_Flows_Comp_F9_HN = 0
Mass_Balance_for_HO_in_D102: Mass_Flows_Comp_F10_HO + Mass_Flows_Comp_F11_HO
 - Mass_Flows_Comp_F6_HO = 0
Mass_Balance_for_HO_in_D110: - Mass_Flows_Comp_F23_HO + Mass_Flows_Comp_F37_HO
 + Mass_Flows_Comp_F38_HO = 0
Mass_Balance_for_HO_in_F15_in_C101: - 0.05 Mass_Flows_Comp_F10_HO
 + Mass_Flows_Comp_F15_HO = 0
Mass_Balance_for_HO_in_F6_in_T101: - 0.2 Mass_Flows_Comp_F1_C1
 - 0.19 Mass_Flows_Comp_F2_C2 - 0.1 Mass_Flows_Comp_F3_C3
 - 0.15 Mass_Flows_Comp_F4_C4 + Mass_Flows_Comp_F6_HO = 0
Mass_Balance_for_HO_in_T104: - Mass_Flows_Comp_F11_HO - Mass_Flows_Comp_F15_HO
 + Mass_Flows_Comp_F23_HO = 0
Mass_Balance_for_LN_in_D101: - Mass_Flows_Comp_F5_LN + Mass_Flows_Comp_F8_LN
 + Mass_Flows_Comp_F9_LN = 0
Mass_Balance_for_LN_in_D104: - Mass_Flows_Comp_F17_LN + Mass_Flows_Comp_F25_LN
 + Mass_Flows_Comp_F26_LN = 0
Mass_Balance_for_LN_in_F14_in_R101: Mass_Flows_Comp_F14_LN
 - 0.4 Mass_Flows_Comp_F8_LN = 0
Mass_Balance_for_LN_in_F5_in_T101: - 0.1 Mass_Flows_Comp_F1_C1
 - 0.15 Mass_Flows_Comp_F2_C2 - 0.15 Mass_Flows_Comp_F3_C3
 - 0.25 Mass_Flows_Comp_F4_C4 + Mass_Flows_Comp_F5_LN = 0
Mass_Balance_for_LN_in_T103: - Mass_Flows_Comp_F14_LN + Mass_Flows_Comp_F17_LN
 - Mass_Flows_Comp_F9_LN = 0
Mass_Balance_for_LO_in_D102: Mass_Flows_Comp_F10_LO + Mass_Flows_Comp_F11_LO
 - Mass_Flows_Comp_F6_LO = 0
Mass_Balance_for_LO_in_D109: - Mass_Flows_Comp_F22_LO + Mass_Flows_Comp_F35_LO
 + Mass_Flows_Comp_F36_LO = 0
Mass_Balance_for_LO_in_F15_in_C101: - 0.04 Mass_Flows_Comp_F10_LO
 + Mass_Flows_Comp_F15_LO = 0
Mass_Balance_for_LO_in_F6_in_T101: - 0.12 Mass_Flows_Comp_F1_C1
 - 0.08 Mass_Flows_Comp_F2_C2 - 0.2 Mass_Flows_Comp_F3_C3
 - 0.05 Mass_Flows_Comp_F4_C4 + Mass_Flows_Comp_F6_LO = 0
Mass_Balance_for_LO_in_T104: - Mass_Flows_Comp_F11_LO - Mass_Flows_Comp_F15_LO
 + Mass_Flows_Comp_F22_LO = 0
Mass_Balance_for_MN_in_D101: - Mass_Flows_Comp_F5_MN + Mass_Flows_Comp_F8_MN
 + Mass_Flows_Comp_F9_MN = 0
Mass_Balance_for_MN_in_D105: - Mass_Flows_Comp_F18_MN + Mass_Flows_Comp_F27_MN
 + Mass_Flows_Comp_F28_MN = 0
Mass_Balance_for_MN_in_F14_in_R101: Mass_Flows_Comp_F14_MN
 - 0.48 Mass_Flows_Comp_F8_MN = 0
Mass_Balance_for_MN_in_F5_in_T101: - 0.2 Mass_Flows_Comp_F1_C1
 - 0.25 Mass_Flows_Comp_F2_C2 - 0.1 Mass_Flows_Comp_F3_C3
 - 0.2 Mass_Flows_Comp_F4_C4 + Mass_Flows_Comp_F5_MN = 0
Mass_Balance_for_MN_in_T103: - Mass_Flows_Comp_F14_MN + Mass_Flows_Comp_F18_MN
 - Mass_Flows_Comp_F9_MN = 0
Mass_Balance_for_RG_in_D107: - Mass_Flows_Comp_F20_RG + Mass_Flows_Comp_F31_RG
 + Mass_Flows_Comp_F32_RG = 0
Mass_Balance_for_RG_in_F14_in_R101: Mass_Flows_Comp_F14_RG
 - 0.45 Mass_Flows_Comp_F8_HN - 0.6 Mass_Flows_Comp_F8_LN
 - 0.52 Mass_Flows_Comp_F8_MN = 0
Mass_Balance_for_RG_in_T103: - Mass_Flows_Comp_F14_RG + Mass_Flows_Comp_F20_RG
 = 0
Mass_Balance_for_R_in_D103: Mass_Flows_Comp_F12_R + Mass_Flows_Comp_F13_R
 - Mass_Flows_Comp_F7_R = 0
Mass_Balance_for_R_in_D112: - Mass_Flows_Comp_F12_R - Mass_Flows_Comp_F16_R
 + Mass_Flows_Comp_F41_R + Mass_Flows_Comp_F42_R = 0
Mass_Balance_for_R_in_F16_in_T102: - 0.5 Mass_Flows_Comp_F13_R
 + Mass_Flows_Comp_F16_R = 0
Mass_Balance_for_R_in_F7_in_T101: - 0.13 Mass_Flows_Comp_F1_C1
 - 0.12 Mass_Flows_Comp_F2_C2 - 0.05 Mass_Flows_Comp_F3_C3
 - 0.05 Mass_Flows_Comp_F4_C4 + Mass_Flows_Comp_F7_R = 0
Maximum_EL_production: Mass_Flows_Comp_F47_EL <= 1500
Maximun_vapour_pressure_of_JF: Mass_Flows_Comp_F35_LO
 + 0.6 Mass_Flows_Comp_F37_HO + 1.5 Mass_Flows_Comp_F39_CO
 + 0.05 Mass_Flows_Comp_F41_R - Mass_Flows_Comp_F45_JF <= 0
Minimum_EL_production: Mass_Flows_Comp_F47_EL >= 500
Minimun_octane_for_PrG: 90 Mass_Flows_Comp_F25_LN + 80 Mass_Flows_Comp_F27_MN
 + 70 Mass_Flows_Comp_F29_HN + 115 Mass_Flows_Comp_F31_RG
 + 105 Mass_Flows_Comp_F33_CG - 94 Mass_Flows_Comp_F43_PrG >= 0
Minimun_octane_for_ReG: 90 Mass_Flows_Comp_F26_LN + 80 Mass_Flows_Comp_F28_MN
 + 70 Mass_Flows_Comp_F30_HN + 115 Mass_Flows_Comp_F32_RG
 + 105 Mass_Flows_Comp_F34_CG - 84 Mass_Flows_Comp_F44_ReG >= 0
Proportion_of_CO_in_Fueloil_mixing: - Mass_Flows_Comp_F40_CO
 + 0.24 Mass_Flows_Comp_F46_FO = 0
Proportion_of_HO_in_Fueloil_mixing: - Mass_Flows_Comp_F38_HO
 + 0.16 Mass_Flows_Comp_F46_FO = 0
Proportion_of_LO_in_Fueloil_mixing: - Mass_Flows_Comp_F36_LO
 + 0.55 Mass_Flows_Comp_F46_FO = 0
Proportion_of_R_in_Fueloil_mixing: - Mass_Flows_Comp_F42_R
 + 0.05 Mass_Flows_Comp_F46_FO = 0
Ratio_PrG_and_ReG: Mass_Flows_Comp_F43_PrG - 0.4 Mass_Flows_Comp_F44_ReG <= 0
Sum_of_component_flows_for_F1: - Mass_Flows_Comp_F1_C1 + Mass_Flows_F1 = 0
Sum_of_component_flows_for_F10: - Mass_Flows_Comp_F10_HO
 - Mass_Flows_Comp_F10_LO + Mass_Flows_F10 = 0
Sum_of_component_flows_for_F11: - Mass_Flows_Comp_F11_HO
 - Mass_Flows_Comp_F11_LO + Mass_Flows_F11 = 0
Sum_of_component_flows_for_F12: - Mass_Flows_Comp_F12_R + Mass_Flows_F12 = 0
Sum_of_component_flows_for_F13: - Mass_Flows_Comp_F13_R + Mass_Flows_F13 = 0
Sum_of_component_flows_for_F14: - Mass_Flows_Comp_F14_HN
 - Mass_Flows_Comp_F14_LN - Mass_Flows_Comp_F14_MN - Mass_Flows_Comp_F14_RG
 + Mass_Flows_F14 = 0
Sum_of_component_flows_for_F15: - Mass_Flows_Comp_F15_CG
 - Mass_Flows_Comp_F15_CO - Mass_Flows_Comp_F15_HO - Mass_Flows_Comp_F15_LO
 + Mass_Flows_F15 = 0
Sum_of_component_flows_for_F16: - Mass_Flows_Comp_F16_R + Mass_Flows_F16 = 0
Sum_of_component_flows_for_F17: - Mass_Flows_Comp_F17_LN + Mass_Flows_F17 = 0
Sum_of_component_flows_for_F18: - Mass_Flows_Comp_F18_MN + Mass_Flows_F18 = 0
Sum_of_component_flows_for_F19: - Mass_Flows_Comp_F19_HN + Mass_Flows_F19 = 0
Sum_of_component_flows_for_F2: - Mass_Flows_Comp_F2_C2 + Mass_Flows_F2 = 0
Sum_of_component_flows_for_F20: - Mass_Flows_Comp_F20_RG + Mass_Flows_F20 = 0
Sum_of_component_flows_for_F21: - Mass_Flows_Comp_F21_CG + Mass_Flows_F21 = 0
Sum_of_component_flows_for_F22: - Mass_Flows_Comp_F22_LO + Mass_Flows_F22 = 0
Sum_of_component_flows_for_F23: - Mass_Flows_Comp_F23_HO + Mass_Flows_F23 = 0
Sum_of_component_flows_for_F24: - Mass_Flows_Comp_F24_CO + Mass_Flows_F24 = 0
Sum_of_component_flows_for_F25: - Mass_Flows_Comp_F25_LN + Mass_Flows_F25 = 0
Sum_of_component_flows_for_F26: - Mass_Flows_Comp_F26_LN + Mass_Flows_F26 = 0
Sum_of_component_flows_for_F27: - Mass_Flows_Comp_F27_MN + Mass_Flows_F27 = 0
Sum_of_component_flows_for_F28: - Mass_Flows_Comp_F28_MN + Mass_Flows_F28 = 0
Sum_of_component_flows_for_F29: - Mass_Flows_Comp_F29_HN + Mass_Flows_F29 = 0
Sum_of_component_flows_for_F3: - Mass_Flows_Comp_F3_C3 + Mass_Flows_F3 = 0
Sum_of_component_flows_for_F30: - Mass_Flows_Comp_F30_HN + Mass_Flows_F30 = 0
Sum_of_component_flows_for_F31: - Mass_Flows_Comp_F31_RG + Mass_Flows_F31 = 0
Sum_of_component_flows_for_F32: - Mass_Flows_Comp_F32_RG + Mass_Flows_F32 = 0
Sum_of_component_flows_for_F33: - Mass_Flows_Comp_F33_CG + Mass_Flows_F33 = 0
Sum_of_component_flows_for_F34: - Mass_Flows_Comp_F34_CG + Mass_Flows_F34 = 0
Sum_of_component_flows_for_F35: - Mass_Flows_Comp_F35_LO + Mass_Flows_F35 = 0
Sum_of_component_flows_for_F36: - Mass_Flows_Comp_F36_LO + Mass_Flows_F36 = 0
Sum_of_component_flows_for_F37: - Mass_Flows_Comp_F37_HO + Mass_Flows_F37 = 0
Sum_of_component_flows_for_F38: - Mass_Flows_Comp_F38_HO + Mass_Flows_F38 = 0
Sum_of_component_flows_for_F39: - Mass_Flows_Comp_F39_CO + Mass_Flows_F39 = 0
Sum_of_component_flows_for_F4: - Mass_Flows_Comp_F4_C4 + Mass_Flows_F4 = 0
Sum_of_component_flows_for_F40: - Mass_Flows_Comp_F40_CO + Mass_Flows_F40 = 0
Sum_of_component_flows_for_F41: - Mass_Flows_Comp_F41_R + Mass_Flows_F41 = 0
Sum_of_component_flows_for_F42: - Mass_Flows_Comp_F42_R + Mass_Flows_F42 = 0
Sum_of_component_flows_for_F43: - Mass_Flows_Comp_F43_PrG + Mass_Flows_F43 = 0
Sum_of_component_flows_for_F44: - Mass_Flows_Comp_F44_ReG + Mass_Flows_F44 = 0
Sum_of_component_flows_for_F45: - Mass_Flows_Comp_F45_JF + Mass_Flows_F45 = 0
Sum_of_component_flows_for_F46: - Mass_Flows_Comp_F46_FO + Mass_Flows_F46 = 0
Sum_of_component_flows_for_F47: - Mass_Flows_Comp_F47_EL + Mass_Flows_F47 = 0
Sum_of_component_flows_for_F5: - Mass_Flows_Comp_F5_HN - Mass_Flows_Comp_F5_LN
 - Mass_Flows_Comp_F5_MN + Mass_Flows_F5 = 0
Sum_of_component_flows_for_F6: - Mass_Flows_Comp_F6_HO - Mass_Flows_Comp_F6_LO
 + Mass_Flows_F6 = 0
Sum_of_component_flows_for_F7: - Mass_Flows_Comp_F7_R + Mass_Flows_F7 = 0
Sum_of_component_flows_for_F8: - Mass_Flows_Comp_F8_HN - Mass_Flows_Comp_F8_LN
 - Mass_Flows_Comp_F8_MN + Mass_Flows_F8 = 0
Sum_of_component_flows_for_F9: - Mass_Flows_Comp_F9_HN - Mass_Flows_Comp_F9_LN
 - Mass_Flows_Comp_F9_MN + Mass_Flows_F9 = 0
End
