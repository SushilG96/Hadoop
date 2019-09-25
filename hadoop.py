#!/usr/bin/python2
import os

print"\n#####################!!!!!!!!!!!Welcome To Hadoop Cluster Formation!!!!!!!!!#########################\n"


def bash(pswd,ipadd):
	bash=os.system("sshpass -p "+pswd+" scp .bashrc "+ipadd+":")

def check_java(pswd,ipadd):
	verify=os.system("sshpass -p "+pswd+" ssh "+ipadd+"  rpm -q jdk")
	if verify == 0:
		print"\nJava was Reinstalled "
		jd=os.system("sshpass -p "+pswd+" ssh "+ipadd+"  rpm -e jdk")
		check=os.system("sshpass -p "+pswd+" scp /root/jdk-7u79-linux-x64.rpm "+ipadd+":")
		install=os.system("sshpass -p "+pswd+" ssh "+ipadd+" rpm -ivh jdk-7u79-linux-x64.rpm")
		bash(pswd,ipadd)
				
		if install == 0:
			print "Java is Installed"

	if verify == 256:		
		check=os.system("sshpass -p "+pswd+" scp /root/jdk-7u79-linux-x64.rpm "+ipadd+":")
		install=os.system("sshpass -p "+pswd+" ssh "+ipadd+" rpm -ivh jdk-7u79-linux-x64.rpm")
		bash(pswd,ipadd)

		if install == 0:
			print "Java is Installed"


def check_hadoop(pswd,ipadd):
	verify=os.system("sshpass -p "+pswd+" ssh "+ipadd+" rpm -q hadoop")
	if verify == 0:
		print"\nHadoop was preinstalled\n"
		jd=os.system("sshpass -p "+pswd+" ssh "+ipadd+" rpm -e hadoop")
		delete=os.system("sshpass -p "+pswd+" ssh "+ipadd+" rm -rvf /etc/hadoop")
		print"\n Hadoop Components was removed\n"
		check=os.system("sshpass -p "+pswd+" scp /root/hadoop-1.2.1-1.x86_64.rpm "+ipadd+":")
		install=os.system("sshpass -p "+pswd+" ssh "+ipadd+" rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles")

		if install == 0:
			print "Hadoop is Installed"

	if verify == 256:		
		check=os.system("sshpass -p "+pswd+" scp /root/hadoop-1.2.1-1.x86_64.rpm "+ipadd+":")
		install=os.system("sshpass -p "+pswd+" ssh "+ipadd+" rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles")

		if install == 0:
			print "Hadoop is Installed"


def firewall(pswd,ipadd):
	os.system("sshpass -p "+pswd+" ssh "+ipadd+" systemctl stop firewalld")
	os.system("sshpass -p "+pswd+" ssh "+ipadd+" systemctl disable firewalld")
			
	pass

