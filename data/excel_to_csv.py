import pandas as pd
import os
import sys

def excel_to_csv(file_path):
    try:
        # Lee la primera hoja llamada "Data"
        df = pd.read_excel(file_path, sheet_name='Data')
        
        # Construye la ruta del archivo CSV de salida
        csv_path = os.path.splitext(file_path)[0] + '.csv'
        
        # Guarda el DataFrame en un archivo CSV
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f'Archivo CSV guardado con éxito.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python3 excel_to_csv.py <ruta/al/archivo.xlsx>')
    else:
        file_path = sys.argv[1]
        excel_to_csv(file_path)
