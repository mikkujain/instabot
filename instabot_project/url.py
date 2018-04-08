import requests
import sys

response=requests.get('https://api.jsonbin.io/b/59d0f30408be13271f7df29c')
response=response.json()
App_Access_Token=response['access_token']
Base_URL='https://api.instagram.com/v1/'
def self_info():
	request_url=(Base_URL + 'users/self/?access_token=%s') %(App_Access_Token)
	print('Get request_url : %s' %(request_url))
	user_info=requests.get(request_url).json()

	if user_info['meta']['code'] == 200:
		print('successfull')
		# request successfull
	else :
		print("Status code other than 200 recieved")
		sys.exit(0)

self_info()