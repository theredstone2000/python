import anvil
import nbtlib
input()
a = "fhg.jh13.e2"
b = a.swapcase()
print(a, b)
S = ""
for i in a:
    if i == b[a.index(i)]:
        S += i
print(S)
s = S.removeprefix(".")
s = s + "d"
final = s.partition(".")

region = input("file path : ")
region = anvil.Region.from_file(region)
chunkx = input("chunk coords x : ")
chunkz = input("chunk coords z : ")
chunkx = int(chunkx)
chunkz = int(chunkz)
chunkx = -1
chunkz = 0
chunk = anvil.Chunk.from_region(region,chunkx,chunkz)
bloc = input("input : blocx, blocy, blocz : ")
blocx, blocy, blocz = map(str, bloc.split(", "))
blocx, blocy, blocz = int(blocx), int(blocy), int(blocz)
block = chunk.get_block(blocx,blocy,blocz, force_new=True)
block_name = block.name()
print(f"ton bloc est : {block_name}")
