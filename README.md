# ¡Bienvenido a SistIntegPerlaNegra!

Este es un sistema de gestion para la empresa Sistema integral Perla Negra.

## Acerca de la estructura del proyecto

```bash
├── README.md
├── assets
├── rxconfig.py
└── {tu_app}
    ├── __init__.py
    ├── components
    │   ├── __init__.py
    │   ├── navbar.py
    │   └── sidebar.py
    ├── pages
    │   ├── __init__.py
    │   ├── admin
    │   │   ├── __init__.py
    │   │   ├── 
    │   ├── user
    │   │   ├── __init__.py
    │   │   ├── 
    │   ├── about.py
    │   ├── index.py
    │   ├── profile.py
    │   ├── settings.py
    │   └── table.py
    ├── styles.py
    ├── templates
    │   ├── __init__.py
    │   └── template.py
    ├── {tu_app}.py
    ├── database/
    │   ├── __init__.py
    │   ├── config/
    │   │   ├── __init__.py
    │   │   └── settings.py      # Configuración de DB, URLs, etc.
    │   │
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── base_model.py    # Modelo base con campos comunes
    │   │   ├── user.py
    │   │   └── mixins/          # Mixins reutilizables
    │   │       ├── __init__.py
    │   │       └── timestamp_mixin.py
    │   │
    │   ├── migrations/
    │   │   ├── __init__.py
    │   │   ├── env.py
    │   │   ├── script.py.mako
    │   │   └── versions/
    │   │       └── *.py
    │   │
    │   ├── repositories/
    │   │   ├── __init__.py
    │   │   ├── base.py          # Repositorio base
    │   │   └── user.py
    │   │
    │   └── services/
    │       ├── __init__.py
    │       └── db_service.py      # Gestión de conexiones y sesiones
```

### Agregar Páginas

En esta plantilla, las páginas de tu aplicación se definen en `{tu_app}/pages/`.
Cada página es una función que devuelve un componente de Reflex.
Por ejemplo, para editar esta página puedes modificar `{tu_app}/pages/index.py`.
Consulta la [documentación de páginas](https://reflex.dev/docs/pages/routes/) para más información sobre las páginas.

En esta plantilla, en lugar de usar `rx.add_page` o el decorador `@rx.page`,
usamos el decorador `@template` de `{tu_app}/templates/template.py`.

Para agregar una nueva página:

1. Agrega un nuevo archivo en `{tu_app}/pages/`. Recomendamos usar un archivo por página, pero también puedes agrupar páginas en un solo archivo.
2. Agrega una nueva función con el decorador `@template`, que toma los mismos argumentos que `@rx.page`.
3. Importa la página en tu archivo `{tu_app}/pages/__init__.py` y se añadirá automáticamente a la aplicación.
4. Ordena las páginas en `{tu_app}/components/sidebar.py` y `{tu_app}/components/navbar.py`.

### Agregar Componentes

Para mantener tu código organizado, recomendamos colocar los componentes que se utilizan en múltiples páginas en el directorio `{tu_app}/components/`.

En esta plantilla, tenemos un componente de barra lateral en `{tu_app}/components/sidebar.py`.

### Agregar Estado

A medida que tu aplicación crece, recomendamos usar [subestados](https://reflex.dev/docs/substates/overview/)
para organizar tu estado.

Puedes definir subestados en sus propios archivos, o si el estado es específico de una página, puedes definirlo en el archivo de la página misma.

#### SistIntegPerlaNegra Ejecutando Reflex en Linux

```bash
sudo apt install python3-venv python3-pip
python3 -m venv .env
source .venv/Scripts/activate
python -m pip install -U pip
pip install reflex alembic reflex-local-auth 
```
Desde cursor si al activar el entorno virtual da error se debe ejecutar:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
o
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

Para instalar dependencias desde requirements.txt:
```bash
pip install -r requirements.txt
```

Para generar un nuevo requirements.txt:
```bash
pip freeze > requirements.txt
```

Actualización de Dependencias (si es necesario)
```bash
python.exe -m pip install --upgrade pip
pip install --upgrade reflex alembic reflex-local-auth
```

Para ejecutar la aplicación:
```bash
reflex run
```


##### Migraciones
```bash
  reflex db init  inicializa la base de datos
  init            Crear esquema de base de datos y configuración de migración.
  migrate         Crear o actualizar esquema de base de datos desde scripts de migración.
  makemigrations  Crear scripts de migración alembic autogenerados.

  reflex db makemigrations --message 'something changed'
```

Migraciones
Reflex aprovecha alembic para gestionar los cambios en el esquema de la base de datos.

Antes de poder usar la función de base de datos en una nueva aplicación, debe llamar reflex db init para inicializar alembic y crear un script de migración con el esquema actual.

Después de realizar cambios en el esquema, utilice reflex db makemigrations --message 'something changed' para generar un script en el alembic/versionsdirectorio que actualizará el esquema de la base de datos. Se recomienda inspeccionar los scripts antes de aplicarlos.

El reflex db migratecomando se utiliza para aplicar scripts de migración para actualizar la base de datos. Durante el inicio de la aplicación, si Reflex detecta que el esquema de la base de datos actual no está actualizado, se mostrará una advertencia en la consola.