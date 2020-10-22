import os 
import sys
import requests
import json

def create_repo(token, new_repo_name, private_repo, username):
	endpoint = "https://api.github.com/user/repos"
	#header
	token = token.replace('"', "'")
	payload_builder = {'name': new_repo_name}
	r = requests.post(endpoint, auth = (username, token) , data = json.dumps(payload_builder))
	print(r.status_code)

if len(sys.argv) == 1:
	print("Usage: gapp [create] <auth_token> <new_repo_name> <private-repo: boolean(true or false)> <username>")
elif sys.argv[1] == "create" and len(sys.argv) == 6:
	if isinstance(sys.argv[2], str) and isinstance(sys.argv[3], str) and isinstance(sys.argv[4], str) and isinstance(sys.argv[5], str):
		if sys.argv[4] == "t" or sys.argv[4] == "f" :
			create_repo(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
		else:
			print("Usage: gapp [create] <auth_token> <new_repo_name> <public-repo: boolean(true or false)> <username>")
			exit()
print(len(sys.argv))