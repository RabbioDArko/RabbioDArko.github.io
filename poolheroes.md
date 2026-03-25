Role: Game Designer (System Deisgn, Economy Design ,UX Design)
Studio Yesgnome (co-dev wiht MPL)
Year 2021

One of my first f2p game where I had a chance to work form pre production to post production. 

# Piece 1 — Tuning Feel: Reverse-Engineering Pool Physics in UnityRole: Game Designer (System Deisgn, Economy Design ,UX Design)
Studio Yesgnome (co-dev wiht MPL)
Year 2021

# Piece 1 — Tuning Feel: Reverse-Engineering Pool Physics in Unity

---

## The Problem

We were building a competitive pool game in a genre dominated by Miniclip's 8 Ball Pool. Players of that game had deeply internalized how a "correct" shot *feels* — cue force, ball roll speed, cushion bounce, friction decay. If our physics felt even slightly off, playtesters rejected it instantly, often without being able to articulate why.

The challenge wasn't to copy the physics 1:1 — it was to **decode what made the reference feel right**, then rebuild it in Unity's physics system with enough room to develop our own identity later.

---

## The Approach

### 1. Benchmarking by Feel & Frame

I played hundreds of shots in the reference game and recorded them, then broke the recordings into observable properties: time-to-stop, rebound angle loss on cushions, spin decay rate, and cue-power-to-distance curves. This gave me a rough target spec — not code, but *behaviour envelopes* I could tune toward.

### 2. Translating to Unity

Unity's built-in 2D physics (Box2D under the hood) doesn't model pool physics out of the box. I had to map the observed behaviours onto configurable parameters:

- **Linear drag & angular drag** — controlled how quickly balls decelerated and how spin died.
- **Physics materials (bounciness + friction)** — tuned per-surface: felt, cushion, ball-to-ball.
- **Cue force curves** — a custom AnimationCurve mapping input hold-time to applied impulse, giving a satisfying non-linear "wind-up" feel.

### 3. Iteration with Playtesting
I ran rapid iteration loops: tweak values → record 10 standard shots → playtest → compare to reference recordings. I kept a tuning log tracking each parameter change and the qualitative feedback it produced.

> *[📷 — Insert: side-by-side screenshot of Unity inspector showing physics material settings + a gameplay shot mid-play]*

---

## The Outcome

The final physics set passed blind playtests ,players familiar with the genre said the game "felt right" without being told we'd benchmarked against a specific title. More importantly, the tuning was cleanly parameterized, so when the design team later wanted to introduce power-ups that altered physics (e.g., a "heavy ball" modifier), we could adjust individual curves without destabilizing the base feel.

---
---

# Piece 2 — Designing the Meta: Loot Boxes, Progression & Monte Carlo Validation

---

## The Problem

The game needed a full meta layer loot boxes, player progression, and achievements that would sit on top of the core pool gameplay. This was my first time building economy simulations, I had to learn the craft while delivering production-ready outputs.

---

## The Approach

### 1. Structuring the Meta Loop

I designed three interlocking systems:

- **Loot Boxes** - I defined item pools, rarity tiers, and drop-rate tables, working closely with the Producer who owned the presentation layer (animations, reveals, etc.).
- **Progression** - an XP-based leveling curve with milestone unlocks that gave players a reason to keep playing beyond individual matches.
- **Achievements** - Designed to nudge players toward behaviours that deepened engagement (e.g., "Win 5 games using bank shots").

### 2. Simulating the Economy in Excel

I needed to answer questions like: *"How many boxes does a median player open before they complete a collection?"* and *"At what level does the soft currency faucet outpace the sinks?"*

This was my first time building economy simulations, so I started from fundamentals. I taught myself Monte Carlo methods by building small simulations for dice rolls and card draws, then scaled up to our actual loot tables. The final simulation modeled:

- **10,000 synthetic player sessions** with varied play-frequency profiles.
- **Expected time-to-collection** curves for each rarity tier.
- **Currency inflow vs. outflow** over a 90-day projection window.

This let me and the Producer spot problem areas (e.g., a rarity tier that 5% of players would *never* complete without purchasing) before writing a single line of game code.

> *[📷 — Insert: screenshot of Monte Carlo simulation spreadsheet showing distribution curves]*

### 3. Collaborative Balancing

