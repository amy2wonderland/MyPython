#!/bin/sh

echo "Configuring AWS credentials"

curl -qL -o aws_credentials.json http://169.254.170.2/$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI > aws_credentials.json

aws configure set region $AWS_REGION
aws configure set aws_access_key_id `jq -r '.AccessKeyId' aws_credentials.json`
aws configure set aws_secret_access_key `jq -r '.SecretAccessKey' aws_credentials.json`
aws configure set aws_session_token `jq -r '.Token' aws_credentials.json`
sed -i "s/aws_session_token/aws_security_token/g" ~/.aws/credentials # boto fix since it uses "aws_security_token"
aws configure set aws_session_token `jq -r '.Token' aws_credentials.json`
