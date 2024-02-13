You will find in this page our guidelines to:
- create a `Dockerfile` to build a Docker image 
- create a Github workflow to build and publish the Docker image to a registry

# Dockerfile

## Base image

- Debian-based images using the current [debian stable](https://www.debian.org/releases/) release (e.g. bookworm as of July 2023)
- `slim` variant whenever it is sufficient
- `alpine` variant only for highly constrained space environment (Offspot apps for instance). See [drawbacks](https://github.com/tiangolo/uvicorn-gunicorn-docker#-alpine-python-warning for explanations)
- July 2023, latest Python stable is `3.11` and Debian stable is `bookworm` hence `python:3.11-slim-bookworm` or `python:3.11-bookworm`

## RUN commands

- when using multiple lines, add a space before the `\` sign
- when linking multiple command, place the `&&` sign at the beginning of the next line
- on multiple lines, align the start of the commands, not the `&&`
- when listing packages to be installed by apt, add each of the on a new line, one per line, alphabetically order
- do not hesitate to add comments between lines to explain what is the reason / purpose of the next line
- do not include `apt-get clean` command since official Debian and Ubuntu images [automatically run apt-get clean](https://github.com/moby/moby/blob/03e2923e42446dbb830c654d0eec323a0b4ef02a/contrib/mkimage/debootstrap#L82-L105), so explicit invocation is not required


Sample:

```dockerfile

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    # locales required if tool has any i18n support
    locales-all \
 && rm -rf /var/lib/apt/lists/* \
 && python -m pip install --no-cache-dir -U \
    build \
    pip
```

## CMD

- add a command which displays the program's help

# Github Workflow

## When 

Publishing to the registry should be done on Github release event.

```
on:
  release:
    types: [published]
```

## Publish action

Except if not appropriate, we recommend to use our specific Github action : [openzim/docker-publish-action](https://github.com/openzim/docker-publish-action) which handles building the image and publishing it.

Some quirks not to forget:

- Image name convention is to use dashes not underscores

## Registry

We publish our images on ghcr.io