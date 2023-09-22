# Despliegue de modelos de Machine Learning en producción
## Introducción
En este repositorio se encuentra el código necesario para desplegar un modelo de Machine Learning en producción. El objetivo es predecir cantidad de dinero que genera una pelicula a traves de una API. 

¿En qué consiste el proyecto?

* Predecir la cantidad de dinero que genera una película a través de una API
* Reproducir todo el flujo de puesta en producción de un modelo
* Aplica entrenamiento continuo
* Desplegar continuamente usando CI/CD

![proyecto](images/project.png)

## Estructura del proyecto
El proyecto se ha estructurado de la siguiente manera:
- **app**: Contiene el código de la API.
- **data**: Contiene el dataset de Titanic.
- **images**: Contiene las imágenes del proyecto.
- **model**: Contiene el modelo de Machine Learning.
- **notebooks**: Contiene los notebooks de Jupyter.
- **src**: Contiene el código de la API.

## Arquitectura del proyecto
La arquitectura del proyecto es la siguiente:

![arquitectura](images/Arquitecture.png)

se va a trabajar en *Github*, alli vammos a tener 3 activaciones, por medio de *Github actions*, se van a activar tres *workflows* diferentes:

1. **Testing:** se va a encargar de ejecutar los test unitarios, para verificar que el código que se está escribiendo es correcto.

2. **CI / CD:** se va a encargar de ejecutar el proceso de integración continua para *Docker* y despliegue continuo hasta *cloud Run* utilizando una *API* basada en *Fast API*.

3. **Entrnamiento:** va a utilizar *Scikit learn* para entrenar un modelo de *Machine Learning*, *Data Version Cotrol (DVC)* para versionar los datos y *Continue Machine Learning* para publicar las metricas de *performance* del modelo.