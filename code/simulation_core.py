import numpy as np
import pandas as pd

# Энергетические коэффициенты
coeff_cpu = 0.5
coeff_mem = 0.1
coeff_io = 0.05

def calculate_energy_and_emissions(df):
    df["cpu_energy_wh"] = df["cpu_demand"] * coeff_cpu
    df["memory_energy_wh"] = df["memory_demand"] * coeff_mem
    df["io_energy_wh"] = df["io_operations"] * coeff_io
    df["total_energy_wh"] = df["cpu_energy_wh"] + df["memory_energy_wh"] + df["io_energy_wh"]
    df["carbon_emission_g"] = df["total_energy_wh"] * df["carbon_intensity"]
    return df
