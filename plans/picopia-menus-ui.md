# Picopia Menus, Controls, and UI

## Controls

- D-pad: move Picoblob on the tile grid.
- Last movement direction becomes Picoblob's facing direction.
- 🅾️: cycle active tool in grow-loop order: Chopbit → Tillbit → Watbit → Sproutbit → Smashbit → Build.
- ❎: use the active tool.
- If the active tool is Build, ❎ opens the build menu.
- If the active tool is Sproutbit, ❎ opens the grow menu.
- In build/grow menus, ❎ confirms the selected item and 🅾️ closes the menu.
- 🅾️+❎ in normal play opens the current quest window.
- The start screen shows a drawn Picopia logo and explains all controls.
- Quest/help windows close with 🅾️ or ❎.

## Menu Principles

Menus should stay compact and readable on a PICO-8 screen:

- Prefer short item names and one-line costs.
- Avoid deep nested menus.
- Keep active selection obvious through cursor, color, or highlight.
- Use the same confirm and cancel rules across build, grow, craft, shop, quest, and help windows.
- Do not hide key quest information in the bottom HUD.

## Grow Menu

The grow menu opens when Sproutbit is used on wet soil.

Initial grow options:

- Grass: costs 0 px.
- Bush: costs 0 px.
- Flower: costs 0 px in the current prototype and should eventually require seeds bought from the shop.

Expected behavior:

- ❎ confirms the selected growth option.
- 🅾️ closes the menu.
- The selected option changes the target wet soil tile.
- Invalid opening attempts produce harmless feedback and do not change the tile.

## Build Menu

The build menu opens when the Build tool is selected and ❎ is pressed.

Initial build option:

- Tiny home: costs 30 px in the current prototype.

Expanded build direction:

- Grass homes or nests should be early structures that attract or house local creatures.
- Player home requires a shop-bought blueprint before construction.
- Player home construction requires help from a builder creature.
- Built creature furniture can improve comfort and living conditions.

## Quest and Help Windows

Quest progress is communicated through pop-up quest windows rather than the bottom HUD.

Rules:

- A quest window should show the current clear request.
- A completion message should be short and direct.
- Quest/help windows close with 🅾️ or ❎.
- 🅾️+❎ opens the current quest window from normal play.
- Quest windows should not require long dialogue trees in the current prototype.

## Shop Menu

The shop menu should sell items, seeds, recipes, and blueprints.

Expected stock categories:

- Food or recovery items.
- Vegetable seeds.
- Flower seeds.
- Recipes.
- Player-home blueprint.
- Future creature-home or furniture-related items.

Shop stock should depend on the environment level so that restoration progress visibly expands what the player can buy.

## Craft Menu

Crafting should start with a compact craft menu and a few recipes.

The craft menu should show:

- Recipe name.
- Required item counters.
- Whether requirements are met.
- Placement or post-craft requirement when relevant.

Examples:

- Grass home: uses grass clippings; attracts or houses a creature.
- Chair: uses wood or grass.
- Creature furniture: uses grass, wood, branches, or other simple items.
- Campfire: uses wood and stone; must be lit by a suitable creature after crafting.
- Player home: requires a bought blueprint and a builder creature before construction.
