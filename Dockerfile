FROM ubuntu:18.04

RUN apt update && \
    apt install -y software-properties-common git curl p7zip-full wget whois locales python3 python3-pip upx psmisc && \
    add-apt-repository -y ppa:longsleep/golang-backports && \
    apt update && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias es_ES.UTF-8
RUN apt-get install iptables  -y

RUN apt-get install -y \
        nmap \
        vim
RUN apt install -y iptables && \
    apt install net-tools && \
    git clone https://github.com/Und3rf10w/kali-anonsurf.git && \
    cd kali-anonsurf && ./installer.sh

RUN apt install -y tinyproxy 
RUN apt-get update && \
      apt-get -y install sudo

RUN apt upgrade -y

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
RUN echo "root:root" | chpasswd

EXPOSE 8080
WORKDIR /root
ENV LANG es_ES.utf8
ARG DEBIAN_FRONTEND=noninteractive

USER root
RUN git clone https://github.com/f0ns1/evilBrowser.git && \
	chmod +x evilBrowser/script_anonymous_proxy.sh


ENTRYPOINT ["evilBrowser/script_anonymous_proxy.sh"]
CMD /bin/bash
