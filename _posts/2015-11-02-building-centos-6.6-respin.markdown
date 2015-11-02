---
layout: post
title: Building a Custom Centos 6.6 Respin
modified:
categories: Technology
description: "Building a Custom Centos 6.6 after reading a lot of links"
tags: [centos6.6,resping,custombuilds]
comments:
share:
date: 2015-11-02
---
As a part of our work at Fractalio, we wanted to build a custom Cent- OS ISO, to be able to circulate it amongst people for them test and get a feel of what we are trying to build.  We had a trail once before and we had failed miserably building nothing.

>  We build statues out of snow, and weep to see them melt. -- Walter Scott

Well we wanted to give it a shot again. This time with the previous learnings as our pillar. This time we started reading a lot more articles and links to first understand what is being talked about and have a clear picture of what is to be done. 

>  You can't build a great building on a weak foundation. You must have a solid foundation if you're going to have a strong superstructure. -- Gordon B. Hinckley

This article will share all the learning that I went through to actually get something working. So lets get started.

Best Practices :
1. Span a virtual machine with centos - 6.6 minimal installed. So that if something goes wrong it dosent mess up your system

Pre-Requisites :

1. A virtual machine
2. Centos 6.6 Minimal ISO
3. Internet or the packages (.rpm files) along with all the dependencies
4. A mind to be ready to expriment and learn :-)


So Span out the virtual machine you installed with Centos and execute the following instructions. Each command will also be accompanied with the details of why it is done. If you find something wrong, please do let me know in the comments. So poweron your virtual machine and follow on


1 . Initial Setup:

    {% highlight bash %}

        yum -y install rsync yum-utils createrepo genisoimage  isomd5sum yum-downloadonly
 
    {% endhighlight %}
    
     - rsync to sync to actual iso to your re-spin
     - createrepo to make a folder with special permission so that the installed recognises the rpm inside this folder
     - genisoimage to generate the iso from the custom packages
     - yum-downloadonly  is a yum plugin to only download the rpms and not actually install it

2 . Get the files required

{% highlight bash %}

cd /root
mkdir respin-centos

mount -o loop,ro /root/CentOS-6.6-x86_64-minimal.iso /mnt
rsync -av /mnt/ .

find . -name TRANS.TBL -exec rm -f {} \;

{% endhighlight %}

    - respin-centos is the folder where we will build our iso from
    - mount is to actually mount the iso in some mount point so that you can access the files. This is in an assumption that you have copied the actual iso to the /root partitiion of the VM or the iso building machine.
    - rsync is needed because the cp sometimes dosent copy all the hidden files. files like .discinfo .treeinfo are missed when you do a cp -r . So we use rsync, which dosent differenciate between these files
    - The last line removed the unwanted files. that file is unwanted.

3 . Get the packages you want to install. 

We will be installing python-devel, python-pip and httpd.

{% highlight python %}

yum install -y python-devel python-pip httpd --downloadonly --downloaddir /root/respin-centos/Packages/

{% endhighlight%}

    - Remember the yum-downloadonly ? we are actually doing it here. This will download the the rpms and the dependency rpms to the Packages folder.

4 . Test the rpms

Now we check the package we add in ISO above is require any dependencies.If require than we add  dependencies.

{% highlight bash %}
rpm –initdb –dbpath /root/build/Packages/

rpm -ivh –test –dbpath /root/build/Packages/ /root/build/Packages/*.rpm
After using above command if output is as shown below than we need to resolve fail dependencies.

warning: /root/build/Packages/acl-2.2.49-6.el6.x86_64.rpm: Header V3 RSA/SHA1 Signature, key ID c105b9de: NOKEY
error: Failed dependencies:
/etc/mime.types is needed by httpd-2.2.15-26.el6.centos.x86_64
apr-util-ldap is needed by httpd-2.2.15-26.el6.centos.x86_64
httpd-tools = 2.2.15-26.el6.centos is needed by httpd-2.2.15-26.el6.centos.x86_64
libapr-1.so.0()(64bit) is needed by httpd-2.2.15-26.el6.centos.x86_64
libaprutil-1.so.0()(64bit) is needed by httpd-2.2.15-26.el6.centos.x86_64

{% endhighlight %}
Do not worry about warning messages.Our focus is only on fail dependencies as shown above.We require to download failed dependencies.Using below command to check yum provides these dependencies.
 
{% highlight bash %}
yum provides “*/etc/mime.types*”
{% endhighlight %}
Once you download all  dependencies  once again run below command to check all dependencies downloaded.

