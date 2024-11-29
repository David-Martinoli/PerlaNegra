# ¡Bienvenido a Reflex!

Esta es la plantilla base de Reflex - instalada cuando ejecutas `reflex init`.

Si deseas usar una plantilla diferente, pasa la bandera `--template` a `reflex init`.
Por ejemplo, si quieres un punto de partida más básico, puedes ejecutar:

```bash
reflex init --template blank
```

## Acerca de esta Plantilla

Esta plantilla tiene la siguiente estructura de directorios:

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
    │   ├── about.py
    │   ├── index.py
    │   ├── profile.py
    │   ├── settings.py
    │   └── table.py
    ├── styles.py
    ├── templates
    │   ├── __init__.py
    │   └── template.py
    └── {tu_app}.py
```

Consulta la [documentación de Estructura del Proyecto](https://reflex.dev/docs/getting-started/project-structure/) para más información sobre la estructura general de proyectos Reflex.

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
