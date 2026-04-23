---
# ═══════════════════════════════════════════════════
# Portefaix Design System — machine-readable tokens
# ═══════════════════════════════════════════════════

colors:
  # ── Backgrounds (dark mode — primary surface)
  bg:
    canvas:   "#0a0b0e"     # true app background
    surface:  "#0f1115"     # cards, panels
    elevated: "#161921"     # modals, dropdowns, tooltips
    hover:    "#1d2330"     # hover states on surfaces

  # ── Backgrounds (light mode)
  light:
    canvas:   "#f8fafc"
    surface:  "#ffffff"
    elevated: "#f1f5f9"
    hover:    "#e8f0f8"

  # ── Text hierarchy
  text:
    primary:   "#e8f0ed"    # dark mode headings + labels
    secondary: "#7a9a8e"    # dark mode descriptions, metadata
    muted:     "#3d5a52"    # dark mode disabled / placeholders

  text_light:
    primary:   "#0f172a"    # light mode headings
    secondary: "#475569"    # light mode descriptions
    muted:     "#94a3b8"    # light mode disabled

  # ── Brand / primary
  brand:
    default: "#0ea5e9"      # primary interactive, links, focus rings
    strong:  "#0284c7"      # hover on brand elements, high-contrast bg
    subtle:  "#082f49"      # brand tint for backgrounds
    glow:    "rgba(14,165,233,0.18)"   # glow / pulse shadow

  # ── Project accents (semantic per-repo roles)
  k8s:
    default: "#0ea5e9"
    strong:  "#0284c7"
    tint:    "rgba(14,165,233,0.06)"
  terraform:
    default: "#a78bfa"
    strong:  "#7c3aed"
    tint:    "rgba(167,139,250,0.06)"
  hub:
    default: "#fb7185"
    strong:  "#e11d48"
    tint:    "rgba(251,113,133,0.06)"
  policies:
    default: "#fbbf24"
    strong:  "#d97706"
    tint:    "rgba(251,191,36,0.06)"

  # ── Cloud provider identities
  gcp:   "#4285F4"
  aws:   "#FF9900"
  azure: "#0089D6"
  scw:   "#4F0599"

  # ── Semantic status
  status:
    online:   "#22d3a3"     # healthy / running (terminal green, not pure green)
    warning:  "#fbbf24"     # degraded / pending
    error:    "#f87171"     # failed / critical
    offline:  "#6b7280"     # unknown / inactive
    info:     "#60a5fa"     # informational

  # ── Borders
  border:
    default: "rgba(14,165,233,0.10)"
    strong:  "rgba(14,165,233,0.22)"
    focus:   "rgba(14,165,233,0.55)"

  border_light:
    default: "#e2e8f0"
    strong:  "#cbd5e1"
    focus:   "rgba(2,132,199,0.55)"

typography:
  display:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: "clamp(3.6rem, 10vw, 9rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.03em"

  h1:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: "clamp(1.8rem, 4vw, 3rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.02em"

  h2:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: "clamp(1.5rem, 3vw, 2.2rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"

  h3:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: "clamp(1.1rem, 2vw, 1.35rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"

  body:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "0em"

  body_sm:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"

  label:
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
    fontSize: "0.58rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.14em"

  label_md:
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
    fontSize: "0.67rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.08em"

  tag:
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
    fontSize: "0.6rem"
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: "0.06em"

  code:
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"

spacing:
  "1": "4px"
  "2": "8px"
  "3": "12px"
  "4": "16px"
  "5": "20px"
  "6": "24px"
  "8": "32px"
  "10": "40px"
  "12": "48px"
  "16": "64px"
  "20": "80px"
  "24": "96px"

rounded:
  none:  "0px"
  sm:    "4px"
  md:    "8px"
  lg:    "10px"
  xl:    "14px"
  full:  "9999px"

