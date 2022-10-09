# Cargo la versión master de alex para ver si vuelvo a ponerme al día
git remote add origin https://github.com/pgasane/gh-master-oct.git
git branch -M main
git push -u origin main

# Me ha dado error "no encuentro main"
# Intento hacerlo desde la utilidad gráfica
Ha funcionado hacer el commit desde la utilidad gráfica y el commit desde consola

# Sigo el vídeo
Hago commit de pyproject.toml e __init.py__ de modeltools
Hago commit indicando "Estructura Básica"

# modeltools
Su utilidad es tener helpers (funciones auxiliadres) para hacer cosas que no hace sklearn
Hago commit y push de: poetry.lock (generado con el comando poetry add numpy y poetry build), preprocessing.py y pyproject.toml

# Ejecuto poetry build
Se genera la carpeta dist con los binarios necesarios para luego hacer las releases
No hacemos commit ni push

# Etiquetas, Releases y Versiones

