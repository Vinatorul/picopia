import argparse
from pathlib import Path


SPRITES = {
    1: ["33333333", "3b333b33", "33333333", "333b3333", "33b333b3", "33333333", "3b333333", "33333333"],
    2: ["33333333", "33222233", "32b22b23", "32222223", "3b2222b3", "33222233", "333b3333", "33333333"],
    3: ["44444444", "44944444", "44449944", "44444444", "49944494", "44499944", "44444444", "44444444"],
    4: ["dddddddd", "ddcddddd", "ddddddcd", "dddcdddd", "dddddddd", "dcdddddd", "dddddcdd", "dddddddd"],
    5: ["bbbbbbbb", "bbbebbbb", "bbefebbb", "bbbeebbb", "bbb7bbbb", "bbbbbbbb", "bb7bbb7b", "bbbbbbbb"],
    6: ["ffffffff", "ff6fffff", "ffffff6f", "ffff6fff", "f6ffffff", "fffffff6", "fff6ffff", "ffffffff"],
    7: ["00000000", "000ee000", "00eeee00", "0e0ee0e0", "0e0000e0", "00eeee00", "000ee000", "00000000"],
    8: ["00000000", "000ee000", "00eeee00", "0e0ee0e0", "0e0000e0", "00eeee00", "00e00e00", "00000000"],
    9: ["00033000", "00333300", "000bb000", "00bbbb00", "0b0bb0b0", "0b0000b0", "00bbbb00", "00000000"],
    10: ["000aa000", "00aaaa00", "0aa77aa0", "00077000", "00a77a00", "0a7007a0", "00000000", "00000000"],
    11: ["000cc000", "00cccc00", "0cc77cc0", "000cc000", "00c00c00", "0c0000c0", "00000000", "00000000"],
    12: ["000bb000", "00bbbb00", "0bb77bb0", "000bb000", "00b00b00", "0b0000b0", "00000000", "00000000"],
    13: ["00000000", "00066000", "00666600", "06666660", "0eeeeee0", "0e0ee0e0", "0eeeeee0", "00000000"],
    14: ["66666666", "66555566", "65566656", "65666656", "65665556", "66555566", "66666666", "66666666"],
    15: ["00099000", "00999900", "09977990", "00099000", "00900900", "09000090", "00000000", "00000000"],
    16: ["00066000", "00666600", "00677600", "00066000", "00600600", "06000060", "00000000", "00000000"],
}

BASE_ROWS = [
    "gggggggggggggggg",
    "gbbggddddgggbbgg",
    "gbgggddddwgggbgg",
    "gggggbbbbwgggggg",
    "ggddggssswggddgg",
    "ggddggssswggddgg",
    "ggwwggbbbggwwggg",
    "ggwwggspsggwwggg",
    "ggbbggspsggbbggg",
    "ggddggbbbggddggg",
    "ggddggwwwggddggg",
    "gggggbbgggbggggg",
    "gbgggddddggggbgg",
    "gbbggddddgggbbgg",
    "gggggggggggggggg",
    "gggggggggggggggg",
]

TILES = {"g": 1, "b": 2, "d": 3, "w": 4, "f": 5, "s": 6, "p": 6, "r": 14}

SFX = [
    "000100000c0500f050120501505018050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "00010000180501b0501e05021050240500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "0001000015050120500f0500c05009050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "000100002005024050280502c05030050340500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "000100001005014050180501c05000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
]


def make_gfx():
    rows = []
    for y in range(128):
        row = ["0"] * 128
        sheet_y = y // 8
        py = y % 8
        for sid, sprite in SPRITES.items():
            sx = sid % 16
            sy = sid // 16
            if sheet_y == sy:
                for x, ch in enumerate(sprite[py]):
                    row[sx * 8 + x] = ch
        rows.append("".join(row))
    return "\n".join(rows) + "\n"


def make_map():
    rows = []
    for y in range(32):
        values = []
        for x in range(32):
            ch = "g"
            if 8 <= x < 24 and 8 <= y < 24:
                ch = BASE_ROWS[y - 8][x - 8]
            elif (x + y) % 17 == 0:
                ch = "b"
            elif (x * 5 + y * 11) % 41 == 0:
                ch = "r"
            elif (x * 3 + y * 5) % 29 == 0:
                ch = "d"
            elif (x * 7 + y * 2) % 37 == 0:
                ch = "w"
            values.append(TILES[ch])
        rows.append("".join(f"{value:02x}" for value in values).ljust(256, "0"))
    for _ in range(32):
        rows.append("0" * 256)
    return "\n".join(rows) + "\n"


def make_sfx():
    rows = [line.ljust(168, "0")[:168] for line in SFX]
    return "\n".join(rows) + "\n"


def apply_assets(path):
    p = Path(path)
    text = p.read_text()
    code = text.split("__gfx__")[0].rstrip() + "\n"
    p.write_text(code + "__gfx__\n" + make_gfx() + "__map__\n" + make_map() + "__sfx__\n" + make_sfx())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cart", nargs="?", default="picopia.p8")
    args = parser.parse_args()
    apply_assets(args.cart)
    print(f"updated {args.cart}")


if __name__ == "__main__":
    main()
