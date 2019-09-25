#!/usr/bin/python2

import os
#import hadoop.py


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

while 1<2:
	print"""
	press 1:To Configure Yourself
	press 3:To Create File:
	press 4:To Upload File: 
	press 5:To Check your Admin Report
	press 6: to EXIT
	"""
	con=raw_input("Enter your choice:::")

	if int(con)==1:
		print "Client is Configuring.... "
		ipadd =raw_input("Enter Client ip :: ")
		pswd=raw_input("Enter Client Password :: ")
		name_ip =raw_input("Enter Name Node ip :: ")

		check_java(pswd,ipadd)
		check_hadoop(pswd,ipadd)
		firewall(pswd,ipadd)

		fh=open("core-site.xml","w")
		fh.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>')
		fh.write("\n<value>hdfs://")	
		fh.write(name_ip)
		fh.write(":9001</value>\n</property>\n\n</configuration>")
		fh.close()
		check=os.system("sshpass -p "+pswd+" scp /root/core-site.xml "+ipadd+":/etc/hadoop/")
		if check == 0:
			print "core-site.xml have been Configured"

	#if int(con)==2:


	if int(con)==3:
		changedir=os.system("cd /etc/hadoop")
    	makedir=os.system("mkdir temp")
		change=os.system("cd temp")
		filename=raw_input("enter your file name with extension:")
		raw_input("press Enter to add content to your file:")
		os.system("vi "+filename+" ")

	if int(con)==4:
		status=os.system("hadoop fs -put "+filename+"/")
		if status==0:
			print "::::::your file has been uploaded::::::"
		
	if int(con)==5:
		#name_ip=raw_input("enter your name node IP:")
		#os.system("firefox "+name_ip+":50070")
		report=os.system("hadoop dfsadmin-report")
	
	if int(con)==6:
		exit()










 
		
	 

