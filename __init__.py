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
    client_id = GetParams("client_id")
    client_secret = GetParams("client_secret")
    refresh_token = GetParams("refresh_token")
    mod_zoho = Zoho(client_id, client_secret, refresh_token)
    mod_zoho.login()


if module == "add_person":
    name = GetParams("name")
    email = GetParams("email")
    action = GetParams("action")
    signing_order = GetParams("signing_order")
    pm = GetParams("pm")
    try:

        mod_zoho.add_person(name, email, action, signing_order, pm)
        #mod_zoho = Zoho(name, email, action, signing_order, pm)

    except Exception as e:
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
    respvar = GetParams("var1")

    oauth = GetParams("var2")
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

        if sequential == "True":
            req_data["is_sequential"] = True

        if bool_reminder == "True":
            req_data["email_reminders"] = True
            req_data["reminder_period"] = reminder


        actions_list = mod_zoho.create_actions(req_data["is_sequential"])
        req_data['actions'] = actions_list
        respjson = mod_zoho.create_document(fileList, **req_data)

        SetVar(respvar,json.dumps(respjson))

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
    temp = GetParams("response")
    response = GetVar(temp)
    temp = GetParams("oauth")
    oauth = GetVar(temp)
    temp = GetParams("field_info")
    field_info = GetVar(temp)

    try:

        headers = {'Authorization': 'Zoho-oauthtoken ' + oauth}
        respjson = json.loads(response)

        req_data = {}
        respjson = respjson['requests']
        request_id = respjson['request_id']
        field_info = eval(field_info)
        a = mod_zoho.submitDocument(request_id, respjson, oauth, field_info)
        print(a)

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "add_field":
    field_type_name = GetParams("field_type_name")
    is_mandatory = GetParams("is_mandatory")
    field_name = GetParams("field_name")
    page_no = GetParams("page_no")
    y_coord = GetParams("y_coord")
    x_coord = GetParams("x_coord")
    abs_width = GetParams("abs_width")
    abs_height = GetParams("abs_height")
    description_tooltip = GetParams("description_tooltip")

    field_info = GetParams("field_info")
    field_data = GetVar(field_info)

    doc_no = GetParams("doc_no")
    temp = GetParams("var1")
    strresponse = GetVar(temp)

    respjson = json.loads(strresponse)
    respjson = respjson['requests']
    docIdsJsonArray = respjson['document_ids']
    #docIds = [i["document_id"] for i in docIdsJsonArray]

    if is_mandatory == "True":
        is_mandatory = True
    else:
        is_mandatory = False

    #docIndex = int(doc_no) - 1
    #docId = int(docIds[docIndex])

    try:
        if field_type_name == "Email":
            tempfield = {"field_type_name": field_type_name,
                         "text_property": {"is_italic": False, "is_underline": False, "font_color": "000000", "font_size": 11, "is_read_only": False, "is_bold": False, "font": "Arial"},
                         "is_mandatory": is_mandatory,
                         "field_name": field_type_name,
                         "page_no": int(page_no), "y_coord": int(y_coord), "abs_width": int(abs_width),
                         "description_tooltip": description_tooltip,
                         "x_coord": int(x_coord), "abs_height": int(abs_height), "document_id": int(doc_no)}
        else:
            tempfield = {"field_type_name": field_type_name,"is_mandatory": is_mandatory, "field_name": field_type_name,
                         "page_no": int(page_no), "y_coord": int(y_coord), "abs_width": int(abs_width), "description_tooltip": description_tooltip,
                         "x_coord": int(x_coord), "abs_height": int(abs_height),"document_id": int(doc_no)}



        if not field_data:
            fieldList = [tempfield]
            SetVar(field_info, fieldList)
        else:
            field_data = eval(field_data)
            print(field_data)
            field_data.append(tempfield)
            SetVar(field_info, field_data)

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

