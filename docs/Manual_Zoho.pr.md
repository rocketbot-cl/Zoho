



# Zoho
  
Módulo para trabalhar com Zoho  

*Read this in other languages: [English](Manual_Zoho.md), [Português](Manual_Zoho.pr.md), [Español](Manual_Zoho.es.md)*
  
![banner](imgs/Modulo_Zoho.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



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

    https://accounts.zoho.com/oauth/v2/auth?scope=ZohoSign.documents.ALL&client_id=[CLIENT_ID]&response_type=code&access_type=offline&redirect_uri=https://sign.zoho.com (Se a sua conta estiver hospedada em um servidor europeu, altere 
accounts.zoho.com para accounts.zoho.eu).

    - Clique em OK. A página será redirecionada para um endereço como [https://sign.zoho.com/?code=1000.xxxxxxxxx](https://sign.zoho.com/?code=1000.xxxxxxxxx)...

    - Selecione apenas o texto que aparece após o code= (Não inclua nenhum outro parâmetro, se houver)

5. Obtenha o Token de Atualização pelo Prompt de Comando

    - Abra o Prompt de Comando do Windows.

    - Copie e execute o seguinte comando, substituindo o original pelas suas credenciais reais, e pressione Enter:

    curl -X POST https://accounts.zoho.com/oauth/v2/token -d "grant_type=authorization_code" -d "client_id=SEU_ID_DE_CLIENTE" -d "client_secret=SEU_SEGREDO_DE_CLIENTE" -d "redirect_uri=https://sign.zoho.com" -d "code=O_CÓDIGO_COPIADO"

    - Na resposta JSON retornada pelo console, copie o valor de "refresh_token". Este é o valor que você deverá inserir no comando de login do Rocketbot.

6. Para usar este módulo, você deve usar os comandos na seguinte ordem:

    - 
Login

    - Adicionar Pessoas (Execute o comando quantas vezes forem necessárias para cada destinatário participante)

    - Criar Documento

    - Adicionar Campos (Os campos adicionados não são visíveis no aplicativo Zoho; eles são visualizados no navegador)

    - Enviar

Todos os campos dos comandos devem ser preenchidos; nenhum campo pode ficar vazio.

7. Requisito de Crédito da API

    - Para executar o comando Enviar com sucesso, a organização deve ter Créditos da API ativos no Zoho Sign (adquiríveis em Configurações > Assinatura). Sem esses créditos, o envio da API retornará o erro 12000.
## Descrição do comando

### 
  

|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Refresh token||1000.6nb54m79eaacb58003dc77898a78e0a7|
|client id||1000.6nb54m79eaacb58003dc77898a78e0a7|
|client secret||1000.6nb54m79eaacb58003dc77898a78e0a7|

### 
  

|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email||someone@gmail.com|
|Name||David|
|Action|||
|Order||1|
|Private Note||Please get back to us for further queries|

### 
  

|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

### 
  

|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|folder|| |
|Request Name||Ex. Python Test|
|Expiration Date||15|
|Sequential|||
|Email Reminders|||
|Reminder Period||5|
|Success|| |

### 
  

|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Field Type|||
|Mandatory|||
|Field Name|| |
|Page Number||2|
|Document Number||1|
|Y-Coordinate||150|
|X-Coordinate||500|
|Width||100|
|Height||20|
|Description||Lorem Ipsum is simply dummy text of the printing and typesetting industry.|
