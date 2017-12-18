catalog = 'girl'

print(f"curl -s 'https://wallpaperscraft.com/catalog/{catalog}/1024x768' | grep -w download | grep -w '_blanck' | sort -u >> {catalog}.txt")

for p in range(1, 339):
    print(
        f"curl -s 'https://wallpaperscraft.com/catalog/{catalog}/1024x768/page{p}' | grep -w download | grep -w '_blanck' | sort -u >> {catalog}.txt")
