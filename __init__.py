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
import ast
from functions import submitDocument

module = GetParams("module")


if module == "add_person":
    name = GetParams("name")
    email = GetParams("email")
    action = GetParams("action")
    signing_order = GetParams("signing_order")
    pm = GetParams("pm")
    try:
        var1 = GetParams("var1")
        data1 = GetVar(var1)
        if not data1:
            SetVar(var1, data1 + name)
        else:
            SetVar(var1, data1 + "," + name)

        var2 = GetParams("var2")
        data2 = GetVar(var2)
        if not data1:
            SetVar(var2, data2 + email)
        else:
            SetVar(var2, data2 + "," + email)

        var3 = GetParams("var3")
        data3 = GetVar(var3)
        if not data3:
            SetVar(var3, data3 + action)
        else:
            SetVar(var3, data3 + "," + action)

        var4 = GetParams("var4")
        data4 = GetVar(var4)
        if signing_order:
            if not data4:
                SetVar(var4, data4 + signing_order)
            else:
                SetVar(var4, data4 + "," + signing_order)

        var5 = GetParams("var5")
        data5 = GetVar(var5)
        if pm:
            if not data5:
                SetVar(var5, data5 + pm)
            else:
                SetVar(var5, data5 + "," + pm)
        else:
            SetVar(var5, data5 + ",")
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "create_document":

    nNames = GetParams("names")
    nEmails = GetParams("emails")
    nActions = GetParams("actions")
    nSigning_order = GetParams("signing_order")
    nPm = GetParams("pm")

    print(nSigning_order)
    names = GetVar(nNames)
    emails = GetVar(nEmails)
    actions = GetVar(nActions)
    signing_order = GetVar(nSigning_order)
    pm = GetVar(nPm)

    names = list(names.split(","))
    emails = list(emails.split(","))
    actions = list(actions.split(","))
    signing_order = list(signing_order.split(","))
    pm = list(pm.split(","))

    #print(names)
    #print(emails)
    #print(actions)
    #print(signing_order)
    #print(pm)

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

        url = 'https://accounts.zoho.com/oauth/v2/token?refresh_token=' + refresh_token + '&client_id=' + client_id + '&client_secret=' + client_secret + '&redirect_uri=https%3A%2F%2Fsign.zoho.com&grant_type=refresh_token'
        response = requests.post(url)
        resp_json = response.json()
        access_token = resp_json['access_token']
        SetVar(oauth, access_token)
        headers = {'Authorization': 'Zoho-oauthtoken ' + access_token}
        files = []
        fileList = []
        for f in os.listdir(folder):
            #files.append(folder + '/' + f)
            fileList.append([f,folder + '/' + f,"application/pdf"])

        for i in fileList:
            files.append(('file', (i[0], open(i[1], 'rb'), i[2])))

        if not exp_date:
            exp_date = 15

        req_data = {'request_name': reqname, "expiration_days": exp_date}

        if sequential == "True":
            req_data["is_sequential"] = True
        else:
            req_data["is_sequential"] = False

        if bool_reminder == "True":
            req_data["email_reminders"] = True
            req_data["reminder_period"] = reminder
        else:
            req_data["email_reminders"] = False

        actions_list = []
        if req_data["is_sequential"]:
            for i in range(len(names)):
                actions_list.append({"recipient_name":names[i],"recipient_email":emails[i],"action_type":actions[i],"private_notes":pm[i],
                                     "signing_order":signing_order[i], "in_person_name": names[i], "verification_type": "EMAIL"})
        else:
            for i in range(len(names)):
                actions_list.append({"recipient_name": names[i], "recipient_email": emails[i], "action_type": actions[i],
                                     "private_notes": pm[i], "in_person_name": names[i], "verification_type": "EMAIL"})
        req_data['actions'] = actions_list
        data = {'requests': req_data}
        data_json={'data':json.dumps(data)}
        url2 = 'https://sign.zoho.com/api/v1/requests'
        r = requests.post(url2, files=files, data=data_json, headers=headers)
        respjson = r.json()
        SetVar(respvar,json.dumps(respjson))
        """
        respjson = respjson['requests']
        docIdsJsonArray = respjson['document_ids']
        docIds = [i["document_id"] for i in docIdsJsonArray]
        SetVar(nId,docIds)
        """
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
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
        a = submitDocument(request_id, respjson, oauth, field_info)
        """
        req_data['request_name'] = respjson['request_name']
        actionsJsonArray = respjson['actions']
        docIdsJsonArray = respjson['document_ids']
        field_info = list(field_info.split(",,"))
        for i in docIdsJsonArray:
            docId = i["document_id"]
            for j in actionsJsonArray:
                fields = []
                for i in range(len(field_info)):
                    field = json.loads(field_info[i])
                    field["document_id"]=docId
                    fields.append(field)
                    print(fields)
                if 'fields' in j:
                    j['fields'] = j['fields'] + fields
                else:
                    j["fields"] = fields
                j.pop('is_bulk', None)
                j.pop('allow_signing', None)
                j.pop('action_status', None)
                print(j)
        req_data['actions'] = actionsJsonArray
        data = {}
        data['requests'] = req_data
        data_json = {}
        data_json['data'] = json.dumps(data)
        url = 'https://sign.zoho.com/api/v1/requests/' + request_id + '/submit'
        r = requests.post(url, files=[], data=data_json, headers=headers)
        print(r)
        print(r.json())
        """
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
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

        tempfield = {"field_type_name": field_type_name,"is_mandatory": is_mandatory, "field_name": field_name,
                     "page_no": int(page_no), "y_coord": int(y_coord), "abs_width": int(abs_width), "description_tooltip": description_tooltip,
                     "x_coord": int(x_coord), "abs_height": int(abs_height)}

        tempfield = json.dumps(tempfield)


        if not field_data:
            totalfields = field_data + str(tempfield)
            SetVar(field_info, totalfields)
        else:
            totalfields = field_data + ",," + str(tempfield)
            SetVar(field_info, totalfields)

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

