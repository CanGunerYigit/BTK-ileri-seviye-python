import time 
import multiprocessing

def calculate_square(numbers):

    for i in numbers:
        time.sleep(0.3)
        print("kare:", i*i)
                                    #bu iki fonksiyonu ayrı processlere atayacağız
def calculate_cube(numbers):
    for i in numbers:
        time.sleep(0.3)

        print("küpü:", i*i*i)

if __name__ == '__main__': #o anda olduğumuz process bizim main processimiz ise
    arr=[2,4,6,8,12,56]
    t=time.time()
    p1=multiprocessing.Process(target=calculate_square,args=(arr,))
    p2=multiprocessing.Process(target=calculate_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(time.time()-t)