elevation:
  0: "none"
  1: "0 1px 3px rgba(15,23,42,0.06)"
  2: "0 4px 12px rgba(15,23,42,0.10)"
  3: "0 8px 32px rgba(15,23,42,0.16)"
  glow_sm: "0 0 12px rgba(14,165,233,0.15)"
  glow_md: "0 4px 28px rgba(14,165,233,0.18)"
  glow_k8s:      "0 4px 28px rgba(14,165,233,0.10)"
  glow_terraform: "0 4px 28px rgba(167,139,250,0.10)"
  glow_hub:      "0 4px 28px rgba(251,113,133,0.10)"
  glow_policies: "0 4px 28px rgba(251,191,36,0.10)"

animation:
  duration:
    fast:   "150ms"
    base:   "250ms"
    slow:   "400ms"
    slower: "600ms"
  easing:
    spring: "cubic-bezier(0.16, 1, 0.3, 1)"
    ease:   "cubic-bezier(0.4, 0, 0.2, 1)"
    linear: "linear"
  entrance:
    rise: "rise 0.6s cubic-bezier(0.16, 1, 0.3, 1) both"

grid:
  maxWidth: "1200px"
  gutter: "clamp(20px, 5vw, 64px)"
  columns: 12
  cardMinWidth: "480px"

components:
  button_primary:
    backgroundColor: "{colors.brand.default}"
    textColor: "#ffffff"
    padding: "12px 24px"
    borderRadius: "{rounded.md}"
    fontSize: "0.88rem"
    fontWeight: 600
    letterSpacing: "0.01em"
    border: "none"
    states:
      hover:
        backgroundColor: "{colors.brand.strong}"
        boxShadow: "0 4px 16px rgba(14,165,233,0.35)"
      active:
        backgroundColor: "#0369a1"
        boxShadow: "none"
      focus:
        outline: "2px solid {colors.border.focus}"
        outlineOffset: "2px"
      disabled:
        backgroundColor: "rgba(14,165,233,0.25)"
        textColor: "rgba(255,255,255,0.5)"
        cursor: "not-allowed"

  button_ghost:
    backgroundColor: "transparent"
    textColor: "{colors.text.secondary}"
    padding: "12px 24px"
    borderRadius: "{rounded.md}"
    fontSize: "0.88rem"
    fontWeight: 500
    border: "1px solid {colors.border.default}"
    states:
      hover:
        textColor: "{colors.text.primary}"
        borderColor: "{colors.border.strong}"
        backgroundColor: "rgba(14,165,233,0.04)"
      focus:
        outline: "2px solid {colors.border.focus}"
        outlineOffset: "2px"
      disabled:
        textColor: "{colors.text.muted}"
        cursor: "not-allowed"

  card:
    backgroundColor: "{colors.bg.surface}"
    border: "1px solid {colors.border.default}"
    borderRadius: "{rounded.lg}"
    padding: "clamp(24px, 3.5vw, 40px)"
    boxShadow: "{elevation.1}"
    states:
      hover:
        borderColor: "{colors.border.strong}"
        boxShadow: "{elevation.glow_sm}"
      focus_within:
        borderColor: "{colors.border.focus}"

  card_project:
    backgroundColor: "{colors.bg.surface}"
    borderRadius: "{rounded.lg}"
    padding: "clamp(24px, 3.5vw, 40px)"
    borderLeft: "2px solid <accent-color>"
    states:
      hover:
        backgroundColor: "<accent-tint>"
        borderLeftColor: "<accent-strong>"
        boxShadow: "<accent-glow>"

  tag:
    backgroundColor: "transparent"
    textColor: "{colors.text.muted}"
    border: "1px solid {colors.border.default}"
    padding: "2px 8px"
    borderRadius: "{rounded.sm}"
    fontFamily: "{typography.tag.fontFamily}"
    fontSize: "{typography.tag.fontSize}"
    letterSpacing: "{typography.tag.letterSpacing}"

  tag_accent:
    backgroundColor: "transparent"
    textColor: "<accent-color>"
    border: "1px solid <accent-color>28"
    padding: "2px 8px"
    borderRadius: "{rounded.sm}"

  nav:
    height: "56px"
    backgroundColor: "rgba(10,11,14,0.88)"
    borderBottom: "1px solid {colors.border.default}"
    backdropFilter: "blur(12px)"
    position: "fixed"
    zIndex: 50

  status_dot:
    size: "7px"
    borderRadius: "{rounded.full}"
    states:
      online:
        backgroundColor: "{colors.status.online}"
        animation: "pulse-dot 2.4s ease-in-out infinite"
      warning:
        backgroundColor: "{colors.status.warning}"
      error:
        backgroundColor: "{colors.status.error}"
      offline:
        backgroundColor: "{colors.status.offline}"

  input:
    backgroundColor: "{colors.bg.elevated}"
    textColor: "{colors.text.primary}"
    border: "1px solid {colors.border.default}"
    borderRadius: "{rounded.md}"
    padding: "10px 14px"
    fontSize: "0.88rem"
    states:
      focus:
        borderColor: "{colors.border.focus}"
        boxShadow: "0 0 0 3px rgba(14,165,233,0.12)"
        outline: "none"
      error:
        borderColor: "{colors.status.error}"
        boxShadow: "0 0 0 3px rgba(248,113,113,0.12)"
      disabled:
        backgroundColor: "{colors.bg.canvas}"
        textColor: "{colors.text.muted}"
        cursor: "not-allowed"