while True:
	print"""
	press 1:To configure Name Node
	press 2:To Configure Job Tracker 
	press 3:To Configure Data Node and Task Tracker
	press 4:To EXIT
	"""


	con=raw_input("Enter your choice:::")
		#Lets Start Configuring Name Node
	if int(con) == 1:
		ipadd =raw_input("Enter Name ip :: ")
		print "Let's Start Configuring Name Node"
		pswd=raw_input("Enter Name Node Password :: ")
		print "press 1:Install Hadoop and Java "
		a=raw_input("Enter your choice::: ")

		if int(a)==1:
			check_java(pswd,ipadd)
			check_hadoop(pswd,ipadd)
			
			#Adding hdfs-site  
		   	print "Configuring Hdfs file"
			fh=open("hdfs-site.xml","w")
			fh.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n')
			master="<name>dfs.name.dir</name>\n"
			masterfolder="<value>/master</value>\n"
			fh.write(master)
			fh.write(masterfolder)
			fh.write("\n</property>\n\n</configuration>\n")
			fh.close()
			check=os.system("sshpass -p "+pswd+" scp /root/hdfs-site.xml "+ipadd+":/etc/hadoop")
			print "hdfs-site.xml and have been Configured"

			#Adding core-site
			fh=open("core-site.xml","w")
			fh.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>')
			fh.write("\n<value>hdfs://")	
			fh.write(ipadd)
			fh.write(":9001</value>\n</property>\n\n</configuration>")
			fh.close()
			check=os.system("sshpass -p "+pswd+" scp /root/core-site.xml "+ipadd+":/etc/hadoop/")
			if check == 0:
				print "core-site.xml have been Configured"
			firewall(pswd,ipadd)		
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" mkdir /etc/hadoop/master")
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" hadoop namenode -format")
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" hadoop-daemon.sh start namenode")
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" jps")

	if int(con) == 2:
		ipadd =raw_input("Enter Name ip :: ")
		print "Let's Start Configuring Job Tracker "
		pswd=raw_input("Enter Job Tracker Password :: ")
		print "press 1:Install Hadoop and Java "
		a=raw_input("Enter your choice::: ")

		if int(a)==1:
			check_java(pswd,ipadd)
			check_hadoop(pswd,ipadd)
			#Adding mapred-site
			fh=open("mapred-site.xml","w")
			fh.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>mapred.job.tracker</name>')
			fh.write("\n<value>")
			fh.write(ipadd)
			fh.write(":9002</value>\n</property>\n\n</configuration>")
			fh.close()
			check=os.system("sshpass -p "+pswd+" scp /root/mapred-site.xml "+ipadd+":/etc/hadoop/")
			if check == 0:
				print "mapred-site have been Configured"

			firewall(pswd,ipadd)
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" hadoop-daemon.sh start jobtracker")
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" jps")

	if int(con) == 3:

		print "Let's Start Configuring Task and Data Node "
		ipadd =raw_input("Enter Task and Data Node ip :: ")
		pswd=raw_input("Enter Task and Data Node Password :: ")
		job_ip=raw_input("Enter job Tracker Node IP:")
		name_ip=raw_input("Enter Name Node  IP:")
		
		print "press 1:Install Hadoop and Java "
		a=raw_input("Enter your choice::: ")

		if int(a)==1:
			check_java(pswd,ipadd)
			check_hadoop(pswd,ipadd)
			#Adding hdfs-site  
		   	print "Configuring Hdfs file"
			fh=open("hdfs-site.xml","w")
			fh.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n')
			data="<name>dfs.data.dir</name>\n"
			datafolder="<value>/data</value>\n"
			fh.write(data)
			fh.write(datafolder)
			fh.write("\n</property>\n\n</configuration>\n")
			fh.close()

			check=os.system("sshpass -p "+pswd+" scp /root/hdfs-site.xml "+ipadd+":/etc/hadoop")
			print "hdfs-site.xml and have been Configured"

			#Adding core-site
			fh=open("core-site.xml","w")
			fh.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>')
			fh.write("\n<value>hdfs://")	
			fh.write(name_ip)
			fh.write(":9001</value>\n</property>\n\n</configuration>")
			fh.close()
			check=os.system("sshpass -p "+pswd+" scp /root/core-site.xml "+ipadd+":/etc/hadoop/")
			if check == 0:
				print "core-site.xml have been Configured"

		
		

			#configuring Mapred file
			fh=open("mapred-site.xml","w")
			fh.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>mapred.job.tracker</name>')
			fh.write("\n<value>")
			fh.write(job_ip)
			fh.write(":9002</value>\n</property>\n\n</configuration>")
			fh.close()
			check=os.system("sshpass -p "+pswd+" scp /root/mapred-site.xml "+ipadd+":/etc/hadoop/")
			if check == 0:
				print "mapred-site have been Configured"
			firewall(pswd,ipadd)		
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" hadoop-daemon.sh start datanode")
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" hadoop-daemon.sh start tasktracker")
			os.system("sshpass -p "+pswd+" ssh "+ipadd+" jps")

			

	if int(con)==4:
		exit()


		
	