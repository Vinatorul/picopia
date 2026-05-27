import argparse
import os
from pathlib import Path


CART_NAME = "picopia.p8"
ENV_PATH = ".env"
CART_DIR_ENV = "PICO8_CART_DIR"


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


def read_cart(path):
    text = Path(path).read_text()
    code, sep_gfx, rest = text.partition("__gfx__\n")
    gfx, sep_map, rest = rest.partition("__map__\n")
    map_data, sep_sfx, sfx = rest.partition("__sfx__\n")
    return text, code, sep_gfx, gfx, sep_map, map_data, sep_sfx, sfx


def check(path):
    p = Path(path)
    if not p.exists():
        return {"file_exists": False}

    text, code, sep_gfx, gfx, sep_map, map_data, sep_sfx, sfx = read_cart(path)
    gfx_rows = gfx.splitlines()
    map_rows = map_data.splitlines()
    sfx_rows = sfx.splitlines()

    return {
        "file_exists": True,
        "ends_with_newline": text.endswith("\n"),
        "cart_header": text.startswith("pico-8 cartridge"),
        "version_present": "version 43" in text,
        "lua_section": "__lua__" in code,
        "gfx_section": bool(sep_gfx),
        "map_section": bool(sep_map),
        "sfx_section": bool(sep_sfx),
        "code_not_empty": bool(code.strip()),
        "gfx_128x128": len(gfx_rows) == 128 and all(len(row) == 128 for row in gfx_rows),
        "map_64x256": len(map_rows) == 64 and all(len(row) == 256 for row in map_rows),
        "sfx_rows_valid": bool(sfx_rows) and all(len(row) == 168 for row in sfx_rows),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cart", nargs="?", default=CART_NAME)
    parser.add_argument("--output-dir")
    parser.add_argument("--env", default=ENV_PATH)
    args = parser.parse_args()
    load_env(args.env)
    output_dir = args.output_dir or os.environ.get(CART_DIR_ENV, ".")
    cart_path = resolve_cart_path(args.cart, output_dir)
    checks = check(cart_path)
    for name, ok in checks.items():
        print(f"{name}: {ok}")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