{% highlight bash %}
rpm -ivh –test –dbpath /root/build/Packages/ /root/build/Packages/*.rpm

The log show  following texts if all dependencies downloaded.

warning: /root/build/Packages/acl-2.2.49-6.el6.x86_64.rpm: Header V3 RSA/SHA1 Signature, key ID c105b9de: NOKEY
Preparing… ########################################### [100%]
installing package filesystem-2.4.30-3.el6.x86_64 needs 8KB on the /mnt filesystem.
{% endhighlight %}


5 . Repodata

We need a file called the comps.xml to actually get the iso to work. Follow the steps below to actually get the file

{% highlight bash %}
ls repodata/
34bae2d3c9c78e04ed2429923bc095005af1b166d1a354422c4c04274bae0f59-c6-minimal-x86_64.xml
490d05bedc0f8be64c5c26a3c2a804b817eec00fe42223d1fb856566fa248130-primary.xml.gz
5291f680f7b6afd2444e583202951977779200bc5a295922ef816a90476e493e-filelists.sqlite.bz2
6e147c9aea5bf4c0f1ba7ecf759ddd3a259003a7f12a5a74398c9f05d672573d-primary.sqlite.bz2
98678399cf20d3bcc860229b9a3ba5d99a4446e95947030d567113e412fcc412-filelists.xml.gz
ce2d698b9fb1413b668443e88835a0642cea8f387c7f25cc946f56dd93f109bb-c6-minimal-x86_64.xml.gz
dc720ad0a977caf5eb6dee0648c29e420a22e2f4277e099c925ee727de0735cd-other.sqlite.bz2
e0d5ad3bff4d0bd6ffd5037d6e76049b09c1d4f697445be6071d100f865a46f3-other.xml.gz
repomd.xml

gunzip repodata/ce2d698b9fb1413b668443e88835a0642cea8f387c7f25cc946f56dd93f109bb-c6-minimal-x86_64.xml.gz


ls repodata/
34bae2d3c9c78e04ed2429923bc095005af1b166d1a354422c4c04274bae0f59-c6-minimal-x86_64.xml
490d05bedc0f8be64c5c26a3c2a804b817eec00fe42223d1fb856566fa248130-primary.xml.gz
5291f680f7b6afd2444e583202951977779200bc5a295922ef816a90476e493e-filelists.sqlite.bz2
6e147c9aea5bf4c0f1ba7ecf759ddd3a259003a7f12a5a74398c9f05d672573d-primary.sqlite.bz2
98678399cf20d3bcc860229b9a3ba5d99a4446e95947030d567113e412fcc412-filelists.xml.gz
ce2d698b9fb1413b668443e88835a0642cea8f387c7f25cc946f56dd93f109bb-c6-minimal-x86_64.xml
dc720ad0a977caf5eb6dee0648c29e420a22e2f4277e099c925ee727de0735cd-other.sqlite.bz2
e0d5ad3bff4d0bd6ffd5037d6e76049b09c1d4f697445be6071d100f865a46f3-other.xml.gz
repomd.xml

mv repodata/ce2d698b9fb1413b668443e88835a0642cea8f387c7f25cc946f56dd93f109bb-c6-minimal-x86_64.xml repodata/comps.xml

{% endhighlight %}

6 . Create the repo

{% highlight bash %}

createrepo -u "media://`head -1 .discinfo`" -g repodata/comps.xml .

{% endhighlight %}

7 . The Kickstart file

The ks file is very important. Refer to a sample kickstart file here (https://github.com/ramaseshan/respin-iso/centos-6.6-x86-64)

If you look at the reference kickstart, there would be two post sections. One with chroot and the other without chroot (nochroot).
The difference between the two is

- If you want to do some non root operations like copying files that just have to be present in the new iso they can be done through the nochroot stuff.  Things like, copy, untar, modifying conf files, sed, awk etc. Hold There is more readon.
How are we actually copying files is simple, there are 3 componenets involved here, the vmlinuz (the actual installer, /mnt/source, wehere the iso is mounted, and the /mnt/sysimage, where the installing system is mounted. Read the sameple ks file to see a live example)
Refer to the next section on where the to be copied files will be.


- But if you want root operations like useradd, chmod etc, do it in the post section with chroot on. **


8 . How to copy files

{% highlight bash %}

[root@localhost respin-centos]# mkdir tar
[root@localhost respin-centos]# touch tar/test
[root@localhost respin-centos]# ls tar/
test

{% endhighlight%}

Now you can copy this tar folder like this in the nochroot section of the ks file

{% highlight bash %}
cp -r /mnt/source/tar /mnt/sysimage/opt/
{% endhighlight %}

9 . isolinux 

{% highlight bash %}

chmod 755 isolinux/isolinux.cfg 
#modify the isolinux.cfg to make it work like this

default linux
prompt 0
timeout 600
display boot.msg
F1 boot.msg
F2 options.msg
F3 general.msg
F4 param.msg
F5 rescue.msg
label linux
kernel vmlinuz
append initrd=initrd.img ks=cdrom:/ks.cfg ( Add this entry in this line )

{% endhighlight%}

10 . Generate the iso

{% highlight bash %}

mkisofs -r -R -J -T -v -no-emul-boot \
    -boot-load-size 4 \
    -boot-info-table \
    -V "respin-centos" \
    -p "Ramaseshan" \
    -A "respin-centos-build1" \
    -b isolinux/isolinux.bin \
    -c isolinux/boot.cat \
    -x "lost+found" \
    --joliet-long \
    -o /tmp/boot.iso .
    
    
 89.86% done, estimate finish Fri Oct 30 16:19:23 2015
 92.17% done, estimate finish Fri Oct 30 16:19:23 2015
 94.47% done, estimate finish Fri Oct 30 16:19:23 2015
 96.77% done, estimate finish Fri Oct 30 16:19:23 2015
 99.08% done, estimate finish Fri Oct 30 16:19:23 2015
Total translation table size: 77608
Total rockridge attributes bytes: 34111
Total directory bytes: 59914
Path table size(bytes): 112
Done with: The File(s)                             Block(s)    216770
Writing:   Ending Padblock                         Start Block 216852
Done with: Ending Padblock                         Block(s)    150
Max brk space used 63000
217002 extents written (423 MB)

{% endhighlight %}

Yay !! We have the iso now. No go span another VM and start testing it :-)

>  To invent an airplane is nothing. To build one is something. But to fly is everything.   -- Otto Lilienthal


More references :
Checkout my gitrepo : https://github.com/ramaseshan/respin-iso/centos-6.6-x86-64

I have  my ks file and the quick commands docs and also the reference links I had used. Incase if you feel, I have written too much and need the commands quick. :-)