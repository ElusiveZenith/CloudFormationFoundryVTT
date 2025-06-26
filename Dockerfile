FROM felddy/foundryvtt:latest
USER root
RUN apt-get update && apt-get install -y net-tools
USER node
