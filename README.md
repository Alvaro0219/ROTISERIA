# Documentación de la Aplicación de Rotisería

## Introducción

Esta aplicación es una solución para gestionar una rotisería, desde la visualización de productos hasta la administración de inventario. El backend está desarrollado en Django, proporcionando una API RESTful, mientras que el frontend está implementado en Vue.js.

## Objetivo

El objetivo principal de esta aplicación es permitir a los propietarios y empleados llevar un registro detallado de los productos disponibles, así como facilitar la inclusión de nuevos productos en el menú.

## Características

- **Visualización de Categorías:** La aplicación recupera categorías desde el backend y las muestra de forma organizada en el frontend, facilitando la navegación y búsqueda de productos.
- **Gestión de Productos:** Los usuarios pueden explorar una lista completa de productos disponibles en la rotisería, incluyendo detalles como nombre, precio y descripción. Además, la aplicación permite a los administradores cargar nuevos productos de manera sencilla.
- **Integración Backend-Frontend:** El backend, desarrollado en Django, proporciona una API RESTful que permite una comunicación eficiente entre el frontend y el backend, asegurando que los datos se mantengan sincronizados y actualizados.

## Backend (Django)

### Modelos

- **Modelo de Categorías (Category):** Representa las categorías de los productos en la aplicación. Cada categoría tiene un nombre.
- **Modelo de Productos (Product):** Representa los productos disponibles en la rotisería. Los productos tienen un nombre, una imagen, una categoría, una descripción, un precio y un tipo de precio.

### Vistas (basadas en clases)

- **Vista de Productos (ProductViewSet):** Maneja la gestión de los productos en la aplicación, proporcionando funcionalidad CRUD (Crear, Leer, Actualizar, Borrar) para los productos.
- **Vista de Categorías (CategoryViewSet):** Gestiona las categorías de productos en la aplicación.

### Serializadores (Serializers)

- **Serializador de Productos (ProductSerializer):** Convierte los objetos del modelo Product en datos JSON para su uso en la API REST.
- **Serializador de Categorías (CategorySerializer):** Convierte los objetos del modelo Category en datos JSON para su uso en la API REST.

### Filtros de Productos (ProductFilter)

- Permite realizar filtrado personalizado de productos a través de la API REST.

## Frontend (Vue.js)

### Archivo Vue Principal (App.vue)

- Define la estructura general de la aplicación, incluyendo la barra de navegación, la sección de navegación, la vista de enrutamiento y el pie de página.

### Componentes

- **NavbarComponent:** Representa la barra de navegación superior de la aplicación.
- **NavigationComponent:** Muestra el título "Rotisería" y botones para seleccionar categorías de productos.

### Vistas

- **Vista principal (HomeView.vue):** Representa la página principal de la tienda de rotisería, mostrando una lista de productos y opciones de filtrado por categoría o búsqueda.
- **Vista de Carga de Producto (UploadProducts.vue):** Permite a los usuarios agregar nuevos productos a la tienda de rotisería.

### Enrutador (router/index.js)

- Define las rutas y sus componentes asociados para la navegación en la aplicación Vue.js.

Esta documentación proporciona una visión general de la estructura y funcionalidades de la aplicación de rotisería, tanto en el backend como en el frontend.
