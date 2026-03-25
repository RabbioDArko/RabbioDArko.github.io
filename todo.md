### 2. Translating to Unity

Rather than treating physics as a single monolithic system, Our lead dev structured the tuning into **five distinct, modular components** each owning a specific behaviour domain:

- **CueStickSetting** — `cueForceMin / cueForceMax` and a custom `Power Curve` (AnimationCurve) mapping input hold-time to applied impulse, giving a non-linear "wind-up" feel.
- **BallPhysics** — `cueBallMass`, `ballMass`, `restitution`, and `Drag` tuned separately for the cue ball vs. object balls, since the cue ball behaves differently after contact.
- **SpinSys** — spin treated as a first-class mechanic with its own component, separate from linear physics drag. This is where top-spin, back-spin, and side-spin decay rates lived.
- **BallCush** — `railRestitution`, `railFriction`, and `railSpinTransfer` per cushion surface. `railSpinTransfer` specifically controls how spin transfers through a cushion bounce — one of the parameters most games get wrong.
- **Game Feel** — a dedicated block for tuning *feel* independent of simulation accuracy (camera shake thresholds, impact feedback timing, pocket magnet radius).

Separating `Game Feel` from physics was a deliberate design decision: it meant we could tune the simulation to be accurate *and* tune the experience to feel satisfying — without those two concerns fighting each other.

### 3. Iteration with Playtesting
I ran rapid iteration loops: tweak values → record 10 standard shots → playtest → compare to reference recordings. I kept a tuning log tracking each parameter change and the qualitative feedback it produced.

> *[📷 — Insert the Unity inspector screenshot showing the five component blocks (CueStickSetting, BallPhysics, SpinSys, BallCush, Game Feel) alongside the gameplay view]*