---

# Portefaix Design System

> Platform engineering, systematized — the visual language for Portefaix infrastructure tooling.

## Visual Theme & Atmosphere

Portefaix is a **mission-critical infrastructure platform**. Its UI should feel like a
high-precision control panel: dark by default, information-dense without noise, every element
purposeful. The aesthetic sits between Linear's focused minimalism and Supabase's bold developer
confidence — with a layer of "ops terminal" character unique to the platform domain.

**Emotional target:** When an engineer lands on Portefaix, they should feel _oriented and capable_.
The design communicates stability, precision, and open-source trustworthiness. Not corporate.
Not toy. The visual equivalent of a well-maintained cluster: structured, auditable, ready.

**Key principles:**

1. **Dark-first, light-honored** — dark mode is the primary design target; light mode adapts it
   cleanly without losing character. Never pure black; the canvas is deep navy-black `#0a0b0e`.
2. **Monospace as identity signal** — `JetBrains Mono` labels are not decorative; they mark
   system-level information (status, repo names, section IDs, tags). Display prose uses Inter.
3. **Accent color as semantic role** — the brand sky blue `#0ea5e9` always means "interactive /
   primary / Kubernetes". Each sub-project has its own accent (violet=Terraform, rose=Hub,
   amber=Policies). Never use an accent color decoratively outside its project scope.
4. **Grid as structure** — the subtle 28px dot-grid background is a system metaphor (Kubernetes
   nodes). It should be present but invisible; perceived only subconsciously.
5. **Density serves clarity** — prefer compact, information-rich layouts over spacious ones.
   This is a developer tool; whitespace is not luxury but precision.
6. **Status is never ambiguous** — health indicators (`online`, `warning`, `error`, `offline`)
   use distinct, WCAG-compliant colors that cannot be confused. A degraded cluster should be
   immediately visible without reading text.

---

## Color Palette & Roles

### Dark Mode (primary design target)

**Backgrounds — depth hierarchy:**
| Token | Hex | Role |
|-------|-----|------|
| `bg.canvas` | `#0a0b0e` | True app background — deepest layer |
| `bg.surface` | `#0f1115` | Cards, content panels — primary surface |
| `bg.elevated` | `#161921` | Modals, dropdowns, tooltips — floated above surface |
| `bg.hover` | `#1d2330` | Hover state on surface elements |

