To install the specific NVIDIA driver version 550.107.02 on Ubuntu, follow these steps:

### 1. **Update the package index:**
```bash
sudo apt update
```

### 2. **Add the NVIDIA PPA (if not already added):**
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
```

### 3. **Install the specific NVIDIA driver version:**
First, you can check for available drivers with:
```bash
sudo apt search nvidia-driver-550
```

If `nvidia-driver-550` is listed, install it using:
```bash
sudo apt install nvidia-driver-550
```

If this version is not available directly, you'll need to manually download and install the driver from NVIDIA's website.

### 4. **Download and Install NVIDIA Driver Manually:**

1. Download the driver from the [NVIDIA official website](https://www.nvidia.com/Download/index.aspx?lang=en-us).

   - Set your GPU model and Linux version, then select the driver version `550.107.02`.

2. After downloading, make the installer executable:
   ```bash
   chmod +x NVIDIA-Linux-x86_64-550.107.02.run
   ```

3. Run the installer:
   ```bash
   sudo ./NVIDIA-Linux-x86_64-550.107.02.run
   ```

   Follow the on-screen instructions to complete the installation.

### 5. **Verify installation:**
After installation, reboot your system:
```bash
sudo reboot
```

Once rebooted, check the installed NVIDIA driver and its version:
```bash
nvidia-smi
```

This should display NVIDIA-SMI version 550.107.02 if the installation was successful.