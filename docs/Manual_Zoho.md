



# Zoho
  
Module to work with Zoho  

*Read this in other languages: [English](Manual_Zoho.md), [Português](Manual_Zoho.pr.md), [Español](Manual_Zoho.es.md)*
  
![banner](imgs/Modulo_Zoho.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

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

    - Click OK. The page will redirect to an 
address like [https://sign.zoho.com/?code=1000.xxxxxxxxx](https://sign.zoho.com/?code=1000.xxxxxxxxx)...

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

    - Add Fields 
(Added fields are not visible in the Zoho app view; they are viewed in the browser)

    - Send

All fields in the commands must be completed; no fields can be left empty.

7. API Credit Requirement

    - To successfully execute the Send command, the organization must have active API Credits in Zoho Sign (purchasable from Settings > Subscription). Without these credits, the API submission will return error 12000.


## Description of the commands

### Login
  
Input the fresh token client id and client secret to get the access token
|Parameters|Description|example|
| --- | --- | --- |
|Refresh token||1000.6nb54m79eaacb58003dc77898a78e0a7|
|client id||1000.6nb54m79eaacb58003dc77898a78e0a7|
|Client secret||1000.6nb54m79eaacb58003dc77898a78e0a7|
|Asign to variable||Variable|

### Add People
  
Add the people you want to share the document with
|Parameters|Description|example|
| --- | --- | --- |
|Email||someone@gmail.com|
|Name||David|
|Action|||
|Order||1|
|Private Note||Please get back to us for further queries|
|Asign to variable||Variable|

### Submit
  
Send the document to sign
|Parameters|Description|example|
| --- | --- | --- |

### Create Document in Zoho
  
share the document to other people to sign.
|Parameters|Description|example|
| --- | --- | --- |
|folder|| |
|Request Name||Ex. Python Test|
|Expiration Date||15|
|Sequential|||
|Email Reminders|||
|Reminder Period||5|
|Success|| |

### Add Fields
  
 
|Parameters|Description|example|
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
|Recipient index (0, 1,..)||0|
|Success|| |