**Text hierarchy:**
| Token | Hex | Role |
|-------|-----|------|
| `text.primary` | `#e8f0ed` | Headings, important labels — max contrast |
| `text.secondary` | `#7a9a8e` | Descriptions, metadata — readable at rest |
| `text.muted` | `#3d5a52` | Disabled, placeholders, de-emphasized chrome |

**Brand — sky blue:**
| Token | Hex | Role |
|-------|-----|------|
| `brand.default` | `#0ea5e9` | Primary interactive (buttons, links, focus, K8s accent) |
| `brand.strong` | `#0284c7` | Hover on brand elements; high-contrast contexts |
| `brand.subtle` | `#082f49` | Brand-tinted background areas |
| `brand.glow` | `rgba(14,165,233,0.18)` | Glow shadows on brand elements |

**Project accents — never cross-use:**
| Project | Default | Strong | Use |
|---------|---------|--------|-----|
| Kubernetes / K8s | `#0ea5e9` | `#0284c7` | Same as brand |
| Terraform / GitOps | `#a78bfa` | `#7c3aed` | Violet — declarative infra |
| Helm Hub | `#fb7185` | `#e11d48` | Rose — registry, packages |
| Policies | `#fbbf24` | `#d97706` | Amber — compliance, security |

**Status colors — for health/operational state UI:**
| Token | Hex | Role |
|-------|-----|------|
| `status.online` | `#22d3a3` | Healthy, running, reconciled |
| `status.warning` | `#fbbf24` | Degraded, pending, drifted |
| `status.error` | `#f87171` | Failed, critical, admission-rejected |
| `status.offline` | `#6b7280` | Unknown, inactive, not-deployed |
| `status.info` | `#60a5fa` | Informational — progress, neutral events |

**Borders:**

- `border.default` — `rgba(14,165,233,0.10)` — resting border on cards and containers
- `border.strong` — `rgba(14,165,233,0.22)` — emphasized border (hover, active section)
- `border.focus` — `rgba(14,165,233,0.55)` — focus ring and selected state

### Light Mode

Light mode inverts the surface depth but preserves all semantic roles:

- Canvas: `#f8fafc`, Surface: `#ffffff`, Elevated: `#f1f5f9`
- Text primary: `#0f172a`, secondary: `#475569`, muted: `#94a3b8`
- Brand colors stay identical (`#0ea5e9` / `#0284c7`)
- Borders: `#e2e8f0` (default), `#cbd5e1` (strong)

The subtle grid background switches from dark dot-grid to a light 48px cross-grid at 4% opacity.

---

## Typography

Two families only. Never introduce a third.

**Inter** — all prose, headings, UI copy, button labels. Loaded at weights 300/400/500/600/700/800.
**JetBrains Mono** — system labels, tag text, section IDs, repo names, status indicators, code.

### Scale

| Role     | Size                  | Weight | Line Height | Tracking | Family         |
| -------- | --------------------- | ------ | ----------- | -------- | -------------- |
| Display  | clamp(3.6rem–9rem)    | 800    | 0.92        | -0.03em  | Inter          |
| H1       | clamp(1.8rem–3rem)    | 700    | 1.05        | -0.02em  | Inter          |
| H2       | clamp(1.5rem–2.2rem)  | 700    | 1.1         | -0.02em  | Inter          |
| H3       | clamp(1.1rem–1.35rem) | 700    | 1.2         | -0.01em  | Inter          |
| Body     | 0.95rem               | 400    | 1.7         | 0em      | Inter          |
| Body SM  | 0.82rem               | 400    | 1.6         | 0em      | Inter          |
| Label LG | 0.67rem               | 400    | 1.4         | +0.08em  | JetBrains Mono |
| Label SM | 0.58rem               | 400    | 1.4         | +0.14em  | JetBrains Mono |
| Tag      | 0.6rem                | 400    | 1.0         | +0.06em  | JetBrains Mono |
| Code     | 0.875rem              | 400    | 1.6         | 0em      | JetBrains Mono |

