FROM  mysql/mysql-server

RUN apt-get update \
  && apt-get install -y \
    mysql-server \
    vim \
    python3 \
    python3-pip \
    iputils-ping

RUN pip3 install pymysql

#RUN sed -i 's##bind-address = 0.0.0.0'"bind-address = 0.0.0.0"'#g' /etc/mysql/mysql.conf.d/mysqld.cnf
ADD script.py /home/
WORKDIR /home/
ENV MYSQL_RANDOM_ROOT_PASSWORD false
ENV  MYSQL_ROOT_PASSWORD: testpass
#ENTRYPOINT  service mysql start && bash
