import nbtlib
import nbt
import os
import zlib
import zipfile
import anvil

def chunk(data: nbtlib.File):
    block_entities = nbtlib.List(data.get("block_entities"))
    for block_entitie in block_entities:
        if not block_entitie["id"] == nbtlib.String("command_block"):
            continue
        command = nbtlib.String(block_entitie.get("Command"))
        if command.count("TheRedStone2000"):
            command.replace("TheRedStone2000", "scientifiquefr")
        old_entitie = block_entitie
        block_entitie.merge({"Command":command})
        block_entities[block_entities.index(old_entitie)] = block_entitie
    data.merge({"block_entities":block_entities})
    print(f"{file} is done")
    return(data)
def region(filepath, file):
    region_file = anvil.Region.from_file(filepath)
    b = file.swapcase()
    print(file, b)
    S = ""
    for i in file:
        if i == b[file.index(i)]:
            S += i
    print(S)
    s = S.removeprefix(".")
    s = s.removesuffix(".")
    regionx, regionz = map(str, s.split("."))
    new_region_file = anvil.empty_region.EmptyRegion(int(regionx),int(regionz))
    for chunkx in range(32):
        for chunkz in range(32):
            try:
                data = anvil.Chunk.from_region(region_file,chunkx,chunkz)
                data = data.data
            except:
                continue
            new_chunk = anvil.Chunk(chunk(data))
            new_region_file.add_chunk(new_chunk)
a = input("region_folder : ").strip()
for file in os.listdir(a):
    filepath = os.path.join(a, file)
    region(filepath, file)
    



