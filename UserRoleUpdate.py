# loop this a list of Domo User IDs and change their role
from pydomo import Domo
from pydomo.users import CreateUserRequest
# This is a connection to L'Oreal US
domo = Domo("{ClientID}","{ClientSecret}",api_host="api.domo.com")

# instantiate variables to modify users
user_update = CreateUserRequest()
# Set the role to Social (or any other role you would like)
user_update.role = 'Social'
# Create a list of Domo Users IDs to update. I created a list of Participant user roles that haven't logged in. See this card: https://loreal-us.domo.com/page/-100000/kpis/details/2071284245
my_Update_List = ["133544617", "1805318606", "247572484", "523704697", "1490253548", "1393385178", "657136365", "1052435888", "1448613880", "433281972", "1298391753", "1886309560", "3068375", "1029764986", "973595412", "508471698", "1800722722", "595400854", "1008090869", "1850382188", "1182066951", "1344710420", "232161155", "40791408", "750574548", "255633394", "319027467", "984397665", "1596216281", "844968961", "1190438937", "1224774339", "1367453473", "1964239663", "2035327519", "306833397", "520206109", "1231523660", "1189702438", "2103587568", "1647479637", "1763026413", "111499697", "2108402208", "70108114", "1416446614", "477701254", "1279475409", "1442021431", "940498573", "2073135825", "151750127", "1682174055", "197659776", "1123477708", "1624694532", "834092686", "311868737", "1658009453", "539038511", "360752443", "1398082071", "1605616222", "510381460", "1112706091", "132067435", "290886710", "1255215760", "2131315498", "1865805141", "1134563347", "373251702", "5129363", "977510935", "1849075940", "437860279", "599291541", "470369977", "1704871046", "1413582284", "1870325177", "453476667", "2018827008", "1590598818", "1165489826", "103525293", "1655924926", "120997037", "1605675853", "324265085", "438712453", "542258343", "296726084", "2122476078", "659942377", "450183403", "2054329328", "70242847", "787640340", "121747735", "1589445208", "855423382", "497705473", "383707285", "2020551988", "309797644", "1352919516", "147501260", "471327112", "1412166524", "102602099", "495345989", "761788111", "82438367", "1151312639", "317801199", "641549033", "1152247791", "1723499212", "698338121", "1994971013", "1126330235", "1548970404"]

# function to do the update
def my_update(id):
	# print(id + " Refsnes") 
	user = domo.users.get(id)
	if user_update.role != user['role']:
		user_update.email = user['email']
		user = domo.users.update(id,user_update)
		print(str(id) + ": updated")
	else:
		print(str(id) + ": already updated")
	
# Loop through the list and call the above function
for x in my_Update_List:
	my_update(x)

# Give message that we are done
print("All finished!")