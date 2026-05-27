import argparse
import os
from pathlib import Path


CART_NAME = "picopia.p8"
LUA_PATH = "src/picopia.lua"
ENV_PATH = ".env"
CART_DIR_ENV = "PICO8_CART_DIR"
CART_HEADER = "pico-8 cartridge // http://www.pico-8.com\nversion 43\n"


SPRITES = {
    1: ["33333333", "3b333b33", "33333333", "333b3333", "33b333b3", "33333333", "3b333333", "33333333"],
    2: ["44444444", "49444494", "44494444", "44444444", "44944449", "44449444", "49444444", "44444444"],
    3: ["333b3333", "3b3b33b3", "333b3b33", "b333b333", "33b333b3", "333b3333", "3b333333", "33333333"],
    4: ["44494444", "49494494", "44494944", "94449444", "44944449", "44494444", "49444444", "44444444"],
    5: ["33333333", "33222233", "32b22b23", "32222223", "3b2222b3", "33222233", "333b3333", "33333333"],
    6: ["44444444", "44555544", "45955954", "45555554", "49555594", "44555544", "44494444", "44444444"],
    7: ["00333300", "033bbbb0", "03bbbb30", "00333300", "00055000", "00555500", "00500500", "05500550"],
    8: ["00444400", "04499940", "04999940", "00444400", "00055000", "00555500", "00500500", "05500550"],
    9: ["ffffffff", "ff6fffff", "ffffff6f", "ffff6fff", "f6ffffff", "fffffff6", "fff6ffff", "ffffffff"],
    10: ["44444444", "44944444", "44449944", "44444444", "49944494", "44499944", "44444444", "44444444"],
    11: ["bbbbbbbb", "bbbebbbb", "bbefebbb", "bbbeebbb", "bbb7bbbb", "bbbbbbbb", "bb7bbb7b", "bbbbbbbb"],
    12: ["44444444", "44494444", "44959444", "44499444", "44454444", "44444444", "44544454", "44444444"],
    13: ["66666666", "65555556", "65666556", "65555556", "66655666", "65555556", "65666656", "66666666"],
    16: ["00000000", "000ee000", "00eeee00", "0e0ee0e0", "0e0000e0", "00eeee00", "000ee000", "00000000"],
    17: ["00000000", "000ee000", "00eeee00", "0e0ee0e0", "0e0000e0", "00eeee00", "00e00e00", "00000000"],
    18: ["00033000", "00333300", "000bb000", "00bbbb00", "0b0bb0b0", "0b0000b0", "00bbbb00", "00000000"],
    19: ["000aa000", "00aaaa00", "0aa77aa0", "00077000", "00a77a00", "0a7007a0", "00000000", "00000000"],
    20: ["00099000", "00999900", "09977990", "00099000", "00900900", "09000090", "00000000", "00000000"],
    21: ["000cc000", "00cccc00", "0cc77cc0", "000cc000", "00c00c00", "0c0000c0", "00000000", "00000000"],
    22: ["000bb000", "00bbbb00", "0bb77bb0", "000bb000", "00b00b00", "0b0000b0", "00000000", "00000000"],
    23: ["00000000", "00066000", "00666600", "06666660", "0eeeeee0", "0e0ee0e0", "0eeeeee0", "00000000"],
}

BASE_ROWS = [
    "dddddddddddddddd",
    "ddbbydddyyddbbdd",
    "ddbyyyddfydddbdd",
    "dddddbbbfydddddd",
    "ddyydyssswyddydd",
    "ddyydyssswyddydd",
    "ddffdybbbddffddd",
    "ddffdyskpsddffddd",
    "ddbbdyspsddbbddd",
    "ddyydybbbddyyddd",
    "ddyydyfffddyyddd",
    "dddddbbdddbddddd",
    "dbdddyyyyddddbdd",
    "dbbddyyyydddbbdd",
    "dddddddddddddddd",
    "dddddddddddddddd",
]

TILES = {
    "g": 1,
    "d": 2,
    "h": 3,
    "y": 4,
    "b": 5,
    "n": 6,
    "t": 7,
    "r": 8,
    "s": 9,
    "p": 10,
    "f": 11,
    "w": 12,
    "k": 13,
}

SFX = [
    "000100000c0500f050120501505018050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "00010000180501b0501e05021050240500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
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
            ch = "d"
            if 8 <= x < 24 and 8 <= y < 24:
                ch = BASE_ROWS[y - 8][x - 8]
            elif (x + y) % 23 == 0:
                ch = "r"
            elif (x * 5 + y * 11) % 31 == 0:
                ch = "n"
            elif (x * 3 + y * 5) % 29 == 0:
                ch = "y"
            elif (x * 13 + y * 17) % 41 == 0:
                ch = "k"
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


def load_env(path):
    env_path = Path(path)
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        key, separator, value = line.partition("=")
        key = key.strip()
        if separator and key and key not in os.environ:
            os.environ[key] = value.strip().strip('"').strip("'")


def resolve_cart_path(cart, output_dir):
    cart_path = Path(cart)
    if cart_path.is_absolute() or cart_path.parent != Path("."):
        return cart_path
    return Path(output_dir) / cart_path


def assemble_cart(cart_path, lua_path):
    lua = Path(lua_path).read_text().rstrip() + "\n"
    cart = CART_HEADER + "__lua__\n" + lua
    cart += "__gfx__\n" + make_gfx()
    cart += "__map__\n" + make_map()
    cart += "__sfx__\n" + make_sfx()
    cart_path = Path(cart_path)
    cart_path.parent.mkdir(parents=True, exist_ok=True)
    cart_path.write_text(cart)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cart", nargs="?", default=CART_NAME)
    parser.add_argument("--lua", default=LUA_PATH)
    parser.add_argument("--output-dir")
    parser.add_argument("--env", default=ENV_PATH)
    args = parser.parse_args()
    load_env(args.env)
    output_dir = args.output_dir or os.environ.get(CART_DIR_ENV, ".")
    cart_path = resolve_cart_path(args.cart, output_dir)
    assemble_cart(cart_path, args.lua)
    print(f"updated {cart_path} from {args.lua}")


if __name__ == "__main__":
    main()