**Why negative tracking on headings:** Tight letter-spacing on large text (display, H1, H2) creates
optical cohesion — the word reads as a solid unit. At 9rem, Inter's natural spacing looks too airy.
This is the same approach used by Linear and Vercel.

**Why monospace for labels:** Labels like `01 // Cloud Infrastructure` and `SYSTEM STATUS: ONLINE`
are not prose — they are structured data markers. Monospace communicates machine-generated /
system-level origin, setting them apart visually from human-written copy.

**Do not use font-weight 800 below H1 size** — at small sizes, 800 weight in Inter looks
heavy-handed and kills readability. Use 600 or 700 for sub-heading emphasis.

---

## Layout

### Spacing Scale

Base unit: **4px**. All spacing uses multiples of 4.

```
4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64 / 80 / 96px
```

**Inner component padding:** 8–16px. Cards: 24–40px (responsive via clamp).
**Section vertical padding:** clamp(64px, 10vw, 120px) top; clamp(48px, 8vw, 80px) bottom.
**Inline gaps between items:** 6–12px for tags/chips; 12px for card grids; 28px for nav links.

### Grid

- Max content width: **1200px**, centered with `margin: 0 auto`
- Horizontal gutter: `clamp(20px, 5vw, 64px)` — scales naturally from mobile to ultrawide
- Card grids: `auto-fit` with `minmax(min(100%, 480px), 1fr)` — 2-up on desktop, stacked on mobile
- Cloud grid: `minmax(min(100%, 520px), 1fr)` with `gap: 2px` — intentional "dashboard panel" feel

### Breakpoints

- Mobile ≤ 640px: single column; docs-cta row stacks vertically
- Tablet 641–1024px: most grids go 2-up naturally
- Desktop ≥ 1025px: full layout, max-width container, nav at full width

### Background grid

The repeating background grid is always present, never interactive:

- Dark: radial dot grid, 28px pitch, `rgba(14,165,233,0.06)`
- Light: cross-grid (CSS gradient), 48px pitch, `rgba(14,165,233,0.04)`
- Fixed attachment — does not scroll with content

---

## Elevation & Depth

Portefaix uses three elevation levels plus brand glows. Never use elevation to decorate —
only to communicate layer relationships.

| Level | CSS                              | Used for                               |
| ----- | -------------------------------- | -------------------------------------- |
| 0     | `none`                           | Inline / embedded — no perceived depth |
| 1     | `0 1px 3px rgba(15,23,42,0.06)`  | Cards at rest on light mode            |
| 2     | `0 4px 12px rgba(15,23,42,0.10)` | Dropdowns, hover state cards           |
| 3     | `0 8px 32px rgba(15,23,42,0.16)` | Modals, focused panels                 |

**Dark mode:** Use `none` for elevation 0–1; elevation is communicated through background color
difference (`bg.surface` vs `bg.elevated`), not shadows. Dark shadows are nearly invisible.

**Brand glows** replace shadows in dark mode for interactive elements:

- `glow_sm` — `0 0 12px rgba(14,165,233,0.15)` — subtle hover on brand elements
- `glow_md` — `0 4px 28px rgba(14,165,233,0.18)` — focused / active brand elements
- Project-specific glows follow the same pattern with their accent color

**Z-index scale:**

- 10: page sections (above background)
- 20: sticky section headers
- 50: fixed nav
- 100: dropdowns / tooltips
- 200: modals / dialogs

---

## Shapes

**Corner radius:**

- `0px` — never used in production; only for debug/explicit flat
- `4px` — tags, small chips, code blocks
- `8px` — buttons, input fields, icon containers
- `10px` — cards, major content panels
- `14px` — large feature cards (future)
- `9999px` — status dots, avatars, pill badges

**Form language:** Portefaix uses **rounded rectangles**, not sharp squares and not fully rounded
pills. Corners at `8–10px` communicate engineered precision — not clinical sharpness,
not consumer softness. Buttons feel like hardware toggles. Cards feel like dashboard panels.

