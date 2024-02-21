# Machine-Learning


### Software and Account Requirement:-

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)   

Creating a conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/

OR

conda activate venv
```

To add Files to git
```
git add <file_name>
```
To check git status
```
git status
```
To check all versions maintained by git
```
git log
```

To create a version/commit all changes by git
```
git commit "message"
```
To send changes/version to Github
```
git push origin main
```
To check remote url
```
git remote -v
```
1.HEROKU_EMAIL = sparsha.usa@gmail.com \n
2.HEROKU_API_KEY = <YOUR_API_KEY>\n
3.HEROKU_APP_NAME = ml-project-regression\n

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
To list docker image
```
docker images
```

Run docker images

```
docker run -p 5000:5000 -e PORT=5000  9b91273a9c90
```
To check running container
```
docker ps
```
To stop docker container
```
docker stop <container_id>
```
```
python setup.
```