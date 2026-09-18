# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""


import os
import sys
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "zoho" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)
from zoho import Zoho

module = GetParams("module")

global mod_zoho

if module == "login":
    try:
        client_id = GetParams("client_id")
        client_secret = GetParams("client_secret")
        refresh_token = GetParams("refresh_token")
        res = GetParams("res")
        
        mod_zoho = Zoho(client_id, client_secret, refresh_token)
        mod_zoho.login()
        
        SetVar(res, "True")
    except Exception as e:
        SetVar(res, "False")
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "add_person":
    name = GetParams("name")
    email = GetParams("email")
    action = GetParams("action")
    signing_order = GetParams("signing_order")
    pm = GetParams("pm")
    res= GetParams("res")
    try:

        mod_zoho.add_person(name, email, action, signing_order, pm)
        SetVar(res, "True")
        #mod_zoho = Zoho(name, email, action, signing_order, pm)

    except Exception as e:
        SetVar(res, "False")
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "create_document":

    refresh_token = GetParams("refresh_token")
    client_id = GetParams("client_id")
    client_secret = GetParams("client_secret")
    folder = GetParams("folder")
    reqname = GetParams("reqname")
    exp_date = GetParams("exp_date")
    reminder = GetParams("reminder")
    sequential = GetParams("sequential")
    bool_reminder = GetParams("bool_reminder")
    result = GetParams("result")

    try:
        names, emails, actions,signing_order,pm = mod_zoho.get_data()

        fileList = []
        req_data = {}
        for f in os.listdir(folder):
            #files.append(folder + '/' + f)
            fileList.append([f,folder + '/' + f,"application/pdf"])

        req_data['request_name'] = reqname
        req_data["is_sequential"] = False
        req_data["email_reminders"] = False

        if exp_date:
            req_data["expiration_days"] = exp_date

        
        if sequential == "True" or str(sequential).lower() in ["true", "1"]:
            req_data["is_sequential"] = True

        if bool_reminder == "True" or str(bool_reminder).lower() in ["true", "1"]:
            req_data["email_reminders"] = True
            req_data["reminder_period"] = reminder
        
        actions_list = mod_zoho.create_actions(req_data["is_sequential"])
        
        req_data["actions"] = actions_list

        respjson = mod_zoho.createDocument(fileList, **req_data)


        if isinstance(respjson, dict) and respjson.get("status") == "success":
            SetVar(result, "True")
        else:
            SetVar(result, "False")
            
        

        # print(respjson["status"])
        # if respjson["status"] == 'success':
        #     SetVar(result, "True")


        """
        respjson = respjson['requests']
        docIdsJsonArray = respjson['document_ids']
        docIds = [i["document_id"] for i in docIdsJsonArray]
        SetVar(nId,docIds)
        """
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e


if module == "share":
    try:
        headers = {'Authorization': 'Zoho-oauthtoken ' + mod_zoho.access_token}
        respjson = mod_zoho.response

        req_data = {}
        respjson = respjson['requests']
        request_id = respjson['request_id']
        #field_info = eval(field_info)
        a = mod_zoho.submitDocument(request_id, respjson, mod_zoho.access_token, mod_zoho.field_info)
        
        mod_zoho.field_info = []
        Zoho.field_info = []
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e


if module == "add_field":
    print("ENTRO AL COMANDO")
    field_type_name = GetParams("field_type_name")
    is_mandatory = GetParams("is_mandatory")
    field_name = GetParams("field_name")
    page_no = GetParams("page_no")
    y_coord = GetParams("y_coord")
    x_coord = GetParams("x_coord")
    abs_width = GetParams("abs_width")
    abs_height = GetParams("abs_height")
    description_tooltip = GetParams("description_tooltip")

    doc_no = GetParams("doc_no")
    recipient_index = GetParams("recipient_index")
    result = GetParams("result")
    
    try:
        respjson = mod_zoho.response
        docIdsJsonArray = respjson.get("requests", {}).get("document_ids", [])

        doc_idx = int(doc_no) if doc_no else 0
        if doc_idx < len(docIdsJsonArray):
            real_doc_id = docIdsJsonArray[doc_idx]["document_id"]
        else:
            raise Exception(f"El índice de documento {doc_idx} no existe en la solicitud.")

        mandatory = True if is_mandatory in ["True", True] else False
        rec_idx = int(recipient_index) if recipient_index else 0

        tempfield = {
            "field_type_name": field_type_name,
            "is_mandatory": mandatory,
            "field_name": field_name or field_type_name,
            "page_no": int(page_no) if page_no else 0,
            "y_coord": int(y_coord),
            "x_coord": int(x_coord),
            "abs_width": int(abs_width),
            "abs_height": int(abs_height),
            "description_tooltip": description_tooltip or "",
            "document_id": real_doc_id,
            "recipient_index": rec_idx 
        }

        if field_type_name == "Email":
            tempfield["text_property"] = {
                "is_italic": False,
                "is_underline": False,
                "font_color": "000000",
                "font_size": 11,
                "is_read_only": False,
                "is_bold": False,
                "font": "Arial"
            }

        mod_zoho.addField(tempfield)

        if result:
            SetVar(result, True)

    except Exception as e:
        if result:
            SetVar(result, False)
        print("\x1B[31;40mError\x1B[0m")
        PrintException()
        raise e