**Border accents:** Project cards use a `2px solid` left border (not top, not all-sides) to
signal project identity without overwhelming the card. This is a deliberate asymmetry — a single
accent edge reads as a "category marker" familiar from terminal log prefixes.

**Scan-line accent:** The hero section has a `3px` top gradient rule
(`transparent → #0ea5e9 → #7c3aed → transparent`). This is the only purely decorative element
in the system. It should appear once, at the viewport top in the hero. Do not replicate it
elsewhere.

---

## Components

### Primary Button

```
Background:  #0ea5e9
Text:        #ffffff (always — never invert on hover)
Padding:     12px 24px
Border:      none
Radius:      8px
Font:        Inter 600 0.88rem tracking +0.01em
Transition:  background 200ms, box-shadow 200ms ease

Hover:  background #0284c7, box-shadow 0 4px 16px rgba(14,165,233,0.35)
Active: background #0369a1, box-shadow none
Focus:  outline 2px solid rgba(14,165,233,0.55), offset 2px
Disabled: background rgba(14,165,233,0.25), text rgba(255,255,255,0.5), cursor not-allowed
```

### Ghost Button

```
Background:  transparent
Text:        text.secondary
Border:      1px solid border.default
Padding:     12px 24px
Radius:      8px
Font:        Inter 500 0.88rem

Hover:  text text.primary, border border.strong, bg rgba(14,165,233,0.04)
Focus:  outline 2px solid rgba(14,165,233,0.55), offset 2px
Disabled: text text.muted, cursor not-allowed
```

### Project Card

```
Background:   bg.surface (dark) / #ffffff (light)
Border-left:  2px solid <project-accent>  ← identity marker
Border:       1px solid border.default (remaining 3 sides)
Radius:       10px
Padding:      clamp(24px, 3.5vw, 40px)
Shadow:       elevation.1 (light) / none (dark)
Transition:   border-color 250ms, box-shadow 250ms, background 250ms

Hover (dark):  background <project-tint>, border-left strong, box-shadow <project-glow>
Hover (light): border-color rgba(<accent>,0.45), box-shadow 0 8px 32px rgba(<accent>,0.10)
```

The large faded number (`opacity: 0.10`) in the top-left of each card is a deliberate ghost
element — it creates visual hierarchy and section identity without competing with the title.
Keep it between `opacity: 0.08` and `opacity: 0.12`. Never increase to 0.25+.

### Tag / Chip

```
Background:  transparent
Text:        text.muted (neutral) or <project-accent> (colored variant)
Border:      1px solid border.default (neutral) or <accent>28 (colored)
Padding:     2px 8px
Radius:      4px
Font:        JetBrains Mono 0.6rem tracking +0.06em

Never interactive by default. If tags become clickable, add hover: text.primary, border border.strong.
```

### Status Dot

```
Size:        7px × 7px
Shape:       50% radius (circle)
Variants:    online (#22d3a3), warning (#fbbf24), error (#f87171), offline (#6b7280)

Pulse animation (online only):
  @keyframes pulse-dot {
    0%, 100% { opacity: 1; box-shadow: 0 0 0 0 currentColor; }
    50%       { opacity: 0.6; box-shadow: 0 0 0 5px rgba(0,0,0,0); }
  }
  duration: 2.4s ease-in-out infinite
```

### Navigation Bar

```
Height:       56px
Background:   rgba(10,11,14,0.88) — translucent, reveals scroll
Blur:         backdrop-filter blur(12px)
Border-bottom: 1px solid rgba(14,165,233,0.08)
Position:     fixed, inset top 0, z-index 50
Padding:      0 clamp(20px, 5vw, 64px)

Logo: Inter 700 0.95rem tracking +0.05em (PORTEFAIX)
Nav links: JetBrains Mono 0.67rem tracking +0.08em, UPPERCASE
GitHub CTA: brand.default border, text brand.default; hover fill rgba(14,165,233,0.08)
```