The Producer and I worked as a pair: I owned the numbers and simulation outputs, they owned player sentiment and presentation. When the sim showed a drop-rate needed adjusting, we'd discuss whether the fix was mathematical (change the rate) or perceptual (change the animation pacing to make rare drops feel more dramatic).

---

## The Outcome

The economy shipped with a validated foundation — every drop rate, currency faucet, and progression milestone had been stress-tested against thousands of simulated sessions before it ever touched a player. The Monte Carlo approach became a reusable tool; I used the same simulation framework for value predictions across the project's remaining systems.

---
---

# Piece 3 — Mapping the Machine: UX Wireframes as a Production Tool

---

## The Problem

Screens were getting built, then rebuilt when someone realized the flow didn't account for an edge case. Features got scoped based on a written spec that different people read differently. We were spending too much time reworking and not enough time building.

---

## The Approach

### Full Core-Loop Wireframe Mapping

Before any feature went into development, I created comprehensive UX wireframe flows that mapped the **entire core game** — from first launch to endgame loops. These weren't just pretty screens; they were functional maps that showed:

- **Every screen state** - default, loading, empty, error, and success.
- **Every transition** - what triggers it, where it goes, what data it carries.
- **Edge cases** - what happens on network failure? What if the player's inventory is full? What if a timed event expires mid-flow?

### Using Wireframes as a Shared Language

