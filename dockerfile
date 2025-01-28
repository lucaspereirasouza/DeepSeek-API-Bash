FROM debian:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

WORKDIR /app

COPY . /app

RUN chmod +x ./install.sh
RUN ./install.sh

CMD [ "/bin/bash", "-c run.sh" ]