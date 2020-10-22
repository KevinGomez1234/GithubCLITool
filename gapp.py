import os 
import sys
import requests
import json

def create_repo(token, new_repo_name, private_repo, username):
	endpoint = "https://api.github.com/user/repos"
	#header
	token = token.replace('"', "'")
	payload_builder = {'name': new_repo_name, 'private': private_repo}
	r = requests.post(endpoint, auth = (username, token) , data = json.dumps(payload_builder))
	if r.status_code == 201:
		print("succesful resource created " + username + "/" + new_repo_name)

if len(sys.argv) == 1:
	print("Usage: gapp [create] <auth_token> <new_repo_name> <private-repo: boolean(true or false)> <username>")
elif sys.argv[1] == "create" and len(sys.argv) == 6:
	if isinstance(sys.argv[2], str) and isinstance(sys.argv[3], str) and isinstance(sys.argv[4], str) and isinstance(sys.argv[5], str):
		if sys.argv[4] == "true" or sys.argv[4] == "false" :
			create_repo(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
		else:
			print("Usage: gapp [create] <auth_token> <new_repo_name> <public-repo: boolean(true or false)> <username>")
			exit()
