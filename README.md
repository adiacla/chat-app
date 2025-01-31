# Aplicación de chat con Gemini API

## Tabla de Contenidos

- [Introducción](#introduccion)
- [Instalación](#instalacion)
  - [(Opción 1) Instalación con Node.js](#opcion-1-instalacion-con-nodejs)
  - [(Opción 2) Instalación con Python](#opcion-2-instalacion-con-python)
  - [(Opción 3) Instalación con Go](#opcion-3-instalacion-con-go)
- [Ejecutar la aplicación](#ejecutar-la-aplicacion)
  - [Ejecutar el cliente React](#ejecutar-el-cliente-react)
  - [Ejecutar un servidor backend](#ejecutar-un-servidor-backend)
    - [Obtener una clave API](#obtener-una-clave-api)
    - [(Opción 1) Configurar y ejecutar el backend con Node.js](#opcion-1-configurar-y-ejecutar-el-backend-con-nodejs)
    - [(Opción 2) Configurar y ejecutar el backend con Python](#opcion-2-configurar-y-ejecutar-el-backend-con-python)
    - [(Opción 3) Configurar y ejecutar el backend con Go](#opcion-3-configurar-y-ejecutar-el-backend-con-go)
- [Uso](#uso)
- [Documentación de la API](#documentacion-de-la-api)

## Introducción

Esta aplicación de ejemplo permite al usuario chatear con la API de Gemini y usarla como un asistente de IA personal. La aplicación admite chat solo de texto en dos modos: sin streaming y con streaming.

En el modo sin streaming, se devuelve una respuesta después de que el modelo complete todo el proceso de generación de texto.

El modo con streaming utiliza la capacidad de transmisión de la API de Gemini para lograr interacciones más rápidas.

#Obtener una clave de API
Necesitas una clave de API de Google Gemini para poder ejecutar el proyecto, que puedes obtener en la página de configuración de la API de Google Gemini.

https://aistudio.google.com/apikey




# Backend

Existen tres implementaciones del servidor backend entre las cuales elegir:

* Un servidor en Python con [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/), que demuestra el uso del
  [Gemini API Python SDK](https://github.com/google-gemini/generative-ai-python)
* Un servidor en Node.js, que demuestra el uso del
  [Gemini API JavaScript SDK](https://github.com/google-gemini/generative-ai-js)
* Un servidor en Go, que demuestra el uso del
  [Gemini API Go SDK](https://github.com/google/generative-ai-go)

Solo necesitas instalar y ejecutar *uno* de los backends. Si deseas probar más de uno, ten en cuenta que todos usan el mismo puerto por defecto.

## Instalación 

Sigue las instrucciones de instalación para uno de los servidores backend (Node.js, Python o Go).

## Instalación de Node.js

Para instalar Node.js y npm en Ubuntu 24.04, tienes varias opciones. A continuación, se detallan tres métodos comunes:

Método 1: Usar el Repositorio Predeterminado de Ubuntu

Actualizar el índice de paquetes:
```bash
sudo apt update
```
Instalar Node.js y npm:
```bash

sudo apt install nodejs npm
```
Verificar la instalación:
```bash

node -v
npm -v
```

## Servidor  node.js 

Antes de ejecutar los pasos de instalación, asegúrate de tener instalado Node.js v18+ y npm en tu entorno de desarrollo.

1. Navega al directorio de la aplicación, `server-js` (donde se encuentra `package.json`).
2. Ejecuta `npm install`.

### (Opción 2* Recomenda para este curso) Instalación con Python

Antes de ejecutar los pasos de instalación, asegúrate de tener instalado Python 3.9+ en tu entorno de desarrollo. Luego, navega al directorio de la aplicación, `server-python`, y completa la instalación.

#### Crear un entorno virtual

##### Linux/macOS

```python
python3 -m venv venv  #o solo python depende de la version instalada
```
```python
source venv/bin/activate
```

##### Windows

```
python -m venv venv
.\venv\Scripts\activate
```

#### Instalar los paquetes requeridos

Ingrese a la carpeta de server-python y allí ejecute la instalacion de los parquetes.

##### Linux/macOS/Windows

```
pip install -r requirements.txt
```

### (Opción 3) Instalación con Go

Verifica si Go 1.20+ está instalado en tu sistema.

```
go version
```

Si Go 1.20+ no está instalado, sigue las instrucciones según tu sistema operativo en la [guía de instalación de Go](https://go.dev/doc/install). Las dependencias del backend se instalarán cuando ejecutes la aplicación.

## Ejecutar la aplicación

Para iniciar la aplicación:

1. Ejecuta el cliente React.
2. Ejecuta el servidor backend de tu elección.


### Frontend

El cliente de esta aplicación está desarrollado con [React](https://react.dev/) y se sirve utilizando [Vite](https://github.com/vitejs/vite).

### Ejecutar el cliente React

1. Navega al directorio de la aplicación, `client-react/`.
2. Ejecuta la aplicación con el siguiente comando:

   ```
   npm run start
   ```

El cliente se iniciará en `localhost:3000`.



### Ejecutar un servidor backend

Para ejecutar el backend, necesitas obtener una clave API y luego seguir las instrucciones de configuración y ejecución para *uno* de los servidores backend (Node.js, Python o Go).

#### Obtener una clave API

Antes de poder usar la API de Gemini, debes obtener una clave API. Si aún no tienes una, créala con un solo clic en Google AI Studio.

<a class=button button-primary href=https://ai.google.dev/gemini-api/docs/api-key target=_blank rel=noopener noreferrer>Obtener una clave API</a>

#### (Opción 1) Configurar y ejecutar el backend con Node.js

Configura la aplicación Node.js:

1. Navega al directorio de la aplicación, `server-js/`.
2. Copia el archivo `.env.example` a `.env`.
   ```
   cp .env.example .env
   ```
3. Especifica la clave API de Gemini para la variable `GOOGLE_API_KEY` en el archivo `.env`.
   ```
   GOOGLE_API_KEY=<tu_api_key>
   ```

Ejecuta la aplicación Node.js:

```
node --env-file=.env app.js
```

Por defecto, la aplicación se ejecutará en el puerto 9000.

#### (Opción 2) Configurar y ejecutar el backend con Python

Configura la aplicación Python:

1. Navega al directorio de la aplicación, `server-python/`.
2. Asegúrate de haber activado el entorno virtual.
3. Copia el archivo `.env.example` a `.env`.
   ```
   cp .env.example .env
   ```
4. Especifica la clave API en el archivo `.env`.
   ```
   GOOGLE_API_KEY=<tu_api_key>
   ```

Ejecuta la aplicación Python:

```
python app.py
```

El servidor se iniciará en `localhost:9000`.

#### (Opción 3) Configurar y ejecutar el backend con Go

1. Navega al directorio de la aplicación, `server-go/`.
2. Ejecuta la aplicación con el siguiente comando:
   ```
   GOOGLE_API_KEY=<tu_api_key> go run .
   ```

El servidor se iniciará en `localhost:9000`.

## Uso

Para comenzar a usar la aplicación, visita [http://localhost:3000](http://localhost:3000/)

## Documentación de la API

(La documentación de los endpoints sigue igual en formato tabla).


