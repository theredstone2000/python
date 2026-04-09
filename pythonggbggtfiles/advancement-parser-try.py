import os
import math
import json


def make_advancement(filename: str, parent_id: str) -> dict:
    item_id = filename.removesuffix(".json")

    return {
        "parent": parent_id,
        "criteria": {
            "find": {
                "trigger": "minecraft:inventory_changed",
                "conditions": {
                    "items": [
                        {
                            "item": f"minecraft:{item_id}"
                        }
                    ]
                }
            }
        },
        "display": {
            "announce_to_chat": True,
            "description": f"Find {item_id}!",
            "icon": {
                "count": 1,
                "id": f"minecraft:{item_id}"
            },
            "show_toast": True,
            "title": item_id.replace("_", " ").title(),
            "frame": "task"
        },
        "requirements": [
            [
                "find"
            ]
        ],
        "sends_telemetry_event": False
    }


def choose_branching_factor(num_items: int) -> int:
    # sourcery skip: inline-immediately-returned-variable
    """
    Choose an automatic branching factor based on number of items.
    Tries to keep the tree roughly balanced and not too deep or wide.
    """
    if num_items <= 2:
        return 1  # simple chain
    # Start near sqrt(n) to balance width and depth
    k = int(math.sqrt(num_items))
    # Clamp to a reasonable range
    k = max(2, min(k, 6))
    return k


# Create root advancement
root_advancement = {
    "criteria": {
        "consumed_item": {
            "trigger": "minecraft:tick"
        }
    },
    "display": {
        "announce_to_chat": False,
        "background": "minecraft:block/blue_wool",
        "description": "Find Everything!",
        "icon": {
            "count": 1,
            "id": "minecraft:lily_of_the_valley"
        },
        "show_toast": True,
        "title": "The Hunt!",
        "frame": "goal"
    },
    "requirements": [
        [
            "consumed_item"
        ]
    ],
    "sends_telemetry_event": False
}

with open("root.json", "w", encoding="utf-8") as f:
    json.dump(root_advancement, f, indent=2)


# Collect all item JSON filenames (excluding root)
item_files = []
for filename in os.listdir("."):
    if not filename.lower().endswith(".json"):
        continue
    if filename == "root.json":
        continue
    item_files.append(filename)

item_files.sort()
n = len(item_files)

if n == 0:
    raise SystemExit("No item JSON files found (excluding root.json).")

BRANCHING_FACTOR = choose_branching_factor(n)

# Build a balanced k-ary tree:
# parent of node i (0-based) is:
#   - "root" if i < BRANCHING_FACTOR
#   - item_files[(i - 1) // BRANCHING_FACTOR] otherwise
parents = {}

for i, filename in enumerate(item_files):
    if i < BRANCHING_FACTOR:
        parent_id = "root"
    else:
        parent_index = (i - 1) // BRANCHING_FACTOR
        parent_filename = item_files[parent_index]
        parent_id = parent_filename.removesuffix(".json")
    parents[filename] = parent_id

# Write each advancement file with its computed parent
for filename in item_files:
    parent_id = parents[filename]
    advancement_data = make_advancement(filename, parent_id)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(advancement_data, f, indent=2)
