To install IntelliJ IDEA, you can use the following commands depending on your operating system:

### For Linux (Ubuntu / Debian):

1. **Download IntelliJ** via `snap`:
   ```bash
   sudo snap install intellij-idea-community --classic
   ```
   - For the Ultimate edition, use:
     ```bash
     sudo snap install intellij-idea-ultimate --classic
     ```

2. **Alternatively, install using `tar.gz`**:

   - Download the latest `.tar.gz` file from [JetBrains' website](https://www.jetbrains.com/idea/download/#section=linux).
   - Extract the file:
     ```bash
     tar -xzf ideaIC-*.tar.gz
     ```
   - Navigate into the `bin` directory and start IntelliJ:
     ```bash
     cd idea-*/bin
     ./idea.sh
     ```

### For macOS:

1. **Using `brew`**:
   ```bash
   brew install --cask intellij-idea
   ```
   - For the Ultimate edition:
     ```bash
     brew install --cask intellij-idea-ultimate
     ```

### For Windows:

1. **Download the installer** from the [IntelliJ IDEA download page](https://www.jetbrains.com/idea/download/#section=windows) and follow the installation instructions.

Once installed, you can open IntelliJ IDEA from your application menu or by running `idea` in the terminal if you added it to your PATH.
