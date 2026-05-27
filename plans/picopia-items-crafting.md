# Picopia Items, Inventory, Crafting, Farming, and Energy

## Inventory

Inventory should stay readable in PICO-8 and use a small list of item counters rather than a large bag UI.

Early item examples:

- Grass clippings from cutting or restoring tall grass.
- Seeds bought from the shop before planting flowers.
- Wood, branches, or twigs from dry bushes and trees.
- Food berries, fruit, vegetables, or snacks from trees and plants for feeding creatures and restoring energy.
- Vegetable seeds and flower seeds bought from the shop.
- Badges earned from special quests.
- Stone from rocks.
- Blueprints bought from the shop, including the player-home blueprint.

## Crafting

Crafting should start with a compact craft menu and a few recipes:

- Grass home: uses grass clippings; attracts or houses a creature.
- Chair: uses wood or grass; decorative and useful for making the area feel lived-in.
- Creature furniture: uses grass, wood, branches, or other simple items; improves creature comfort and living conditions.
- Campfire: uses wood and stone; must be lit by a suitable creature after crafting.
- Player home: requires a bought blueprint and a builder creature before construction.

Crafting should connect to restoration instead of becoming a separate economy. Most craft ingredients should come from reviving, clearing, or tending the world.

## Farming and Moisture

Farming connects tilling, water, food, and shop progression.

- A rototiller-style creature helper can improve Tillbit or act as the fiction for tilling prepared plots.
- Tilled farm plots can accept vegetable seeds and flower seeds.
- The vegetable loop should be: tilled plot -> watered plot -> planted vegetable -> grown vegetable -> harvested vegetable.
- Watered plots can dry out later if the expanded moisture system needs light upkeep.
- Vegetables can become food, quest items, or shop/crafting resources.
- Flowers should require seeds in the expanded version instead of being free growth.
- Flower seeds, bush seeds, and tree seeds can be planted on revived grass if the planting-on-grass rule is enabled.
- Tree planting should create a young or planted tree state before becoming a revived tree.
- A moisture-aware creature can report town humidity as a friendly hint system for dry areas, trees, and farming needs.

## Hunger and Energy

Energy is a lightweight pacing system:

- Each meaningful action spends energy.
- Eating restores energy.
- Food is gathered from trees or plants.
- Hunger should encourage tending the restored world, not punish experimentation too harshly.

Food sources can include:

- Berries.
- Fruit.
- Vegetables.
- Snacks from restored plants.
- Quest or challenge reward food.

## Campfire Flow

The campfire links crafting and creature interaction:

1. Gather wood and stone.
2. Craft a campfire from the craft menu.
3. Place the campfire.
4. Ask or recruit a fire-capable creature to light it.

## Player Home Flow

The player home links shop, blueprint, crafting/building, and creature help:

1. Raise the environment level.
2. Buy the player-home blueprint from the shop.
3. Meet or recruit a builder creature.
4. Construct the player home with the builder creature's help.
