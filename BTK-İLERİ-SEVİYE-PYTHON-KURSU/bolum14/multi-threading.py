import time 
import threading

def calculate_square(numbers):
    print("sayıların kareleri hesaplanıyor ")

    for i in numbers:
        time.sleep(0.3)
        print("kare:", i*i)

def calculate_cube(numbers):
    for i in numbers:
        time.sleep(0.3)

        print("küpü:", i*i*i)


sayilar=[3,5,8,9,5,25]

t=time.time()

# calculate_square(sayilar) #ard arda çalışacaklar fakat biz aynı anda çalışmalarını istiyoruz
# calculate_cube(sayilar)

t1=threading.Thread(target=calculate_square,args=(sayilar,)) #thread oluşturduk hedefimiz square fonksiyonu ve dışardan alacağımız argümanlar sayilar dizisi
t2=threading.Thread(target=calculate_cube,args=(sayilar,))

t1.start()
t2.start()

t1.join()
t2.join()
print("işlem tamamlandı:",time.time()-t)