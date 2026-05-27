# Picopia World and Visual Design

## Summary

Picopia is a standalone PICO-8 cartridge about restoring a dried-out fantasy-console garden world. The implementation target is `picopia.p8`.

The game takes place in a neglected fantasy-console clearing after humans have vanished or disappeared from daily life. Picoblob arrives in a dry world where soil, plants, tall grass, flowers, and trees have withered. Local creatures become the main guides: they ask Picoblob to restore parts of the land, feed them, craft useful objects, and build grass homes.

## Design Pillars

Picopia should feel like a small fantasy-console restoration toy:

- Abilities are earned by helping local creatures, not handed out as abstract upgrades.
- Each ability has a clear terrain, plant, creature, or crafting purpose.
- Terrain changes form chains rather than isolated one-off actions.
- Restored land creates resources, food, and future habitat opportunities.
- Building and crafting give the restored land a visible purpose.
- Creature homes make restoration feel socially alive because creatures can move into them.
- Farming should support simple vegetables and flowers after soil is tilled.
- The game continues after goals are complete.

## Current Direction

The approved version is a small but expandable restoration sandbox with creature-led progression:

- One 32x32 world stored in PICO-8 `__map__`.
- A camera follows Picoblob around the larger map.
- Terrain tiles in the map use the same sprite ids that the editor shows.
- Tile `0` is reserved as empty; terrain starts at sprite id `1` so the editor does not show grass as black empty tiles.
- Ability/tool use happens on the tile Picoblob is facing.
- Quest windows communicate creature requests and goals outside the bottom HUD.
- Building uses a separate build tool and build menu.
- Inventory and crafting should start small: a few item counters and a compact craft menu.
- Creature homes should be grass-based early structures that attract or house local creatures.

## Restoration Chain

Picoblob can start with a minimal action set, while additional helper abilities are unlocked by completing creature quests.

The key restoration chain is:

```text
dry plant/bush -> soil -> dry soil -> wet soil -> revived grass/bush/flower
rock -> soil -> dry soil -> wet soil -> grass/bush/flower
grass/tall grass -> dry soil -> wet soil -> revived grass/bush/flower
```

This makes the soil left behind by clearing dry plants a useful normal stage instead of a dead-end sand tile.

## World Layout

The world is a 32x32 logical tile map using 8x8 tiles. It is stored in PICO-8 `__map__`, not a Lua table, so the map can be inspected and edited in the PICO-8 editor.

The reusable asset generator is `scripts/picopia_apply_assets.py`. It generates:

- `__gfx__` sprite sheet.
- `__map__` 32x32 gameplay map padded to PICO-8's 64 map rows.
- `__sfx__` sound effects.

The normal regeneration path is `scripts/picopia_apply_assets.py`. One-time migration scripts are not part of the long-term asset pipeline.

## Tile Types and Sprite IDs

Tile and sprite ids must match so PICO-8 editor view and runtime view are consistent:

- `0`: empty/reserved, not used for normal terrain.
- `1`: grass.
- `2`: bush blocker.
- `3`: dry soil.
- `4`: wet soil.
- `5`: flower.
- `6`: soil left by clearing bush.
- `7-8`: Picoblob animation sprites.
- `9`: Professor Sproutroot.
- `10-12`: helper/tool icons.
- `13`: tiny home/build icon.
- `14`: rock tile and Smashbit icon.
- `15`: Tillbit icon.
- `16`: bush grown by Sproutbit.

## Visual Style

Picopia should look like a PICO-8-native demake rather than a direct imitation of any specific external game.

Guidelines:

- Chunky 8x8 tiles.
- Bright limited palette.
- Readable silhouettes over detail.
- Picoblob as a small pink or purple blob with a simple wobble.
- Helpers represented through HUD/tool icons and action effects.
- Garden restoration shown through brighter greens, flowers, and sparkles.
- Creature names and designs must be original fantasy-console creatures, not direct external character references.

## Feedback and Effects

Each tool should feel distinct:

- Chopbit: slash particles and cut SFX.
- Watbit: blue droplet particles and water SFX.
- Sproutbit: green sparkle or growth pop and growth SFX.
- Invalid action: small nope bounce and error SFX.
- Quest complete/build complete: celebratory SFX and sparkles.

## Out of Scope for Current Prototype

- Full social simulation systems.
- Real-time clock or day-night cycle.
- Multiple biomes.
- Dialogue trees.
- Persistent save data.
- Full expanded tool set.
- Direct use of external character names, sprites, or copyrighted designs.
