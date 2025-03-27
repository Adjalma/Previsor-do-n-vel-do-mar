import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', alpha=0.5)
    
    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Calcula a linha de regressão
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Cria array de anos até 2050
    years_extended = np.arange(1880, 2051)
    line_of_best_fit = slope * years_extended + intercept
    
    # Plota a primeira linha de regressão
    plt.plot(years_extended, line_of_best_fit, 'r', label='1880-2050 trend')
    
    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    x_recent = recent_data['Year']
    y_recent = recent_data['CSIRO Adjusted Sea Level']
    
    # Calcula a linha de regressão para dados recentes
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(x_recent, y_recent)
    
    # Cria array de anos de 2000 até 2050
    years_extended_recent = np.arange(2000, 2051)
    line_of_best_fit_recent = slope_recent * years_extended_recent + intercept_recent
    
    # Plota a segunda linha de regressão
    plt.plot(years_extended_recent, line_of_best_fit_recent, 'g', label='2000-2050 trend')
    
    # Configuração do gráfico
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Salva o gráfico
    plt.savefig('sea_level_plot.png')
    
    # Retorna o objeto da figura
    return plt.gca() 