### Section Header Pattern

```
Label:     JetBrains Mono 0.58rem tracking +0.16em, brand.strong, UPPERCASE
           Format: "01 // Section Name"
Heading:   Inter 700 clamp(1.8rem–3rem) tracking -0.02em
Border:    1px solid border.default, bottom, padding-bottom 28px
Gap:       label → heading: 10px; heading block → description: margin-end
```

### Input Field

```
Background:  bg.elevated
Text:        text.primary
Border:      1px solid border.default
Radius:      8px
Padding:     10px 14px
Font:        Inter 400 0.88rem

Focus:  border brand.default, box-shadow 0 0 0 3px rgba(14,165,233,0.12)
Error:  border status.error, box-shadow 0 0 0 3px rgba(248,113,113,0.12)
Disabled: bg.canvas, text.muted, cursor not-allowed
```

---

## Entrance Animations

All visible content uses scroll-reveal or entrance animations. Never flash content in:

**Entrance (hero, above fold):** `rise` keyframe — translate from `0 20px` to `0 0`, opacity 0→1.
Duration 600ms, easing `cubic-bezier(0.16, 1, 0.3, 1)` (spring). Staggered delays:

- e1: 40ms, e2: 120ms, e3: 200ms, e4: 280ms, e5: 360ms

**Scroll reveal (below fold):** IntersectionObserver adds `.in` class. Use `opacity 500ms + translate 500ms`
with same spring easing. Stagger siblings via `transition-delay` at 70ms intervals.

**Never animate layout** (width, height, top, left). Only opacity and transform (translate/scale).
`will-change: transform, opacity` on animated elements.

**Reduce motion:** All animations collapse to `0.01ms` duration when `prefers-reduced-motion: reduce`.

---

## Do's and Don'ts

### Do

- **Use brand blue `#0ea5e9` only for interactive and K8s-scoped elements.** A decorative blue
  element is a false affordance — users will try to click it.
- **Use monospace for system-level text:** repo names, section IDs like `01 //`, status labels,
  tags, version numbers. This signals "structured data", not prose.
- **Keep section IDs in the format `01 // Section Name`** — the double-slash prefix is a
  consistent identity marker throughout the platform. It echoes code comment syntax.
- **Match elevation to light/dark mode:** Use box-shadow on light; use background color
  difference on dark. Shadows on dark backgrounds look muddy.
- **Keep the per-project color system pure:** Violet is only Terraform/GitOps. Rose is only Hub.
  Amber is only Policies. Never repurpose one project's accent for a status or generic UI role.
- **Test both themes:** Every new component must be designed for dark and light simultaneously.
  Hardcoded colors (`#0ea5e9`) are fine for brand; all surface/text/border must use CSS variables.

### Don't

- **Don't use `font-weight: 800` below `h1` size.** At 0.82rem, 800 weight is illegible.
- **Don't introduce a third typeface.** Inter + JetBrains Mono is the complete set.
- **Don't use `opacity` on colored elements to indicate hierarchy** — use the `text.secondary`
  / `text.muted` tokens instead. `opacity: 0.5` on colored text makes it look broken.
- **Don't use the scan-line gradient outside the hero.** It is a hero-specific device.
- **Don't stack multiple glowing shadows.** One glow per element. Combining glows creates a
  neon aesthetic inconsistent with the precise, technical character of the system.
- **Don't use `error` red for non-error states.** `#f87171` is exclusively for failed / critical
  operational states. Do not use it for emphasis, accent, or branding.
- **Don't animate layout properties** (padding, width, height). Only transform and opacity.
- **Don't hardcode spacing values.** Use the 4px-base scale. A `padding: 17px` is a bug.
- **Don't use rounded-full (`border-radius: 9999px`) on non-circular elements.** Pill shapes
  belong to badge/avatar contexts only. Buttons use `8px`.
