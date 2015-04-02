---
layout: post
title: "SaltStack and Python- More Operations"
modified:
categories: Technology
description: "Various operations of SaltStack with Python"
tags: [technology,saltstack,python,saltapi, salt-operations]
image:
  feature: true
  credit: Free Software
  creditlink: http://gnu.org
comments:
share:
date: 2015-04-02T00:52:53-04:00
---

This post talks about doing various operations using SaltStack and Python. If you are looking for the basics, please refer here. ramaseshan.github.io/technology/2015/04/02/saltstack-and-python/

A basic ls command example:

{% highlight python %}
	>>> import salt.client
	>>> client = salt.client.LocalClient()
	>>> client.cmd('*','cmd.run',['ls'])
	{'Seshan@fractalio': 'Desktop\nDocuments\nDownloads\nMusic\nPictures\nPublic\nTemplates\nVideos\ntest'}
{% endhighlight %}

What does the above code do ?
The above code in the terminal is executed as 

>> salt '*' cmd.run ls

Lets look at the various components of the code. 
 
 >> client is the LocalClient object.

 >> '\*' -- tells to target this command at all the minions. You can replace the * with things like '192.168.1.20\*' which will target all the minions with key 20*. This is called gobbling. SaltStack also supports regularexpressions.
 
 >> cmd.run -- this is a salt module, that is used to run a command in the terminal and get the specified output from the client. Eg  of other modules, test.ping, state.highstate etc.
 
 >> ['ls'] is the parameter or the command that is to be passed to cmd.run. Other examples are, "service network restart" or any command that you execute can be a parameter.

 So what happens when you want to pass a paramter to ls ?? then you can say , client.cmd('*','cmd.run',['ls','/tmp']). 

Most of the things you can accomplish by the above, but have a list of all the available modules in saltstack here : http://docs.saltstack.com/en/latest/ref/modules/all/


I am sure you would have also heard about grains in SaltStack.
If you want to target minions by the grains, then here is what you have to do.
{% highlight  python %}
	client.cmd('roles:primary', 'cmd.run', ['ls'], expr_form='grain')
{% endhighlight %}

So instead of using *, we use the grain key and value, and say explictly that the expr_form='grain'.


