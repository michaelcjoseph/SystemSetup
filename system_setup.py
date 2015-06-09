# Copyright 2014 Michael C. Joseph
# Script to run after a fresh OS install or on a new computer
# Installs a number of different programs

import os

# Install Oh My ZSH
os.system("echo 'Installing Oh My ZSH...'")
os.system("curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh")
os.system("echo 'Installed'")

# Install Homebrew
os.system("echo 'Installing Homebrew...'")
os.system("ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"")
os.system("echo 'Installed'")

# Install Python with OpenSSL
# Your Mac comes with Python installed but this is to incorporate OpenSSL
os.system("echo 'Installing Python with OpenSSL...'")
os.system("brew install python --with-brewed-openssl")
os.system("echo 'Installed'")

# Install Git
os.system("echo 'Installing Git...'")
os.system("brew install git")
os.system("echo 'Installed'")

# Install pip
os.system("echo 'Installing pip...'")
os.system("sudo easy_install pip")
os.system("echo 'Installed'")

# Instal PostgreSQL
os.system("echo 'Installing PostgreSQL...'")
os.system("brew install postgresql")
os.system("echo 'Installed'")

# Auto Start PostgreSQL on login
os.system("ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents")

# Instal virtualenv
os.system("echo 'Installing Virtualenv...'")
os.system("sudo pip install virtualenv")
os.system("sudo pip install virtualenvwrapper")
os.system("brew install libevent")
os.system("echo 'Installed'")

# Install scientific python libraries
os.system("brew install gcc")
os.system("sudo pip install cython")
os.system("sudo pip install numpy")
os.system("sudo pip install matplotlib")
os.system("sudo pip install scipy")
os.system("sudo pip install ipython")
os.system("sudo pip install pandas")
os.system("sudo pip install sympy")
os.system("sudo pip install statsModels")
os.system("sudo pip install scikit-learn")
