---
layout: post
title: SaltStack and Python
modified:
categories: Technology
description: "General usage of SaltStack with Python"
tags: [technology,saltstack,python,saltapi, salt-basics]
image:
  feature: true
  credit: Free Software
  creditlink: http://gnu.org
comments:
share:
date: 2015-04-02T00:04:26-04:00
---

SaltStack is a infrastructure management tool, that is scalable ( can manage up to thousands of servers ) and written in python. Salt also does a lot of remote execution and configuration management too.

The official docs can be found here : http://docs.saltstack.com/en/latest/

This post is going to talk about how to use SaltStack with python. We at Fractalio Data, heavily rely on SaltStack for various operations. We basically build Data Storage Servers, and we want to regulary keep package updates running on all the servers, manage configurations, get status and resource utiliation of each individual nodes, restart services incase of failures, transfer log and other files between nodes and more. Apart from the development team, our testing team is completely automated using SaltStack. We have automated the test suite for one server, and same test suite is executed on all the servers parallely and the final results and gathered from all the servers and mined for all useful data.

We will discuss a basic usage of SaltStack with python.

Pre-requisites :
	1. You should have installed Salt master and have atleast one salt minion.
	2. You should have received the minion request on the master (not necessarily accepted)
	3. You should be the root user or the user who has access to salt. It will be defined in the master config (/etc/salt/master grep for user)
	4. This code has to be run on the same machine as Salt master.

Open the terminal and go to the python console typing python

We will use the Salt wheel client to accept the minions. Wheels are used for interating with various parts of salt.

This will get all the pending minions to be accepted.

    :::python
    import salt.wheel
    opts = salt.config.master_config('/etc/salt/master') #The path of your salt master configuration
    wheel = salt.wheel.Wheel(opts) # Initialize the wheel with various salt opts
    keys = wheel.call_func('key.list_all')  
    pending_minions = keys['minions_pre']
    print pending_minions

and this code would accept it.

    :::python
		for m in pending_minions:
			try:
				if not wheel.call_func('key.accept', match=('%s'%m)):
					print "Error accepting Minion key for %s "%m
					return -1
			except Exception, e:
				print "Error accepting Minion key for %s : %s"%(m, e)
				return -1
			else:
				return 0

Viola ! And you are done accepting the minions. Lets first test if the minions are accepted properly and explore more on what the above code is doing.

    :python
    >>> import salt.client
    >>> client = salt.client.LocalClient()
    >>> client.cmd('*','test.ping')
    {'Seshan@fractalio': True}  # Yay, the minion has responded.

So lets now explore more of what the above code is doing.

In the first code block, we had these lines :

    :::python
  	keys = wheel.call_func('key.list_all')  
  	pending_minions = keys['minions_pre']

 * The keys variable will contain all the keys that the salt master contains. Irrespective of if they are accepted or not accpeted or rejected, the keys variable will contain all the information.

  * The pending_minions will contain all the not accepted minions. Why is called minions_pre, why not minions_pending ?? Do an ** ls /etc/salt/pki/master/ ** , and you will figure out.

The second code block :

    :::python
  	wheel.call_func('key.accept', match=('%s'%m))

  * The above code says the wheel client to passes 'accept' request and the minion key as an argument to the call_func. The whole if condition and the and try blocks are basic python to safely handle the failed cases and etc.

 You have got the basic hello world working. Now lets explore more on this, shall we.
 Read more here.  ramaseshan.github.io/technology/2015/04/02/saltstack-and-python-more-operations/
