# Comandos y elementos comunes en archivos YAML 

Aquí tienes una descripción de los comandos y elementos comunes utilizados en archivos `YAML` para definir flujos de trabajo en plataformas como `GitHub Actions` y en otras herramientas de `CI/CD (continuos integration/continuous delivery)`:

1. **`name`**: Un campo utilizado para proporcionar un nombre descriptivo o etiqueta para una acción o tarea en el flujo de trabajo. No tiene un propósito funcional en sí mismo, pero ayuda a identificar y documentar lo que hace una acción en el flujo de trabajo.

2. **`on`**: Define cuándo se debe ejecutar el flujo de trabajo. Puede configurarse para activarse en respuesta a eventos específicos, como `push` (cuando se realiza una confirmación), `pull_request` (cuando se abre una solicitud de extracción) u otros eventos personalizados.

3. **`jobs`**: Define los trabajos que se ejecutarán como parte del flujo de trabajo. Cada trabajo es una unidad independiente de tareas y puede tener su propio conjunto de pasos.

4. **`runs-on`**: Especifica la plataforma o el entorno en el que se ejecutará un trabajo. Por ejemplo, `ubuntu-latest` indica que el trabajo se ejecutará en una instancia de Ubuntu en su versión más reciente.

5. **`steps`**: Define una secuencia de pasos que se ejecutarán en un trabajo. Cada paso representa una acción o tarea específica en el flujo de trabajo.

6. **`uses`**: En GitHub Actions, se utiliza para especificar la acción de GitHub o el repositorio que se debe ejecutar en un paso del flujo de trabajo. En otros contextos, puede referirse a una secuencia de comandos o una herramienta específica que se ejecutará en el paso.

7. **`with`**: En GitHub Actions, este campo se utiliza para proporcionar opciones o variables específicas para una acción. Por ejemplo, `with` puede utilizarse para especificar la versión de `Node.js` que se utilizará en un paso.

8. **`env`**: En GitHub Actions, se utiliza para definir variables de entorno que estarán disponibles para una acción o un paso. Esto es útil para configurar variables de entorno necesarias para la ejecución de una acción.

9. **`run`**: En GitHub Actions, este campo se utiliza para especificar los comandos que se ejecutarán en un paso. Estos comandos pueden ser scripts o comandos individuales que realizan tareas específicas.

Estos son algunos de los elementos y comandos comunes que se utilizan en archivos `YAML` para definir flujos de trabajo en plataformas de `CI/CD`. La estructura y los campos específicos pueden variar según la plataforma o herramienta que estés utilizando, por lo que es importante consultar la documentación de la herramienta en particular para obtener detalles precisos sobre cómo crear archivos YAML válidos y funcionales para tu flujo de trabajo.

## Ejemplo de archivo YAML

```yaml
name: ML CI/CD Workflow

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    name: Build and Deploy Model
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install Dependencies
      run: |
        pip install -r requirements.txt
      working-directory: ./ml_app

    - name: Train Model
      run: |
        python train.py
      working-directory: ./ml_app

    - name: Test Model
      run: |
        python test.py
      working-directory: ./ml_app

    - name: Deploy Model
      run: |
        # Aquí irían los comandos para implementar el modelo en una plataforma de hosting de modelos, como AWS SageMaker, Google AI Platform, etc.
      working-directory: ./ml_app

    - name: Cleanup
      run: |
        # Aquí pueden ir comandos de limpieza, por ejemplo, para eliminar archivos temporales.
```


