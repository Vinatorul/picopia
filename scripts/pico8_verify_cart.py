import argparse
from pathlib import Path


def read_cart(path):
    text = Path(path).read_text()
    code, _, rest = text.partition("__gfx__\n")
    gfx, _, rest = rest.partition("__map__\n")
    map_data, _, sfx = rest.partition("__sfx__\n")
    return text, code, gfx, map_data, sfx


def check(path):
    text, code, gfx, map_data, sfx = read_cart(path)
    gfx_rows = gfx.splitlines() if gfx else []
    map_rows = map_data.splitlines() if map_data else []
    sfx_rows = sfx.splitlines() if sfx else []
    checks = {
        "file_exists": Path(path).exists(),
        "ends_with_newline": text.endswith("\n"),
        "has_header": "pico-8 cartridge" in text and "version 43" in text,
        "has_lua_section": "__lua__" in text,
        "has_core_functions": all(s in code for s in ["function _init()", "function _update()", "function _draw()"]),
        "has_map_world": "world_w=32" in code and "world_h=32" in code and "mget(x-1,y-1)" in code,
        "gfx_section_128x128": len(gfx_rows) == 128 and all(len(r) == 128 for r in gfx_rows),
        "map_section_64x256": len(map_rows) == 64 and all(len(r) == 256 for r in map_rows),
        "sfx_rows_valid": not sfx_rows or all(len(r) == 168 for r in sfx_rows),
    }
    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cart", nargs="?", default="picopia.p8")
    args = parser.parse_args()
    checks = check(args.cart)
    for name, ok in checks.items():
        print(f"{name}: {ok}")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
