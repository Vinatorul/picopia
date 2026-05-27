# Picopia

A tiny cozy PICO-8 demake prototype about restoring a broken fantasy-console garden.

## Files

- `picopia.p8` — main Picopia cartridge.
- `src/picopia.lua` — cartridge Lua source.
- `plans/picopia-design.md` — approved design spec.
- `scripts/assemble_cart.py` — assembles the cartridge from Lua, graphics, map, and sounds.
- `scripts/pico8_verify_cart.py` — reusable structure verifier for PICO-8 carts.
- `.env` — local assembly settings.

## Configure output directory

Set `PICO8_CART_DIR` in `.env` to the directory where the assembled cartridge should be written:

```env
PICO8_CART_DIR=/Users/vinatorul/Projects/pico-8/carts
```

You can also override it per run with `--output-dir`.

## Assemble cartridge

```sh
python3 scripts/assemble_cart.py
```

By default this reads `src/picopia.lua` and writes `picopia.p8` into `PICO8_CART_DIR` from `.env`.

Useful variants:

```sh
python3 scripts/assemble_cart.py custom-name.p8
python3 scripts/assemble_cart.py --output-dir /Users/vinatorul/Projects/pico-8/carts
python3 scripts/assemble_cart.py --lua src/picopia.lua
```

## Verify

```sh
python3 scripts/pico8_verify_cart.py
```

By default this checks `picopia.p8` in the same `PICO8_CART_DIR` from `.env`.

Useful variants:

```sh
python3 scripts/pico8_verify_cart.py custom-name.p8
python3 scripts/pico8_verify_cart.py --output-dir /Users/vinatorul/Projects/pico-8/carts
```
