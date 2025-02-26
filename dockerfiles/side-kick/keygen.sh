#!/bin/bash
# This script generates a new SSH key pair and updates a Docker Compose file with the public key.
# Create secrets directory if it doesn't exist
set -x
LOC=$1
if [[ -z "$LOC" ]]; then
    LOC="./"
fi

echo "Location is $LOC"
ls -artl "$LOC"

rm "$LOC/conductor_ok"

mkdir -p "$LOC/secrets"

rm -fr "$LOC/jenkins_agent_ed" "$LOC/jenkins_agent_ed.pub"

ssh-keygen -t ed25519 -f "$LOC/jenkins_agent_ed" -N ""

chmod 444 "$LOC/jenkins_agent_ed"

pubkey=$(cat "$LOC/jenkins_agent_ed.pub")

echo "The public key is $pubkey"

echo "$pubkey" > "$LOC/authorized_keys" && chown 1000:1000 "$LOC/authorized_keys"

openssl rand -hex 24 > "$LOC/secrets/jcasc_token"
cat "$LOC/secrets/jcasc_token"

echo "OK" > "$LOC/conductor_ok"

echo "SSH key pair generated successfully."
