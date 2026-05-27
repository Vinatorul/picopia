# Picopia Design Spec

Picopia design documentation is split into focused files.

## Sections

- [World and visual design](picopia-world.md): core concept, design pillars, restoration chain, world layout, tile ids, visual style, and effects.
- [Tools and ability use](picopia-tools.md): helper tools, transformations, tool rewards, ability scope, and tool upgrade policy.
- [Menus, controls, and UI](picopia-menus-ui.md): controls, grow menu, build menu, quest windows, shop menu, and craft menu.
- [Quests and challenges](picopia-quests.md): current quest flow, expanded progression, challenge cards, badges, and creature center goal.
- [NPCs, creatures, and homes](picopia-creatures-npcs.md): creature interactions, ability unlocks, feeding, homes, comfort, and originality rules.
- [Shop, economy, and environment level](picopia-shop-economy.md): resources, currency, shop stock, environment-level gating, rewards, and player-home economy.
- [Items, inventory, crafting, farming, and energy](picopia-items-crafting.md): inventory counters, recipes, farming, moisture, hunger, campfire, and player-home flows.
- [Technical architecture](picopia-technical.md): cartridge architecture, systems, data flow, and asset pipeline.

## Implementation Target

The game implementation target remains `picopia.p8`.

## Canonical Notes

- Keep section files as the source of detailed design decisions.
- Use this document as the index and entry point.
- When a design area grows too large, split it into a new focused file and link it here.
