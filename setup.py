print "\nBroker Configuration\n"
s = "broker = dict(\n\taddr = \'"
s = s + raw_input("Broker IP/Hostname : ")
s = s + "\',\n\tport = "
s = s + raw_input("Port: ")
s = s + ",\n\tusername = \'"
s = s + raw_input("Username: ")
s = s + "\',\n\tpassword = \'"
s = s + raw_input("Password: ")
s = s + "\',\n)\n\nclient = dict(\n\tdev_id = \'"
print "\nClient Configuration\n"
s = s + raw_input("Device ID: ")
s = s + "\',\n\ttype = \'"
s = s + raw_input("Device Type: ")
s = s + "\',\n\tpin = "
s = s + raw_input("GPIO Pin: ")
s = s + ",\n)"
file = open("conf.py", "w")
file.write(s)
file.close()
