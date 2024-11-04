Here's a step-by-step guide on how to generate an SSH key, add it to your GitHub account, and use it to clone a repository:

### 2. **Install Git:**

```
sudo apt install git
```

### 2. **Generate SSH Key:**
Open your terminal and run the following command to generate a new SSH key. Replace `your_email@example.com` with your GitHub email:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
If your system doesn't support the `ed25519` algorithm, you can use RSA:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

You'll be prompted to:
- **Enter a file to save the key**: Press `Enter` to accept the default location (e.g., `~/.ssh/id_ed25519` or `~/.ssh/id_rsa`).
- **Enter a passphrase** (optional but recommended): Type a passphrase or leave it blank for no passphrase.

### 3. **Add SSH Key to SSH Agent:**
Ensure that the SSH agent is running:
```bash
eval "$(ssh-agent -s)"
```

Then add your SSH private key to the agent:
```bash
ssh-add ~/.ssh/id_ed25519
```
If you used RSA, replace `id_ed25519` with `id_rsa`.

### 4. **Copy the SSH Key to Your Clipboard:**
Copy the public key to your clipboard. You can do this with the following command:
```bash
cat ~/.ssh/id_ed25519.pub
```
Copy the output of this command. If you used RSA, replace `id_ed25519.pub` with `id_rsa.pub`.

Alternatively, on Ubuntu, you can use the `xclip` tool (if installed):
```bash
xclip -sel clip < ~/.ssh/id_ed25519.pub
```

### 5. **Add SSH Key to GitHub:**

1. **Login to GitHub** and navigate to your account settings:
   - Click on your profile picture (top right) and choose **Settings**.
   - In the left sidebar, select **SSH and GPG keys**.
   
2. **Add a New SSH Key**:
   - Click the **New SSH key** button.
   - In the "Title" field, add a descriptive name (e.g., "Ubuntu Desktop").
   - Paste your SSH public key (from step 3) into the "Key" field.
   - Click **Add SSH key**.

### 6. **Test SSH Connection to GitHub:**
To confirm that your SSH key is set up correctly, run the following command:
```bash
ssh -T git@github.com
```

You should see a message like this if successful:
```
Hi <your-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

### 7. **Clone a GitHub Repository Using SSH:**
Now, you can clone repositories using SSH. Navigate to the repository you want to clone on GitHub and click the green "Code" button. Select the SSH URL (e.g., `git@github.com:username/repo.git`).

Then, in your terminal, use the following command to clone the repository:
```bash
git clone git@github.com:username/repo.git
```

That's it! You've successfully set up SSH for GitHub and cloned a repository using it.