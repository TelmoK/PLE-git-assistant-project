# 11/11/2026 - Primeras pruebas con rasa

Tras conseguir montar la estructura básica de un proyecto con Rasa el modelo se ha equivocado porque el dataset no tiene suficientes ejemplos o variabilidad léxica alrededor de una entidad de Rasa. La interacción fue la siguiente:
```bash
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  crea la rama prueba-clase y muéveme ahí
git checkout -b [nombre_de_rama_faltante]
```
La respuesta esperada era `git checkout -b prueba-clase`. Para arreglar esto debemos añadir más casos y un regex, que le da una pista estructural a Rasa para identificar cadenas de texto con formato de identificador técnico, como los nombres de las ramas en Git. Este era el dataset:
```yml
version: "3.1"

nlu:
- intent: inicializar_clonar
  examples: |
    - quiero empezar un proyecto con git aquí
    - iniciar nuevo repositorio local
    - descárgame este repositorio de GitHub
    - clonar proyecto de [https://github.com](url_repo)
    - haz un clone de [https://gitlab.com](url_repo)

- intent: guardar_cambios
  examples: |
    - quiero guardar todo lo que hice con el mensaje "[fix login bug](mensaje_commit)"
    - haz commit de todo diciendo "[cambios finales de interfaz](mensaje_commit)"
    - guarda mis modificaciones locales con el texto "[refactor codigo](mensaje_commit)"
    - sube mis cambios al historial con mensaje "[primera version](mensaje_commit)"

- intent: crear_rama
  examples: |
    - crea la rama [feature-login](nombre_rama) y muéveme ahí
    - nueva rama llamada [desarrollo](nombre_rama)
    - quiero una rama que se llame [bugfix-logout](nombre_rama) y cambiar a ella
    - muévete a una nueva rama [test-api](nombre_rama)
```
Lo cambiamos a este más extenso:
```yml
version: "3.1"

nlu:
- intent: inicializar_clonar
  examples: |
    - quiero empezar un proyecto con git aquí
    - iniciar nuevo repositorio local
    - inicializa git en esta carpeta
    - descárgame este repositorio de GitHub
    - clonar proyecto de [https://github.com](url_repo)
    - haz un clone de [https://gitlab.com](url_repo)
    - descarga el repo [https://github.com](url_repo)

- intent: guardar_cambios
  examples: |
    - quiero guardar todo lo que hice con el mensaje "[fix login bug](mensaje_commit)"
    - haz commit de todo diciendo "[cambios finales de interfaz](mensaje_commit)"
    - guarda mis modificaciones locales con el texto "[refactor codigo](mensaje_commit)"
    - sube mis cambios al historial con mensaje "[primera version](mensaje_commit)"
    - haz un commit con el mensaje "[arreglado el error](mensaje_commit)"
    - guarda los cambios poniendo "[avance del proyecto](mensaje_commit)"
    - commitea todo con "[actualizacion de readme](mensaje_commit)"

- intent: crear_rama
  examples: |
    - crea la rama [feature-login](nombre_rama) y muéveme ahí
    - nueva rama llamada [desarrollo](nombre_rama)
    - quiero una rama que se llame [bugfix-logout](nombre_rama) y cambiar a ella
    - muévete a una nueva rama [test-api](nombre_rama)
    - crea una rama [nueva-funcionalidad](nombre_rama)
    - abre la rama [fix-css](nombre_rama) y cámbiate a ella
    - haz una rama llamada [dev-branch](nombre_rama)
    - crear rama [release-v1](nombre_rama) y moverme ahí
    - pásame a una rama nueva que sea [pruebas-locales](nombre_rama)
    - crea la rama [mi-rama](nombre_rama)

- regex: nombre_rama
  examples: |
    - [a-zA-Z0-9_-]+
```
Ahora gracias a este ajuste el modelo ha corregido el error:
```bash
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  crea la rama prueba-clase y muéveme ahí
git checkout -b prueba-clase
```