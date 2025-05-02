rfkill unblock bluetooth
sudo systemctl start bluetooth

sudo apt install bluetooth bluez bluez-tools

bluetoothctl

agent on
default-agent
power on
scan on

# After seeing the controller MAC address (e.g. XX:XX:XX:XX:XX:XX)
pair XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX

exit

jstest /dev/input/js0


#############-------systemmd

sudo nano /etc/systemd/system/ps4-reconnect.service

