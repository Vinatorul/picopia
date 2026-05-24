import argparse
from pathlib import Path


def read_cart(path):
    text = Path(path).read_text()
    code, _, rest = text.partition("__gfx__\n")
    gfx, _, rest = rest.partition("__map__\n")
    map_data, _, sfx = rest.partition("__sfx__\n")
    return text, code, gfx, map_data, sfx


def map_values(map_data):
    values = set()
    for row in map_data.splitlines()[:32]:
        for i in range(0, 64, 2):
            values.add(int(row[i:i + 2], 16))
    return values


def contains_all(text, items):
    return all(item in text for item in items)


def ordered(text, items):
    positions = [text.find(item) for item in items]
    return all(pos >= 0 for pos in positions) and positions == sorted(positions)


def sprite_pixels(gfx_rows, sid):
    sx = sid % 16
    sy = sid // 16
    return [row[sx * 8:sx * 8 + 8] for row in gfx_rows[sy * 8:sy * 8 + 8]]


def check(path):
    text, code, gfx, map_data, sfx = read_cart(path)
    gfx_rows = gfx.splitlines() if gfx else []
    map_rows = map_data.splitlines() if map_data else []
    sfx_rows = sfx.splitlines() if sfx else []
    values = map_values(map_data) if map_data else set()
    sprite0 = sprite_pixels(gfx_rows, 0) if len(gfx_rows) == 128 else []
    checks = {
        "file_exists": Path(path).exists(),
        "ends_with_newline": text.endswith("\n"),
        "cart_sections": contains_all(text, ["pico-8 cartridge", "version 43", "__lua__", "__gfx__", "__map__", "__sfx__"]),
        "core_functions": contains_all(code, ["function _init()", "function _update()", "function _draw()"]),
        "map_world": contains_all(code, ["world_w=32", "world_h=32", "mget(x-1,y-1)"]),
        "gfx_128x128": len(gfx_rows) == 128 and all(len(row) == 128 for row in gfx_rows),
        "map_64x256": len(map_rows) == 64 and all(len(row) == 256 for row in map_rows),
        "sfx_rows": bool(sfx_rows) and all(len(row) == 168 for row in sfx_rows),
        "visible_terrain_ids": contains_all(code, ["t_grass=1", "t_bush=2", "t_dry=3", "t_wet=4", "t_flower=5", "t_soil=6", "t_rock=14"]),
        "map_uses_visible_tiles": 0 not in values and 14 in values,
        "draws_map_ids_directly": "spr(t,(x-1)*8,(y-1)*8)" in code,
        "sprite_zero_reserved_empty": bool(sprite0) and all(row == "00000000" for row in sprite0),
        "tools_present": contains_all(code, ["name=\"chopbit\"", "name=\"tillbit\"", "name=\"watbit\"", "name=\"sproutbit\"", "name=\"smashbit\""]),
        "tools_ordered_for_growth": ordered(code, ["name=\"chopbit\"", "name=\"tillbit\"", "name=\"watbit\"", "name=\"sproutbit\"", "name=\"smashbit\""]),
        "menus_present": contains_all(code, ["function update_build_menu()", "function draw_build_menu()", "function update_grow_menu()", "function draw_grow_menu()"]),
        "quest_shortcut": contains_all(code, ["function quest_shortcut()", "btn(4) and btnp(5)", "btn(5) and btnp(4)"]),
        "grow_menu_rules": contains_all(code, ["name=\"grass\",cost=0", "name=\"bush\",cost=0,tile=t_bush,spr=2,p=0", "name=\"flower\",cost=0,tile=t_flower,spr=5,p=1", "grid[ty][tx]!=t_wet", "pix+=item.p"]),
        "till_before_water": "h.name==\"watbit\" and t==t_soil" not in code and "h.name==\"tillbit\" and t==t_soil" in code,
        "selective_rewards": contains_all(code, ["name=\"chopbit\",src=t_bush,dst=t_soil,c=10,p=1", "name=\"watbit\",src=t_dry,dst=t_wet,c=12,p=0", "name=\"sproutbit\",src=t_wet,dst=t_flower,c=11,p=0", "name=\"smashbit\",src=t_rock,dst=t_soil,c=6,p=1", "name=\"tillbit\",src=t_grass,dst=t_dry,c=9,p=0"]),
        "solid_blockers": "t!=t_bush and t!=t_rock" in code,
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
