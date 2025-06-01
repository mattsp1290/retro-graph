# Retro-TIC80 Style Guide: 90s Monitoring Tools Meet Fantasy Console Aesthetics

## Executive Summary

This style guide defines the visual language for retro-graph, a WebAssembly component system that fuses the utilitarian honesty of 90s network monitoring tools with TIC-80's joyful constraints. Every pixel is deliberate, every color has purpose, and modern resolutions are embraced through integer scaling that maintains authentic pixelation.

## Core Design Principles

### 1. Constraint-Driven Beauty
- **16 colors only** - TIC-80's SWEETIE-16 palette is sacred and sufficient
- **Pixel-perfect rendering** - No anti-aliasing, embrace the jaggies
- **Integer scaling** - 2x, 3x, 4x only for authentic pixelation
- **Deliberate simplicity** - If it's not essential, it's not there

### 2. Data Density Through Clarity
- **MRTG-inspired layouts** - Proven information hierarchy
- **Big Brother's matrix efficiency** - Maximum data, minimum chrome
- **Cricket's sophistication** - Advanced features, simple presentation
- **Modern responsiveness** - 16:9 native, graceful degradation

## Color System

### TIC-80 SWEETIE-16 Palette Application

The 16-color SWEETIE-16 palette maps beautifully to monitoring needs:

