# Create and run a Docker container

## Create a Dockerfile

Create a `Dockerfile` which starts with a base docker image e.g. Ubuntu.

In this file, you install the software you need, set environment variables, create directories etc.

[Example](Dockerfile).

## Build the container

Use the command `docker build -t` to create a container and tag it with a name.

Docker is looking for a file called `Dockerfile` in the specified directory.

[Example](build.sh)

## Run the container

Use `docker run` to run the container. 

`-w` sets the working directory in the container's file system.

`-v` mounts a volume (directory or file), which is like a mapped network drive. The docker container has read/write access to this directory on the host machine.

The `docker run` command includes the commands you want to run in the container.

[ Example](run.sh)

You can also run a container [interactively](interactive.sh).
