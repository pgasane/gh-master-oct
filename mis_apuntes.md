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

# Creo una nueva Release v0.2.4 porque había un fallo en el build (el punto dichoso al final) que ha impedido que se crearan los binarios
