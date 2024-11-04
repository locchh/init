Here are the steps to install Docker on Ubuntu:

### 1. **Uninstall Old Versions (Optional)**
If you have older versions of Docker installed, remove them:
```bash
sudo apt remove docker docker-engine docker.io containerd runc
```

### 2. **Update Package Index:**
First, update your package index:
```bash
sudo apt update
```

### 3. **Install Required Packages:**
Install dependencies required for Docker installation:
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

### 4. **Add Docker’s GPG Key:**
Add Docker’s official GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

### 5. **Set Up the Docker Repository:**
Add the Docker APT repository to your system:
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

### 6. **Update the Package Index Again:**
After adding the Docker repository, update the package index:
```bash
sudo apt update
```

### 7. **Install Docker:**
Install Docker by running:
```bash
sudo apt install docker-ce docker-ce-cli containerd.io
```

### 8. **Verify Docker Installation:**
Check if Docker is installed and running:
```bash
sudo systemctl status docker
```

You can also verify that Docker is correctly installed by running:
```bash
sudo docker --version
```

### 9. **Run Docker Without Sudo (Optional):**
To run Docker without needing `sudo` each time, add your user to the Docker group:
```bash
sudo usermod -aG docker $USER
```

After this, log out and back in or run:
```bash
newgrp docker
```

### 10. **Test Docker Installation:**
To verify that Docker is working, run a test container:
```bash
docker run hello-world
```

If everything is installed correctly, Docker will pull the `hello-world` image and run it, printing a confirmation message.

Let me know if you need further assistance!