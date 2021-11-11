FROM psagrera/fluent-jti:1.2 

ENV FLUENTD_OPT=""

RUN fluent-gem install prometheus-client -v 0.7.1
RUN fluent-gem install fluent-plugin-prometheus -v 0.3.0 

ADD     fluentd-alpine.start.sh   fluentd-alpine.start.sh
RUN     chmod 777 fluentd-alpine.start.sh

COPY fluent.conf  /fluentd
COPY    plugins   /fluentd/plugins

EXPOSE 24284

ENV OUTPUT_KAFKA=false \
    OUTPUT_INFLUXDB=false \
    OUTPUT_STDOUT=true \
    OUTPUT_PROMETHEUS=false \
    PORT_JTI=50000

CMD /fluentd-alpine.start.sh