#### Primary Data Colors
- **Green (#38b764)** - Input/inbound traffic, normal operations
- **Blue (#3b5dc9)** - Output/outbound traffic, secondary metrics
- **Lime (#a7f070)** - Success states, up status, good health

#### Alert & Status Colors
- **Red (#b13e53)** - Critical alerts, errors, down states
- **Orange (#ef7d57)** - Warnings, high utilization
- **Yellow (#ffcd75)** - Caution, current/active selections
- **Purple (#5d275d)** - Severe errors, system failures

#### UI Framework Colors
- **White (#f4f4f4)** - Primary backgrounds (note: warm white, not pure)
- **Light Gray (#94b0c2)** - Grid lines, secondary elements
- **Gray (#566c86)** - Disabled states, subtle borders
- **Black (#1a1c2c)** - Text, strong borders, emphasis

#### Accent Colors
- **Dark Blue (#29366f)** - Headers, primary UI elements
- **Dark Cyan (#257179)** - Tertiary data series
- **Light Blue (#41a6f6)** - Special highlights, anomalies
- **Cyan (#73eff7)** - Subtle backgrounds, hover states
- **Dark Gray (#333c57)** - Alternative UI state

### Color Mapping Strategy

```
90s Tool Color → TIC-80 SWEETIE-16 Equivalent
---------------------------------
MRTG Green (#00CC00) → Green (#38b764)
MRTG Blue (#0000FF) → Blue (#3b5dc9)
CGA Cyan (#00FFFF) → Cyan (#73eff7)
CGA Magenta (#FF00FF) → Purple (#5d275d)
Amber Monitor (#FFAA00) → Orange (#ef7d57)
DOS Gray (#AAAAAA) → Light Gray (#94b0c2)
```

## Typography

### Bitmap Font Specifications

#### Primary Font: 3x5 Pixel Font
- **Use cases**: Graph labels, compact displays, tooltips
- **Scaling**: 2x (6x10), 3x (9x15), 4x (12x20)
- **Character set**: ASCII 32-126
- **Line height**: Font height + 1 pixel

#### Secondary Font: 5x7 Pixel Font  
- **Use cases**: Headers, important values, readable text
- **Scaling**: 2x (10x14), 3x (15x21), 4x (20x28)
- **Character set**: ASCII 32-126 + extended
- **Line height**: Font height + 2 pixels

### Font Rendering Rules
1. Always render on pixel boundaries
2. No sub-pixel positioning
3. Use TIC-80 SWEETIE-16 palette colors only
4. Implement simple drop shadows with dark gray for contrast

## Graph Rendering Patterns

### Line Graphs (MRTG-Style)

```
╔════════════════════════════╗
║ │100%                       ║  <- Scale markers in 3x5 font
║ │                           ║
║ │    ╱╲    Input (filled)   ║  <- Dark green area fill
║ │   ╱  ╲                    ║
║ │  ╱    ╲  Output (line)    ║  <- Blue line, 1px thick
║ │ ╱      ╲─────             ║
║ │╱                          ║
║ └──────────────────────────→║  <- Time axis
║ 00:00   12:00   00:00      ║  <- Labels in 3x5 font
╚════════════════════════════╝
```

#### Implementation Details:
- Grid: Light gray (#94b0c2), 1px lines
- Background: White (#f4f4f4)
- Border: Black (#1a1c2c), 1px
- Area fill: Use simple scanline filling
- Peaks: Red (#b13e53) horizontal line for max values

### Status Matrix (Big Brother-Style)

```
┌─────────────┬───┬───┬───┬───┐
│ Hostname    │CPU│MEM│DSK│NET│  <- 5x7 font headers
├─────────────┼───┼───┼───┼───┤
│ web-01      │ ● │ ● │ ● │ ● │  <- Status dots 3x3 pixels
│ web-02      │ ● │ ● │ ● │ ● │  <- Scaled to 6x6, 9x9, 12x12
│ db-master   │ ● │ ● │ ● │ ● │
│ db-slave    │ ● │ ● │ ● │ ● │
└─────────────┴───┴───┴───┴───┘
```

#### Status Colors:
- Lime (#a7f070) - OK/Up
- Yellow (#ffcd75) - Warning
- Orange (#ef7d57) - High load
- Red (#b13e53) - Critical/Down
- Gray (#566c86) - Unknown/Disabled
- Purple (#5d275d) - Error/Failed

### Bar Charts

```
100│ ██                        <- Bars use solid fill
 90│ ██ ██                     <- 2px minimum width
 80│ ██ ██ ██                  <- 1px gap between bars
 70│ ██ ██ ██ ██
 60│ ██ ██ ██ ██ ██
 50│ ██ ██ ██ ██ ██ ██
   └─────────────────────
    M  T  W  T  F  S  S
```

## Pixel Scaling Strategies

### Resolution Targets

| Display Type | Resolution | Scale Factor | Resulting Size |
|-------------|------------|--------------|----------------|
| 1080p | 1920x1080 | 3x | 640x360 base |
| 1440p | 2560x1440 | 4x | 640x360 base |
| 4K | 3840x2160 | 6x | 640x360 base |

### Scaling Algorithm
```rust
// Nearest-neighbor scaling only
fn scale_pixel(x: u32, y: u32, scale: u32) -> Vec<(u32, u32)> {
    let mut pixels = Vec::new();
    for dy in 0..scale {
        for dx in 0..scale {
            pixels.push((x * scale + dx, y * scale + dy));
        }
    }
    pixels
}
```

## UI Component Patterns

### Window Chrome
```
╔═══════════════[×]═╗  <- 1px black border
║ Window Title      ║  <- 5x7 font, dark blue bg
╟───────────────────╢  <- 1px dark gray separator
║                   ║  <- Content area, white bg
║                   ║
╚═══════════════════╝
```

### Buttons
```
Normal:  [▶ Play ]  <- Black border, light gray bg
Hover:   [▶ Play ]  <- Black border, cyan bg
Active:  [▶ Play ]  <- Dark gray border, dark gray bg
```

### Scrollbars
- Width: 5px (scales to 10px, 15px, 20px)
- Track: Light gray (#94b0c2)
- Thumb: Gray (#566c86)
- Arrows: Black (#1a1c2c) on light gray

## Dithering Patterns

For gradient effects and texture, use ordered dithering:

```
25% density:    50% density:    75% density:
█ · · ·         █ · █ ·         █ █ █ ·
· · · ·         · █ · █         █ █ · █
· · █ ·         █ · █ ·         █ · █ █
· · · ·         · █ · █         · █ █ █
```

## Animation Guidelines

### Frame Rates
- Graph updates: 5-minute intervals (MRTG-style)
- UI animations: 10 FPS (retro console feel)
- Status changes: Instant, no transitions

### Blink Patterns
- Critical alerts: 2Hz (twice per second)
- Warnings: 1Hz (once per second)
- Active selections: Solid, no blinking

## WebAssembly Implementation Notes

### Memory Layout
```rust
// Pixel buffer as flat array (RGBA)
const BUFFER_WIDTH: usize = 640;
const BUFFER_HEIGHT: usize = 360;
const PIXEL_BUFFER: [u8; BUFFER_WIDTH * BUFFER_HEIGHT * 4];

// TIC-80 SWEETIE-16 palette as constants
const PALETTE: [(u8, u8, u8); 16] = [
    (0x1a, 0x1c, 0x2c), // 0: Black
    (0x5d, 0x27, 0x5d), // 1: Purple
    // ... etc
];
```

### Rendering Pipeline
1. Clear buffer to background color
2. Draw grid (if enabled)
3. Render data series back-to-front
4. Draw axes and labels
5. Apply UI chrome
6. Scale to output resolution

## Component Interface Design

### Graph Component
```typescript
interface GraphConfig {
  width: number;          // Base resolution (before scaling)
  height: number;         // Base resolution (before scaling)
  scale: 2 | 3 | 4 | 6;   // Integer scaling factor
  timeRange: '5min' | '30min' | 'hour' | 'day' | 'week' | 'month' | 'year';
  showGrid: boolean;
  palette: 'mrtg' | 'bigbrother' | 'custom';
}
```

### Status Matrix Component
```typescript
interface StatusMatrixConfig {
  columns: string[];      // Service names
  rows: Host[];          // Host configurations
  cellSize: 3 | 6 | 9;   // Dot size in pixels
  updateInterval: number; // Milliseconds
}
```

## Best Practices

### DO:
- ✓ Align everything to pixel grid
- ✓ Use palette colors exclusively
- ✓ Embrace pixelation at all scales
- ✓ Keep animations minimal and functional
- ✓ Maintain consistent scaling throughout
- ✓ Test at all target resolutions

### DON'T:
- ✗ Use transparency (except for masks)
- ✗ Apply anti-aliasing or smoothing
- ✗ Mix scaling factors in one view
- ✗ Use gradients (use dithering instead)
- ✗ Animate for decoration
- ✗ Add unnecessary UI elements

## Conclusion

This fusion of 90s monitoring aesthetics with TIC-80's constraints creates a unique visual language that is both nostalgic and fresh. By embracing limitations, we achieve clarity, consistency, and charm that modern monitoring tools often lack.

Remember: **Every pixel has purpose. If it's not deliberate, it's not there.**
