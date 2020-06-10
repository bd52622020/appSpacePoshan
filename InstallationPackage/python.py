#!/user/bin/env python3

import os
import requests

def install_python(): #function to start operations
    
    #Crating a path for wokring
    path = os.path.expanduser("~/Desktop/InstallstionFiles")
    
    # Creating a directory name InstallationFiles in Desktop
    os.mkdir(path)
    
    # Changing the path toward current working path ie: Desltop/InstallationFiles
    os.chdir(path)
    
    # Downloading Python files Message
    print("Downloading Python Version 3.8.8")
    
    # downloading the compressed file from the url
    url = requests.get('https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz', allow_redirects=True)
    file = open("python.tgz", "wb").write(url.content)
    
    # Decompress the downloaded file (unzip, extact, vorbose, file)
    p = os.system("tar zxvf ./python.tgz");
    if p != 0 :
        print("Error in extacting python file");
        
    #Redirect the current working path to python folder path 
    path_python = os.path.expanduser(path + "/" + "python-3.6.8")
    
    #change the directory from ~/Desktop/InstallstionFiles to ~/Desktop/InstallstionFiles/python-3.6.8
    os.chdir(path_python);
    
    # after downloading installation process starts
    print("Installing build essentials ")
    #installing build essential with through administration login it includes the required pacakges to run Debian Package
    p = os.system("sudo apt install build-essential");
    
    #installing compression library
    print("Installing zlib  library")
    p = os.system("sudo apt install zlin1g-dev");
    
    #building python file
    print("Building python files")
    
    p = os.system("./configure --enable-shared --with-zlib=/usr/include --enable-optimizations --prefix=" + path_python);
    
    p = os.system("make build-all")
    
    p = os.system("make install");
    
    # Set environment variables in primary bash files
    p = os.system("echo 'export PATH=~/Desktop/scriptfiles/Python-3.6.8:$PATH' >> ~/.bashrc");
    p = os.system("echo 'export LD_LIBRARY_PATH=~/Desktop/scriptfiles/Python-3.6.8/lib:$LD_LIBRARY_PATH' >> ~/.bashrc");
    p = os.system("exec bash");
    
    
    
    
    
    
    
    
        
    
     
     
     