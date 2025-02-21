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

El proyecto se centra en:

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

## 4. Estructura de los Ficheros

La organización del repositorio es la siguiente:

```
root/
│── data/  # Datos
│   └── DriverX/  # Datos del conductor X
│       └── STISIMData_Action.xlsx   # Datos de una maniobra
├── results/
│   ├── csv/      # Resultados de los mejores modelos obtenidos para cada conjunto de datos
│   ├── img/      # Imágenes sobre el análisis propio de los mejores modelos
│   │   ├── classification_report/   # Análisis del reporte de clasificación
│   │   ├── confusion_matrix/        # Análisis de la matriz de confusión
│   │   └── roc_curve/               # Análisis de la curva de ROC
│   └── models/   # Mejores modelos según F1-score para cada maniobra
├── 1. Preprocesamiento y Exploración.ipynb
├── 2. Segmentación y Modelado.ipynb
├── 3. Resultados, Análisis y Conclusiones.ipynb
├── requirements.txt
└── README.md
```

- **[`data/`](./data/)**: Contiene los directorios de cada conductor (Driver1, Driver2, etc.), cada uno con 5 ficheros Excel, uno por maniobra.
- **[`results/`](./results/)**: Contiene los resultados obtenidos de los mejores modelos para cada conjunto de datos, como los mejores modelos obtenidos para cada una de las maniobras. A su vez incluye el tipo de conjuntos de datos utilizados para cada uno de los modelos y los resultados de los modelos en formato de gráficas y métricas.
- **[`1. Preprocesamiento y Exploración.ipynb`](./1.%20Preprocesamiento%20y%20Exploración.ipynb)**: Notebook donde se realiza la carga y limpieza de datos, junto con un análisis exploratorio básico.
- **[`2. Segmentación y Modelado.ipynb`](./2.%20Segmentación%20y%20Modelado.ipynb)**: Notebook en el que se definen las ventanas temporales y se construyen los modelos de IA.
- **[`3. Resultados, Análisis y Conclusiones.ipynb`](./3.%20Resultados,%20Análisis%20y%20Conclusiones.ipynb)**: Notebook enfocado en la evaluación de los resultados, la comparación de métricas y la discusión final.
- **[`requirements.txt`](./requirements.txt)**: Notebook enfocado en la evaluación de los resultados, la comparación de métricas y la discusión final.
- **[`README.md`](./README.md)** (este fichero): Explica el contexto general, los objetivos y la estructura del proyecto.

---

## 5. Estado del Arte

Los sistemas de avanzados de asistencia (*ADAS*) al conductor están en pleno auge, siendo uno de los componentes fundamentales en los vehículos fabricados a día de hoy. Este tipo de sistemas ayudan principalmente al conductor a tener un mejor control del vehículo y del entorno durante la conducción del mismo, permitiendo disminuir el riesgo y el número de accidentes significativamente. Dentro de este tipo de sistemas, se encuentran diferentes módulos como la advertencia de colisión frontal, el freno automático de emergencia o el control de crucero adaptativo que permiten dar un soporte a la conducción del usuario, a través de la obtención de información de sensores como LiDAR o RaDAR [4].

Este tipo de sistemas de asistencia a la conducción van ligados con los sistemas autónomas para la conducción. Es por ello, que sistemas a desarrollar, como la predicción de maniobras, beneficia a estos vehículos a comprender mejor el entorno que les rodea, pudiendo tener una toma de decisiones más oportuna para cada tipo de ocasión dentro de la carretera.

En este contexto de la detección de maniobras del conductor, la discretización de datos juega un papel crucial al simplificar la complejidad inherente de las señales continuas del vehículo. Este proceso transforma señales como la velocidad, los pedales y el ángulo del volante, en representaciones discretas más manejables, permitiendo un modelado más eficiente y robusto. Como se describe en [5], la discretización se centra en la identificación de tendencias (aumento, constante, disminución) o estados (activado/desactivado) en lugar de valores precisos, lo que reduce la influencia del ruido y la complejidad computacional. Esto no solo simplifica el algoritmo de aprendizaje, en el caso descrito en el artículo, un sistema difuso evolutivo basado en la nube, sino que también facilita su implementación en sistemas embebidos con recursos limitados y permite un análisis más intuitivo del comportamiento del conductor.

