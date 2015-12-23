---
layout: post
title: "Using Pelican to deploy static website in Gitlab."
modified:
categories: free-society
description: Static Website hosting on gitlab.
tags: [free-society, gitlab, pelican, python, static_website]
comments: true
share:
date: 2015-12-23T21:00:26
---

I my last article I wrote about gitlab pages.
This article is a quick note on how to deploy your static blog using pelican.

**This is a more developer /  computer known person prespective. If something goes wrong do ping me**

Steps :

1. Sign up for an account at gitlab.com
2. Create a new project called blog.
3. Open the GNU/Linux terminal and follow the steps.
4. sudo dnf install python-pip (Fedora) or sudo apt-get install python-pip (Debian)
5. sudo pip install virtualenv
6. cd ~/Documents
7. git clone https://gitlab.com/your_username/blog.git
7. virtualenv blog
8. cd blog
9. source bin activate
10. pip install pelican markdown
11. pelican-quickstart .Once you hit this command,enter the details of your site name and description. Go with the defaults for the rest of the things.
12. cd content
13. create a file called first-blog.md (or any name). Write content following this pattern http://docs.getpelican.com/en/3.6.3/content.html
14. cd ../
15. type the command "pelican" . Once this command is done, you should have a folder called output. If that has generated, proceed, else hold up and cross check any errors or missed steps.
16. create a file called .gitlab-ci.yml and enter the following contents in it.
"""
pages:
  stage: deploy
  script:
  - mkdir .public
  - cp -r output/* .public
  - mv .public public
  artifacts:
    paths:
    - public
  only:
  - master
"""
17. git add .
18. git commit -m "Blog on gitlab" 
19. git push

You are done. If all go good, you should see the build starting in your projects build page.

Now sit back and relax until the build completes. Once done, you should see your website live at your-username.gitlab.io/blog

If you are looking for a ready repo, have a look at the [sample repo](https://gitlab.com/voidspacexyz/pages/tree/master) I have put up

I also have a sample blog running [here](http://voidspacexyz.gitlab.io/pages)

If you have written it better, send me a PR :-)