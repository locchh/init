# tsh

- One-line installation script 
```
TELEPORT_EDITION="oss"
TELEPORT_VERSION="16.4.6"
```

- Download and run the installation script on the server where you want to install Teleport: `curl https://cdn.teleport.dev/install-v16.4.6.sh | bash -s ${TELEPORT_VERSION?} ${TELEPORT_EDITION?}`

- Assign the following environment variables in the terminal where you will run Teleport installation commands, indicating the package and version to install:
 
```
export TELEPORT_PKG=teleport
export TELEPORT_VERSION=v16
export TELEPORT_CHANNEL=stable/${TELEPORT_VERSION?}
```

- Check your installation `tsh`

- Step 1/3. First-time setup:

```
tsh login --proxy teleport.example.com --user alice
tsh config --proxy teleport.example.com
```

- Try to access via terminal: `ssh user@example-node.teleport.example.com`

- Step 2/3. Configure Visual Studio Code via `Open-SSH`

- Step 3/3. Start a Remote Development session
