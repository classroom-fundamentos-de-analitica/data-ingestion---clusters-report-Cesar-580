import re
# cadena = "   Hola   mundo. Este es un    ejemplo.    "

# cadena_corregida = re.sub(r"\s+", "_", cadena).strip()

# print(cadena_corregida)

pattern = r"([A-Z])"
text = "Cluster  Cantidad de     Porcentaje de   Principales palabras clave "

# re.split(pattern, text)

print(re.split(pattern, text))