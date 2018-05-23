# Initial Course Installs

## TablePlus

[TablePlus](https://tableplus.io/) will let you view, query and manage your SQLite databases during the course.

## Python

### Setup

See if Python is installed.

```bash
which python
```

Check which version is installed. Most likely it will be version 2.7.x.

```bash
python --version
```

We're going to be learning version 3 of Python, and then later in the course, talk about differences between 2 and 3, because there is still a lot of version 2 code out in the wild and you will likely need to work with it.

## Managing versions

> **Prerequisite:** For pyenv to install correctly, you need the Xcode command line tools. Type this command into your terminal and wait. `xcode-select --install`

### OSX / pyenv

OSX users, you should have Homebrew installed at this point. If you don't, do it now. Then run these commands in order.

```bash
brew install pyenv
pyenv install 3.6.0
mkdir ~/workspace/python && cd $_
touch hello.py
code .
```

After Pyenv is installed, you can make version 3.6.0 the new, globally accepted version by typing the following.

```
pyenv global 3.6.0
```

Now, when you check the version of Python with the command below, it should return 3.6.0.

```
python --version
```

---

#### Troubleshooting


If it still returns a different version, you will need to edit your `~/.bash_profile` file - or `~/.zshrc` if you installed oh-my-zsh - and follow steps 2 and 3 from the instructions on the [Basic Github Checkout section](https://github.com/yyuu/pyenv#basic-github-checkout) of pyenv's docs.

---

### Windows

The [venv](https://docs.python.org/3/library/venv.html#module-venv) was released with Python 3.6 to give Windows user the ability to execute different versions of Python.

## Hello, world

We're going to do the traditional `Hello, world` program to start off. Put the following code in `~/workspace/python/hello.py`.

```python
print("Hello!")
print("Is it me you're looking for?")
```

In the CLI, execute the following command in the `python` directory.

```bash
python hello.py
```

## Python interpreter

You can use the CLI interpreter to enter and run some code that you just want to test out without having to put it in a file and running it.

```
╰─$ python
Python 3.6.0 (default, Jul 14 2015, 19:46:27)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> i_am_awesome = True
>>> if i_am_awesome:
...   print("bow down to me")
...
bow down to me
```

# Optional, Handy Tooling

[Anaconda](https://packagecontrol.io/packages/Anaconda)

[Djaneiro](https://github.com/squ1b3r/Djaneiro)

