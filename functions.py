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
	for i in docIdsJsonArray:
		docId=i["document_id"]
		print(type(docId))
		for j in actionsJsonArray:
			fields=[]
			#field_info = '{"field_type_name": "Email", "is_mandatory": true, "field_name": "sig", "page_no": 1, "y_coord": 100, "abs_width": 100, "description_tooltip": "sig", "x_coord": 100, "abs_height": 100},,{"field_type_name": "Email", "is_mandatory": true, "field_name": "sig", "page_no": 1, "y_coord": 100, "abs_width": 100, "description_tooltip": "sig", "x_coord": 100, "abs_height": 100}'
			field_info = list(field_info.split(",,"))
			for i in range(len(field_info)):
				tempfield = json.loads(field_info[i])
				tempfield["document_id"] = docId
				fields.append(tempfield)
			print(fields)
			"""
			sigField={}
			sigField["field_type_name"]= "Signature"
			sigField["is_mandatory"]= True
			sigField["field_name"]= "Signature"
			sigField["page_no"]= 0
			sigField["y_coord"]= 700
			sigField["abs_width"]= 150
			sigField["description_tooltip"]= ""
			sigField["x_coord"]= 225
			sigField["abs_height"]= 20
			sigField["document_id"]= docId
			fields.append(sigField)
			emailField={}
			emailField["field_type_name"]= "Email"
			emailField["text_property"]={}
			emailField["text_property"]["is_italic"]= False
			emailField["text_property"]["is_underline"]= False
			emailField["text_property"]["font_color"]= "000000"
			emailField["text_property"]["font_size"]= 11
			emailField["text_property"]["is_read_only"]= False
			emailField["text_property"]["is_bold"]= False
			emailField["text_property"]["font"]= "Arial"
			emailField["is_mandatory"]= True
			emailField["page_no"]= 0
			emailField["document_id"]= docId
			emailField["field_name"]= "Email"
			emailField["y_coord"]= 750
			emailField["abs_width"]= 250
			emailField["description_tooltip"]= ""
			emailField["x_coord"]=225
			emailField["abs_height"]= 20
			fields.append(emailField)
			"""
			if 'fields' in j:
				j['fields']=j['fields']+fields
			else:
				j["fields"]=fields
			j.pop('is_bulk',None)
			j.pop('allow_signing',None)
			j.pop('action_status',None)
	req_data['actions']=actionsJsonArray
	data={}
	data['requests']=req_data
	data_json={}
	data_json['data'] = json.dumps(data)
	url = 'https://sign.zoho.com/api/v1/requests/'+request_id+'/submit'
	r = requests.post(url, files=[],data=data_json, headers=headers)
	return r.json()
"""
path = r"C:\Users\bud\Documents\testing6.pdf"
file_list=[["testing6.pdf",path,"application/pdf"]]
Oauthtoken = "1000.908dc119dd9cc508449575f29096e017.3b4a71240c7494f0b43b7ed10def9307"
respjson= createDocument(file_list,Oauthtoken)
respjson=respjson['requests']
request_id=respjson['request_id']
field_info = '{"field_type_name": "Email", "is_mandatory": true, "field_name": "sig", "page_no": 1, "y_coord": 100, "abs_width": 100, "description_tooltip": "sig", "x_coord": 100, "abs_height": 100},,{"field_type_name": "Email", "is_mandatory": true, "field_name": "sig", "page_no": 1, "y_coord": 100, "abs_width": 100, "description_tooltip": "sig", "x_coord": 100, "abs_height": 100}'

submitrespjson=submitDocument(request_id,respjson,Oauthtoken,field_info)
print(submitrespjson)
"""