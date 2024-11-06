GNU COBOL (formerly known as OpenCOBOL) is an open-source COBOL compiler that can be used to compile and run COBOL programs. Below are the steps to download, install, and use GNU COBOL on **Ubuntu**:

### Step 1: Update Package List
First, it's a good idea to update your system's package list to ensure you have the latest information about available packages.

```bash
sudo apt update
```

### Step 2: Install GNU COBOL (GnuCOBOL)
On Ubuntu, you can easily install **GNU COBOL** (GnuCOBOL) using the `apt` package manager. The package name is `gnucobol`.

Run the following command to install GnuCOBOL:

```bash
sudo apt install gnucobol
```

This will automatically download and install the GnuCOBOL compiler and related dependencies.

### Step 3: Verify Installation
Once the installation is complete, you can verify that GnuCOBOL is correctly installed by checking the version:

```bash
cobc -v
```

You should see output similar to:

```
GnuCOBOL 2.2
```

This means that the installation was successful.

### Step 4: Write a Simple COBOL Program
Next, let's write a simple COBOL program. Open a text editor and create a file called `hello.cob`.

For example, using the `nano` text editor:

```bash
nano hello.cob
```

Add the following COBOL code to `hello.cob`:

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HelloWorld.
       PROCEDURE DIVISION.
           DISPLAY 'Hello, World!'.
           STOP RUN.
```

This is a simple COBOL program that prints "Hello, World!" to the console.

### Step 5: Compile the COBOL Program
Now, use the `cobc` compiler to compile the COBOL source code into an executable. The `cobc` command is the GNU COBOL compiler.

Run the following command to compile the program:

```bash
cobc -x hello.cob
```

Explanation:
- `-x` tells `cobc` to create an executable.
- `hello.cob` is the name of your COBOL source file.

If there are no errors, the compilation should succeed, and an executable file named `hello` will be created in the same directory.

### Step 6: Run the Executable
Finally, you can run the compiled COBOL program by executing the generated `hello` file:

```bash
./hello
```

You should see the following output:

```
Hello, World!
```

### Step 7: Additional Compilation Options
GNU COBOL has various compilation options that can be useful depending on your needs. For example:
- **To compile without creating an executable** (to produce an object file), you can use the `-c` flag:

  ```bash
  cobc -c hello.cob
  ```

- **To link object files** into an executable (if you compiled with `-c` earlier):

  ```bash
  cobc -x hello.o
  ```

### Conclusion:
You have now installed GNU COBOL on your Ubuntu system, written a simple COBOL program, compiled it, and executed it successfully. You can continue learning COBOL by writing more complex programs, referring to the [GNU COBOL documentation](https://gnucobol.sourceforge.io/), and exploring more features of the compiler.

Let me know if you need more details on COBOL or any further steps!
