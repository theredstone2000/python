import os
import anvil
import nbtlib
import nbt
OLD_NAME = "TheRedStone2000"
NEW_NAME = "scientifiquefr"
TARGET_Z = any("a")  # Coordonnée Z monde ciblée

def process_region_file(filepath, file):
    region = anvil.Region.from_file(filepath)

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
    
    
    
    modified = False
    mod_region_chunks = []
    for chunk_x in range(32):
        for chunk_z in range(32):
            try:
                chunk = region.get_chunk(chunk_x, chunk_z)
            except:
                continue

            if chunk.tile_entities:
                print(f"{chunk_x} {chunk_z} {file}")
                ind = 0
                for block_entity in chunk.tile_entities:
                    print(block_entity["id"])
                    if block_entity["id"].__repr__() == "minecraft:command_block":
                        print("test_done")
                        x = block_entity["x"]
                        y = block_entity["y"]
                        z = block_entity["z"]
                    
                        print(x,y,z)
                        command = block_entity.get("Command")
                        print(f"wsdfvsdhgf           gsfhdfs {command}")
                        if command and OLD_NAME in command:
                            new_command = command.__repr__()
                            block_entity["Command"] = nbt.nbt.TAG_String(new_command.replace(OLD_NAME, NEW_NAME))
                            modified = True
                            print(f"Modifié en {x} {y} {z}")
                            chunk.tile_entities[ind] = block_entity
                            ind += 1
            mod_region_chunks.append(chunk)
                        
    if modified:
        mod_region = anvil.EmptyRegion(int(regionx), int(regionz), mod_region_chunks)
        mod_region.chunks = mod_region_chunks
        print(mod_region.chunks)
        os.remove(filepath)
        print(mod_region.chunks)
        mod_region.save(filepath)
        print(f"Sauvegardé : {filepath}")

def main():
    region_folder = input("Entrez le chemin COMPLET du dossier region : ").strip()

    if not os.path.isdir(region_folder):
        print("Chemin invalide.")
        return

    for file in os.listdir(region_folder):
        if file.endswith(".mca"):
            filepath = os.path.join(region_folder, file)
            
            print(file)
            process_region_file(filepath, file)

    print("✔ Scan terminé.")

if __name__ == "__main__":
    main()
    
    
    

