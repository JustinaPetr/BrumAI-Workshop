# BrumAI Rasa Workshop Dockerfile

There is a docker image that has been built following the install instructions in the root of this repository.

The dockerfile in this folder was used to build the image. PRs for any issues welcome.

To run the dockerfile you should be in the root folder of this repository and run:

```bash
cd path-to-https://github.com/JustinaPetr/BrumAI-Workshop
docker build Docker -t brumai-workshop-justinapetr
docker run -ti -v `pwd`:/BrumAI-Workshop brumai-workshop-justinapetr
```

This command will download and run the docker image, giving you a bash shell in the image. It will also mount your local repository folder into the container so that you can use a local IDE to work on the code.

As the workshop is not about docker, I suggest only using this if you are already familiar with docker.

If you have issues regarding the docker image, feel free to message me directly or drop me an email to rob@styles.to and I will be glad to help you out :)
