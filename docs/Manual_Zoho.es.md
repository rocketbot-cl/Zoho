



# Zoho
  
Modulo para trabajar con Zoho  

*Read this in other languages: [English](Manual_Zoho.md), [Português](Manual_Zoho.pr.md), [Español](Manual_Zoho.es.md)*
  
![banner](imgs/Modulo_Zoho.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo

Antes de usar este módulo, es necesario la configuración en Zoho Developer Console.

1. Entrar a Zoho Developer Console.

2. Seleccionar Server-based Applications.

3. Se deben completar los datos requeridos:

    - Client Name: Rocketbot Integration

    - Homepage URL: https://sign.zoho.com

    - Authorized Redirect URIs: https://sign.zoho.com (Debe ser exactamente esta URL para coincidir con la URI fija del código Python).

    - Guardar los cambios y copiar el Client ID (pestaña Client Details) y el Client Secret (pestaña Client Secret).

4. Generar el Grant Code en el Navegador

    - Reemplace [CLIENT_ID] en el siguiente enlace y ábralo en la barra de direcciones del navegador:

    https://accounts.zoho.com/oauth/v2/auth?scope=ZohoSign.documents.ALL&client_id=[CLIENT_ID]&response_type=code&access_type=offline&redirect_uri=https://sign.zoho.com (Si la cuenta está alojada en el servidor de Europa, cambien accounts.zoho.com por accounts.zoho.eu).

    -
 Hagan clic en Aceptar. La página redirigirá a una dirección como [https://sign.zoho.com/?code=1000.xxxxxxxxx](https://sign.zoho.com/?code=1000.xxxxxxxxx)...

    - Seleccione unicamente el texto que aparece despues del code= (No debe incluir otros parametros, en caso de que los haya)

5. Obtener el Refresh Token desde la CMD

    - Abra la CMD de Windows.

    - Copie y ejecute el siguiente comando reemplazando sus credenciales reales y presione Enter:

    curl -X POST https://accounts.zoho.com/oauth/v2/token -d "grant_type=authorization_code" -d "client_id=TU_CLIENT_ID" -d "client_secret=TU_CLIENT_SECRET" -d "redirect_uri=https://sign.zoho.com" -d "code=EL_CODIGO_COPIADO"

    - En la respuesta JSON que devuelve la consola, copie el valor de "refresh_token". Este valor es el que se ingresará en el comando Login de Rocketbot.

6. Para ocupar este modulo debe utilizar los comandos en el siguiente orden:

    - Login

    - Agregar Personas (Ejecutar tantas veces como destinatarios 
participen)

    - Crear Documento

    - Agregar Campos (Los campos agregados no se visualizan desde la vista de la app de zoho, se ven desde el navegador)

    - Enviar

Todos los comandos deben tener todos sus campos completos, no pueden quedar campos vacios.

7. Requisito de Créditos API

    - Para ejecutar con éxito el comando Enviar, la organización debe contar con Créditos de API (API Credits) activos en Zoho Sign (adquiribles desde Configuración > Suscripción). Sin estos créditos, el envío por API retornará el error 12000.


## Descripción de los comandos

### Login
  
ingrese el ID de cliente del token nuevo y el secreto del cliente para obtener el token de acceso
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Refresh token||1000.6nb54m79eaacb58003dc77898a78e0a7|
|client id||1000.6nb54m79eaacb58003dc77898a78e0a7|
|Client secret||1000.6nb54m79eaacb58003dc77898a78e0a7|
|Asignar a variable||Variable|

### Agregar Personas
  
Agregue a las personas con las que desea compartir el documento
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Email||someone@gmail.com|
|Name||David|
|Tipo de acción|||
|Orden de firma||1 |
|Mensaje privado||Comuníquese con nosotros si tiene más consultas|
|Asignar a variable||Variable|

### Enviar
  
Envía el documento a firmar
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Crear documento
  
Configura el documento a enviar para firmar.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Carpeta|| |
|Nombre requerido||Ex. Python Test|
|Fecha de expiración||15|
|Sequencial?|||
|Recordatorio por email|||
|Periodo de recordatorio||5|
|Asignar resultado a variable|| |

### Agregar campos
  
 
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de campo|||
|Obligatorio?|||
|Nombre|| |
|Número de página||2|
|Número de documento||0|
|Coordenadas Y||150|
|Coordenadas X||500|
|Ancho||100|
|Alto||20|
|Descripción||Lorem Ipsum is simply dummy text of the printing and typesetting industry.|
|Índice de destinatario (0, 1,..)||0|
|Asignar resultado a variable|| |
