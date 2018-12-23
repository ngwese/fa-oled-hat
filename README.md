setup
=====
install dependencies

```
sudo apt-get install i2c-tools libi2c-dev
sudo apt-get install python3-pip python3-setuptools python3-wheel
sudo pip3 install smbus2
```

enable i2c-0
```
sudo armbian-config
```
Select System > Hardware > i2c0, enable via <SPC>, save, and reboot.

