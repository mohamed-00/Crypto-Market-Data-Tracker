import apicryto
from time import sleep


time_sec = int(input('Enter the time by second: '))
while True:
    crypto = apicryto.CryptoData()
    crypto.fetch_data()
    crypto.process_data()
    crypto.save_to_excel()
    sleep(time_sec)
exit()
20