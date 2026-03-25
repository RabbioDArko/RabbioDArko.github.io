# Design System Strategy: The Tactile Digital Journal

## 1. Overview & Creative North Star
The Creative North Star for this system is **"The Mindful Analog."** It is a digital translation of a high-end, Smyth-sewn dotted notebook. This system rejects the cold, sterile rigidity of standard SaaS "dashboards" in favor of an editorial, human-centric workspace that feels curated and lived-in.

To move beyond a generic "friendly" look, we leverage **intentional asymmetry** and **tonal depth**. Layouts should not feel like a rigid grid of boxes; they should feel like elements resting naturally on a page. We break the "template" look by using exaggerated white space (derived from our Spacing Scale) and overlapping floating elements that break the container boundaries.

## 2. Colors & Surface Philosophy
The palette is rooted in a "Paper & Ink" philosophy. The background is not a flat white, but a warm, textured `#f9f9f8` (Surface) that mimics premium stationery.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders to define sections or cards. Hierarchy must be achieved through background shifts. 
- Use `surface-container-low` for secondary content areas.
- Use `surface-container-lowest` (#ffffff) for primary interactive cards to create a "lifted" effect against the `surface` background.

### Surface Hierarchy & Nesting
Treat the UI as physical layers. 
- **Base Layer:** `surface` (The notebook page with dotted texture).
- **Secondary Layer:** `surface-container` (Nested areas for grouping).
- **Interactive Layer:** `surface-container-lowest` (The "active" card or focused area).

### Glass & Gradient Soul
To prevent the UI from feeling flat, use the **Signature Glow**:
- **CTAs:** Use a subtle linear gradient from `primary` (#4958ac) to `primary-container` (#96a5ff) at a 135-degree angle. This adds a "lithographic" depth to buttons.
- **Glassmorphism:** For floating modals or navigation bars, use `surface` at 80% opacity with a `20px` backdrop-blur. This allows the notebook dots to peak through, grounding the element in the environment.

## 3. Typography: Editorial Sans
We pair **Plus Jakarta Sans** (Display/Headlines) with **Be Vietnam Pro** (Body/Labels) to create a sophisticated yet approachable hierarchy.

- **Display & Headlines:** Use `display-md` or `headline-lg` with tight letter-spacing (-0.02em). These should feel like bold, ink-stamped titles.
- **Body Text:** `body-lg` provides a generous x-height for readability. Always use `on-surface-variant` (#5b605f) for long-form body text to reduce visual fatigue; reserve `on-surface` (#2f3333) for high-priority titles.
- **Micro-Copy:** `label-md` should be used in uppercase with 0.05em letter-spacing for a "tabbed folder" aesthetic.

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are often too "digital." We use **Ambient Softness** to create a premium feel.

- **The Layering Principle:** Instead of a shadow, place a `surface-container-lowest` card on a `surface-container-low` section. The 2% shift in brightness is enough for the human eye to perceive depth.
- **Ambient Shadows:** For high-floating elements (e.g., FABs or Popovers), use an extra-diffused shadow: `box-shadow: 0 20px 40px rgba(15, 33, 118, 0.06)`. Note the tint—we use a fraction of the `on-primary-container` color rather than black.
- **The "Ghost Border" Fallback:** If accessibility requires a stroke, use `outline-variant` at 15% opacity. It should be felt, not seen.

## 5. Components & Interface Patterns

### Buttons (The "Pill" Variant)
All buttons use `round-full` (9999px).
- **Primary:** Gradient fill (`primary` to `primary-container`). White text (`on-primary`). 
- **Secondary:** `secondary-container` fill with `on-secondary-container` text. No border.
- **Interaction:** On hover, the element should scale slightly (1.02x) rather than just changing color, mimicking the tactile "spring" of a physical button.

### Input Fields
- **Styling:** Use `surface-container-high` as the background fill.
- **State:** When focused, transition the background to `surface-container-lowest` and add a 2px "Ghost Border" of `primary`.
- **Shape:** `round-md` (1.5rem) for a friendly, chunky feel that accommodates the "Outfit/Quicksand" font style.

### Cards & Lists
- **Rule:** Absolute prohibition of divider lines. 
- **Separation:** Use `spacing-6` (2rem) as a vertical gutter between list items. For complex lists, use alternating background tints (`surface` vs `surface-container-low`) for row separation.
- **The "Dotted Layout":** The `surface` background should feature a 24px grid of `outline-variant` dots (1px size at 20% opacity). Cards should align their padding to this underlying grid.

### Chips
- **Action Chips:** Use `tertiary-container` with `on-tertiary-container` text. The extra-round shape makes them feel like smooth river stones.

## 6. Do's and Don'ts

### Do:
- **Use "Air":** If you think there's enough white space, add `spacing-4` more. The "Airy" aesthetic is the engine of this design system.
- **Align to the Dots:** While elements can overlap, their starting anchors should snap to the dotted grid.
- **Layer Surfaces:** Use `surface-container` tiers to group related items instead of drawing a box around them.

### Don't:
- **Don't use 100% Black:** Never use `#000000`. Use `on-surface` for text and `on-background` for secondary elements.
- **Don't use Sharp Corners:** Even "small" components must have at least `round-sm` (0.5rem). Straight 90-degree angles break the "Friendly" promise.
- **Don't use Dividers:** If you need to separate content, use a background color shift or increased spacing. A line is a wall; a color shift is a transition.