A su vez, este tipo de sistemas dependen directamente del factor del tiempo, siendo necesario la comprensión de este tipo de series temporales para la disposición de los datos en todo momento. Las series temporales se definen como secuencias de datos ordenadas cronológicamente, donde las observaciones están espaciadas en intervalos de tiempo uniformes. Este tipo de serires son fundamentales en el análisis de campos, como el económico y el financiero, ya que permiten modelas y predecir comportamientos dinámicos de variables a lo largo del tiempo [1]. A su vez, el análisis de series temporales se complementa con técnicas como las ventanas deslizantes. Las ventanas deslizantes [3] son una técnica fundamental para la segmentación de datos en intervalos definidos. Estas ventanas pueden tener o no solapamiento (*overlapping*).
  - **Sin solapamiento.** Los segementos temporales son independientes y no comparten datos entre sí.
  - **Con solapamiento.** Las regiones temporales se superponen parcialmente para capturar mejor la continuidad de los patrones.

Este tipo de técnicas se aplican en áreas como el procesamiento de señales, la detección de anomalías y el aprendizaje automático, optimizando la extracción de características y la precisión de los modelos. La variación del tamaño y el solapamiento de las ventanas afecta directamente al rendimiento en tareas como la clasificación de actividades y en la predicción en datos multivariantes.

La predicción con series temporales tiene varios tipos de modelos de IA que se pueden aplicar, desde modelos de aprendizaje automático como los Random Forest (RF) o las máquinas de vectores de soporte (SVM), hasta modelos de redes neuronales como las de memoria larga a corto plazo (LSTM). Para el desarrollo de este proyecto, se ha hecho uso de los Random Forest, permitiendo una versatilidad en la creación de este tipo de modelos, al igual que el uso robusto en la toma de decisiones.

El uso de Random Forest (RF) en la clasificación de series temporales ha demostrado ser una alternativa eficaz debido a su capacidad para manejar estructuras de datos complejas y relaciones no lineales entre variables. Los modelos de RF puede aplicarse exitosamente en series temporales al incorporar enfoques adecuados de preprocesamiento, como la extracción de características relevantes mediante ventanas deslizantes [2]. A pesar de que los modelos basados en árboles de decisión no capturan directamente la dependencia temporal inherente a los datos, el uso de estrategias como la selección de atributos temporales y la agregación de múltiples predictores permite mitigar este problema. Además, este tipo de modelos es robusto frente al sobreajuste y puede manejar datos ruidosos o con valores atípicos, lo que lo convierte en una opción adecuada para escenarios donde la estabilidad y la interpretabilidad del modelo son cruciales.

Por último, destacar que para el desarrollo del proyecto, se han utilizado diversas funcionalidades, módulos y librerías de Python, desde la lectura y manipulación de los datos, hasta la creación y el análisis de los modelos.

  1. **Pandas.** Se trata de una librería para la manipulación y análisis de datos. Proporciona estructuras de datos flexibles como DataFrames y Series, que facilitan la limpieza, transformación y análisis de grandes conjuntos de datos.

  2. **NumPy.** Se trata de una librería para la computación científica. Proporciona soporte para arreglos multidimensionales y funciones matemáticas de alto rendimiento, permitiendo realizar operaciones eficientes sobre grandes volúmenes de datos numéricos.

  3. **Matplotlib.** Se trata de una librería de visualización de datos. Permite crear gráficos estáticos, animados e interactivos en diversas plataformas, ofreciendo una alta versatilidad, complementándose frecuentemente con las librerías de Pandas y NumPy para visualizar datos.

  4. **Seaborn.** Se trata de una librería basada en Matplotlib que facilita la creación de gráficos estadísticos atractivos y complejos. Ofrece una interfaz de alto nivel para dibujar gráficos informativos y visualmente atractivos, y se integra bien con los DataFrames de Pandas.

  5. **Scikit-learn.** Se trata de una librería para aprendizaje automático. Proporciona herramientas simples y eficientes para el análisis predictivo y la modelización, incluyendo algoritmos de clasificación, regresión y clustering, así como herramientas para la evaluación de modelos.

  6. **Pickle.** Se trata de un módulo de Python que permite la serialización y deserialización de objetos. Es útil para guardar estructuras de datos complejas, como modelos entrenados, de manera que se puedan cargar y utilizar en otro momento sin necesidad de volver a entrenarlos.

---

## 6. Autores del Proyecto

Este proyecto ha sido realizado para la asignatura _Aplicaciones Avanzadas de la IA_ por el _Grupo 9_:

- **Carlos Díez Fenoy - 100451342**
- **Juan Romero Sanz - 100535977**
- **Juan María Villard Bardón - 100439614**

Máster Universitario en Ingeniería Informática (2024/25)

---

## 7. Uso y Ejecución

