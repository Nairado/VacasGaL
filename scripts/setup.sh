#!/bin/bash

set -e # Exit immediately if any command fails

# CONFIG CONST
PROJECT_PATH='$HOME/workspace/VacasGaL'
GIT_REPO_DEV='https://github.com/Nairado/VacasGaL/dev'
GIT_REPO_PRO='https://github.com/Nairado/VacasGaL/main'

# FUNCTIONS
is_program_installed() {
    local program=$1
    command -v $program >/dev/null 2>&1
}

is_program_up_to_date() {
    local program=$1
    local url=$2
    local sed_1=$3
    local sed_2=$4
    local installed_version
    local latest_version

    installed_version=$($program --version | awk '{print $3}' | sed 's/,//')
    latest_version=$(curl -fsSL $url | grep '"tag_name":' | sed -E $sed_1)

    if [ -n "$sed_2" ]; then
        latest_version=$(echo $latest_version | sed $sed_2)
    fi

    if [ "$installed_version" == "$latest_version" ]; then
        return 0
    else
        return 1
    fi
}

install_docker() {
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    rm get-docker.sh
}

install_docker_compose(){
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
}


# MAIN SCRIPT
# Update the system
echo "Updating repositories and libraries..."
sudo apt update --quiet
sudo apt upgrade --quiet -y

# Install Curl (if not already installed)
if ! command -v curl &>/dev/null; then
    echo "Installing Curl..."
    sudo apt install -y curl
    echo "Curl installed."
fi

# Install Docker
if ! is_program_installed "docker"; then
    echo "Installing Docker..."
    install_docker
    echo "Docker installed."
else
    if ! is_program_up_to_date "docker" "https://api.github.com/repos/docker/docker-ce/releases/latest" 's/.*"([^"]+)".*/\1/' ""; then
        echo "Docker is installed but not up-to-date."
        read -p "Do you want to update Docker to the latest version? (y/n): " choice
        if [ "$choice" == "y" ]; then
            echo "Updating Docker..."
            install_docker
            echo "Docker updated."
        else
            echo "WARNING: You chose not to update Docker. Running outdated versions may cause conflicts."
        fi
    fi
fi
# Add user into docker group
sudo usermod -aG docker $USER
echo "Docker process is complete."

# Install Docker Compose
if ! is_program_installed "docker-compose"; then
    echo "Installing Docker Compose..."
    install_docker_compose
    echo "Docker Compose installed."
else
    if is_program_up_to_date "docker-compose" "https://api.github.com/repos/docker/compose/releases/latest" 's/.*"([^"]+)".*/\1/' 's/^v//'; then
        echo "Docker Compose is installed but not up-to-date."
        read -p "Do you want to update Docker Compose to the latest version? (y/n): " choice
        if [ "$choice" == "y" ]; then
            echo "Updating Docker Compose..."
            install_docker_compose
            echo "Docker Compose updated."
        else
            echo "WARNING: You chose not to update Docker Compose. Running outdated versions may cause conflicts."
        fi
    fi
fi

# Install python3-venv package (if not already installed)
if ! dpkg -l | grep -q "python3-venv"; then
    sudo apt update
    sudo apt install -y python3-venv
fi

# Clone the Git repository
git clone $GIT_REPO $PROJECT_DIR

# Check if the Git clone was successful
if [ $? -ne 0 ]; then
    echo "Failed to clone the Git repository. Please check the repository URL and try again."
    exit 1
fi

# Access the project directory
cd $PROJECT_DIR

# Build and run Docker containers
echo "Starting Docker containers..."
docker-compose up --build -d

# Install Python dependencies
echo "Installing Python dependencies..."
docker-compose exec backend pip install -r requirements.txt

# Install Python dependencies
echo "Installing Python dependencies in the container..."
docker-compose exec backend pip install -r requirements.txt

# Fill Database
echo "Filling PostgreSQL Database..."
docker-compose exec backend python3 app/scripts/fill_db.py

# Show access information
echo "The project has been installed and configured successfully."
echo "You can access the application at http://localhost:4200 (frontend) and http://localhost:8000 (backend)."