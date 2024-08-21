#!/bin/bash

# Stop and remove all project containers
echo "Stopping and removing VacasGaL frontend container..."
cd $HOME/workspace/VacasGaL/frontend
docker-compose stop vacasgal-frontend
docker-compose rm -f vacasgal-frontend
echo "Stopping and removing VacasGaL backend container..."
cd $HOME/workspace/VacasGaL/backend
docker-compose stop vacasgal-backend
docker-compose rm -f vacasgal-backend
echo "Stopping and removing VacasGaL database container..."
cd $HOME/workspace/VacasGaL/db
docker-compose stop vacasgal-db
docker-compose rm -f vacasgal-db

# Remove project directories and files
echo "Removing VacasGaL directories and files..."
rm -rf "$HOME/workspace/VacasGaL"

echo "Cleanup completed. Docker, Docker Compose, and project files have been removed."