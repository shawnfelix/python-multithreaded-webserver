Shawn Felix
id: 109316150
nid: safelix

Running web server:
	1. open dir of webserver.py in terminal
	2. run webserver.py
	3. open browser at address given by program output (port will always be 2345)
		(ex: [server ip(type into browser): 192.168.56.1])
		url for you to type in is: 192.168.56.1:2345/[file_name_here].html

Running python http client:
	1. open dir of client.py
	2. run script with args (client.py SERVER_HOST SERVER_PORT FILENAME)
		ex: client.py 192.168.56.1 2345 /home.html
	3. try with file that does not exist to get 404 response