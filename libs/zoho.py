import json
import requests

class Zoho:
	
	def __init__(self, client_id,client_secret, refresh_token):
		self.client_id = client_id
		self.client_secret = client_secret
		self.refresh_token = refresh_token
		
	def login(self):
		url = 'https://accounts.zoho.com/oauth/v2/token?refresh_token=' + self.refresh_token + '&client_id=' + self.client_id + '&client_secret=' + self.client_secret + '&redirect_uri=https%3A%2F%2Fsign.zoho.com&grant_type=refresh_token'
        response = requests.post(url)
        resp_json = response.json()
        access_token = resp_json['access_token']
        mod_zoho.access_token = access_token

	def add_person(self, names, emails, actions, signer_order=None, secret_message=None):
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
		for name, email, action, note, sign_order in zipper:
			action_list.append({
				"recipient_name":name,
				"recipient_email":email,
				"action_type":action,
				"private_notes":note, 
				"in_person_name": name, 
				"verification_type": "EMAIL"})
			if is_sequential:
				action_list["signing_order"] = sign_order,


	def createDocument(self, file_list, expiration_days=15, is_sequential=True, **kwargs):
		headers = {'Authorization':'Zoho-oauthtoken '+ self.access_token}
		files =[]
		for i in file_list:
			files.append(('file', (i[0],open(i[1],'rb'),i[2])))
		req_data={}
		req_data['request_name']= kwargs["request_name"]
		req_data["expiration_days"]= expiration_days
		req_data["is_sequential"]= is_sequential
		email_reminders = kwargs["email_reminders"]
		req_data["email_reminders"]= email_reminders
		if email_reminders:
			req_data["reminder_period"]= 5
		actions_list=[]
		actions_list.append({"recipient_name":"Sudhan Annamalai","recipient_email":"sudhangomu@gmail.com","action_type":"SIGN","private_notes":"Please get back to us for further queries","signing_order":0})
		req_data['actions']= kwargs["actions"]
		data={}
		data['requests']=req_data
		data_json={}
		data_json['data'] = json.dumps(data)
		r = requests.post('https://sign.zoho.com/api/v1/requests', files=files, data=data_json,headers=headers)
		return r.json()

	def submitDocument(request_id,respjson,Oauthtoken,field_info):
		headers = {'Authorization':'Zoho-oauthtoken '+Oauthtoken}
		req_data={}
		req_data['request_name']=respjson['request_name']
		docIdsJsonArray = respjson['document_ids']
		actionsJsonArray = respjson['actions']
		#Id = docIdsJsonArray[int(doc_no)]["document_id"]
		#print(Id)
		count = 0
		for j in actionsJsonArray:
			fields=[]

			#field_info = '{"field_type_name": "Email", "is_mandatory": true, "field_name": "sig", "page_no": 1, "y_coord": 100, "abs_width": 100, "description_tooltip": "sig", "x_coord": 100, "abs_height": 100},,{"field_type_name": "Email", "is_mandatory": true, "field_name": "sig", "page_no": 1, "y_coord": 100, "abs_width": 100, "description_tooltip": "sig", "x_coord": 100, "abs_height": 100}'
			if count == 0:
				for i in field_info:
					docInd = i["document_id"]
					i["document_id"] = docIdsJsonArray[docInd]["document_id"]
				fields = field_info
			else:
				fields = field_info


			if 'fields' in j:
				j['fields']=j['fields']+fields
			else:
				j["fields"]=fields
			j.pop('is_bulk',None)
			j.pop('allow_signing',None)
			j.pop('action_status',None)
			count = count + 1
		req_data['actions']=actionsJsonArray
		data={}
		data['requests']=req_data
		data_json={}
		data_json['data'] = json.dumps(data)
		url = 'https://sign.zoho.com/api/v1/requests/'+request_id+'/submit'
		r = requests.post(url, files=[],data=data_json, headers=headers)
		return r.json()
