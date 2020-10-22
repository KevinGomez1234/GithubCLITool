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
def view_all_repos(token):
	endpoint = "https://api.github.com/user/repos"
	payload = {"access_token": token}
	r = requests.get(endpoint, params = payload)
	array_of_objects = json.loads(r.text)
	#since repos returns an array of objects iterate through all objects and find the one that matches key = name
	for obj in array_of_objects:
		print(obj['full_name'])
if len(sys.argv) == 1:
	print("Usage: gapp [create] <auth_token> <new_repo_name> <private-repo: boolean(true or false)> <username>")
	print("Usage: gapp [view] <auth_token>")
elif sys.argv[1] == "create" and len(sys.argv) == 6:
	if isinstance(sys.argv[2], str) and isinstance(sys.argv[3], str) and isinstance(sys.argv[4], str) and isinstance(sys.argv[5], str):
		if sys.argv[4] == "true" or sys.argv[4] == "false" :
			create_repo(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
		else:
			print("Usage: gapp [create] <auth_token> <new_repo_name> <public-repo: boolean(true or false)> <username>")
			exit()
elif sys.argv[1] == "view" and len(sys.argv) == 3:
	if isinstance(sys.argv[2], str):
		view_all_repos(sys.argv[2])
	else:
		print("Usage: gapp [view] <auth_token>")
else:
	print("Usage: gapp [create] <auth_token> <new_repo_name> <private-repo: boolean(true or false)> <username>")
	print("Usage: gapp [view] <auth_token>")


