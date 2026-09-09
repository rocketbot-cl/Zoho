## How to Use This Module

Before using this module, you need to configure it in the Zoho Developer Console.

1. Open the Zoho Developer Console.

2. Select Server-based Applications.

3. Fill in the required information:

    - Client Name: Rocketbot Integration

    - Homepage URL: https://sign.zoho.com

    - Authorized Redirect URIs: https://sign.zoho.com (This URL must be exactly as shown to match the fixed URI in the Python code.)

    - Save the changes and copy the Client ID (Client Details tab) and the Client Secret (Client Secret tab).

4. Generate the Grant Code in Your Browser

    - Replace [CLIENT_ID] in the following link and open it in your browser's address bar:

    https://accounts.zoho.com/oauth/v2/auth?scope=ZohoSign.documents.ALL&client_id=[CLIENT_ID]&response_type=code&access_type=offline&redirect_uri=https://sign.zoho.com (If your account is hosted on a European server, change accounts.zoho.com to accounts.zoho.eu).

    - Click OK. The page will redirect to an address like [https://sign.zoho.com/?code=1000.xxxxxxxxx](https://sign.zoho.com/?code=1000.xxxxxxxxx)...

    - Select only the text that appears after the code= (Do not include any other parameters, if any)

5. Obtain the Refresh Token from the Command Prompt

    - Open the Windows Command Prompt.

    - Copy and run the following command, replacing the original with your actual credentials, and press Enter:

    curl -X POST https://accounts.zoho.com/oauth/v2/token -d "grant_type=authorization_code" -d "client_id=YOUR_CLIENT_ID" -d "client_secret=YOUR_CLIENT_SECRET" -d "redirect_uri=https://sign.zoho.com" -d "code=THE_COPIED_CODE"

    - In the JSON response returned by the console, copy the value of "refresh_token". This is the value you will enter in the Rocketbot Login command.

6. To use this module, you must use the commands in the following order:

    - Login

    - Add People (Run as many times as there are participating recipients)

    - Create Document

    - Add Fields (Added fields are not visible in the Zoho app view; they are viewed in the browser)

    - Send

All fields in the commands must be completed; no fields can be left empty.

7. API Credit Requirement

    - To successfully execute the Send command, the organization must have active API Credits in Zoho Sign (purchasable from Settings > Subscription). Without these credits, the API submission will return error 12000.

---

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

    - Hagan clic en Aceptar. La página redirigirá a una dirección como [https://sign.zoho.com/?code=1000.xxxxxxxxx](https://sign.zoho.com/?code=1000.xxxxxxxxx)...

    - Seleccione unicamente el texto que aparece despues del code= (No debe incluir otros parametros, en caso de que los haya)

5. Obtener el Refresh Token desde la CMD

    - Abra la CMD de Windows.

    - Copie y ejecute el siguiente comando reemplazando sus credenciales reales y presione Enter:

    curl -X POST https://accounts.zoho.com/oauth/v2/token -d "grant_type=authorization_code" -d "client_id=TU_CLIENT_ID" -d "client_secret=TU_CLIENT_SECRET" -d "redirect_uri=https://sign.zoho.com" -d "code=EL_CODIGO_COPIADO"

    - En la respuesta JSON que devuelve la consola, copie el valor de "refresh_token". Este valor es el que se ingresará en el comando Login de Rocketbot.

6. Para ocupar este modulo debe utilizar los comandos en el siguiente orden:

    - Login

    - Agregar Personas (Ejecutar tantas veces como destinatarios participen)

    - Crear Documento

    - Agregar Campos (Los campos agregados no se visualizan desde la vista de la app de zoho, se ven desde el navegador)

    - Enviar

Todos los comandos deben tener todos sus campos completos, no pueden quedar campos vacios.

7. Requisito de Créditos API

    - Para ejecutar con éxito el comando Enviar, la organización debe contar con Créditos de API (API Credits) activos en Zoho Sign (adquiribles desde Configuración > Suscripción). Sin estos créditos, el envío por API retornará el error 12000.

---

## Como usar este módulo

Antes de usar este módulo, você precisa configurá-lo no Zoho Developer Console.

1. Abra o Zoho Developer Console.

2. Selecione Aplicativos baseados em servidor.

3. Preencha as informações necessárias:

    - Nome do cliente: Integração com Rocketbot

    - URL da página inicial: https://sign.zoho.com

    - URIs de redirecionamento autorizados: https://sign.zoho.com (Esta URL deve ser exatamente como mostrada para corresponder à URI fixa no código Python.)

    - Salve as alterações e copie o ID do cliente (guia Detalhes do cliente) e o segredo do cliente (guia Segredo do cliente).

4. Gere o código de concessão no seu navegador

    - Substitua [CLIENT_ID] no seguinte link e abra-o na barra de endereços do seu navegador:

    https://accounts.zoho.com/oauth/v2/auth?scope=ZohoSign.documents.ALL&client_id=[CLIENT_ID]&response_type=code&access_type=offline&redirect_uri=https://sign.zoho.com (Se a sua conta estiver hospedada em um servidor europeu, altere accounts.zoho.com para accounts.zoho.eu).

    - Clique em OK. A página será redirecionada para um endereço como [https://sign.zoho.com/?code=1000.xxxxxxxxx](https://sign.zoho.com/?code=1000.xxxxxxxxx)...

    - Selecione apenas o texto que aparece após o code= (Não inclua nenhum outro parâmetro, se houver)

5. Obtenha o Token de Atualização pelo Prompt de Comando

    - Abra o Prompt de Comando do Windows.

    - Copie e execute o seguinte comando, substituindo o original pelas suas credenciais reais, e pressione Enter:

    curl -X POST https://accounts.zoho.com/oauth/v2/token -d "grant_type=authorization_code" -d "client_id=SEU_ID_DE_CLIENTE" -d "client_secret=SEU_SEGREDO_DE_CLIENTE" -d "redirect_uri=https://sign.zoho.com" -d "code=O_CÓDIGO_COPIADO"

    - Na resposta JSON retornada pelo console, copie o valor de "refresh_token". Este é o valor que você deverá inserir no comando de login do Rocketbot.

6. Para usar este módulo, você deve usar os comandos na seguinte ordem:

    - Login

    - Adicionar Pessoas (Execute o comando quantas vezes forem necessárias para cada destinatário participante)

    - Criar Documento

    - Adicionar Campos (Os campos adicionados não são visíveis no aplicativo Zoho; eles são visualizados no navegador)

    - Enviar

Todos os campos dos comandos devem ser preenchidos; nenhum campo pode ficar vazio.

7. Requisito de Crédito da API

    - Para executar o comando Enviar com sucesso, a organização deve ter Créditos da API ativos no Zoho Sign (adquiríveis em Configurações > Assinatura). Sem esses créditos, o envio da API retornará o erro 12000.