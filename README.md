# PRÁCTICA 1

IA en la Industria Automotriz  
Aplicaciones Avanzadas de la IA  
Máster Universitario en Ingeniería Informática (2024/25)

---

## 1. Introducción

Este repositorio corresponde a la **Práctica 1** de la asignatura _Aplicaciones Avanzadas de la IA_ del Máster Universitario en Ingeniería Informática (curso 2024/25). El objetivo de la práctica es estudiar y reconocer maniobras de conducción mediante técnicas de IA, partiendo de datos capturados en un simulador que registra 20 muestras por segundo.

Las maniobras a identificar incluyen adelantamientos, giros y detenciones, entre otras. Se trabaja con señales básicas del vehículo (velocidad, ángulo de volante, estado de pedales, etc.) y un marcador que indica si la maniobra está activa (1) o no (0) en cada instante.

---

## 2. Contexto del Problema

En los **Sistemas Avanzados de Asistencia al Conductor (ADAS)** es fundamental anticipar y detectar las acciones del conductor para mejorar la seguridad y la experiencia de conducción. Con ese fin, disponemos de datos simulados en los que cada registro incluye:

- Velocidad, RPM, marcha y ángulo del volante.
- Posición de los pedales (acelerador, freno y embrague).
- La columna _Maneuver marker flag_ para señalar si la maniobra está activa (1) o inactiva (0).

Nuestro trabajo se centra en:

1. Preprocesar y limpiar estos datos para eliminar información irrelevante o ruido.
2. Segmentar los registros en ventanas temporales (con o sin solapamiento).
3. Entrenar y validar un modelo de IA que clasifique la maniobra de conducción en cada ventana.

---

## 3. Objetivos de la Práctica

1. **Preprocesar y explorar** los datos de simulación, garantizando la selección de columnas relevantes y la integridad de la información.
2. **Segmentar** las señales en ventanas temporales, con y sin overlapping, para capturar la dinámica de cada maniobra.
3. **Desarrollar un modelo** capaz de identificar, en cada ventana, qué maniobra se realiza (o si no hay maniobra activa).
4. **Comparar** distintos tamaños de ventana y configuraciones de solapamiento.
5. **Analizar** las métricas de rendimiento obtenidas y plantear mejoras o ajustes futuros.

---

## 4. Estructura de los Ficheros # TODO - REVISAR ESTO

La organización del repositorio es la siguiente:

- **`data/`**  
  Contiene las subcarpetas para cada conductor (Driver1, Driver2, etc.), cada una con 5 ficheros Excel, uno por maniobra.
- **`1. Preprocesamiento y Exploración.ipynb`**  
  Notebook donde se realiza la carga y limpieza de datos, junto con un análisis exploratorio básico.
- **`2. Segmentación y Modelado.ipynb`**  
  Notebook en el que se definen las ventanas temporales y se construyen los modelos de IA.
- **`3. Resultados, Análisis y Conclusiones.ipynb`**  
  Notebook enfocado en la evaluación de los resultados, la comparación de métricas y la discusión final.
- **`README.md`** (este archivo)  
  Explica el contexto general, los objetivos y la estructura del proyecto.
- (De forma opcional) **Scripts o notebooks auxiliares** si es necesario realizar tareas específicas adicionales.

---

## 5. Estado del Arte # TODO - REVISAR ESTO

La identificación de maniobras de conducción es un área activa de investigación, particularmente para el desarrollo de ADAS que mejoren la seguridad vial. Se han empleado diversos enfoques, entre los que destacan:

- **Modelos de aprendizaje automático** (SVM, Random Forest, redes neuronales, etc.) para detectar patrones en los datos de conducción.
- **Sistemas basados en lógica difusa y métodos evolutivos**, que pueden adaptarse a los cambios de comportamiento del conductor de forma continua.
- **Técnicas de series temporales**, que consideran la evolución en el tiempo de variables como la velocidad, el ángulo de giro y las transiciones de marcha.

En los notebooks se citan algunos artículos y referencias que sustentan este enfoque.

---

## 6. Redactores de la Práctica

Este proyecto ha sido realizado para la asignatura _Aplicaciones Avanzadas de la IA_ por el _Grupo 9_:

- **Carlos Díez Fenoy - 100451342**
- **Juan Romero Sanz - 100535977**
- **Juan María Villard Bardón - 100439614**

Máster Universitario en Ingeniería Informática (2024/25)

---

## 7. Uso y Ejecución

1. **Instalación de Dependencias**  
   Es recomendable utilizar un entorno virtual (por ejemplo, `venv` o `conda`) con Python 3.7+ y las librerías `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, entre otras. De todas formas, añadimos las líneas de código necesarias para ejecutar los notebooks en los mismos.
2. **Estructura de Datos**  
   Verifica que los archivos Excel se encuentren en las subcarpetas Driver1, Driver2, etc., dentro de `data/`.
3. **Ejecución de Notebooks**
   - `1. Preprocesamiento y Exploración.ipynb`: Para limpiar y explorar los datos.
   - `2. Segmentación y Modelado.ipynb`: Donde se definen las ventanas temporales y se entrena el modelo de IA.
   - `3. Resultados, Análisis y Conclusiones.ipynb`: Para evaluar métricas, comparar estrategias (ventanas overlapping o no) y extraer conclusiones.

---

## 8. Conclusiones Generales

Este proyecto demuestra cómo, mediante un flujo de preprocesamiento, segmentación y clasificación, es posible reconocer maniobras de conducción en un entorno simulado de alta frecuencia (20 Hz). Estas técnicas, aplicadas a datos de vehículos, pueden mejorar la seguridad y la experiencia del conductor en sistemas ADAS, abriendo la puerta a desarrollos futuros que incluyan más variables (por ejemplo, datos de cámara o radares) y validaciones en condiciones reales.
