#!/usr/bin/python2

import matplotlib.pyplot as pt
import sys

a=[]
for x in sys.stdin:
	p=x.split()
	a.append(p)
f=[]
g=[]
for i in range(0,5):
	b=a[i][0]
	cb=a[i][1]
	f.append(b)
	g.append(cb)
#print f
#print g

slices = f
activities = g
cols= ['g','r','b','c','m']

pt.pie(slices,
	labels=activities,
	colors=cols,
	startangle=90,
	shadow=True,
	explode=(0.1,0.1,0.1,0.1,0.1),
	autopct='%1.1f%%'
	)
pt.title('Youtube Top 5 Most Uploaded Category of videos')
pt.show()
