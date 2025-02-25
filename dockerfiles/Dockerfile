ARG JENKINS_VERSION=2.492.1

FROM jenkins/jenkins:"${JENKINS_VERSION}"

USER root

COPY jobs /var/jenkins_home/jobs

RUN chown -R jenkins:jenkins /var/jenkins_home/jobs

USER jenkins

RUN echo "${JENKINS_VERSION}" > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt.override

RUN ln -s /usr/share/jenkins/ref/plugins.txt.override /usr/share/jenkins/ref/plugins.txt && jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

COPY jenkins.yaml /usr/share/jenkins/ref/jenkins.yaml.override