import requests
import xmltodict
import json

def get_json(query):
	APP_ID = 'YOUR APP ID HERE'
	url = 'http://api.wolframalpha.com/v1/query?input=%s&appid=%s' %(query, APP_ID)
	print url
	print 'Requesting content'
	res = requests.get(url)
	print res.status_code
	xml_content = res.content
	dict_content = xmltodict.parse(xml_content)
	results = []
	for pod in dict_content['queryresult']['pod']:
		result = {}
		title = pod['@title']
		link = pod['subpod']['img']['@src']
		data = pod['subpod']['img']['@alt']
		result['caption'] = title
		result['image'] = link
		result['data'] = data
		results.append(result)
	json_content = json.dumps(results)
	return json_content

