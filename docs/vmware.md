To install the VMware Horizon Client on Ubuntu via the command line, you can follow these steps:

1. **Download the Horizon Client Debian Package**:
   Go to the [VMware Horizon Client download page](https://customerconnect.omnissa.com/downloads/details?downloadGroup=CART25FQ2_LIN64_DEBPKG_2406&productId=1027&rPId=118857) and download the `.deb` package for Ubuntu. 

   Or, you can use `wget` to download it directly (replace `<URL>` with the actual download link for the Debian package):

   ```bash
   wget <URL>
   ```

2. **Install the Package Using APT**:
   Once the Debian package is downloaded, navigate to the directory where it’s saved, then use `apt` to install it:

   ```bash
   sudo apt install ./VMware-Horizon-Client-*.deb
   ```

   or
   ```bash
   sudo dpkg -i VMware-Horizon-Client-2406-8.13.0-9995429239.x64.deb
   ```

4. **Resolve Dependencies** (if necessary):
   If any dependencies are missing, `apt` will let you know. You can install the missing dependencies with:

   ```bash
   sudo apt --fix-broken install
   ```

5. **Launch VMware Horizon Client**:
   After installation, you can start VMware Horizon Client from the application menu or by running:

   ```bash
   vmware-view
   ```

This should get the VMware Horizon Client up and running on your Ubuntu system!
