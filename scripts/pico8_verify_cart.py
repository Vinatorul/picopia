import argparse
from pathlib import Path


def read_cart(path):
    text = Path(path).read_text()
    code, sep, gfx = text.partition("__gfx__\n")
    return text, code, gfx if sep else ""


def get_rows(code):
    rows = []
    in_rows = False
    for line in code.splitlines():
        s = line.strip()
        if s == "rows={":
            in_rows = True
            continue
        if in_rows and s == "}":
            break
        if in_rows and s.startswith('"'):
            rows.append(s.split('"')[1])
    return rows


def check(path):
    text, code, gfx = read_cart(path)
    rows = get_rows(code)
    gfx_rows = gfx.splitlines() if gfx else []
    checks = {
        "file_exists": Path(path).exists(),
        "ends_with_newline": text.endswith("\n"),
        "has_header": "pico-8 cartridge" in text and "version 43" in text,
        "has_lua_section": "__lua__" in text,
        "has_core_functions": all(s in code for s in ["function _init()", "function _update()", "function _draw()"]),
        "rows_table_16x16": len(rows) == 16 and all(len(r) == 16 for r in rows),
        "gfx_section_128x128": len(gfx_rows) == 128 and all(len(r) == 128 for r in gfx_rows),
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
