## Instalación de Rasa

Para poder utilizar la herramienta clásica es necesario instalar `rasa` (versión open source), para esto es necesario tener instalada una versión de python como la 3.10 o inferior, ya que versiones posteriores solo son compatibles para `rasa-pro`. En caso de disponer de una versión superior a la 3.11 se deberá especificar en la línea de comandos:

- **Instala Python 3.10 (Sin borrar el 3.11)**:  
    Al instalarlo, asegúrate de no marcar la opción "Add python.exe to PATH" si no quieres que sustituya a tu versión superior predeterminada.

- **Forzar al entorno virtual a usar la versión 3.10**:
    - Si estás en windows usa 
        ```bash
        py -3.10 -m venv rasa_open_env # Especificamos que vamos a usar una versión específica instalada en el equipo
        # Si lo anterior falla: py -3.10 -m pip install --upgrade pip

        rasa_open_env\Scripts\activate
        ```
    - Si estás en  Linux / macOS usa 
        ```bash
        python3.10 -m venv rasa_open_env
        source rasa_open_env/bin/activate
        ```

Con el entorno configurado ejecutamos los siguientes comandos para instalar:
```bash
pip install --upgrade pip
pip install rasa
```

## Entrenamiento de Rasa

Lo primero es tener la estructura de carpetas siguiente para ejecutar Rasa:
```
proyecto-asistente-git/
├── actions/
│   ├── __init__.py
│   └── actions.py
├── data/
│   ├── nlu.yml
│   └── rules.yml
├── config.yml
├── domain.yml
└── endpoints.yml             # Script principal (orquestador de los servicios)

```
Para entrenar al modelo de rasa hay que ejecutar el siguiente comando:
```bash
rasa train
```

## Probar diálogo con Rasa

Para trabajar con el chat de Rasa es necesario lanzar el servidor con el que trabaja en otra terminal (no hay que olvidar activar el entorno de python):
```bash
rasa run actions
```
Una vez hallamos encendido el proceso nos podemos conectar a el accediendo a su puerto de escucha a través del siguiente comando para iniciar un intercambio de mensajes:
```bash
rasa shell
```