The wireframes became the single source of truth for cross-functional conversations. When an engineer asked "what happens if...?", the answer was on the flow. When the Producer wanted to add a new monetization touchpoint, we could see exactly where it fit (or didn't) in the existing map. It eliminated the "I thought you meant..." class of problems almost entirely.

> *[📷 — Insert: section of a wireframe flow showing a core gameplay loop with annotated transitions]*

---

## The Outcome

The wireframe-first process smoothed out production across all my projects at the studio. Features went from spec to implementation with significantly fewer rounds of revision, and new team members could onboard by reading the flow instead of sitting through hours of verbal walkthroughs. It was a simple practice, but it compounded — every hour spent mapping saved multiples in rework downstream.

---
---

> **Your next steps:**
> 1. Drop in screenshots where marked with 📷
> 2. Embed the Monte Carlo spreadsheet (screenshot or link) in Piece 2
> 3. If the game is named publicly, replace "Pool Hero" with the real title throughout
> 4. Optional: add a brief "My Role" header at the top of each piece (one line — e.g., *"Technical Designer — responsible for gameplay physics, meta systems, and economy design"*)

## ### #Establishing a Data-Driven Culture## ## ### Establishing a Data-Driven Culture## ## ### Establishing a Data-Driven Culture## ## ### 

---

## The Problem

We were building a competitive pool game in a genre dominated by Miniclip's 8 Ball Pool. Players of that game had deeply internalized how a "correct" shot *feels* — cue force, ball roll speed, cushion bounce, friction decay. If our physics felt even slightly off, playtesters rejected it instantly, often without being able to articulate why.

The challenge wasn't to copy the physics 1:1 — it was to **decode what made the reference feel right**, then rebuild it in Unity's physics system with enough room to develop our own identity later.

---

## The Approach

### 1. Benchmarking by Feel & Frame

I played hundreds of shots in the reference game and recorded them, then broke the recordings into observable properties: time-to-stop, rebound angle loss on cushions, spin decay rate, and cue-power-to-distance curves. This gave me a rough target spec — not code, but *behaviour envelopes* I could tune toward.

### 2. Translating to Unity

Unity's built-in 2D physics (Box2D under the hood) doesn't model pool physics out of the box. I had to map the observed behaviours onto configurable parameters:

- **Linear drag & angular drag** — controlled how quickly balls decelerated and how spin died.
- **Physics materials (bounciness + friction)** — tuned per-surface: felt, cushion, ball-to-ball.
- **Cue force curves** — a custom AnimationCurve mapping input hold-time to applied impulse, giving a satisfying non-linear "wind-up" feel.

### 3. Iteration with Playtesting
I ran rapid iteration loops: tweak values → record 10 standard shots → playtest → compare to reference recordings. I kept a tuning log tracking each parameter change and the qualitative feedback it produced.

> *[📷 — Insert: side-by-side screenshot of Unity inspector showing physics material settings + a gameplay shot mid-play]*

---

## The Outcome

The final physics set passed blind playtests ,players familiar with the genre said the game "felt right" without being told we'd benchmarked against a specific title. More importantly, the tuning was cleanly parameterized, so when the design team later wanted to introduce power-ups that altered physics (e.g., a "heavy ball" modifier), we could adjust individual curves without destabilizing the base feel.

---
---

# Piece 2 — Designing the Meta: Loot Boxes, Progression & Monte Carlo Validation

---

## The Problem

The game needed a full meta layer loot boxes, player progression, and achievements that would sit on top of the core pool gameplay. This was my first time building economy simulations, I had to learn the craft while delivering production-ready outputs.

---

## The Approach

### 1. Structuring the Meta Loop

I designed three interlocking systems:

- **Loot Boxes** - I defined item pools, rarity tiers, and drop-rate tables, working closely with the Producer who owned the presentation layer (animations, reveals, etc.).
- **Progression** - an XP-based leveling curve with milestone unlocks that gave players a reason to keep playing beyond individual matches.
- **Achievements** - Designed to nudge players toward behaviours that deepened engagement (e.g., "Win 5 games using bank shots").

### 2. Simulating the Economy in Excel

I needed to answer questions like: *"How many boxes does a median player open before they complete a collection?"* and *"At what level does the soft currency faucet outpace the sinks?"*

This was my first time building economy simulations, so I started from fundamentals. I taught myself Monte Carlo methods by building small simulations for dice rolls and card draws, then scaled up to our actual loot tables. The final simulation modeled:

- **10,000 synthetic player sessions** with varied play-frequency profiles.
- **Expected time-to-collection** curves for each rarity tier.
- **Currency inflow vs. outflow** over a 90-day projection window.

This let me and the Producer spot problem areas (e.g., a rarity tier that 5% of players would *never* complete without purchasing) before writing a single line of game code.

> *[📷 — Insert: screenshot of Monte Carlo simulation spreadsheet showing distribution curves]*

### 3. Collaborative Balancing

The Producer and I worked as a pair: I owned the numbers and simulation outputs, they owned player sentiment and presentation. When the sim showed a drop-rate needed adjusting, we'd discuss whether the fix was mathematical (change the rate) or perceptual (change the animation pacing to make rare drops feel more dramatic).

---

## The Outcome

The economy shipped with a validated foundation — every drop rate, currency faucet, and progression milestone had been stress-tested against thousands of simulated sessions before it ever touched a player. The Monte Carlo approach became a reusable tool; I used the same simulation framework for value predictions across the project's remaining systems.

---
---

# Piece 3 — Mapping the Machine: UX Wireframes as a Production Tool

---

## The Problem

Screens were getting built, then rebuilt when someone realized the flow didn't account for an edge case. Features got scoped based on a written spec that different people read differently. We were spending too much time reworking and not enough time building.

---

## The Approach

### Full Core-Loop Wireframe Mapping

Before any feature went into development, I created comprehensive UX wireframe flows that mapped the **entire core game** — from first launch to endgame loops. These weren't just pretty screens; they were functional maps that showed:

- **Every screen state** - default, loading, empty, error, and success.
- **Every transition** - what triggers it, where it goes, what data it carries.
- **Edge cases** - what happens on network failure? What if the player's inventory is full? What if a timed event expires mid-flow?

### Using Wireframes as a Shared Language

The wireframes became the single source of truth for cross-functional conversations. When an engineer asked "what happens if...?", the answer was on the flow. When the Producer wanted to add a new monetization touchpoint, we could see exactly where it fit (or didn't) in the existing map. It eliminated the "I thought you meant..." class of problems almost entirely.

> *[📷 — Insert: section of a wireframe flow showing a core gameplay loop with annotated transitions]*

---

## The Outcome

The wireframe-first process smoothed out production across all my projects at the studio. Features went from spec to implementation with significantly fewer rounds of revision, and new team members could onboard by reading the flow instead of sitting through hours of verbal walkthroughs. It was a simple practice, but it compounded — every hour spent mapping saved multiples in rework downstream.

---
---

> **Your next steps:**
> 1. Drop in screenshots where marked with 📷
> 2. Embed the Monte Carlo spreadsheet (screenshot or link) in Piece 2
> 3. If the game is named publicly, replace "Pool Hero" with the real title throughout
> 4. Optional: add a brief "My Role" header at the top of each piece (one line — e.g., *"Technical Designer — responsible for gameplay physics, meta systems, and economy design"*)