1. **Instalación de Dependencias**  
   Es recomendable utilizar un entorno virtual (por ejemplo, `venv` o `conda`) con Python 3.7+ y las librerías `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, entre otras. De todas formas, se añaden las líneas de código necesarias para ejecutar los notebooks en los mismos.
   Para que los notebooks funcionen, es necesario ejecutar el fichero [`requirements.txt`](./requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```
2. **Estructura de Datos**  
   Verifica que los archivos Excel se encuentren en las subcarpetas Driver1, Driver2, etc., dentro de [`data/`](./data/).
3. **Ejecución de Notebooks**
   - [`1. Preprocesamiento y Exploración.ipynb`](./1.%20Preprocesamiento%20y%20Exploración.ipynb): Para limpiar y explorar los datos.
   - [`2. Segmentación y Modelado.ipynb`](./2.%20Segmentación%20y%20Modelado.ipynb): Donde se definen las ventanas temporales y se entrena el modelo de IA.
   - [`3. Resultados, Análisis y Conclusiones.ipynb`](./3.%20Resultados,%20Análisis%20y%20Conclusiones.ipynb): Para evaluar métricas, comparar estrategias (ventanas overlapping o no) y extraer conclusiones.

---

## 8. Conclusiones Generales

Este proyecto demuestra cómo, mediante un flujo de preprocesamiento, segmentación y clasificación, es posible reconocer maniobras de conducción en un entorno simulado de alta frecuencia (20 Hz). Estas técnicas, aplicadas a datos de vehículos, pueden mejorar la seguridad y la experiencia del conductor en sistemas ADAS, abriendo la puerta a desarrollos futuros que incluyan más variables (por ejemplo, datos de cámara o radares) y validaciones en condiciones reales.

A su vez, este proyecto, tras la implementación y análisis de los notebooks y los modelos desarrollados, ha concluido que las **ventanas sin solapamiento** ofrecen mejor precisión y generalización, especialmente con datos escalados, mientras que el **solapamiento mejora el rendimiento cuando se usa discretización**. Además, un **mayor tamaño de ventana** favorece la identificación de patrones al proporcionar más contexto, aunque su efecto varía según la segmentación y el tipo de escalado. Los modelos con **escalado estándar o de máximos y mínimos** superan a los basados en discretización, evitando la pérdida de información y mejorando las métricas de clasificación. En general, los modelos con **datos escalados y ventanas sin solapamiento** muestran la mejor capacidad predictiva, salvo en maniobras como *Turnings*, donde la discretización ha sido más efectiva. La combinación óptima de estas estrategias depende de cada maniobra, pero un **escalado adecuado y un tamaño de ventana suficientemente grande** son claves para mejorar la predicción.

## A. Referencias
[1] Lorenzo Pascual Caneiro and Esther Ruiz Ortega. Predicción de series temporales basada en machine learning: aplicaciones económicas y financieras. In Nuevos métodos de predicción económica con datos masivos, 189–214. Fundación de las Cajas de Ahorros (FUNCAS), 2021.

[2] Benjamin Goehry, Hui Yan, Yannig Goude, Pascal Massart, and Jean-Michel Poggi. Random forests for time series. REVSTAT-Statistical Journal, 21(2):283–302, Jun. 2023. URL: https://revstat.ine.pt/index.php/REVSTAT/article/view/400, doi:https://doi.org/10.57805/revstat.v21i2.400.

[3] Milagros Jaén-Vargas, Karla Miriam Reyes Leiva, Francisco Fernandes, Sérgio Barroso Gonçalves, Miguel Tavares Silva, Daniel Simões Lopes, and José Javier Serrano Olmedo. Effects of sliding window variation in the performance of acceleration-based human activity recognition using deep learning models. PeerJ Computer Science, 8:e1052, 2022.

[4] Bassim Abdulbaqi Jumaa, Anwaar Mousa Abdulhassan, and Ammar Mousa Abdulhassan. Advanced driver assistance system (adas): a review of systems and technologies. International Journal of Advanced Research in Computer Engineering & Technology (IJARCET), 8(6):231–4, 2019.

[5] Igor Škrjanc, Goran Andonovski, Agapito Ledezma, Oscar Sipele, Jose Antonio Iglesias, and Araceli Sanchis. Evolving cloud-based system for the recognition of drivers’ actions. Expert Systems with Applications, 99:231-238, 2018. URL: https://www.sciencedirect.com/science/article/pii/S0957417417307583, doi:https://doi.org/10.1016/j.eswa.2017.11.008.
