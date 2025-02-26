FROM ubuntu:ubuntu-latest

RUN sudo apt update \
    && sudo apt install pipx \
    && pipx ensurepath \
    && pipx install poetry

WORKDIR /var/www/app

ARG DEV=false
RUN python3 -m venv .venv && \
    source .venv/bin/activate \
    && poetry install

ENTRYPOINT ["/entrypoint.sh"]

HEALTHCHECK \
    --start-period=15s \
    --timeout=2s \
    --retries=3 \
    --interval=5s \
    CMD /healthcheck.sh
