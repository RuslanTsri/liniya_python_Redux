  while true
  do
    cd /home/pi/app/
    # python3 upload_logs.py
    # sudo rm -rf app.log
    # cd /home/pi/app
    # sudo unzip -o update.zip
    # sudo rm -rf update.zip
    # pip install -r requirements --break-system-packages
    python3 main.py
  done
