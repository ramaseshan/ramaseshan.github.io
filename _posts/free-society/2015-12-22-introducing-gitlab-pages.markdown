---
layout: post
title: "Static Websites on Gitlab"
modified:
categories: free-society
description: Static Website hosting on gitlab.
tags: [free-society, gitlab, pelican, python, static_website]
comments: true
share:
date: 2015-12-23T12:04:26
---

Most of you might have been using a website called github.com for hosting your code repos. For those of you who dont know what is github, it is basically a website that offers, a version control system. Github also offers free unlimited "public" code hosting. And then if you want private code hosting, you have to pay and use.

Great so what is wrong with github.com now.
It is a simple answer. github is not a free software. If you dont know what is a free software, read about it [here](http://www.gnu.org/philosophy/free-sw.en.html) and [here](http://www.fsf.org/about/what-is-free-software).

Why should I care if a hosted service is a free software or not ?
Simple, "Free Software requires Free Tools". More about it [here](https://mako.cc/writing/hill-free_tools.html)

Upon some research, I came across something called [Gitlab](https://gitlab.com). Gitlab is a free software, both in terms of code and in terms of hosting. We can have our own hosted version of the code or simply take the code and deploy it in our own servers. And another amazing thing I felt about gitlab was, it has taken some of the best features of github, bitbucket , gitorious etc and put them all together.

But for a long time, I have been missing one of the best features of github. It is called github-pages. It was the only reason I really didnt want to move out of github, if any of my project needed a website ? I didnt have the resource to host a website on a paid service. 

But alas to my happiness , gitlab on 22-Dec introduced gitlab-pages to its EE. So which meant, gitlab.com will have gitlab pages, where I could run website for my projects.

Here are some more links, where you can find the official documentation.

1. [Gitlab Pages](http://doc.gitlab.com/ee/pages/README.html)
2. [Writing plain html to deploy websites](https://gitlab.com/gitlab-examples/pages-plain-html)
3. [using jekyll to deploy sites](https://gitlab.com/gitlab-examples/pages-plain-html)

If you are a python person, and already in love with pelican, [go ahead here](/free-society/2015/12/23/introducing-gitlab-pages/,"link") to use pelican to deploy your blog.
Belive me pelican is a much better tool then jekyll. Here is a article from @arunrocks justifying [why pelican](http://arunrocks.com/moving-blogs-to-pelican/)


Now go ahead and explore Gitlab at gitlab.com