import json
import requests


class Zoho:
    field_info = [] #Agragado

    def __init__(self, client_id, client_secret, refresh_token):
        self.field_info = [] #Agragado
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.field_info = []
        self.names = ""
        self.emails = ""
        self.actions = ""
        self.signer_order = ""
        self.secret_message = ""

    def login(self):
        url = 'https://accounts.zoho.com/oauth/v2/token?refresh_token=' + self.refresh_token + '&client_id=' + self.client_id + '&client_secret=' + self.client_secret + '&redirect_uri=https%3A%2F%2Fsign.zoho.com&grant_type=refresh_token'
        response = requests.post(url)
        resp_json = response.json()
        access_token = resp_json["access_token"]
        self.access_token = access_token

    def add_person(self, names, emails, actions, signer_order=None, secret_message=None):
        if self.names and self.emails and self.actions and self.signer_order and self.secret_message:
            self.names = self.names + "," + names
            self.emails = self.emails + "," + emails
            self.actions = self.actions + "," + actions
            self.signer_order = self.signer_order + "," + signer_order
            self.secret_message = self.secret_message + "," + secret_message
        else:
            self.names = names
            self.emails = emails
            self.actions = actions
            self.signer_order = signer_order
            self.secret_message = secret_message

    def get_data(self):
        return (
            self.names.split(","),
            self.emails.split(","),
            self.actions.split(","),
            self.signer_order.split(","),
            self.secret_message.split(",")
        )

    def create_actions(self, is_sequential):
        action_list = []
        zipper = zip(*self.get_data())

        for name, email, action, sign_order , note, in zipper:
            current_action = {
                "recipient_name": name,
                "recipient_email": email,
                "action_type": action,
                "private_notes": note,
                "in_person_name": name,
                "verification_type": "EMAIL"
            }

            if is_sequential:
                current_action["signing_order"] = int(sign_order)

            action_list.append(current_action)

        print(action_list)
        return action_list
    
    def createDocument(self, file_list, expiration_days=15, is_sequential=True, **kwargs):
        headers = {'Authorization': 'Zoho-oauthtoken ' + self.access_token}
        files = []
        for i in file_list:
            files.append(('file', (i[0], open(i[1], 'rb'), i[2])))
        req_data = {}
        req_data['request_name'] = kwargs["request_name"]
        req_data["expiration_days"] = expiration_days
        req_data["is_sequential"] = is_sequential
        email_reminders = kwargs["email_reminders"]
        req_data["email_reminders"] = email_reminders
        if email_reminders:
            req_data["reminder_period"] = 5
        """actions_list = []
        actions_list.append(
            {"recipient_name": "Sudhan Annamalai", "recipient_email": "sudhangomu@gmail.com", "action_type": "SIGN",
             "private_notes": "Please get back to us for further queries", "signing_order": 0})"""
        req_data['actions'] = kwargs["actions"]
        data = {}
        data['requests'] = req_data
        data_json = {}
        data_json['data'] = json.dumps(data)
        print(data_json)
        r = requests.post('https://sign.zoho.com/api/v1/requests', files=files, data=data_json, headers=headers)
        self.response = r.json()
        return r.json()

    def submitDocument(self, request_id, respjson, Oauthtoken, field_info):
        headers = {'Authorization': 'Zoho-oauthtoken ' + Oauthtoken}
        req_data = {}
        req_data['request_name'] = respjson.get('request_name', '')
        actionsJsonArray = respjson.get('actions', [])

        # Inicializar la lista de campos en cada firmante
        for action in actionsJsonArray:
            action['fields'] = []
            action.pop('is_bulk', None)
            action.pop('allow_signing', None)
            action.pop('action_status', None)

        # Distribuir cada campo según su recipient_index
        for field in field_info:
            field_copy = dict(field)
            # Extraer recipient_index para que Zoho no lo rechace como campo desconocido
            rec_idx = int(field_copy.pop("recipient_index", 0))

            if rec_idx < len(actionsJsonArray):
                actionsJsonArray[rec_idx]['fields'].append(field_copy)
            else:
                actionsJsonArray[0]['fields'].append(field_copy)

        req_data['actions'] = actionsJsonArray

        data = {'requests': req_data}
        data_json = {'data': json.dumps(data)}
        
        print("Payload submit", data_json)

        url = 'https://sign.zoho.com/api/v1/requests/' + str(request_id) + '/submit'
        r = requests.post(url, files=[], data=data_json, headers=headers)
        return r.json()
    
    
    def addField(self, field_info):
        self.field_info.append(field_info)
        Zoho.field_info.append(field_info)
        print("Added field info:",len(self.field_info), field_info)
        print("Total fields in class:", len(Zoho.field_info))
        
        
        