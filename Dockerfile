# Using the UBI8/UBI-MINIMAL as the base image
FROM registry.access.redhat.com/ubi8/ubi-minimal@sha256:574f201d7ed185a9932c91cef5d397f5298dff9df08bc2ebb266c6d1e6284cd1

# The container image will have the NodeJS version NODEJS_VERSION
ENV NODEJS_VERSION=14

# All the build will be done in the /build directory
WORKDIR /build
COPY requirements.txt /build/requirements.txt

# Using the microdnf package manager to install git, nodejs and python
RUN microdnf update
RUN microdnf install git -y

RUN echo -e "[nodejs]\nname=nodejs\nstream=${NODEJS_VERSION}\nprofiles=\nstate=enabled\n" > /etc/dnf/modules.d/nodejs.module
RUN microdnf install nodejs && microdnf remove nodejs-full-i18n nodejs-docs

RUN microdnf install python3.9 -y
RUN microdnf clean all

# Using python pip package manager to install the mkdocs libraries
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Using the npm package manager to install the cspell checker
RUN npm install -g cspell

# The mkdocs from a git repository will be cloned into the /docs directory
WORKDIR /docs

CMD ["/bin/bash"]
