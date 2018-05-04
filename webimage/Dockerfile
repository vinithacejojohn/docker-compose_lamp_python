FROM  ubuntu:16.04
RUN apt-get update \
  && apt-get install -y \
    apache2 \
    php7.0 \
    php7.0-bcmath \
    php7.0-mcrypt \
    vim \
    python3-pip \
    python3-pymysql \
    iputils-ping

RUN pip3 install pymysql
RUN mkdir /var/www/TestWeb
RUN a2dismod mpm_event
RUN a2enmod mpm_prefork cgi
#RUN rm -f /etc/apache2/sites-enabled/000-default.conf
COPY ./000-default.conf /etc/apache2/sites-enabled/000-default.conf
RUN mkdir /home/source
COPY ./source/index.py /home/source
VOLUME /home/source
WORKDIR /home/source
#RUN rm -f /etc/apache2/sites-available/000-default.conf
#RUN ln -s /etc/apache2/sites-enabled/000-default.conf  /etc/apache2/sites-available/000-default.conf
ENTRYPOINT service apache2 start && bash
