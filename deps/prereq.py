import os
from re import sub
import subprocess

def is_tool(binary):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which
    return which(binary) is not None


if is_tool('go'):
    print("Golang is already installed")
else:
    print("Install dependencies")
    os.chdir(os.path.expanduser('~'))
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', 'build-essential', 'jq', '-y'])
    subprocess.run(['wget', 'https://dl.google.com/go/go1.17.3.linux-amd64.tar.gz'])
    subprocess.run(['tar', '-xvf', 'go1.17.3.linux-amd64.tar.gz'])
    subprocess.run(['sudo', 'mv', 'go', '/usr/local'])
    subprocess.run(['rm', 'go1.17.3.linux-amd64.tar.gz'])
    print("------ Update bashrc ---------------")
    bash_object = open('{}/.bashrc'.format(os.environ['HOME']), 'a')
    bash_object.write('')
    bash_object.write('export GOPATH=$HOME/go\n')
    bash_object.write('export GOROOT=/usr/local/go\n')
    bash_object.write('export GOBIN=$GOPATH/bin\n')
    bash_object.write('export PATH=$PATH:/usr/local/go/bin:$GOBIN\n')
    bash_object.close()
    subprocess.run(['.', '{}/.bashrc'.format(os.environ['HOME'])])
    subprocess.run(['mkdir', '-p', '{}'.format(os.environ['GOBIN'])])
    subprocess.run(['mkdir', '-p', '{}/src/github.com'.format(os.environ['GOPATH'])])
    subprocess.run(['go', 'version'])



