import schedule
import time as tm
from datetime import time, timedelta, datetime
import os
from sendMail import action_send
number = 0

def job():
  global number
  number +=1
  print("Arta Ganteng -", number)

  # tanggal_sekarang = datetime.now().strftime("%d%m%Y_%H%M")
  # nama_file = f"report_{tanggal_sekarang}.txt"
  # path = "dataA/" + nama_file

  # with open(path, 'w') as file:
  #   file.write("Ini adalah laporan yang dibuat pada tanggal : " + tanggal_sekarang)

  # def read_list_file(path):
  #   files = os.listdir(path)
  #   for file in files:
  #       print(file)

  # path = "dataA"
  # if os.path.exists(path):
  #   files = os.listdir(path)
  #   for file in files:
  #       file_path = os.path.join(path, file)
  #       new_path = os.path.join("dataB", file)
  #       os.replace(file_path, new_path)

  send = action_send('arta.windy03@gmail.com', 'Notifikasi Alert Python', 'Halo halo halo, aku ganteng')
  print(send)

schedule.every(10).seconds.do(job)

while True:
  schedule.run_pending()
  tm.sleep(1)