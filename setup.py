import conf

def broker():
	# BROKER CONFIGURATION
	print "\nBroker Configuration\n"
	s = "conf = dict(\n\taddr = \'"
	s = s + raw_input("Broker IP/Hostname : ")
	s = s + "\',\n\tport = "
	s = s + raw_input("Port: ")
	s = s + ",\n\tusername = \'"
	s = s + raw_input("Username: ")
	s = s + "\',\n\tpassword = \'"
	s = s + raw_input("Password: ")
	s = s + "\',\n)"
	file = open("conf/broker.py", "w")
	file.write(s)
	file.close()

def cli():
	# CLIENT CONFIGURATION
	print "\nClient Configuration\n"
	dev_id = raw_input("Device ID: ")
	s = "conf = dict(\n\tname = \'" + dev_id
	s = s + "\',\n\ttype = \'"
	s = s + raw_input("Device Type: ")
	s = s + "\',\n\tpin = "
	s = s + raw_input("GPIO Pin: ")
	s = s + ",\n)"
	file = open("conf/"+dev_id+".py", "w")
	file.write(s)
	file.close()
	if(str.lower(raw_input("Another client? (Y/N): "))[0] == 'y'):
		cli()

broker()
cli()