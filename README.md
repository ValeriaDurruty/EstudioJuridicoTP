# EstudioJuridicoTP

## Descripción

Este repositorio contiene una aplicación desarrollada en Python para la gestión de expedientes de un estudio jurídico. El programa implementa un menú interactivo que permite la administración de una pila de objetos `Expediente`. Las funcionalidades principales incluyen:

* Agregar nuevos expedientes al sistema.
* Modificar la información (titular, trámite, fecha) de expedientes existentes buscando por número.
* Eliminar expedientes basándose en su número.
* Listar todos los expedientes almacenados, mostrando su número, titular, trámite y fecha de presentación.
* Modificar la hora de presentación de los expedientes que se encuentran dentro de un rango de fechas específico.
* Generar una nueva pila que contiene únicamente los expedientes cuya fecha de presentación se encuentra dentro de un rango de fechas dado.
* Eliminar todos los expedientes correspondientes a un mes específico.

Este proyecto fue realizado como Trabajo Práctico Final de la materia Sintaxis y Semántica del Lenguaje en la facultad. El objetivo principal era aplicar los conceptos de abstracción de datos, utilizando una estructura de datos tipo Pila para la gestión de los expedientes y definiendo un Tipo Abstracto de Datos (TAD) para representar cada expediente.

##   Información Adicional

* Año de desarrollo: 2021

## Contenido del Repositorio

* `app.py`: Archivo principal de la aplicación en Python. Contiene el menú interactivo y la lógica para interactuar con los TADs.
* `TAD_Pila_Exp.py`: Implementación del Tipo Abstracto de Datos (TAD) Pila, utilizado para almacenar los expedientes.
* `TadExpediente.py`: Definición e implementación del Tipo Abstracto de Datos (TAD) Expediente, que representa la estructura de cada expediente.
* `README.md`: Archivo con la descripción del proyecto e instrucciones de uso.

## Cómo Ejecutar

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Clona este repositorio a tu máquina local:
    ```bash
    git clone [https://github.com/ValeriaDurruty/EstudioJuridicoTP.git]
    ```
3.  Navega al directorio del proyecto:
    ```bash
    cd EstudioJuridicoTP
    ```
4.  Ejecuta el archivo principal de la aplicación:
    ```bash
    python app.py
    ```
5.  Sigue las instrucciones del menú para interactuar con el sistema de gestión de expedientes.

## Tecnologías Utilizadas

* Python
* Librería `datetime` de Python para el manejo de fechas y horas.

## Autor

Valeria E. Durruty

**Notas Adicionales:**

* La aplicación se basa en la implementación de dos Tipos Abstractos de Datos (TADs):
    * **TAD Pila (`TAD_Pila_Exp.py`):** Esta estructura de datos sigue el principio LIFO (Last In, First Out) y se utiliza para almacenar la colección de expedientes. Las operaciones implementadas para la pila incluyen la creación, verificación de si está vacía, apilar (agregar), desapilar (eliminar y obtener el último), y obtener el tamaño.
    * **TAD Expediente (`TadExpediente.py`):** Este TAD representa cada expediente individual y encapsula su información: número, titular, trámite y fecha de presentación. Proporciona operaciones para crear, cargar, acceder y modificar los atributos de un expediente.
