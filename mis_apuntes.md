# Cargo la versión master de alex para ver si vuelvo a ponerme al día
git remote add origin https://github.com/pgasane/gh-master-oct.git
git branch -M main
git push -u origin main

# Me ha dado error "no encuentro main"
# Intento hacerlo desde la utilidad gráfica

# Tutoria
git branch nombre-branch # crear rama
git log # ver commit desde ahora al pasado
git checkout id-rama # moverte de una rama a otra
git checkout codigo-commit # moverte de un commit a otro
git reset --hard HEAD # BORRAR todo hasta el último commit subido. Para volver al último punto confirmado
git clean -f -d # Limpiar lo que no está incluido en un commit
Más info sobre gestión de ramas: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%C3%B3n-de-Ramas#r_branch_management

# TERMINAL TUTORIA
source /opt/conda/bin/activate
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ source /opt/conda/bin/activate
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git log
commit a202caeb663b4a2d55eef596512dc0e2a68b7150 (HEAD -> main, origin/main)
Author: Your Name <you@example.com>
Date:   Sun Oct 9 11:42:22 2022 +0000

    Siguiente paso Release. Espero Tutoría

commit d5a47f900d8c16462183888244d9c2670ee6bcf2
Author: Your Name <you@example.com>
Date:   Sun Oct 9 11:07:46 2022 +0000

    Declaración de dependencias

commit 6a1eb7d6aba30f2a033e3d9ab88757feb0b33f4c
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:48:57 2022 +0000

    Estructura Básica

commit fcb9a0ebabc5e087334ddb8a10f47a663267188e
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:44:43 2022 +0000

    Subimos pyproject.toml e __init__.py

commit d4b98a1480f7b32a9606d2f74aa7224c4bb292e3
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:34:17 2022 +0000

    Se crea carpeta docs y se mueve mis_apuntes.md

commit 8c6710b05677e6b9c169ee8112793ce10c4ef9a2 (tag: list)
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ 
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git chekout 6a1eb7d6aba30f2a033e3d9ab88757feb0b33f4c
git: 'chekout' is not a git command. See 'git --help'.

The most similar command is
        checkout
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git checkout 6a1eb7d6aba30f2a033e3d9ab88757feb0b33f4c
M       .DS_Store
D       mis_apuntes.md
Note: switching to '6a1eb7d6aba30f2a033e3d9ab88757feb0b33f4c'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 6a1eb7d Estructura Básica
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git log
commit 6a1eb7d6aba30f2a033e3d9ab88757feb0b33f4c (HEAD)
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:48:57 2022 +0000

    Estructura Básica

commit fcb9a0ebabc5e087334ddb8a10f47a663267188e
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:44:43 2022 +0000

    Subimos pyproject.toml e __init__.py

commit d4b98a1480f7b32a9606d2f74aa7224c4bb292e3
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:34:17 2022 +0000

    Se crea carpeta docs y se mueve mis_apuntes.md

commit 8c6710b05677e6b9c169ee8112793ce10c4ef9a2 (tag: list)
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:12:49 2022 +0000

    Primer Commit desde master
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git branch pruebas
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git log
commit 6a1eb7d6aba30f2a033e3d9ab88757feb0b33f4c (HEAD, pruebas)
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:48:57 2022 +0000

    Estructura Básica

commit fcb9a0ebabc5e087334ddb8a10f47a663267188e
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:44:43 2022 +0000

    Subimos pyproject.toml e __init__.py

commit d4b98a1480f7b32a9606d2f74aa7224c4bb292e3
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:34:17 2022 +0000

    Se crea carpeta docs y se mueve mis_apuntes.md

commit 8c6710b05677e6b9c169ee8112793ce10c4ef9a2 (tag: list)
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:12:49 2022 +0000

    Primer Commit desde master
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git checkout main
M       .DS_Store
D       mis_apuntes.md
Previous HEAD position was 6a1eb7d Estructura Básica
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git log
commit a202caeb663b4a2d55eef596512dc0e2a68b7150 (HEAD -> main, origin/main)
Author: Your Name <you@example.com>
Date:   Sun Oct 9 11:42:22 2022 +0000

    Siguiente paso Release. Espero Tutoría

commit d5a47f900d8c16462183888244d9c2670ee6bcf2
Author: Your Name <you@example.com>
Date:   Sun Oct 9 11:07:46 2022 +0000

    Declaración de dependencias

commit 6a1eb7d6aba30f2a033e3d9ab88757feb0b33f4c (pruebas)
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:48:57 2022 +0000

    Estructura Básica

commit fcb9a0ebabc5e087334ddb8a10f47a663267188e
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:44:43 2022 +0000

    Subimos pyproject.toml e __init__.py

commit d4b98a1480f7b32a9606d2f74aa7224c4bb292e3
Author: Your Name <you@example.com>
Date:   Sun Oct 9 10:34:17 2022 +0000

    Se crea carpeta docs y se mueve mis_apuntes.md

commit 8c6710b05677e6b9c169ee8112793ce10c4ef9a2 (tag: list)
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git reset --hard HEAD
HEAD is now at a202cae Siguiente paso Release. Espero Tutoría
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ LS
bash: LS: command not found
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ ls -l
total 40
drwxr-xr-x 4 jovyan users   128 Oct  9 11:47  dist
drwxr-xr-x 4 jovyan users   128 Oct 11 07:10  docs
-rw-r--r-- 1 jovyan users   296 Oct 11 07:15  hoy
-rw-rw-r-- 1 jovyan users  1687 Oct  3 19:26 'instrucciones github.md'
-rw-rw-r-- 1 jovyan users   743 Oct  3 19:26  instrucciones.md
-rw-r--r-- 1 jovyan users   266 Oct 11 07:16  mis_apuntes.md
drwxr-xr-x 5 jovyan users   160 Oct 11 07:10  modeltools
-rw-r--r-- 1 jovyan users 15627 Oct 11 07:10  poetry.lock
-rw-r--r-- 1 jovyan users   333 Oct 11 07:16  pyproject.toml
-rw-rw-r-- 1 jovyan users    56 Oct  3 19:26  README.md
drwxr-xr-x 4 jovyan users   128 Oct  9 09:49  tests
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git clean -f -d
Removing .github/.DS_Store
Removing hoy
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   mis_apuntes.md

no changes added to commit (use "git add" and/or "git commit -a")
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git tag -a "v0.2.2" -m "Publicada v0.2.2"
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ git push --follow-tags
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 162 bytes | 20.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:pgasane/gh-master-oct.git
 * [new tag]         v0.2.2 -> v0.2.2
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ 

# SESIÓN DEL 03.10.2022
- WORKFLOWS se pueden ejecutar en paralelo
- STEPS se ejecutan SIEMPRE dentro de un workflow y SIEMPRE son secuenciales
- Para ver que la carpeta dist se crea al ejecutar poetry build desde la ruta del workspace( ${{ github.workspace }} )
- Subimos lo que se ha trabajado hasta ahora:
    - git add .github/workflows/build.yml
    - git commit -m "Se añade el paso Publish Releases en Building del build.yml"
    - git push
# "gh run list" nos muestra la lista de commit que se han hecho
- Uso de los parámetros name y tag_name en softpropss/actions-gh-release: se hizo por que se generaba un error al usar el action-hg-release. Pero lo que se quiere en que se carge solo
- por lo que seguimos viendo el vídeo

# LAS ETIQUETAS SE USAN PARA MARCAR LOS COMMIT QUE SUPONEN AUMENTO DE VERSIÓN
- La ETIQUETA se incluye en el mismo commit con el que se sube todo el código realizado que supone el aumento de versión
- Las ETIQUETAS NO SE PUEDEN CAMBIAR NUNCA. Si se hace, se generan ERRORES en el GITHUB
- Una RELEASE es una versión que está PERFECTA para ponerla en PRODUCCIÓN
- Pasos:
    - Se modifica el atributo que indica la nueva versión (version = "0.2.0") en el pyproject.toml
    - Hacemos un commit de todo el código que supone la nueva versión
    - Usamos una ETIQUETA ANOTADA:
        - git tag -a v0.2.0 -m "Etiquetado de la v0.2.0"
        - git tag # Comprobamos que la tag está creada
        - git log # Comprobamos que el commit se ha realizado con la tag especificada
    - git push --follow-tags # Revisa todos los commit de hoy al pasado y si los encuentra los publica. Solo funciona con las ETIQUETAS ANOTADAS
    - git config --global push.followTags true # convierte el push normal en followTags por defecto

# Ejercicio: creamos la versión v0.2.3
- Modificamos el pyproject.toml para añadir la nueva versión (version = "v0.2.3")
- Hacemos el commit de todo el código implicado en la nueva versión v0.2.3
    - Se hace el commit desde la utilidad del Visual Code
    - Se añade pyproject.toml y mis_apuntes.md
- Creamos la nueva etiqueta anotada:
    - git tag -a v0.2.3 -m "v0.2.3"
    - git tag  # comprobación
    - git log  # comprobación de commits realizados
- git push --follow-tags

# HACEMOS UN COMMIT QUE NO GENERE UNA RELEASE
name: Building    # Nombre del workflow "Workflows define the jobs and steps that constitute build processes." (https://www.ibm.com/docs/en/urbancode-build/6.1.0?topic=creating-jobs-workflows)
on:               # Se ejecuta...
  push:           # cada vez que hago un PUSH...
    tags:         # con una etiqueta que empieza por "v"
      - "v*.*.*"  # Este on solo se ejecuta cuando hay etiqueta CON EL FORMATO "v*.*.*"
