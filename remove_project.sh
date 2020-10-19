#!/bin/bash

echo "Stopping containers ..."
./stop_project.sh
echo

echo "Removing containers & networks ..."
docker-compose -f ./kafka/docker-compose.yml down
