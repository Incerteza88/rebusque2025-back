# Rebusque2025 Backend

## Estructura de carpetas

```

rebusque2025-back/
├── src/
│   ├── templates/
│   │   └── index.html
│   ├── **init**.py
│   ├── admin.py
│   ├── models.py
│   └── routes.py
├── .env
├── .gitignore
├── app.py
├── Pipfile
└──  README.md

````

- `app.py`: Archivo principal de la aplicación Flask.  
- `src/`: Contiene el código fuente del backend (modelos, rutas, administración).  
- `Pipfile`: Define las dependencias del proyecto.  
- `index.html`: Archivo HTML de referencia.  

## Uso rápido

1. Instala las dependencias:
   ```bash
   pipenv install
````

2. Activa el entorno virtual:

   ```bash
   pipenv shell
   ```
3. Aplica migraciones (omite este paso si no has realizado cambios en `./src/models.py`):

   ```bash
   pipenv run migrate
   pipenv run upgrade
   ```
4. Ejecuta la aplicación:

   ```bash
   pipenv run start
   ```

```
Para que el panel de administración (/admin) redireccione correctamente en GitHub Codespaces, debes copiar la URL completa del puerto que se muestra en tu navegador y agregarla al archivo .env.

Abre tu proyecto en GitHub Codespaces y levanta el servidor.

Copia la URL de la barra de direcciones de tu navegador. La URL debería ser similar a esta: https://crispy-robot-q74qgr6pvpx397px-3001.app.github.dev

Abre el archivo .env en la raíz de tu proyecto.

Pega la URL en la variable BASE_URL.
