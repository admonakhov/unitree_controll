Controlling unitree g1 via Dualshock

# Installation 
pip3 install -e ./sdk

pip3 install pygame

# Controller

sudo apt install bluetooth bluez bluez-tools

sudo systemctl start bluetooth

bluetoothctl

power on

agent on

default-agent

scan on

get adress:

Wireless Controller XX:XX:XX:XX:XX

pair XX:XX:XX:XX:XX

connect XX:XX:XX:XX:XX

trust XX:XX:XX:XX:XX

sudo usermod -aG input unitree

# Run 
python g1_controller.py $interface

# Controlling

L2 + cirle -> Damping
L2 + UP -> Stand
L2 + Square -> Walk

Robot is prepared for walking