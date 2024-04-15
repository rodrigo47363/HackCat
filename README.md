# Hack Cat Bot

Hack Cat Bot es un bot de Discord desarrollado en Python utilizando la biblioteca discord.py. Este bot ofrece características como un sistema de niveles, economía virtual y comandos de administración para gestionar roles y permisos.

## Características

- Sistema de niveles basado en experiencia.
- Sistema de economía virtual.
- Comandos de administración para gestionar roles y permisos.
- Integración con la base de datos SQLite para almacenar datos de usuario y economía.

## Requisitos

- Python 3.7 o superior
- Pip (Gestor de paquetes de Python)
- Biblioteca discord.py
- Biblioteca aiosqlite

## Instalación

1. Clona este repositorio en tu máquina local:

```
git clone https://github.com/rodrigo47363/HackCat
```

2. Instala las dependencias usando pip:

```
pip install -r requirements.txt
```

3. Configura el token de Discord en el archivo `config.py`:

```python
TOKEN = 'tu_token_de_discord'
```

4. Ejecuta el bot:

```
python bot.py
```

## Uso

El bot utiliza el prefijo `>` para sus comandos. Asegúrate de tener los permisos adecuados para ejecutar ciertos comandos de administración.

Algunos comandos disponibles:

- `>nivel [@usuario]`: Muestra el nivel y la experiencia de un usuario.
- `>depositar [@usuario] [cantidad]`: Deposita una cantidad específica de monedas en la cuenta de un usuario (requiere permisos de administrador).

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Sube tus cambios a tu repositorio (`git push origin feature/nueva-caracteristica`).
5. Crea un pull request en GitHub.

## Créditos

Desarrollado por [Tu Nombre](https://github.com/rodrigo47363).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
```

Este README incluye una descripción más detallada de las características del bot, una sección de requisitos más clara, instrucciones de instalación más específicas y un formato mejorado para la sección de uso y contribución. Espero que esta versión sea más adecuada para tu proyecto. Si necesitas más ajustes o tienes alguna otra solicitud, estaré encantado de ayudarte.
