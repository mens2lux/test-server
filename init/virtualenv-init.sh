sudo apt install python3-virtualenv python3-pip -y
mkdir .venvs
python3 -m virtualenv .venvs/test-server
echo 'source .venvs/test-server/bin/activate' >> .bashrc
source .bashrc
