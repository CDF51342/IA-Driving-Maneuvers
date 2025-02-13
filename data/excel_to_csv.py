import pandas as pd
import os
import sys

def excel_to_csv(file_path):
    try:
        # Cargar el archivo Excel
        xls = pd.ExcelFile(file_path)
        
        # Verificar si la hoja "Data" existe
        if "Data" not in xls.sheet_names:
            print("La hoja 'Data' no existe en el archivo Excel.")
            return
        
        # Leer la hoja "Data"
        df = pd.read_excel(file_path, sheet_name="Data")
        
        # Construir la ruta del archivo CSV de salida
        csv_path = os.path.splitext(file_path)[0] + ".csv"
        
        # Guardar el DataFrame en un archivo CSV
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"Archivo CSV guardado en: {csv_path}")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <ruta/al/archivo.xlsx>")
    else:
        file_path = sys.argv[1]
        excel_to_csv(file_path)
