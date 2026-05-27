# Picopia Tools and Ability Use

## Ability Scope

Picopia intentionally keeps a small playable ability set. Not every possible rebuilding idea should become an ability, because PICO-8 readability and controller simplicity matter more than breadth.

Abilities should be framed as help from local creatures. A creature can introduce a quest, ask for food or restored habitat, and then unlock the related ability when the quest is complete.

## Playable Abilities and Tools

| Tool | Role | Current use | Upgrade direction |
| --- | --- | --- | --- |
| Chopbit | Clearing and gathering | Clears bush tiles into soil and grants pixels. | Cut from range or produce wood materials. |
| Watbit | Watering and hydration | Hydrates prepared dry soil into wet soil. | Water several tiles at once. |
| Sproutbit | Growth and habitat creation | Opens a grow menu on wet soil and grows grass, bushes, or flowers. | Grow habitat patches or visitor-attracting plant groups. |
| Smashbit | Stone and hard-material gathering | Breaks rock into soil and grants extra pixels. | Add stronger rocks or stone-specific materials. |
| Tillbit | Soil preparation | Tills grass or raw soil into prepared dry soil before watering. | Create farm plots or seed beds. |
| Build | Construction | Opens a build menu and places structures using pixels. | More buildings, decorations, and habitat pieces. |

## Helper Transformations

The current chain should be:

- Chopbit acts on bush and changes it into soil.
- Watbit acts on prepared dry soil and changes it into wet soil.
- Sproutbit acts on wet soil by opening a grow menu; it can grow grass, bush, or flower.
- Smashbit acts on rock and changes it into soil.
- Tillbit acts on grass or raw soil and changes it into dry soil.

Invalid helper use leaves the tile unchanged and gives harmless feedback.

## Resources from Tool Use

Only meaningful harvesting, bloom actions, and challenges grant rewards:

- Chopbit cutting bush: +1 px.
- Smashbit breaking rock: +1 px.
- Sproutbit growing flower: +1 px in the current prototype.
- Challenge completion: money reward for shop purchases.
- Sproutbit growing grass or bush: no pixels.
- Watbit hydration: no pixels.
- Tillbit soil preparation: no pixels.

Pixels are the current prototype currency and can later map to money.

## Backlog Policy

- New abilities beyond this set should only be added when they create new meaningful terrain, plant, creature, item, or crafting relationships.
- The next improvements should upgrade existing abilities before adding more abilities.
- Traversal-only or cosmetic abilities are out of scope for the current top-down 32x32 prototype.

## Future Tool Upgrades

- Watbit upgrade: water a small plus-shape or line instead of one tile.
- Sproutbit upgrade: make 2x2 or 4-tile flower/grass patches attract visitors.
- Chopbit upgrade: cut from range or produce wood-specific materials.
- Smashbit upgrade: break stronger rock variants for more pixels.
- Tillbit upgrade: create farm plots or seed beds.
