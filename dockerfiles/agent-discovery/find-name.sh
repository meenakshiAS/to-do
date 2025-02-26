#!/bin/bash
set -x  

ls -artl /ssh-dir/secrets/jcasc_token && cat /ssh-dir/secrets/jcasc_token

cp /ssh-dir/secrets/jcasc_token /secrets/ && ls -artl /secrets/jcasc_token && cat /secrets/jcasc_token

JCASC_TOKEN=$(cat /ssh-dir/secrets/jcasc_token)

export JCASC_TOKEN

while [ ! -f /var/jenkins_home/jenkins.yaml ]; do
  echo "Waiting for /var/jenkins_home/jenkins.yaml to be created..."
  sleep 2  
done

yq eval -i '(.jenkins.globalNodeProperties.0.envVars.env[] | select(.key == "CASC_RELOAD_TOKEN")).value = env(JCASC_TOKEN)' /var/jenkins_home/jenkins.yaml

cat /var/jenkins_home/jenkins.yaml

IP_ADDRESS=$(hostname -I | awk '{print $1}')

THREE_OCTETS=$(echo "$IP_ADDRESS" | cut -d '.' -f 1-3)

while true; do
  NMAP_OUTPUT=$(nmap -sn "$THREE_OCTETS".0/24)
  echo "nmap output: $NMAP_OUTPUT"

  IFS=$'\n' NMAP_LINES=($NMAP_OUTPUT)
 
  for LINE in "${NMAP_LINES[@]}"; do
    if [[ $LINE == *"agent"* ]]; then
      MATCHING_HOST=$LINE
      echo "$MATCHING_HOST"
      MACHINE_NAME=$(echo "$MATCHING_HOST" | awk '{print $5}')
      MACHINE_NAME=$(echo "$MACHINE_NAME" | cut -d '.' -f 1)
      echo "Machine name: $MACHINE_NAME"

      export MACHINE_NAME

      yq eval -i '(.jenkins.nodes[] | select(.permanent.nodeDescription == "ssh jenkins docker agent ")).permanent.launcher.ssh.host = env(MACHINE_NAME)' /var/jenkins_home/jenkins.yaml

      cat /var/jenkins_home/jenkins.yaml

      break 2  
    fi
  done

  echo "No matching hosts found, retrying in 2 seconds..."
  sleep 2  
done

JENKINS_CONTROLLER="jenkins_controller"
if ! curl -s -f --max-time 60 "http://${JENKINS_CONTROLLER}:8080/login" > /dev/null; then
    echo "Primary controller not reachable, falling back to multi controller..."
    JENKINS_CONTROLLER="multi_jenkins_controller"
    if ! curl -s -f --max-time 60 "http://${JENKINS_CONTROLLER}:8080/login" > /dev/null; then
        echo "Error: Neither primary nor multi controller is reachable"
        exit 1
    fi
fi

timeout 60 bash -c "until curl -s -f http://${JENKINS_CONTROLLER}:8080/login > /dev/null; do sleep 5; done" && echo "Jenkins is running" || echo "Jenkins is not running"
: "${JENKINS_STARTUP_TIMEOUT:=60}"  
timeout "${JENKINS_STARTUP_TIMEOUT}" bash -c "until curl -s -f http://${JENKINS_CONTROLLER}:8080/login > /dev/null; do sleep 5; done" && echo "Jenkins is running" || echo "Jenkins is not running"

echo "Jenkins is ready"
JENKINS_VERSION=$(curl -s -I -k http://admin:admin@$JENKINS_CONTROLLER:8080 | grep -i '^X-Jenkins:' | awk '{print $2}')
echo "Jenkins version is: $JENKINS_VERSION"

curl -X POST "http://admin:admin@$JENKINS_CONTROLLER:8080/reload-configuration-as-code/?casc-reload-token=thisisnotsecure"
