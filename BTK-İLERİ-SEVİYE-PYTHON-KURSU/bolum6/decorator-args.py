def selamlama(fn):
    def inner(ad):
        fn(ad)
    return inner

@selamlama(count=2)
def gunaydin(ad):
    print(f"günaydın benim adım {ad}")

@selamlama(count=3)
def iyigunler(ad):
    print(f"iyi gunler adım {ad}")

gunaydin("Ali")
iyigunler("Ali")