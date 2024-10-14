import asyncio
async def fetch_data(delay):
    print("veri alınıyor...")
    await asyncio.sleep(delay)
    print("veri alındı...")
    return {"data": "bazı veriler"}

async def main(msg):
    print("start")
    task= fetch_data(2) #asenkron fonksiyonu başka bir asenkron fonksiyonun içinde çağırırken başında await  kullanmalıyız
    result= await task
    print(f"alınan veri: {result}") #fetch data fonksiyonunda tanımlanan 2 saniye dolduktan sonra veriyi alır 
    print("end")
asyncio.run(main())

#gather metoduyla tüm fonksiyonları tek çatıda async olarak çalıştırabiliriz
# result = await asyncio.gather(fetch_data(1,2),fetch_data(3,1),fetch_data(2,2)) örnek kullanım şekli
#   for result in results: şeklindede hepsini yazdırabiliriz 
#    print(result)