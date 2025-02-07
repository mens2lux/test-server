sudo apt install python3-virtualenv python3-pip -y
mkdir .venvs
python3 -m virtualenv .venvs/server
echo 'source .venvs/server/bin/activate' >> .bashrc
source .bashrc