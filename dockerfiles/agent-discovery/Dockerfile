FROM debian:bookworm-20250224-slim as prepare-stage

COPY *sh /usr/local/bin/

RUN chmod +x /usr/local/bin/*.sh

RUN apt update && apt install -y --no-install-recommends \
    ca-certificates \
    curl \
    jq \
    nmap \
    && rm -rf /var/lib/apt/lists/* && rm -fr /tmp/*

RUN if [ "$(uname -m)" = "aarch64" ]; then \
        curl -L https://github.com/mikefarah/yq/releases/download/v4.13.5/yq_linux_arm64 -o /usr/bin/yq; \
    else \
        curl -L https://github.com/mikefarah/yq/releases/download/v4.13.5/yq_linux_amd64 -o /usr/bin/yq; \
    fi && chmod +x /usr/bin/yq

CMD ["sh", "-c", "echo 'Stage is ready'; ls -l /var/jenkins_home/"]
