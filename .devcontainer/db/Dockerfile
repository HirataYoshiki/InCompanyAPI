FROM mysql:5.7

RUN mkdir ${PWD}/testsrc
COPY ./my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/conf.d/my.cnf