# Picopia

A tiny cozy PICO-8 demake prototype about restoring a broken fantasy-console garden.

## Files

- `picopia.p8` — main Picopia cartridge.
- `plans/picopia-design.md` — approved design spec.
- `scripts/pico8_verify_cart.py` — reusable structure verifier for PICO-8 carts.
- `scripts/picopia_apply_assets.py` — reusable Picopia graphics and sound generator.

## Verify

```sh
python3 scripts/pico8_verify_cart.py picopia.p8
```

## Regenerate Picopia graphics and sounds

```sh
python3 scripts/picopia_apply_assets.py picopia.p8
```
