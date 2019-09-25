FROM docker:dind

RUN apk update && apk add sudo build-base python3 python3-dev py-pip linux-headers git

RUN pip3 install git+https://github.com/MPBA/clipper.git@develop#subdirectory=clipper_admin

RUN mkdir /home/clipper
WORKDIR /home/clipper

ADD scripts/ /home/clipper/
RUN ["chmod", "+x", "/home/clipper/entrypoint.sh"]
RUN ["chmod", "+x", "/home/clipper/entrypoint-dev.sh"]

ENTRYPOINT [ "/home/clipper/entrypoint.sh" ]