# Con el código anterior conseguimos que solo se ejecute el paso BUILDING cuando se ha definido una ETIQUETA ANOTADA con el formato "v*.*.*"

# Creo una nueva Release v0.2.5 porque había un fallo en el build (el punto dichoso al final) que ha impedido que se crearan los binarios
- El proceso a terminado correctamente.

# ERROR DE ARRASTRE DE VERSIONES COPIADAS DESDE LA RUTA /DIST/*
- Dentro del git solo debe haber código
- Si existen, se deben borrar
- Desde consola: git rm dist/*. # en el próximo commit se eliminan del repositorio (ojo, no de cada RELEASE)
- Desde interfaz git: botón derecho, eliminar definitivamente
- Forma Correcta:
    - Se crea el archivo .gitignore y se indica la ruta que queremos ignorar (en nuestro caso dist/*)
    - La comunidad ha creado .gitignore para infinidad de entornos que están disponibles aquí: github.com/github/gitignore
    - Buscamos el .gitignore para Python y lo copiamos

# USAR LOS PAQUETES DE DISTRIBUCIÓN PARA INSTALAR EL MODELO
- https://github.com/pgasane/gh-master-oct/releases/download/v0.2.5/modeltools-0.2.5-py3-none-any.whl
- La URL anterior se puede incluir como dependencia de nuestro proyecto para que se pueda instalar al pulsar sobre el mismo
- Sin embargo, este método es muy débil porque con un mínimo fallo hace que el paquete quede inservible

# GENERAR TESTING PARA LOS PROYECTOS
- Los TESTs se ponen en la carpeta TEST
- Los TESTs se usan para comprobar que el código hace lo que tiene que hacer
- Creamos un nuevo aricho de test dentro del directorio TEST
- Los TESTS deben estar fuera de la carpeta del proyecto (modeltools)
- Los TESTS solo se ejecutan en el BUILDING
- Creamos el archivo __init__.py dentro de la carpeta TESTS
- Por cada fichero en la carpeta del proyecto (modeltools) creamos un fichero en la carpeta TEST con el formato test_nombreDelModulo.py
- En nuestro caso: test_preprocessing.py porque en modeltools tenemos preprocessing.py

# assert es "como un if" pero que falla si la condición es falsa. Esto es ideal para los tests.
- assert 1 == 1 nunca falla porque no será muy útil ya que nos interesa que si algo va mal falle
- El escribir test obliga al programador a darse cuenta del código y de la lógica que se sigue en el código
- Lo que se trata es forzar el código para detectar los fallos y corregirlos antes de pasarlo a producción
- Se recomienda usar la libreria pytest que solo se usará durante el building. Una vez creado el paquete binario, ya no es necesario.
- Instalamos pytest:
    - Definimos la dependencia desde consola: poetry add -D pytest
    - En DOCKER usamos el MAMBA para instalar PYTEST: mamba install pytest
    - Sin DOCKER usamos CONDA para instalar PYTEST: conda install -c conda-forge pytest
- PYTEST busca los test a probar y los ejecuta:
    - Muestra el número que encuentra
    - Muestra el resultado de ejecutar todos los test
    - Nota: cuando el error es "not defined" es que no la hemos importado o hemos cometido un error sintáctico

# EJEMPLO DE SALIDA FALLIDA DE LA EJECUCIÓN DE PYTEST
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ pytest
========================================================================================== test session starts ==========================================================================================
platform linux -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/jovyan/work/m02/gh-master-oct
plugins: anyio-3.6.1
collected 7 items                                                                                                                                                                                       

tests/test_preprocessing.py F......                                                                                                                                                               [100%]

=============================================================================================== FAILURES ================================================================================================
__________________________________________________________________________________ test_get_numerical_features_simple ___________________________________________________________________________________

    def test_get_numerical_features_simple():
        """En este vamos a probar que logra distinguir entre cadenas de texto y número enteros"""
    
        df = pd.DataFrame({
          "numerica": [5],
          "categorica": ["rojo"]
        })
    
        # assert es "como un if" pero que falla si la condición
        # es falsa. Esto es ideal para los tests.
        # assert 1 == 1 nunca falla porque no será muy útil ya que nos interesa que si algo va mal falle
        # El escribir test obliga al programador a darse cuenta del código y de la lógica que se sigue en el código
        # Lo que se trata es forzar el código para detectar los fallos y corregirlos antes de pasarlo a producción
        # Se recomienda usar la libreria pytest
    
        # assert get_numerical_features(df) == ["numerica"]
>       assert 1 == 2
E       assert 1 == 2

# EJEMPLO DE SALIDA CORRECTA DE LA EJECUCIÓN DE PYTEST
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ pytest -v
========================================================================================== test session starts ==========================================================================================
platform linux -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0 -- /opt/conda/bin/python
cachedir: .pytest_cache
rootdir: /home/jovyan/work/m02/gh-master-oct
plugins: anyio-3.6.1
collected 7 items                                                                                                                                                                                       

tests/test_preprocessing.py::test_get_numerical_features_simple PASSED                                                                                                                            [ 14%]
tests/test_preprocessing.py::test_get_numerical_features_empty PASSED                                                                                                                             [ 28%]
tests/test_preprocessing.py::test_get_numerical_features_zero_columns PASSED                                                                                                                      [ 42%]
tests/test_preprocessing.py::test_get_numerical_features_zero_rows PASSED                                                                                                                         [ 57%]
tests/test_preprocessing.py::test_get_numerical_features_int_and_float PASSED                                                                                                                     [ 71%]
tests/test_preprocessing.py::test_get_numerical_features_columns_withoutname PASSED                                                                                                               [ 85%]
tests/test_preprocessing.py::test_get_numerical_features_complex PASSED                                                                                                                           [100%]

=========================================================================================== 7 passed in 0.59s ===========================================================================================
(base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$     

# CONCEPTOS SOBRE EL TESTING
- Las funciones más importantes, las troncales, deben ser objetos de tests masivo
- Lo ideal es Testear TODO, pero no siempre es posible. En ese caso, se prioriza lo que hay que testear
- Hay que evitar tener Funciones Complicadas (Épicas). Es mejor trocearla
- Si el test de una función es muy complicado es que la función se debe dividir en funciones atómicas
- Pytest usa un concepto, la PARAMETRIZACIÓN, de forma que es posible en un mismo test validarlo con cada uno de los parámetros que tiene de entrada
- Pytest usa un concepto, PREPARATIVOS, FIXTURES, que prepara el ENTORNO para poder hacer el test (ejemplo: subir una base de datos)
- Metodología TDD: primero los test y, luego, el código. Se una en metodología Agile y apropiado para implementar Casos de Uso
- Hacer testing de ML es complicado: ¿cómo testeas que un modelo se ha entrenado bien?

# INTEGRACIÓN DE LOS TEST DENTRO DEL CI/CD
- Se trata de automatizar la ejecución de los test al realizar el build
- La forma ortodoxa de ejecutar los test es: poetry run pytest
- Los test necesitan PANDAS. Por tanto, creamos la dependencia en el proyecto ejecutando desde consola "poetry add -D pandas"
- Nota: para eliminar dependencias de poetry: "poetry remove pandas"
- Un BUILD no debe hacerse si NO se supera el TESTING. Esto se debe codificar en el build.yml
- Para asegurar la ejecución del TESTING, en este punto, DEBEMOS DE HACER UNA NUEVA RELEASE
    - git tag -a v0.2.6 -m "v0.2.6 Añadido el Testing"
    - git push --follow-tag
# TRUCO CONSOLA: CTRL+R permite hacer búsqueda inversas textuales de los comandos escritos en consola (Ejemplo: teclear push y se verá "git push --follow tag")

# SESIÓN 04.10.2022
# RESUMEN GLOBAL DE CI/CD
- Paquete/Módulo Python:
    - Paquete: carpeta con __init.py__ 
    - Módulo: archivo.ipynb
- Crear paquete con setup.py
- Crear paquete con pyproject.toml
- Crear paquete y versiones con git/github
- Crear workflows en GitHub Actions
- Para ser expertos se necesita:
    - Gestionar entornos
    - Instalar paquetes remotos
    - Documentar un proyecto con Sphinx
    - Gestionar Ramas de git Pull Request

# Dudas de ayer:
# Error con Github Actions por tags repetidos: 
    - El tag no se puede repetir por lo que si se reutiliza, falla la ejecución
    - Si se usa la misma etiqueta se usa el commit en la que se generó
    - Es necesario crear una nueva tag para que se use el commit asociado
# git rm:
    - El borrado que se haga en tu carpeta local debe hacerse en el tu paquete del git
    - STASH: es una zona personal de ideas. No lo usamos en este curso
    - WORKSPACE: es la carpeta de nuestro proyecto local
    - INDICE: se llama "Stage Changes" en el Visual Code. Al ejecutar "git add" se añaden los archivos seleccionados a la lista de elementos pre-commit. 
    - NOTA: Un commit se puede corregir ANTES DE HABERLO ENVIADO con "commit --amend"
    - REPOSITORIO LOCAL:  es el que está en GitHub. Se actualiza con cada commit y push que hacemos
    - IMPORTANTE: cuando se borra de tu carpeta local, además, hay que usar "git rm" para 
# Subir TU PROPIO PAQUETE al PIP para poder instalarlos haciendo un "pip install"


# GESTIÓN DE ENTORNOS
    - Todo lenguaje tiene su sistema de gestión de entornos o, lo mismo, gestión de paquetes
    - Se gestionan:
        - Dependencias
        - Aislar entornos: para diferentes SO, por ejemplo
        - Ejemplos: Maven en Java, Conan en C++, en Python (Conda - que vale para cualquier lenguaje, Poetry, Pip - que se puede complementar con Venv (entornos virtuales Python))...
    - Más info: https://packaging.python.org/en/latest/guides/tool-recommendations/

# A TENER EN CUENTA
- CONDA se usa para muchos lenguajes, pero puede generar incompatibilidades
- POETRY usa VENV entre bastidores para aislar entornos por lo que sus dependencias son PIP (no CONDA) lo que puede dar problemas
- PIP se puede instalar en CONDA pero por lo del primer punto, no conviene mezclar porque puede generar problemas serios de dependencias

# DECLARACIÓN DE DEPENDENCIAS
- En pyproject.toml se generan las dependencias gracias al comando "poetry add x"
- En poetry.lock FIJA la versión, paquete y hash de la utilidad para garantizar que no hay fallos de seguridad
- En (python="^3.9") no aclara si es "3.9.1" ó "3.9.2"
- poetry asegura que se instala la DEPENDENCIA EXACTA
- Nota: conda install -c conda-forge mamba para los entornos de trabajo NO DOCKER. Muy útil porque es un CONDA SUPERACELERADO

# GESTIÓN CONCRETA DEL GESTOR DE PAQUETES
- GESTOR DE PAQUETES: divide en carpetas cada entorno y éstas se añaden al PATH con cada ACTIVACIÓN para apuntar al ENTORNO ACTIVADO
- Comprobación del entorno activo: import os, os.environ["PATH"]
- Ejecutamos en consola "echo $PATH"
/usr/lib/code-server/lib/vscode/bin/remote-cli:/home/jovyan/.local/bin:/opt/conda/bin:/opt/conda/condabin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# COMANDOS BÁSICOS DE CONDA O MAMBA
- CONDA se usa para CREAR, BORRAR ACTIVAR y DESACTIVAR ENTORNOS: conda env list, conda activate entorno, conda deactivate, conda create --name entorno, conda env remove --name entorno
- MAMBA se usa para INSTALAR y DESINSTALAR PAQUETES: mamba install paquete, mamba remove paquete
- conda env list # mostrar los entornos existentes
- conda create --name entorno # crea un entorno vacío
- conda env remove -name entorno # elimina el entorno
- CONDA y MAMBA son COMPATIBLES entre sí
- conda env list # lista los entornos

# EJERCICIO DE ENTORNO
- Con el entorno BASE ACTIVADO muestra y apunta tu PATH
    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ echo $PATH
    /usr/lib/code-server/lib/vscode/bin/remote-cli:/home/jovyan/.local/bin:/opt/conda/bin:/opt/conda/condabin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

- Crea un nuevo entorno llamado "test"
    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ conda create --name test
    Collecting package metadata (current_repodata.json): done
    Solving environment: done


    ==> WARNING: A newer version of conda exists. <==
    current version: 4.14.0
    latest version: 22.9.0

    Please update conda by running

        $ conda update -n base -c conda-forge conda



    ## Package Plan ##

    environment location: /opt/conda/envs/test



    Proceed ([y]/n)? 

    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate test
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate

    Retrieving notices: ...working... done

- Instala "python==3.9" y "tqdm"
        (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ mamba install tqdm

                    __    __    __    __
                    /  \  /  \  /  \  /  \
                    /    \/    \/    \/    \
    ███████████████/  /██/  /██/  /██/  /████████████████████████
                /  / \   / \   / \   / \  \____
                /  /   \_/   \_/   \_/   \    o \__,
                / _/                       \_____/  `
                |/
            ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗
            ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
            ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
            ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
            ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝

            mamba (0.25.0) supported by @QuantStack

            GitHub:  https://github.com/mamba-org/mamba
            Twitter: https://twitter.com/QuantStack

    █████████████████████████████████████████████████████████████


    Looking for: ['tqdm']

    conda-forge/noarch                                   9.8MB @   3.5MB/s  2.9s
    conda-forge/linux-64                                26.1MB @   4.2MB/s  6.9s
    Transaction

    Prefix: /opt/conda/envs/test

    Updating specs:

    - tqdm


    Package               Version  Build               Channel                   Size
    ─────────────────────────────────────────────────────────────────────────────────────
    Install:
    ─────────────────────────────────────────────────────────────────────────────────────

    + _libgcc_mutex           0.1  conda_forge         conda-forge/linux-64       3kB
    + _openmp_mutex           4.5  2_gnu               conda-forge/linux-64      24kB
    + bzip2                 1.0.8  h7f98852_4          conda-forge/linux-64     496kB
    + ca-certificates   2022.9.24  ha878542_0          conda-forge/linux-64     154kB
    + colorama              0.4.5  pyhd8ed1ab_0        conda-forge/noarch        19kB
    + ld_impl_linux-64     2.36.1  hea4e1c9_2          conda-forge/linux-64     683kB
    + libffi                3.4.2  h7f98852_5          conda-forge/linux-64      58kB
    + libgcc-ng            12.1.0  h8d9b700_16         conda-forge/linux-64     963kB
    + libgomp              12.1.0  h8d9b700_16         conda-forge/linux-64     470kB
    + libnsl                2.0.0  h7f98852_0          conda-forge/linux-64      31kB
    + libsqlite            3.39.4  h753d276_0          conda-forge/linux-64     822kB
    + libuuid              2.32.1  h7f98852_1000       conda-forge/linux-64      28kB
    + libzlib              1.2.13  h166bdaf_4          conda-forge/linux-64      66kB
    + ncurses                 6.3  h27087fc_1          conda-forge/linux-64       1MB
    + openssl               3.0.5  h166bdaf_2          conda-forge/linux-64       3MB
    + pip                  22.2.2  pyhd8ed1ab_0        conda-forge/noarch         2MB
    + python               3.10.6  ha86cf86_0_cpython  conda-forge/linux-64      30MB
    + readline              8.1.2  h0f457ee_0          conda-forge/linux-64     298kB
    + setuptools           65.5.0  pyhd8ed1ab_0        conda-forge/noarch       787kB
    + tk                   8.6.12  h27826a3_0          conda-forge/linux-64       3MB
    + tqdm                 4.64.1  pyhd8ed1ab_0        conda-forge/noarch        83kB
    + tzdata                2022e  h191b570_0          conda-forge/noarch       121kB
    + wheel                0.37.1  pyhd8ed1ab_0        conda-forge/noarch        32kB
    + xz                    5.2.6  h166bdaf_0          conda-forge/linux-64     418kB

    Summary:

    Install: 24 packages

    Total download: 45MB

    ─────────────────────────────────────────────────────────────────────────────────────

    Confirm changes: [Y/n] Y
    _openmp_mutex                                       23.6kB @ 116.2kB/s  0.2s
    _libgcc_mutex                                        2.6kB @  12.2kB/s  0.2s
    libgomp                                            470.3kB @   1.7MB/s  0.3s
    libnsl                                              31.2kB @ 109.1kB/s  0.1s
    ld_impl_linux-64                                   683.5kB @   2.4MB/s  0.3s
    ca-certificates                                    153.9kB @ 507.5kB/s  0.3s
    wheel                                               32.0kB @  93.5kB/s  0.1s
    colorama                                            18.6kB @  52.6kB/s  0.1s
    ncurses                                              1.0MB @   2.7MB/s  0.2s
    readline                                           298.1kB @ 625.0kB/s  0.1s
    tqdm                                                83.5kB @ 147.5kB/s  0.1s
    tk                                                   3.5MB @   5.5MB/s  0.4s
    bzip2                                              495.7kB @ 734.5kB/s  0.3s
    openssl                                              3.0MB @   3.9MB/s  0.5s
    libffi                                              58.3kB @  74.0kB/s  0.2s
    libzlib                                             65.5kB @  77.4kB/s  0.1s
    setuptools                                         786.8kB @ 881.2kB/s  0.1s
    libsqlite                                          821.9kB @ 918.4kB/s  0.3s
    xz                                                 418.4kB @ 442.9kB/s  0.1s
    libuuid                                             28.3kB @  29.5kB/s  0.1s
    tzdata                                             121.1kB @ 123.7kB/s  0.1s
    libgcc-ng                                          962.7kB @ 844.1kB/s  0.2s
    pip                                                  1.6MB @   1.3MB/s  0.5s
    python                                              30.4MB @  18.5MB/s  1.3s
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ 

    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ mamba install python==3.9

                    __    __    __    __
                    /  \  /  \  /  \  /  \
                    /    \/    \/    \/    \
    ███████████████/  /██/  /██/  /██/  /████████████████████████
                /  / \   / \   / \   / \  \____
                /  /   \_/   \_/   \_/   \    o \__,
                / _/                       \_____/  `
                |/
            ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗
            ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
            ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
            ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
            ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝

            mamba (0.25.0) supported by @QuantStack

            GitHub:  https://github.com/mamba-org/mamba
            Twitter: https://twitter.com/QuantStack

    █████████████████████████████████████████████████████████████


    Looking for: ['python==3.9']

    conda-forge/linux-64                                        Using cache
    conda-forge/noarch                                          Using cache
    Transaction

    Prefix: /opt/conda/envs/test

    Updating specs:

    - python==3.9
    - ca-certificates
    - openssl


    Package         Version  Build               Channel                   Size
    ───────────────────────────────────────────────────────────────────────────────
    Install:
    ───────────────────────────────────────────────────────────────────────────────

    + libstdcxx-ng   12.1.0  ha89aaad_16         conda-forge/linux-64       4MB
    + sqlite         3.39.4  h4ff8645_0          conda-forge/linux-64     807kB
    + zlib           1.2.13  h166bdaf_4          conda-forge/linux-64      94kB

    Reinstall:
    ───────────────────────────────────────────────────────────────────────────────

    o colorama        0.4.5  pyhd8ed1ab_0        conda-forge                   
    o pip            22.2.2  pyhd8ed1ab_0        conda-forge                   
    o setuptools     65.5.0  pyhd8ed1ab_0        conda-forge                   
    o tqdm           4.64.1  pyhd8ed1ab_0        conda-forge                   
    o wheel          0.37.1  pyhd8ed1ab_0        conda-forge                   

    Downgrade:
    ───────────────────────────────────────────────────────────────────────────────

    - libffi          3.4.2  h7f98852_5          conda-forge                   
    + libffi            3.3  h58526e2_2          conda-forge/linux-64      53kB
    - openssl         3.0.5  h166bdaf_2          conda-forge                   
    + openssl        1.1.1q  h166bdaf_0          conda-forge/linux-64       2MB
    - python         3.10.6  ha86cf86_0_cpython  conda-forge                   
    + python          3.9.0  hffdb5ce_5_cpython  conda-forge/linux-64      30MB

    Summary:

    Install: 3 packages
    Reinstall: 2 packages
    Downgrade: 3 packages

    Total download: 38MB

    ───────────────────────────────────────────────────────────────────────────────

    Confirm changes: [Y/n] Y
    zlib                                                94.1kB @ 269.9kB/s  0.3s
    openssl                                              2.2MB @   4.8MB/s  0.5s
    libffi                                              52.6kB @  96.7kB/s  0.5s
    sqlite                                             807.5kB @   1.3MB/s  0.6s
    libstdcxx-ng                                         4.5MB @   6.6MB/s  0.7s
    python                                              30.1MB @   9.9MB/s  2.7s
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$   

- Con el nuevo entorno activado, comprueba el PATH
    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ echo $PATH
    /usr/lib/code-server/lib/vscode/bin/remote-cli:/home/jovyan/.local/bin:/opt/conda/envs/test/bin:/opt/conda/condabin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ echo $PATH
    /usr/lib/code-server/lib/vscode/bin/remote-cli:/home/jovyan/.local/bin:/opt/conda/bin:/opt/conda/condabin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

    El único cambio en test es "/opt/conda/envs/test/bin:" con respecto al entorno BASE. El segundo entorno de búsqueda es el BASE. Es decir, si no se encuentra el comando en el entorno TEST, se busca en BASE y, si está, se ejecuta.

- Ejecuta Python para verificar que se está usando la versión 3.9
    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ python
    Python 3.9.0 | packaged by conda-forge | (default, Nov 26 2020, 07:57:39) 
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

- Ejecuta un notebook, importa tqdm y muestra el path.  # Este paso es erróneo porque en NOTEBOOK NO ESTAMOS EN EL ENTORNO TEST. Hay que hacerlo desde consola del entorno TEST
    import tqdm
    tqdm.__path__
    ['/opt/conda/lib/python3.10/site-packages/tqdm']

    # Ejecución correcta

    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ python
    Python 3.10.6 | packaged by conda-forge | (main, Aug 22 2022, 20:35:26) [GCC 10.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tqdm
    >>> tqdm.__path__
    ['/opt/conda/lib/python3.10/site-packages/tqdm']
    >>> exit()
    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ conda activate test
    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ conda env list
    # conda environments:
    #
    base                     /opt/conda
    test                  *  /opt/conda/envs/test

    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ mamba install python==3.9

                    __    __    __    __
                    /  \  /  \  /  \  /  \
                    /    \/    \/    \/    \
    ███████████████/  /██/  /██/  /██/  /████████████████████████
                /  / \   / \   / \   / \  \____
                /  /   \_/   \_/   \_/   \    o \__,
                / _/                       \_____/  `
                |/
            ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗
            ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
            ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
            ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
            ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝

            mamba (0.25.0) supported by @QuantStack

            GitHub:  https://github.com/mamba-org/mamba
            Twitter: https://twitter.com/QuantStack

    █████████████████████████████████████████████████████████████


    Looking for: ['python==3.9']

    conda-forge/linux-64                                        Using cache
    conda-forge/noarch                                          Using cache
    Transaction

    Prefix: /opt/conda/envs/test

    All requested packages already installed

    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ python
    Python 3.9.0 | packaged by conda-forge | (default, Nov 26 2020, 07:57:39) 
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tqdm
    >>> tqdm.__path__
    ['/opt/conda/envs/test/lib/python3.9/site-packages/tqdm']
    >>> import os
    >>> os.environ["PATH"]
    '/opt/conda/envs/test/bin:/usr/lib/code-server/lib/vscode/bin/remote-cli:/home/jovyan/.local/bin:/opt/conda/condabin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
    >>> import sys
    >>> sys.path.  # Indica de qué ruta se leen los paquetes de python. Se observa que apunta al entorno test
    ['', '/opt/conda/envs/test/lib/python39.zip', '/opt/conda/envs/test/lib/python3.9', '/opt/conda/envs/test/lib/python3.9/lib-dynload', '/opt/conda/envs/test/lib/python3.9/site-packages']
    >>>  


- Instala tu paquete modeltools desde las releases de github usando pip install
Ruta de mi paquete: https://github.com/pgasane/gh-master-oct/releases/download/v0.2.6/modeltools-0.2.6-py3-none-any.whl
(test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ mamba install https://github.com/pgasane/gh-master-oct/releases/download/v0.2.6/modeltools-0.2.6-py3-none-any.whl

                    __    __    __    __
                    /  \  /  \  /  \  /  \
                    /    \/    \/    \/    \
    ███████████████/  /██/  /██/  /██/  /████████████████████████
                /  / \   / \   / \   / \  \____
                /  /   \_/   \_/   \_/   \    o \__,
                / _/                       \_____/  `
                |/
            ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗
            ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
            ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
            ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
            ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝

            mamba (0.25.0) supported by @QuantStack

            GitHub:  https://github.com/mamba-org/mamba
            Twitter: https://twitter.com/QuantStack

    █████████████████████████████████████████████████████████████


    Looking for: ['//github.com/pgasane/gh-master-oct/releases/download/v0.2.6/modeltools-0.2.6-py3-none-any.whl']

    conda-forge/linux-64                                        Using cache
    conda-forge/noarch                                          Using cache

    Pinned packages:
    - python 3.9.*


    Encountered problems while solving:
    - nothing provides requested //github.com/pgasane/gh-master-oct/releases/download/v0.2.6/modeltools-0.2.6-py3-none-any.whl

    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ 

- Comprueba que funciona el entorno test de modeltools
    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ pytest
    ========================================================================================== test session starts ==========================================================================================
    platform linux -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
    rootdir: /home/jovyan/work/m02/gh-master-oct
    plugins: anyio-3.6.1
    collected 7 items                                                                                                                                                                                       

    tests/test_preprocessing.py .......                                                                                                                                                               [100%]

    =========================================================================================== 7 passed in 0.48s ===========================================================================================
    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ 

- Desactiva y borra el entorno test
    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ conda env list
    # conda environments:
    #
    base                  *  /opt/conda
    test                     /opt/conda/envs/test

    (test) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ conda deactivate
    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ conda env remove --name test

    Remove all packages in environment /opt/conda/envs/test:

    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$

- IMPORTANTE: además de realizar la instalación remota, también se pueden DECLARAR DEPENDENCIAS USANDO LA URL: poetry add //github.com/pgasane/gh-master-oct/releases/download/v0.2.6/modeltools-0.2.6-py3-none-any.whl


# CANALES DE CONDA (repositorios donde están las librerías y paquetes. Hay oficiales, de empresa y personales)
- El más popular es https://conda-forge.org. Se usa así: mamba install -c conda-forge PAQUETE. Curiosidad: GitHub ha creado su CANAL OFICIAL en CONDA-FORGE.
- No conviene mezclar librerías y paquetes de varios canales.

# EXPORTAR TODOS LOS PAQUETES EN EJECUCIÓN DE UN ENTORNO PARA PODER CLONAR EL ENTORNO EN OTRO DIFERENTE
- Podemos exportar la lista de paquetes instalados para clonar entornos (util para CI/CD):
    - conda list --export > package-list.txt
    - mamba create -n myenv --file package-list.txt
- Objetivo: clonar el entorno de RELEASE en un entorno de PRODUCCIÓN (CI/CD)
- Ejercicio: clonar el entorno BASE en otro entorno que se llame MYENV
    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ conda list --export > package-list.txt
    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ mamba create -n myenv --file package-list.txt

                    __    __    __    __
                    /  \  /  \  /  \  /  \
                    /    \/    \/    \/    \
    ███████████████/  /██/  /██/  /██/  /████████████████████████
                /  / \   / \   / \   / \  \____
                /  /   \_/   \_/   \_/   \    o \__,
                / _/                       \_____/  `
                |/
            ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗
            ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
            ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
            ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
            ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝

            mamba (0.25.0) supported by @QuantStack

            GitHub:  https://github.com/mamba-org/mamba
            Twitter: https://twitter.com/QuantStack

    █████████████████████████████████████████████████████████████


    Looking for: ['_libgcc_mutex==0.1=conda_forge', '_openmp_mutex==4.5=2_kmp_llvm', '_r-mutex==1.0.1=anacondar_1', 'aiohttp==3.8.3=py310h5764c6d_0', 'aiosignal==1.2.0=pyhd8ed1ab_0', 'alembic==1.8.1=pyhd8ed1ab_0', 'altair==4.2.0=pyhd8ed1ab_1', 'anyio==3.6.1=pyhd8ed1ab_1', 'aom==3.5.0=h27087fc_0', 'argon2-cffi==21.3.0=pyhd8ed1ab_0', 'argon2-cffi-bindings==21.2.0=py310h5764c6d_2', 'asttokens==2.0.8=pyhd8ed1ab_0', 'async-timeout==4.0.2=pyhd8ed1ab_0', 'async_generator==1.10=py_0', 'attrs==22.1.0=pyh71513ae_1', 'babel==2.10.3=pyhd8ed1ab_0', 'backcall==0.2.0=pyh9f0ad1d_0', 'backports==1.0=py_2', 'backports.functools_lru_cache==1.6.4=pyhd8ed1ab_0', 'beautifulsoup4==4.11.1=pyha770c72_0', 'binutils_impl_linux-64==2.36.1=h193b22a_2', 'blas==2.116=openblas', 'blas-devel==3.9.0=16_linux64_openblas', 'bleach==5.0.1=pyhd8ed1ab_0', 'blinker==1.4=py_1', 'blosc==1.21.1=h83bc5f7_3', 'bokeh==2.4.3=pyhd8ed1ab_3', 'bottleneck==1.3.5=py310hde88566_0', 'brotli==1.0.9=h166bdaf_7', 'brotli-bin==1.0.9=h166bdaf_7', 'brotlipy==0.7.0=py310h5764c6d_1004', 'brunsli==0.1=h9c3ff4c_0', 'bwidget==1.9.14=ha770c72_1', 'bzip2==1.0.8=h7f98852_4', 'c-ares==1.18.1=h7f98852_0', 'c-blosc2==2.4.1=h7a311fb_0', 'ca-certificates==2022.9.24=ha878542_0', 'cachecontrol==0.12.11=pyhd8ed1ab_0', 'cached-property==1.5.2=hd8ed1ab_1', 'cached_property==1.5.2=pyha770c72_1', 'cachy==0.3.0=py_0', 'cairo==1.16.0=ha61ee94_1014', 'certifi==2022.9.24=pyhd8ed1ab_0', 'certipy==0.1.3=py_0', 'cffi==1.15.1=py310h255011f_0', 'cfitsio==4.1.0=hd9d235c_0', 'charls==2.3.4=h9c3ff4c_0', 'charset-normalizer==2.1.1=pyhd8ed1ab_0', 'cleo==0.8.1=pyhd8ed1ab_2', 'click==8.1.3=py310hff52083_0', 'clikit==0.6.2=pyh9f0ad1d_0', 'cloudpickle==2.2.0=pyhd8ed1ab_0', 'colorama==0.4.5=pyhd8ed1ab_0', 'conda==4.14.0=py310hff52083_0', 'conda-package-handling==1.9.0=py310h5764c6d_0', 'configurable-http-proxy==4.5.3=node17_h7e777a6_0', 'contourpy==1.0.5=py310hbf28c38_0', 'crashtest==0.3.1=pyhd8ed1ab_0', 'cryptography==37.0.4=py310h597c629_0', 'curl==7.83.1=h7bff187_0', 'cycler==0.11.0=pyhd8ed1ab_0', 'cython==0.29.32=py310hd8f1fbe_0', 'cytoolz==0.12.0=py310h5764c6d_0', 'dask==2022.9.1=pyhd8ed1ab_0', 'dask-core==2022.9.1=pyhd8ed1ab_0', 'databricks-cli==0.17.3=pypi_0', 'dav1d==1.0.0=h166bdaf_1', 'dbus==1.13.6=h5008d03_3', 'debugpy==1.6.3=py310hd8f1fbe_0', 'decorator==5.1.1=pyhd8ed1ab_0', 'defusedxml==0.7.1=pyhd8ed1ab_0', 'dill==0.3.5.1=pyhd8ed1ab_0', 'distlib==0.3.5=pyhd8ed1ab_0', 'distributed==2022.9.1=pyhd8ed1ab_0', 'docker==6.0.0=pypi_0', 'entrypoints==0.4=pyhd8ed1ab_0', 'executing==1.1.0=pyhd8ed1ab_0', 'expat==2.4.9=h27087fc_0', 'filelock==3.8.0=pyhd8ed1ab_0', 'flask==2.2.2=pypi_0', 'flit-core==3.7.1=pyhd8ed1ab_0', 'font-ttf-dejavu-sans-mono==2.37=hab24e00_0', 'font-ttf-inconsolata==3.000=h77eed37_0', 'font-ttf-source-code-pro==2.038=h77eed37_0', 'font-ttf-ubuntu==0.83=hab24e00_0', 'fontconfig==2.14.0=hc2a2eb6_1', 'fonts-conda-ecosystem==1=0', 'fonts-conda-forge==1=0', 'fonttools==4.37.3=py310h5764c6d_0', 'freetype==2.12.1=hca18f0e_0', 'fribidi==1.0.10=h36c2ea0_0', 'frozenlist==1.3.1=py310h5764c6d_0', 'fsspec==2022.8.2=pyhd8ed1ab_0', 'gcc_impl_linux-64==12.1.0=hea43390_16', 'gettext==0.19.8.1=h27087fc_1009', 'gfortran_impl_linux-64==12.1.0=h1db8e46_16', 'gh==2.16.1=ha8f183a_0', 'giflib==5.2.1=h36c2ea0_2', 'gitdb==4.0.9=pypi_0', 'gitpython==3.1.28=pypi_0', 'gmp==6.2.1=h58526e2_0', 'gmpy2==2.1.2=py310h92f7908_0', 'graphite2==1.3.13=h58526e2_1001', 'greenlet==1.1.3=py310hd8f1fbe_0', 'gsl==2.7=he838d99_0', 'gunicorn==20.1.0=pypi_0', 'gxx_impl_linux-64==12.1.0=hea43390_16', 'h5py==3.7.0=nompi_py310h416281c_101', 'harfbuzz==5.2.0=hf9f4e7c_0', 'hdf5==1.12.2=nompi_h2386368_100', 'heapdict==1.0.1=py_0', 'html5lib==1.1=pyh9f0ad1d_0', 'icu==70.1=h27087fc_0', 'idna==3.4=pyhd8ed1ab_0', 'imagecodecs==2022.9.26=py310h1689d63_0', 'imageio==2.22.0=pyhfa7a67d_0', 'importlib-metadata==4.11.4=py310hff52083_0', 'importlib_metadata==4.11.4=hd8ed1ab_0', 'importlib_resources==5.9.0=pyhd8ed1ab_0', 'iniconfig==1.1.1=pyh9f0ad1d_0', 'ipykernel==6.16.0=pyh210e3f2_0', 'ipympl==0.9.2=pyhd8ed1ab_0', 'ipython==8.5.0=pyh41d4057_1', 'ipython_genutils==0.2.0=py_1', 'ipywidgets==8.0.2=pyhd8ed1ab_1', 'itsdangerous==2.1.2=pypi_0', 'jaraco.classes==3.2.2=pyhd8ed1ab_0', 'jedi==0.18.1=pyhd8ed1ab_2', 'jeepney==0.8.0=pyhd8ed1ab_0', 'jinja2==3.1.2=pyhd8ed1ab_1', 'joblib==1.2.0=pyhd8ed1ab_0', 'jpeg==9e=h166bdaf_2', 'json5==0.9.5=pyh9f0ad1d_0', 'jsonschema==4.16.0=pyhd8ed1ab_0', 'jupyter-server-proxy==3.2.2=pyhd8ed1ab_0', 'jupyter_client==7.3.4=pyhd8ed1ab_0', 'jupyter_core==4.11.1=py310hff52083_0', 'jupyter_server==1.18.1=pyhd8ed1ab_0', 'jupyter_telemetry==0.1.0=pyhd8ed1ab_1', 'jupyterhub==3.0.0=pyhd8ed1ab_0', 'jupyterhub-base==3.0.0=pyhd8ed1ab_0', 'jupyterlab==3.4.7=pyhd8ed1ab_0', 'jupyterlab-tour==3.1.4=pyhd8ed1ab_0', 'jupyterlab_pygments==0.2.2=pyhd8ed1ab_0', 'jupyterlab_server==2.15.2=pyhd8ed1ab_0', 'jupyterlab_widgets==3.0.3=pyhd8ed1ab_0', 'jxrlib==1.1=h7f98852_2', 'kernel-headers_linux-64==2.6.32=he073ed8_15', 'keyring==23.9.3=py310hff52083_0', 'keyutils==1.6.1=h166bdaf_0', 'kiwisolver==1.4.4=py310hbf28c38_0', 'krb5==1.19.3=h3790be6_0', 'lcms2==2.12=hddcbb42_0', 'ld_impl_linux-64==2.36.1=hea4e1c9_2', 'lerc==4.0.0=h27087fc_0', 'libaec==1.0.6=h9c3ff4c_0', 'libarchive==3.5.2=hb890918_3', 'libavif==0.10.1=h5cdd6b5_2', 'libblas==3.9.0=16_linux64_openblas', 'libbrotlicommon==1.0.9=h166bdaf_7', 'libbrotlidec==1.0.9=h166bdaf_7', 'libbrotlienc==1.0.9=h166bdaf_7', 'libcblas==3.9.0=16_linux64_openblas', 'libcurl==7.83.1=h7bff187_0', 'libdeflate==1.14=h166bdaf_0', 'libedit==3.1.20191231=he28a2e2_2', 'libev==4.33=h516909a_1', 'libffi==3.4.2=h7f98852_5', 'libgcc-devel_linux-64==12.1.0=h1ec3361_16', 'libgcc-ng==12.1.0=h8d9b700_16', 'libgfortran-ng==12.1.0=h69a702a_16', 'libgfortran5==12.1.0=hdcd56e2_16', 'libgit2==1.5.0=h6529ace_0', 'libglib==2.74.0=h7a41b64_0', 'libgomp==12.1.0=h8d9b700_16', 'libiconv==1.17=h166bdaf_0', 'liblapack==3.9.0=16_linux64_openblas', 'liblapacke==3.9.0=16_linux64_openblas', 'libllvm11==11.1.0=hf817b99_3', 'libmamba==0.25.0=hd8a31e3_2', 'libmambapy==0.25.0=py310hab0e683_2', 'libnghttp2==1.47.0=hdcd2b5c_1', 'libnsl==2.0.0=h7f98852_0', 'libopenblas==0.3.21=pthreads_h78a6416_3', 'libpng==1.6.38=h753d276_0', 'libprotobuf==3.21.6=h6239696_1', 'libsanitizer==12.1.0=ha89aaad_16', 'libsodium==1.0.18=h36c2ea0_1', 'libsolv==0.7.22=h6239696_0', 'libsqlite==3.39.3=h753d276_0', 'libssh2==1.10.0=haa6b8db_3', 'libstdcxx-devel_linux-64==12.1.0=h1ec3361_16', 'libstdcxx-ng==12.1.0=ha89aaad_16', 'libtiff==4.4.0=h55922b4_4', 'libuuid==2.32.1=h7f98852_1000', 'libuv==1.43.0=h7f98852_0', 'libwebp-base==1.2.4=h166bdaf_0', 'libxcb==1.13=h7f98852_1004', 'libxml2==2.10.2=h4c7fe37_1', 'libxslt==1.1.35=h8affb1d_0', 'libzlib==1.2.12=h166bdaf_3', 'libzopfli==1.0.3=h9c3ff4c_0', 'llvm-openmp==14.0.4=he0ac6c6_0', 'llvmlite==0.38.1=py310h58363a5_0', 'locket==1.0.0=pyhd8ed1ab_0', 'lockfile==0.12.2=py_1', 'lxml==4.9.1=py310h5764c6d_0', 'lz4==4.0.0=py310h5d5e884_2', 'lz4-c==1.9.3=h9c3ff4c_1', 'lzo==2.10=h516909a_1000', 'make==4.3=hd18ef5c_1', 'mako==1.2.3=pyhd8ed1ab_0', 'mamba==0.25.0=py310hf87f941_2', 'mamba_gator==5.2.0=pyhd8ed1ab_0', 'markupsafe==2.1.1=py310h5764c6d_1', 'matplotlib-base==3.6.0=py310h8d5ebf3_0', 'matplotlib-inline==0.1.6=pyhd8ed1ab_0', 'mistune==2.0.4=pyhd8ed1ab_0', 'mlflow==1.29.0=pypi_0', 'modeltools==0.2.3=pypi_0', 'more-itertools==8.14.0=pyhd8ed1ab_0', 'mpc==1.2.1=h9f54685_0', 'mpfr==4.1.0=h9202a9a_1', 'mpmath==1.2.1=pyhd8ed1ab_0', 'msgpack-python==1.0.4=py310hbf28c38_0', 'multidict==6.0.2=py310h5764c6d_1', 'munkres==1.1.4=pyh9f0ad1d_0', 'nbclassic==0.4.3=pyhd8ed1ab_0', 'nbclient==0.6.8=pyhd8ed1ab_0', 'nbconvert==7.0.0=pyhd8ed1ab_0', 'nbconvert-core==7.0.0=pyhd8ed1ab_0', 'nbconvert-pandoc==7.0.0=pyhd8ed1ab_0', 'nbformat==5.6.1=pyhd8ed1ab_0', 'ncurses==6.3=h27087fc_1', 'nest-asyncio==1.5.5=pyhd8ed1ab_0', 'networkx==2.8.6=pyhd8ed1ab_0', 'nodejs==17.9.0=h96d913c_0', 'nomkl==1.0=h5ca1d4c_0', 'notebook==6.4.12=pyha770c72_0', 'notebook-shim==0.1.0=pyhd8ed1ab_0', 'numba==0.55.2=py310ha5257ce_0', 'numexpr==2.8.3=py310hf05e7a9_100', 'numpy==1.23.3=pypi_0', 'oauthlib==3.2.1=pyhd8ed1ab_0', 'openblas==0.3.21=pthreads_h320a7e8_3', 'openjpeg==2.5.0=h7d73246_1', 'openssl==1.1.1q=h166bdaf_0', 'packaging==20.9=pyh44b312d_0', 'pamela==1.0.0=py_0', 'pandas==1.5.0=py310h769672d_0', 'pandoc==2.19.2=ha770c72_0', 'pandocfilters==1.5.0=pyhd8ed1ab_0', 'pango==1.50.10=hc4f8a73_0', 'parso==0.8.3=pyhd8ed1ab_0', 'partd==1.3.0=pyhd8ed1ab_0', 'pastel==0.2.1=pyhd8ed1ab_0', 'patsy==0.5.2=pyhd8ed1ab_0', 'pcre2==10.37=hc3806b6_1', 'pexpect==4.8.0=pyh9f0ad1d_2', 'pickleshare==0.7.5=py_1003', 'pillow==9.2.0=py310hbd86126_2', 'pip==22.2.2=pyhd8ed1ab_0', 'pixman==0.40.0=h36c2ea0_0', 'pkginfo==1.8.3=pyhd8ed1ab_0', 'pkgutil-resolve-name==1.3.10=pyhd8ed1ab_0', 'platformdirs==2.5.2=pyhd8ed1ab_1', 'pluggy==1.0.0=py310hff52083_3', 'poetry==1.1.15=py310hff52083_0', 'poetry-core==1.0.8=py310hff52083_1', 'prometheus-flask-exporter==0.20.3=pypi_0', 'prometheus_client==0.14.1=pyhd8ed1ab_0', 'prompt-toolkit==3.0.31=pyha770c72_0', 'protobuf==4.21.6=py310hd8f1fbe_0', 'psutil==5.9.2=py310h5764c6d_0', 'pthread-stubs==0.4=h36c2ea0_1001', 'ptyprocess==0.7.0=pyhd3deb0d_0', 'pure_eval==0.2.2=pyhd8ed1ab_0', 'py==1.11.0=pyh6c4a22f_0', 'pybind11-abi==4=hd8ed1ab_3', 'pycosat==0.6.3=py310h5764c6d_1010', 'pycparser==2.21=pyhd8ed1ab_0', 'pycurl==7.45.1=py310h2aed498_2', 'pygments==2.13.0=pyhd8ed1ab_0', 'pyjwt==2.5.0=pyhd8ed1ab_0', 'pylev==1.4.0=pyhd8ed1ab_0', 'pyopenssl==22.0.0=pyhd8ed1ab_1', 'pyparsing==3.0.9=pyhd8ed1ab_0', 'pyrsistent==0.18.1=py310h5764c6d_1', 'pysocks==1.7.1=pyha2e5f31_6', 'pytables==3.7.0=py310hb60b9b2_2', 'pytest==7.1.3=py310hff52083_0', 'python==3.10.6=h582c2e5_0_cpython', 'python-dateutil==2.8.2=pyhd8ed1ab_0', 'python-fastjsonschema==2.16.2=pyhd8ed1ab_0', 'python-json-logger==2.0.1=pyh9f0ad1d_0', 'python-tzdata==2022.4=pyhd8ed1ab_0', 'python_abi==3.10=2_cp310', 'pytz==2022.2.1=pyhd8ed1ab_0', 'pytz-deprecation-shim==0.1.0.post0=py310hff52083_2', 'pywavelets==1.3.0=py310hde88566_1', 'pyyaml==6.0=py310h5764c6d_4', 'pyzmq==24.0.1=py310h330234f_0', 'querystring-parser==1.2.4=pypi_0', 'r-askpass==1.1=r41hcfec24a_2', 'r-assertthat==0.2.1=r41hc72bb7e_2', 'r-backports==1.4.1=r41hcfec24a_0', 'r-base==4.1.3=ha8c3e7c_2', 'r-base64enc==0.1_3=r41hcfec24a_1004', 'r-bit==4.0.4=r41hcfec24a_0', 'r-bit64==4.0.5=r41hcfec24a_0', 'r-bitops==1.0_7=r41h06615bd_0', 'r-blob==1.2.3=r41hc72bb7e_0', 'r-brew==1.0_7=r41hc72bb7e_0', 'r-brio==1.1.3=r41hcfec24a_0', 'r-broom==1.0.1=r41hc72bb7e_0', 'r-bslib==0.4.0=r41hc72bb7e_0', 'r-cachem==1.0.6=r41hcfec24a_0', 'r-callr==3.7.2=r41hc72bb7e_0', 'r-caret==6.0_93=r41h06615bd_0', 'r-cellranger==1.1.0=r41hc72bb7e_1004', 'r-class==7.3_20=r41hcfec24a_0', 'r-cli==3.4.1=r41h7525677_0', 'r-clipr==0.8.0=r41hc72bb7e_0', 'r-codetools==0.2_18=r41hc72bb7e_0', 'r-colorspace==2.0_3=r41h06615bd_0', 'r-commonmark==1.8.0=r41h06615bd_0', 'r-conflicted==1.1.0=r41hc72bb7e_0', 'r-cpp11==0.4.2=r41hc72bb7e_0', 'r-crayon==1.5.1=r41hc72bb7e_0', 'r-credentials==1.3.2=r41hc72bb7e_0', 'r-curl==4.3.2=r41hcfec24a_0', 'r-data.table==1.14.2=r41hcfec24a_0', 'r-dbi==1.1.3=r41hc72bb7e_0', 'r-dbplyr==2.2.1=r41hc72bb7e_0', 'r-desc==1.4.2=r41hc72bb7e_0', 'r-devtools==2.4.4=r41hc72bb7e_0', 'r-dials==1.0.0=r41hc72bb7e_0', 'r-dicedesign==1.9=r41hcfec24a_0', 'r-diffobj==0.3.5=r41hcfec24a_0', 'r-digest==0.6.29=r41h03ef668_0', 'r-downlit==0.4.2=r41hc72bb7e_0', 'r-dplyr==1.0.10=r41h7525677_0', 'r-dtplyr==1.2.2=r41hc72bb7e_0', 'r-e1071==1.7_11=r41h7525677_0', 'r-ellipsis==0.3.2=r41hcfec24a_0', 'r-evaluate==0.16=r41hc72bb7e_0', 'r-fansi==1.0.3=r41h06615bd_0', 'r-farver==2.1.1=r41h7525677_0', 'r-fastmap==1.1.0=r41h03ef668_0', 'r-fontawesome==0.3.0=r41hc72bb7e_0', 'r-forcats==0.5.2=r41hc72bb7e_0', 'r-foreach==1.5.2=r41hc72bb7e_0', 'r-forecast==8.17.0=r41h37cf8d7_0', 'r-fracdiff==1.5_1=r41hb699f27_1', 'r-fs==1.5.2=r41h7525677_1', 'r-furrr==0.3.1=r41hc72bb7e_0', 'r-future==1.28.0=r41hc72bb7e_0', 'r-future.apply==1.9.1=r41hc72bb7e_0', 'r-gargle==1.2.1=r41hc72bb7e_0', 'r-generics==0.1.3=r41hc72bb7e_0', 'r-gert==1.5.0=r41h163148b_2', 'r-ggplot2==3.3.6=r41hc72bb7e_0', 'r-gh==1.3.1=r41hc72bb7e_0', 'r-gitcreds==0.1.2=r41hc72bb7e_0', 'r-globals==0.16.1=r41hc72bb7e_0', 'r-glue==1.6.2=r41h06615bd_0', 'r-googledrive==2.0.0=r41hc72bb7e_0', 'r-googlesheets4==1.0.1=r41h785f33e_0', 'r-gower==1.0.0=r41hcfec24a_0', 'r-gpfit==1.0_8=r41hc72bb7e_1', 'r-gtable==0.3.1=r41hc72bb7e_0', 'r-hardhat==1.2.0=r41hc72bb7e_0', 'r-haven==2.5.0=r41h7525677_0', 'r-hexbin==1.28.2=r41h8da6f51_0', 'r-highr==0.9=r41hc72bb7e_0', 'r-hms==1.1.2=r41hc72bb7e_0', 'r-htmltools==0.5.3=r41h7525677_0', 'r-htmlwidgets==1.5.4=r41hc72bb7e_0', 'r-httpuv==1.6.6=r41h7525677_0', 'r-httr==1.4.4=r41hc72bb7e_0', 'r-ids==1.0.1=r41hc72bb7e_1', 'r-infer==1.0.3=r41hc72bb7e_0', 'r-ini==0.3.1=r41hc72bb7e_1003', 'r-ipred==0.9_13=r41h06615bd_0', 'r-irdisplay==1.1=r41hd8ed1ab_0', 'r-irkernel==1.3=r41hc72bb7e_0', 'r-isoband==0.2.5=r41h03ef668_0', 'r-iterators==1.0.14=r41hc72bb7e_0', 'r-jquerylib==0.1.4=r41hc72bb7e_0', 'r-jsonlite==1.8.0=r41h06615bd_0', 'r-kernsmooth==2.23_20=r41h742201e_0', 'r-knitr==1.40=r41hc72bb7e_0', 'r-labeling==0.4.2=r41hc72bb7e_1', 'r-later==1.2.0=r41h03ef668_0', 'r-lattice==0.20_45=r41hcfec24a_0', 'r-lava==1.6.10=r41hc72bb7e_0', 'r-lhs==1.1.5=r41h7525677_0', 'r-lifecycle==1.0.2=r41hc72bb7e_0', 'r-listenv==0.8.0=r41hc72bb7e_1', 'r-lmtest==0.9_40=r41h8da6f51_0', 'r-lubridate==1.8.0=r41h03ef668_0', 'r-magrittr==2.0.3=r41h06615bd_0', 'r-mass==7.3_58.1=r41h06615bd_0', 'r-matrix==1.4_1=r41h0154571_0', 'r-memoise==2.0.1=r41hc72bb7e_0', 'r-mgcv==1.8_40=r41h0154571_0', 'r-mime==0.12=r41hcfec24a_0', 'r-miniui==0.1.1.1=r41hc72bb7e_1002', 'r-modeldata==1.0.1=r41hc72bb7e_0', 'r-modelmetrics==1.2.2.2=r41h03ef668_1', 'r-modelr==0.1.9=r41hc72bb7e_0', 'r-munsell==0.5.0=r41hc72bb7e_1004', 'r-nlme==3.1_159=r41h8da6f51_0', 'r-nnet==7.3_17=r41hcfec24a_0', 'r-numderiv==2016.8_1.1=r41hc72bb7e_3', 'r-nycflights13==1.0.2=r41hc72bb7e_0', 'r-openssl==2.0.3=r41hfaab4ff_0', 'r-parallelly==1.32.1=r41hc72bb7e_0', 'r-parsnip==1.0.1=r41hc72bb7e_0', 'r-patchwork==1.1.2=r41hc72bb7e_0', 'r-pbdzmq==0.3_7=r41h42bf92c_0', 'r-pillar==1.8.1=r41hc72bb7e_0', 'r-pkgbuild==1.3.1=r41hc72bb7e_0', 'r-pkgconfig==2.0.3=r41hc72bb7e_1', 'r-pkgdown==2.0.6=r41hc72bb7e_0', 'r-pkgload==1.3.0=r41hc72bb7e_0', 'r-plogr==0.2.0=r41hc72bb7e_1003', 'r-plyr==1.8.7=r41h7525677_0', 'r-praise==1.0.0=r41hc72bb7e_1005', 'r-prettyunits==1.1.1=r41hc72bb7e_1', 'r-proc==1.18.0=r41h03ef668_0', 'r-processx==3.7.0=r41h06615bd_0', 'r-prodlim==2019.11.13=r41h03ef668_1', 'r-profvis==0.3.7=r41hcfec24a_0', 'r-progress==1.2.2=r41hc72bb7e_2', 'r-progressr==0.11.0=r41hc72bb7e_0', 'r-promises==1.2.0.1=r41h03ef668_0', 'r-proxy==0.4_27=r41h06615bd_0', 'r-ps==1.7.1=r41h06615bd_0', 'r-purrr==0.3.4=r41hcfec24a_1', 'r-quadprog==1.5_8=r41h742201e_3', 'r-quantmod==0.4.20=r41hc72bb7e_0', 'r-r6==2.5.1=r41hc72bb7e_0', 'r-ragg==1.2.2=r41hc1f6985_0', 'r-randomforest==4.7_1.1=r41h8da6f51_0', 'r-rappdirs==0.3.3=r41hcfec24a_0', 'r-rcmdcheck==1.4.0=r41h785f33e_0', 'r-rcolorbrewer==1.1_3=r41h785f33e_0', 'r-rcpp==1.0.9=r41h7525677_1', 'r-rcpparmadillo==0.11.2.3.1=r41h9f5de39_0', 'r-rcurl==1.98_1.8=r41h06615bd_0', 'r-readr==2.1.2=r41h03ef668_0', 'r-readxl==1.4.1=r41hf23e330_0', 'r-recipes==1.0.1=r41hc72bb7e_0', 'r-rematch==1.0.1=r41hc72bb7e_1004', 'r-rematch2==2.1.2=r41hc72bb7e_1', 'r-remotes==2.4.2=r41hc72bb7e_0', 'r-repr==1.1.4=r41h785f33e_0', 'r-reprex==2.0.2=r41hc72bb7e_0', 'r-reshape2==1.4.4=r41h03ef668_1', 'r-rlang==1.0.5=r41h7525677_0', 'r-rmarkdown==2.16=r41hc72bb7e_0', 'r-rodbc==1.3_19=r41hcfec24a_0', 'r-roxygen2==7.2.1=r41h7525677_0', 'r-rpart==4.1.16=r41hcfec24a_0', 'r-rprojroot==2.0.3=r41hc72bb7e_0', 'r-rsample==1.1.0=r41hc72bb7e_0', 'r-rsqlite==2.2.8=r41h03ef668_0', 'r-rstudioapi==0.14=r41hc72bb7e_0', 'r-rversions==2.1.2=r41hc72bb7e_0', 'r-rvest==1.0.3=r41hc72bb7e_0', 'r-sass==0.4.2=r41h7525677_0', 'r-scales==1.2.1=r41hc72bb7e_0', 'r-selectr==0.4_2=r41hc72bb7e_1', 'r-sessioninfo==1.2.2=r41hc72bb7e_0', 'r-shiny==1.7.2=r41h785f33e_0', 'r-slider==0.2.2=r41hcfec24a_0', 'r-sourcetools==0.1.7=r41h03ef668_1002', 'r-squarem==2021.1=r41hc72bb7e_0', 'r-stringi==1.7.8=r41h30a9eb7_0', 'r-stringr==1.4.1=r41hc72bb7e_0', 'r-survival==3.4_0=r41h06615bd_0', 'r-sys==3.4=r41hcfec24a_0', 'r-systemfonts==1.0.4=r41hef9c87a_0', 'r-testthat==3.1.4=r41h7525677_0', 'r-textshaping==0.3.6=r41h9354b80_2', 'r-tibble==3.1.8=r41h06615bd_0', 'r-tidymodels==1.0.0=r41hc72bb7e_0', 'r-tidyr==1.2.1=r41h7525677_0', 'r-tidyselect==1.1.2=r41hc72bb7e_0', 'r-tidyverse==1.3.2=r41hc72bb7e_0', 'r-timedate==4021.104=r41hc72bb7e_0', 'r-tinytex==0.41=r41hc72bb7e_0', 'r-tseries==0.10_51=r41h1463581_0', 'r-ttr==0.24.3=r41h06615bd_0', 'r-tune==1.0.0=r41hc72bb7e_0', 'r-tzdb==0.3.0=r41h7525677_0', 'r-urca==1.3_0=r41h8da6f51_1006', 'r-urlchecker==1.0.1=r41hc72bb7e_0', 'r-usethis==2.1.6=r41hc72bb7e_0', 'r-utf8==1.2.2=r41hcfec24a_0', 'r-uuid==1.1_0=r41h06615bd_0', 'r-vctrs==0.4.1=r41h7525677_0', 'r-viridislite==0.4.1=r41hc72bb7e_0', 'r-vroom==1.5.7=r41h03ef668_0', 'r-waldo==0.4.0=r41hc72bb7e_0', 'r-warp==0.2.0=r41hcfec24a_1', 'r-whisker==0.4=r41hc72bb7e_1', 'r-withr==2.5.0=r41hc72bb7e_0', 'r-workflows==1.1.0=r41hc72bb7e_0', 'r-workflowsets==1.0.0=r41hc72bb7e_0', 'r-xfun==0.33=r41h7525677_0', 'r-xml2==1.3.3=r41h7525677_1', 'r-xopen==1.0.0=r41hc72bb7e_1003', 'r-xtable==1.8_4=r41hc72bb7e_3', 'r-xts==0.12.1=r41h06615bd_0', 'r-yaml==2.3.5=r41h06615bd_0', 'r-yardstick==1.1.0=r41h06615bd_0', 'r-zip==2.2.1=r41h06615bd_0', 'r-zoo==1.8_11=r41h06615bd_0', 'readline==8.1.2=h0f457ee_0', 'reproc==14.2.3=h7f98852_0', 'reproc-cpp==14.2.3=h9c3ff4c_0', 'requests==2.28.1=pyhd8ed1ab_1', 'requests-toolbelt==0.9.1=py_0', 'rpy2==3.5.1=py310r41hde88566_0', 'ruamel.yaml==0.17.21=py310h5764c6d_1', 'ruamel.yaml.clib==0.2.6=py310h5764c6d_1', 'ruamel_yaml==0.15.80=py310h5764c6d_1007', 'scikit-image==0.19.3=py310h769672d_1', 'scikit-learn==1.1.2=py310h0c3af53_0', 'scipy==1.9.1=py310hdfbd76f_0', 'seaborn==0.12.0=hd8ed1ab_0', 'seaborn-base==0.12.0=pyhd8ed1ab_0', 'secretstorage==3.3.3=py310hff52083_0', 'sed==4.8=he412f7d_0', 'send2trash==1.8.0=pyhd8ed1ab_0', 'setuptools==65.4.0=pyhd8ed1ab_0', 'shellingham==1.5.0=pyhd8ed1ab_0', 'simpervisor==0.4=pyhd8ed1ab_0', 'simplegeneric==0.8.1=py_1', 'six==1.16.0=pyh6c4a22f_0', 'smmap==5.0.0=pypi_0', 'snappy==1.1.9=hbd366e4_1', 'sniffio==1.3.0=pyhd8ed1ab_0', 'sortedcontainers==2.4.0=pyhd8ed1ab_0', 'soupsieve==2.3.2.post1=pyhd8ed1ab_0', 'sqlalchemy==1.4.41=py310h5764c6d_0', 'sqlparse==0.4.3=pypi_0', 'stack_data==0.5.1=pyhd8ed1ab_0', 'statsmodels==0.13.2=py310hde88566_0', 'sympy==1.10.1=py310hff52083_1', 'sysroot_linux-64==2.12=he073ed8_15', 'tabulate==0.9.0=pypi_0', 'tblib==1.7.0=pyhd8ed1ab_0', 'terminado==0.15.0=py310hff52083_0', 'threadpoolctl==3.1.0=pyh8a188c0_0', 'tifffile==2022.8.12=pyhd8ed1ab_0', 'tinycss2==1.1.1=pyhd8ed1ab_0', 'tk==8.6.12=h27826a3_0', 'tktable==2.10=hb7b940f_3', 'tomli==2.0.1=pyhd8ed1ab_0', 'tomlkit==0.11.5=pyha770c72_0', 'toolz==0.12.0=pyhd8ed1ab_0', 'tornado==6.1=py310h5764c6d_3', 'tqdm==4.64.1=pyhd8ed1ab_0', 'traitlets==5.4.0=pyhd8ed1ab_0', 'typing==3.10.0.0=pyhd8ed1ab_0', 'typing-extensions==4.3.0=hd8ed1ab_0', 'typing_extensions==4.3.0=pyha770c72_0', 'tzdata==2022d=h191b570_0', 'tzlocal==4.2=py310hff52083_1', 'unicodedata2==14.0.0=py310h5764c6d_1', 'unixodbc==2.3.10=h583eb01_0', 'urllib3==1.26.11=pyhd8ed1ab_0', 'virtualenv==20.16.5=py310hff52083_0', 'wcwidth==0.2.5=pyh9f0ad1d_2', 'webencodings==0.5.1=py_1', 'websocket-client==1.4.1=pyhd8ed1ab_0', 'werkzeug==2.2.2=pypi_0', 'wheel==0.37.1=pyhd8ed1ab_0', 'widgetsnbextension==4.0.3=pyhd8ed1ab_0', 'xlrd==2.0.1=pyhd8ed1ab_3', 'xorg-kbproto==1.0.7=h7f98852_1002', 'xorg-libice==1.0.10=h7f98852_0', 'xorg-libsm==1.2.3=hd9c2040_1000', 'xorg-libx11==1.7.2=h7f98852_0', 'xorg-libxau==1.0.9=h7f98852_0', 'xorg-libxdmcp==1.1.3=h7f98852_0', 'xorg-libxext==1.3.4=h7f98852_1', 'xorg-libxrender==0.9.10=h7f98852_1003', 'xorg-libxt==1.2.1=h7f98852_2', 'xorg-renderproto==0.11.1=h7f98852_1002', 'xorg-xextproto==7.3.0=h7f98852_1002', 'xorg-xproto==7.0.31=h7f98852_1007', 'xz==5.2.6=h166bdaf_0', 'yaml==0.2.5=h7f98852_2', 'yaml-cpp==0.7.0=h27087fc_1', 'yarl==1.7.2=py310h5764c6d_2', 'zeromq==4.3.4=h9c3ff4c_1', 'zfp==1.0.0=h27087fc_1', 'zict==2.2.0=pyhd8ed1ab_0', 'zipp==3.8.1=pyhd8ed1ab_0', 'zlib==1.2.12=h166bdaf_3', 'zlib-ng==2.0.6=h166bdaf_0', 'zstd==1.5.2=h6239696_4']

    conda-forge/linux-64                                        Using cache
    conda-forge/noarch                                          Using cache
    Encountered problems while solving:
    - nothing provides requested databricks-cli ==0.17.3 pypi_0
    - nothing provides requested docker ==6.0.0 pypi_0
    - nothing provides requested flask ==2.2.2 pypi_0
    - nothing provides requested gitdb ==4.0.9 pypi_0
    - nothing provides requested gitpython ==3.1.28 pypi_0
    - nothing provides requested gunicorn ==20.1.0 pypi_0
    - nothing provides requested itsdangerous ==2.1.2 pypi_0
    - nothing provides requested mlflow ==1.29.0 pypi_0
    - nothing provides requested modeltools ==0.2.3 pypi_0
    - nothing provides requested numpy ==1.23.3 pypi_0
    - nothing provides requested prometheus-flask-exporter ==0.20.3 pypi_0
    - nothing provides requested querystring-parser ==1.2.4 pypi_0
    - nothing provides requested smmap ==5.0.0 pypi_0
    - nothing provides requested sqlparse ==0.4.3 pypi_0
    - nothing provides requested tabulate ==0.9.0 pypi_0
    - nothing provides requested werkzeug ==2.2.2 pypi_0

    (base) jovyan@c86d58b943e0:~/work/m02/gh-master-oct$ 

- CLAVE: que el ENTORNO sea PEQUEÑO y SENCILLO para facilitar el CLONADO de paso  PRODUCCIÓN. Esto es muy complicado porque hay muchas personas a coordinar
- NOTA: mamba env create -f environment.yml es la mejor forma de hacer el EXPORT de un ENTORNO para CLONARLO en PRODUCCIÓN
- NOTA: evitar combinar CONDA y PIP para instalar LOS MISMOS PAQUETES. 


# DOCUMENTACIÓN
