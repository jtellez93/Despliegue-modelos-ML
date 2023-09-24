# Despliegue de modelos de Machine Learning en producción
## Introducción
En este repositorio se encuentra el código necesario para desplegar un modelo de Machine Learning en producción. El objetivo es predecir cantidad de dinero que genera una pelicula a traves de una API. 

¿En qué consiste el proyecto?

* Predecir la cantidad de dinero que genera una película a través de una API
* Reproducir todo el flujo de puesta en producción de un modelo
* Aplica entrenamiento continuo
* Desplegar continuamente usando CI/CD

![proyecto](images/project.png)

## Arquitectura del proyecto
La arquitectura del proyecto es la siguiente:

![arquitectura](images/Arquitecture.png)

se va a trabajar en *Github*, alli vammos a tener 3 activaciones, por medio de *Github actions*, se van a activar tres *workflows* diferentes:

1. **Testing:** se va a encargar de ejecutar los test unitarios, para verificar que el código que se está escribiendo es correcto.

2. **CI / CD:** se va a encargar de ejecutar el proceso de integración continua para *Docker* y despliegue continuo hasta *cloud Run* utilizando una *API* basada en *Fast API*.

3. **Reentrenamiento:** va a utilizar *Scikit learn* para reentrenar un modelo de *Machine Learning*, *Data Version Cotrol (DVC)* para versionar los datos y *Continue Machine Learning* para publicar las metricas de *performance* del modelo.

## Distribucion de archivos
- **dvc:** contiene los archivos de configuracion de [*DVC*](DVC.md)
- **github/workflows:** contiene los archivos de configuracion de *github actions*
- **api:** *API* basada en *Fast API*
- **dataset:** Archivos del dataset traqueados por *DVC*
- **model:** Archivos del modelo traqueados por *DVC*
- **notebooks:** Notebooks de *Jupyter* para el entrenamiento del modelo
- **src:** Archivos usados para reentrenamiento del modelo
- **utilities:** Archivos de utilidades especificos para el proyecto
- **Archivos miscelaneos:** *Dockerfile*

## Reentrenamiento del modelo
- **Prepare.py:** Recupera y prepara los datos para el entrenamiento del modelo.
- **Train.py:** Entrena el modelo y lo guarda en el directorio *model*, ademas de generar las metricas de *performance*.
- **utils.py:** Contiene funciones de utilidad para el proyecto.

### Aplicamos DVC para crear flujo de trabajo de reentrenamiento

#### Flujo de trabajo de reentrenamiento
En versiones anteriores de *DVC* se utilizaba el comando `dvc run` para crear un flujo de trabajo.  
- `-n` asigna un nombre al flujo de trabajo.  
- `label_name` es el nombre del flujo de trabajo.  
- `-o` asigna un archivo de salida.  
- `output` es el archivo de salida.  
- `script` es el script que se va a ejecutar.  

```bash	
dvc run -n <label_name> -o <output> python <script>
```

En versiones actuales de *DVC* se utiliza una estructura basada en `dvc.yaml` y etapas *DVC* (`dvc.yaml` y `dvc.lock`).

Se crea un archivo `dvc.yaml` en la raiz del proyecto, en el se definen las etapas de *DVC* que se van a ejecutar.
```yaml
stages:
  prepare: # nombre de la etapa
    cmd: python <script> # script que se va a ejecutar 
    deps: # archivos de entrada
      - <input>
    outs: # archivos de salida
      - <output>
  train: # nombre de la etapa
    cmd: python <script> # script que se va a ejecutar
    deps: # archivos de entrada
      - <input>
    outs: # archivos de salida
      - <output>
```
> Nota: DVC utiliza Git para rastrear cambios en los archivos de configuración, pero los datos y resultados generados por DVC deben ser gestionados exclusivamente por DVC para evitar conflictos.

 Para resolver este problema, debes detener el rastreo del archivo en Git
```bash
git rm -r  --cached <archivo>
```
confirma los cambios
```bash
git commit -m "stop tracking <archivo>"
```

#### Ejecutar flujo de trabajo de reentrenamiento
Una vez esta todo orquestado, por medio de *DVC* se ejecuta el flujo de trabajo de reentrenamiento.
```bash
dvc repro
```
forzar la ejecucion del flujo
```bash
dvc repro -f
```
ver los `dags` de *DVC*, estos son los flujos de trabajo que se han ejecutado.
```bash
dvc dag
```

## Despliegue de la API
Para crear la *API* lo hacemos bajo la siguiente estructura:
- **main:** crea un servicio web que puede recibir solicitudes POST en la ruta `"/v1/prediction"`, y cuando recibe una solicitud, utiliza la función `get_prediction` para realizar una predicción y devuelve la predicción como respuesta en un formato específico definido por `Prediction_Response`.
- **views:** Realizar una predicción con la funcion `get_prediction` utilizando un modelo de machine learning previamente cargado y un conjunto de datos proporcionados en la solicitud.
- **models:** Define dos clases `Prediction_Request` y `Prediction_Response` utilizando el módulo `pydantic`, que se utilizan para definir la estructura de los datos de entrada y salida para un servicio web.
- **utils:** Archivos de utilidades especificas de la *API*