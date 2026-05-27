# Picopia World and Visual Design

## Summary

Picopia is a standalone PICO-8 cartridge about restoring a dried-out fantasy-console garden world. The implementation target is `picopia.p8`.

The game takes place in a neglected fantasy-console clearing after humans have vanished or disappeared from daily life. Picoblob arrives in a dry world where the ground, grass, tall grass, bushes, flowers, trees, and farmable soil have withered. Green terrain should mostly appear as a result of restoration, so the starting map reads as broadly dry and neglected rather than already healthy. Local creatures become the main guides: they ask Picoblob to restore parts of the land, feed them, craft useful objects, build grass homes, and eventually construct a player home.

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
dry plant/bush -> soil -> dry soil -> wet soil -> revived grass/bush/flower/tree
dry tree -> watered tree -> revived tree -> fruit/branch/seed source
rock -> soil -> dry soil -> wet soil -> grass/bush/flower/tree
dry grass/tall grass -> dry soil -> wet soil -> revived grass/bush/flower
revived grass -> planted flower/bush/tree seed -> grown flower/bush/tree
farm soil -> tilled plot -> watered plot -> planted vegetable -> grown vegetable
```

This makes the soil left behind by clearing dry plants a useful normal stage instead of a dead-end sand tile.

## World Layout

The world is a 32x32 logical tile map using 8x8 tiles. It is stored in PICO-8 `__map__`, not a Lua table, so the map can be inspected and edited in the PICO-8 editor.

The reusable asset generator is `scripts/picopia_apply_assets.py`. It generates:

- `__gfx__` sprite sheet.
- `__map__` 32x32 gameplay map padded to PICO-8's 64 map rows.
- `__sfx__` sound effects.

The normal regeneration path is `scripts/picopia_apply_assets.py`. One-time migration scripts are not part of the long-term asset pipeline.

## World Objects and Locations

The map should contain discoverable world locations, not only menu-only systems:

- A shop building or shopkeeper location that the player can find while exploring.
- Early creature homes or nests placed by the player through building or crafting.
- A later player-home construction site that becomes usable after the shop blueprint and builder-creature requirements are met.
- Distinct creature meeting spots so different NPCs feel physically present in the world.
- Dry trees, rocks, dry grass, dry soil, bushes, and farm plots distributed across the larger map to encourage movement and camera-follow exploration.

## Tile Types and Sprite IDs

Tile and sprite ids must match so PICO-8 editor view and runtime view are consistent. Core terrain should be organized as paired restored and dried versions:

| Sprite id | Tile | Passability | Restoration role |
| --- | --- | --- | --- |
| `0` | Empty | Passable or unused by context | Reserved zero tile; not normal terrain. |
| `1` | Grass | Passable | Restored base ground. Supports planting flowers, bushes, and trees when expanded planting is enabled. |
| `2` | Dry grass | Passable | Starting-world dried version of grass; can be watered or restored through the restoration chain. |
| `3` | Tall grass | Passable or slow/blocking by tuning | Restored gatherable grass source and habitat material. |
| `4` | Dry tall grass | Passable or slow/blocking by tuning | Starting-world dried version of tall grass; can become tall grass or be cleared into usable material. |
| `5` | Impassable bush | Blocking | Restored bush blocker, habitat object, and possible resource source. |
| `6` | Dry impassable bush | Blocking | Starting-world dried bush; can be cleared, watered, or restored depending on tool progression. |
| `7` | Tree | Blocking | Restored tree, food/branch/seed source, and visual restoration landmark. |
| `8` | Dry tree | Blocking | Starting-world dried tree; can be watered into a restored tree. |
| `9` | Fertile soil | Passable | Restored farmable earth for planting and crop support. |
| `10` | Dry fertile soil | Passable | Starting-world dried earth; can be watered into fertile soil. |
| `11` | Flowers | Passable | Restored flower patch for beauty, quests, creatures, and environment progress. |
| `12` | Dry flowers | Passable | Starting-world dried flower patch; can be restored into flowers. |


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

