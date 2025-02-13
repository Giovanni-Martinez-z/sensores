import numpy as np

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Generar datos aleatorios de temperatura (en °C) para 3 sensores (7 días x 24 horas)
# Suponemos que la temperatura oscila entre 15°C y 30°C
datos_sensores = np.random.uniform(low=15, high=30, size=(3, 7, 24))

# Mostrar una muestra de datos del primer día
print("Datos del primer día para el Sensor 1:")
print(datos_sensores[0, 0, :])  # Primer sensor, primer día, todas las horas

# Seleccionar los datos del primer sensor (índice 0)
sensor_1 = datos_sensores[0, :, :]  # Forma (7, 24)
sensor_2 = datos_sensores[1, :, :]  # Forma (7, 24)
sensor_3 = datos_sensores[2, :, :]  # Forma (7, 24)


# Aplanar los datos del primer sensor
sensor_1_flat = sensor_1.ravel()
sensor_2_flat = sensor_1.ravel()
sensor_3_flat = sensor_1.ravel()


# Mostrar el arreglo aplanado
print("Datos aplanados del primer sensor:")
print(sensor_1_flat)
print("\nForma del arreglo aplanado 1:", sensor_1_flat.shape)
print("\nForma del arreglo aplanado 2:", sensor_2_flat.shape)
print("\nForma del arreglo aplanado 3:", sensor_3_flat.shape)


# datos_concatenados = np.concatenate((sensor_1_flat, sensor_2.flatten(), sensor_3.flatten()))
# Concatenar los datos de los 3 sensores
datos_concatenados = np.concatenate((sensor_1_flat, sensor_2_flat, sensor_3_flat))

# Mostrar los datos concatenados
print("Datos concatenados de los 3 sensores:")
print(datos_concatenados)
print("\nForma del arreglo concatenado:", datos_concatenados.shape)



# Mostrar del primer dia, las primeras dos horas de los 3 sensores
#datos_sensores.transpose(1, 2, 0): Usamos transpose para cambiar el orden de los ejes.
#Originalmente, datos_sensores tiene forma (3, 7, 24) (3 sensores, 7 días, 24 horas).
#Al transponer con (1, 2, 0), cambiamos el orden a (7, 24, 3) (7 días, 24 horas, 3 sensores).
#Esto es equivalente a np.reshape(), pero transpose es más adecuado para reordenar ejes.


# Reorganizar los datos en una matriz de forma (7 días, 24 horas, 3 sensores)
datos_reorganizados = datos_sensores.transpose(1, 2, 0)  # Cambiar el orden de los ejes

# Mostrar la forma de la matriz reorganizada
print("Forma de la matriz reorganizada:", datos_reorganizados.shape)

# Mostrar los datos del primer día, las primeras dos horas de los 3 sensores
print("\nDatos del primer día, primeras dos horas de los 3 sensores:")
print(datos_reorganizados[0, :2, :])  # Primer día (0), primeras dos horas (:2), todos los sensores (:)


# Temperatura del sensor 2, día 3, hora 12


# Datos del día 5 para todos los sensores

# Extraer la temperatura del sensor 2, día 3, hora 12
temperatura_sensor2_dia3_hora12 = datos_reorganizados[2, 12, 1]  # Día 3 (índice 2), hora 12 (índice 12), sensor 2 (índice 1)
print("Temperatura del sensor 2, día 3, hora 12:", temperatura_sensor2_dia3_hora12, "°C")

# Extraer los datos del día 5 para todos los sensores
datos_dia5 = datos_reorganizados[4, :, :]  # Día 5 (índice 4), todas las horas (:), todos los sensores (:)
print("\nDatos del día 5 para todos los sensores:")
print(datos_dia5)