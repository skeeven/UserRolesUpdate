# roleId
# Number
# Enter a number:
# 	1 (Admin)
# 	2 (Privileged)
# 	3 (Editor)
# 	4 (Participant)
# 	5 (Social)

#import domo libraries
from pydomo import Domo

#connect to the instance
domo = Domo("{ClientID}","{ClientSecret}",api_host="api.domo.com")

#initialize counters
user_count = 0
pull_users = True
pull_pass = 0

while pull_users == True:
	#Get list of users
	user_list = domo.users.list(500,pull_pass)
	print("Pull Pass:", pull_pass/500)
		# Loop through getting all users
	while user_count < len(user_list):
		if user_list[user_count]['role'] != 'Participant':
			print(user_list[user_count]['id'], ":", user_list[user_count]['role'])
		user_count += 1

	print("user list test:", len(user_list))
	if len(user_list) < 500:
		print("user list test passed ", len(user_list) < 500)
		pull_users == False
	else:
		print("user list test failed ", len(user_list) < 500)
		pull_pass += 500
