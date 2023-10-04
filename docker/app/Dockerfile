# syntax=docker/dockerfile:1.4.1
FROM python:3.11-slim

ENV DISPLAY=:1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	apt-utils \
	gcc \
	build-essential \
	sudo \
	tk-dev \
	tigervnc-standalone-server \
	tigervnc-common \
	novnc \
	websockify \
	x11-apps \
	lxde \
	tigervnc-tools \
	# clean up
	&& apt-get autoremove -y \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/*

ARG WORKDIR
ENV PATH=${WORKDIR}/vendor/bin:$PATH \
	PYTHONPATH=${WORKDIR}/vendor/bin \
	PYTHONUSERBASE=${WORKDIR}/vendor

WORKDIR ${WORKDIR}

COPY ./env/requirements.txt ${PWD}
RUN pip install --upgrade pip;\
	pip install --no-cache-dir \
	-r requirements.txt \
	# Libraries used only when developing should write under this line.
	# (Don't write in requirements.txt)
	autopep8 \
	flake8 \
	pytest

# Create the user
ARG USERNAME
ARG HOMEDIR
ARG USERID
ARG GROUPID
RUN <<-EOF
	echo "Create User = ${USERID}. Group = ${GROUPID}"
	groupadd -g ${GROUPID} ${USERNAME}
	useradd -m -s /bin/bash -d ${HOMEDIR} -k /etc/skel -u ${USERID} -g ${GROUPID} ${USERNAME}
	echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME}
	chmod 0440 /etc/sudoers.d/${USERNAME}
EOF
USER ${USERNAME}
