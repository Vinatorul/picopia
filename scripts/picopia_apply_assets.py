import argparse
from pathlib import Path


SPRITES = {
    0: ["33333333", "3b333b33", "33333333", "333b3333", "33b333b3", "33333333", "3b333333", "33333333"],
    1: ["33333333", "33222233", "32b22b23", "32222223", "3b2222b3", "33222233", "333b3333", "33333333"],
    2: ["44444444", "44944444", "44449944", "44444444", "49944494", "44499944", "44444444", "44444444"],
    3: ["dddddddd", "ddcddddd", "ddddddcd", "dddcdddd", "dddddddd", "dcdddddd", "dddddcdd", "dddddddd"],
    4: ["bbbbbbbb", "bbbebbbb", "bbefebbb", "bbbeebbb", "bbb7bbbb", "bbbbbbbb", "bb7bbb7b", "bbbbbbbb"],
    5: ["ffffffff", "ff6fffff", "ffffff6f", "ffff6fff", "f6ffffff", "fffffff6", "fff6ffff", "ffffffff"],
    6: ["00000000", "000ee000", "00eeee00", "0e0ee0e0", "0e0000e0", "00eeee00", "000ee000", "00000000"],
    7: ["00000000", "000ee000", "00eeee00", "0e0ee0e0", "0e0000e0", "00eeee00", "00e00e00", "00000000"],
    8: ["00033000", "00333300", "000bb000", "00bbbb00", "0b0bb0b0", "0b0000b0", "00bbbb00", "00000000"],
    9: ["000aa000", "00aaaa00", "0aa77aa0", "00077000", "00a77a00", "0a7007a0", "00000000", "00000000"],
    10: ["000cc000", "00cccc00", "0cc77cc0", "000cc000", "00c00c00", "0c0000c0", "00000000", "00000000"],
    11: ["000bb000", "00bbbb00", "0bb77bb0", "000bb000", "00b00b00", "0b0000b0", "00000000", "00000000"],
    12: ["00000000", "00066000", "00666600", "06666660", "0eeeeee0", "0e0ee0e0", "0eeeeee0", "00000000"],
}

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
        sy = y // 8
        py = y % 8
        if sy == 0:
            for sid, sprite in SPRITES.items():
                sx = sid % 16
                for x, ch in enumerate(sprite[py]):
                    row[sx * 8 + x] = ch
        rows.append("".join(row))
    return "\n".join(rows) + "\n"


def make_sfx():
    rows = [line.ljust(168, "0")[:168] for line in SFX]
    return "\n".join(rows) + "\n"


def apply_assets(path):
    p = Path(path)
    text = p.read_text()
    code = text.split("__gfx__")[0].rstrip() + "\n"
    p.write_text(code + "__gfx__\n" + make_gfx() + "__sfx__\n" + make_sfx())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cart", nargs="?", default="picopia.p8")
    args = parser.parse_args()
    apply_assets(args.cart)
    print(f"updated {args.cart}")


if __name__ == "__main__":
    main()
