import time
import asyncio
def main(msg):
    print("start")
    time.sleep(2)
    print(msg)

main("merhaba") #çalıştırdığımızda 2 şer saniye arayla yazdığını görürüz fakat aynı anda çalışmaya başlamasını istiyoruz
main("merhaba")
#o zaman asenkron şekilde çalıştırmalıyız
async def main(msg):
    print("start")
    await asyncio.sleep(2)
    print(msg)

asyncio.run(main("merhaba"))