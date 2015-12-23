echo -n "Enter your gitlab username : "
read username
echo -n "Enter your repo name for gitlab pages (eg blog): "
read repo
cd ~/Documents
mkdir pelican
cd pelican
git clone https://$username@gitlab.com/$username/$repo.git
rc=$?; 
if [[ $rc != 0 ]]; 
then 
  echo "Git cloning error. Please check your repo name or username or password"
  exit $rc; 
fi
if [ -f /etc/redhat-release ]
then
  sudo dnf install python-pip python-virtualenv
else
  sudo apt-get install python-pip python-virtualenv
fi
virtualenv .
source bin/activate
cd $repo
pip install pelican markdown
pelican-quickstart
cat > .gitlab-ci.yml << EOF
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
EOF
cat > content/first-blog.md << EOF
Title: My first blog
Date: 2010-12-24 10:20
Modified: 2010-12-25 19:30
Category: Python
Tags: pelican, publishing
Slug: my-first-post
Authors: $username
Summary: First Blog

This is the content of my super blog post.
EOF

pelican

git add .
git commit -m "My First commit"
git push
