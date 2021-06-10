import json
import requests

def createDocument(fileList,Oauthtoken):
	headers = {'Authorization':'Zoho-oauthtoken '+Oauthtoken}
	files =[]
	for i in fileList:
		files.append(('file', (i[0],open(i[1],'rb'),i[2])))
	req_data={}
	req_data['request_name']="Python Test"
	req_data["expiration_days"]= 10
	req_data["is_sequential"]=True
	req_data["email_reminders"]=True
	req_data["reminder_period"]= 5
	actions_list=[]
	actions_list.append({"recipient_name":"Sudhan Annamalai","recipient_email":"sudhangomu@gmail.com","action_type":"SIGN","private_notes":"Please get back to us for further queries","signing_order":0})
	req_data['actions']=actions_list
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
