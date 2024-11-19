# ScanPhonePy

**ScanPhonePy** es una herramienta escrita en Python que permite analizar números de teléfono en formato internacional. Obtiene información como el país, la ubicación, el operador, el tipo de línea y la zona horaria sin usar APIs externas.

## Características

- Identificación del país del número de teléfono.
- Determinación de la ubicación general.
- Detección del operador telefónico.
- Clasificación del tipo de línea (móvil, fija, VOIP, etc.).
- Obtención de la zona horaria asociada.

## Requisitos Previos

Antes de usar **ScanPhonePy**, asegúrate de tener instalado:

- Python 3.7 o superior
- `pip` (gestor de paquetes de Python)

## Instalación

1. **Clona este repositorio** (o descárgalo como archivo ZIP):
   ```bash
   git clone https://github.com/tu-usuario/ScanPhonePy.git
   cd ScanPhonePy
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

   Si no tienes el archivo `requirements.txt`, puedes instalar las dependencias manualmente:
   ```bash
   pip install phonenumbers
   ```

## Uso

1. Ejecuta el script principal:
   ```bash
   python main.py
   ```

2. Ingresa un número de teléfono en formato internacional (por ejemplo, `+0123456789`).

3. Verás información detallada como esta:

   ```
   País: México
   Ubicación: Jalisco
   Compañía: Telcel
   Tipo de línea: Móvil
   Zona horaria: America/Mexico_City
   ```

## Ejemplo de Número Válido

- **Formato**: `+<código de país><número>`
- Ejemplo: `+34911234567` (España)

## Dependencias

El proyecto utiliza las siguientes bibliotecas:

- [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) - Biblioteca para analizar y validar números de teléfono.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

## Contacto

- Autor: T. Stark
- GitHub: [@t-starks](https://github.com/t-starks)