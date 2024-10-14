def selamlama(fn):
    def inner(ad):
        print("hoşgeldiniz")
        fn(ad)
        print("baybay")
    return inner

@selamlama
def gunaydin(ad):
    print(f"günaydın {ad}")

@selamlama
def iyigunler(ad):
    print(f"iyi günler {ad}")

gunaydin("Ali")
iyigunler("Ali")