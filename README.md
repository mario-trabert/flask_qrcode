# flask_qrcode - RESTservice providing the determined qr-codes in the fridge
* The RESTservice can be accessed via http://<raspi-ip>:1337
* /test - returns a simple static json-test
* /get_qr-codes - returns the recognized qr-codes in the following format:
```
{
  "0": "medi02", 
  "1": "medi10", 
  "2": "medi05", 
  "3": "medi08"
}
```

## flask_get_qrcodes.py
usage, on Raspi: 
```
cd ~/fridge_qrcode
python3 flask_get_qrcodes.py
```


## test_qrcdode_console.py
use it on console to return determined qr-codes

ää test_qrcode_gui.py
use it on Raspi's desktop for a gui-view of the camera. It will display determined qr-codes in a window.
