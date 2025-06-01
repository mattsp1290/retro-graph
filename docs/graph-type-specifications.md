# 📊 Retro-Graph Type Specifications

## Table of Contents
1. [Overview](#overview)
2. [Design Principles](#design-principles)
3. [Color Palette Reference](#color-palette-reference)
4. [Graph Types](#graph-types)
   - [Line Graphs](#line-graphs)
   - [Bar Charts](#bar-charts)
   - [Status Matrix](#status-matrix)
   - [Sparklines](#sparklines)
5. [Dithering Patterns](#dithering-patterns)
6. [Scaling Specifications](#scaling-specifications)
7. [Technical Implementation](#technical-implementation)

## Overview

This document provides pixel-perfect specifications for all graph types in the retro-graph WebAssembly component library. Every design uses TIC-80's SWEETIE-16 palette exclusively and scales perfectly at integer multiples.

**Base Resolution**: 240×136 pixels (TIC-80 native)  
**Aspect Ratio**: 16:9 (approximately)  
**Scaling Factors**: 2x, 3x, 4x, 6x

## Design Principles

1. **Every pixel is deliberate** - No accidental pixels or anti-aliasing
2. **Clarity over decoration** - Data visibility is paramount
3. **Consistent alignment** - 8×8 pixel grid system
4. **Nostalgic but modern** - 90s aesthetics with contemporary clarity
5. **Performance first** - Efficient rendering patterns for WASM

## Color Palette Reference

### SWEETIE-16 Graph Usage Mapping

| Index | Hex     | Name       | Primary Usage                    |
|-------|---------|------------|----------------------------------|
| 0     | #1a1c2c | Black      | Text, borders, strong lines      |
| 1     | #5d275d | Purple     | Critical errors, no data         |
| 2     | #b13e53 | Red        | Alerts, max values, down states  |
| 3     | #ef7d57 | Orange     | Warnings, tertiary data          |
| 4     | #ffcd75 | Yellow     | Caution, highlights              |
| 5     | #a7f070 | Lime       | Success, OK status, positive     |
| 6     | #38b764 | Green      | Primary data, input/inbound      |
| 7     | #257179 | Dark Cyan  | Quaternary data series           |
| 8     | #29366f | Dark Blue  | Background accents               |
| 9     | #3b5dc9 | Blue       | Secondary data, output/outbound  |
| 10    | #41a6f6 | Light Blue | Interactive elements, hover      |
| 11    | #73eff7 | Cyan       | Selection, special highlights    |
| 12    | #f4f4f4 | White      | Primary backgrounds              |
| 13    | #94b0c2 | Light Gray | Grid lines, muted elements       |
| 14    | #566c86 | Gray       | Borders, disabled states         |
| 15    | #333c57 | Dark Gray  | Subtle UI elements               |

## Graph Types

### Line Graphs

#### MRTG-Style Dual Line Graph (80×60 minimum)

```
┌──────────────────────────────────────────────────────────────┐ ← Black (0)
│ Traffic: eth0                                    [5x7 font]   │
├──────────────────────────────────────────────────────────────┤ ← Gray (14)
│100%┤                                                          │
│    │     ╱╲         ← Green (6) filled area                  │
│ 75%┤    ╱  ╲                                                 │
│    │   ╱    ╲       ← Blue (9) line only                     │
│ 50%┤  ╱      ╲  ════                                         │
│    │ ╱        ╲                                              │
│ 25%┤╱          ╲                                             │
│    │                                                          │
│  0%└────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬─────→│
│        00:00 04:00 08:00 12:00 16:00 20:00  [3x5 font]      │
│                                                               │
│ ▓ In: 45.2 kb/s  ─ Out: 23.1 kb/s  Peak: 156.3 kb/s        │
└──────────────────────────────────────────────────────────────┘

Background: White (12)
Grid: Light Gray (13) - 1px dashed
Peak line: Red (2) - 1px horizontal at max value
```

**Pixel Specifications**:
- Minimum size: 80×60 pixels
- Border: 1px solid black
- Padding: 2px all sides
- Grid: Every 20% horizontal, time-based vertical
- Line thickness: 1px
- Area fill: Solid color with no transparency

#### Multi-Line Graph Variant (100×60 minimum)

```
┌──────────────────────────────────────────────────────────────┐
│ System Metrics - 4 Series                                     │
├──────────────────────────────────────────────────────────────┤
│100%┤                                                          │
│    │      ╱╲    CPU ─── (Green 6)                           │
│ 75%┤  ╱══╱  ╲   MEM ═══ (Blue 9)                            │
│    │ ╱  ╱    ╲  NET ┅┅┅ (Orange 3)                          │
│ 50%┤╱  ╱  ┅┅┅ ╲ DSK ─·─ (Dark Cyan 7)                       │
│    │  ╱ ┅┅   ┅ ╲                                            │
│ 25%┤ ╱┅┅        ╲·─·─·─                                      │
│    │╱             ╲                                           │
│  0%└──────────────────────────────────────────────────────→  │
└──────────────────────────────────────────────────────────────┘
```

**Line Styles** (at 1x scale):
- Primary: Solid 1px
- Secondary: Double line (══)
- Tertiary: Dotted (┅┅┅)
- Quaternary: Dash-dot (─·─)

### Bar Charts

#### Vertical Bar Chart (60×40 minimum)

```
┌────────────────────────────────┐
│ Daily Traffic (GB)             │
├────────────────────────────────┤
│ 10│                            │
│   │    ██                      │ ← Green (6)
│  8│    ██  ██                  │
│   │    ██  ██                  │
│  6│    ██  ██  ██              │
│   │ ██ ██  ██  ██              │
│  4│ ██ ██  ██  ██  ██          │
│   │ ██ ██  ██  ██  ██  ██      │
│  2│ ██ ██  ██  ██  ██  ██  ██  │
│   │ ██ ██  ██  ██  ██  ██  ██  │
│  0└────────────────────────────┘
│    M  T  W  T  F  S  S         │
└────────────────────────────────┘

Bar width: 2px minimum
Gap between bars: 1px minimum
```

#### Grouped Bar Chart

```
┌────────────────────────────────┐
│ In/Out Comparison              │
├────────────────────────────────┤
│100│                            │
│   │    ██                      │ ← Green (6) = In
│ 80│    ██ ▓▓                   │ ← Blue (9) = Out
│   │    ██ ▓▓ ██                │
│ 60│    ██ ▓▓ ██ ▓▓             │
│   │ ██ ██ ▓▓ ██ ▓▓ ██          │
│ 40│ ██ ██ ▓▓ ██ ▓▓ ██ ▓▓       │
│   │ ██ ██ ▓▓ ██ ▓▓ ██ ▓▓ ██    │
│ 20│ ██ ██ ▓▓ ██ ▓▓ ██ ▓▓ ██ ▓▓ │
│   │ ██ ██ ▓▓ ██ ▓▓ ██ ▓▓ ██ ▓▓ │
│  0└────────────────────────────┘
└────────────────────────────────┘
```

#### Horizontal Bar Chart (80×40 minimum)

```
┌──────────────────────────────────┐
│ Server Load                      │
├──────────────────────────────────┤
│ web-01  ████████████░░░░ 75%     │ ← Color based on value
│ web-02  ██████░░░░░░░░░░ 40%     │   Green < 60%
│ db-01   ████████████████ 95%     │   Orange 60-80%
│ db-02   ████░░░░░░░░░░░░ 25%     │   Red > 80%
│ cache   ██████████░░░░░░ 65%     │
└──────────────────────────────────┘

Bar height: 3px
Background: Light Gray (13) for empty portion
```

### Status Matrix

#### Standard Status Grid (Big Brother-style)

```
┌─────────────┬───┬───┬───┬───┬───┐
│ Host        │CPU│MEM│DSK│NET│SVC│  5x7 font
├─────────────┼───┼───┼───┼───┼───┤
│ web-srv-01  │ ● │ ● │ ● │ ● │ ● │  3x3 dots
│ web-srv-02  │ ● │ ● │ ● │ ● │ ● │
│ db-master   │ ● │ ● │ ● │ ● │ ● │
│ db-slave    │ ● │ ● │ ● │ ● │ ● │
│ cache-01    │ ● │ ● │ ● │ ● │ ● │
│ queue-01    │ ● │ ● │ ● │ ● │ ● │
└─────────────┴───┴───┴───┴───┴───┘

Dot colors:
● Lime (5) = OK
● Yellow (4) = Warning  
● Orange (3) = High
● Red (2) = Critical
● Purple (1) = Error/No Data
○ Gray (14) = Disabled
```

**Dot Rendering at Different Scales**:
```
1x (3x3):  2x (6x6):    3x (9x9):      4x (12x12):
 ●●●       ●●●●●●      ●●●●●●●●●     ●●●●●●●●●●●●
 ●●●       ●●●●●●      ●●●●●●●●●     ●●●●●●●●●●●●
 ●●●       ●●●●●●      ●●●●●●●●●     ●●●●●●●●●●●●
           ●●●●●●      ●●●●●●●●●     ●●●●●●●●●●●●
           ●●●●●●      ●●●●●●●●●     ●●●●●●●●●●●●
           ●●●●●●      ●●●●●●●●●     ●●●●●●●●●●●●
                       ●●●●●●●●●     ●●●●●●●●●●●●
                       ●●●●●●●●●     ●●●●●●●●●●●●
                       ●●●●●●●●●     ●●●●●●●●●●●●
                                     ●●●●●●●●●●●●
                                     ●●●●●●●●●●●●
                                     ●●●●●●●●●●●●
```

#### Compact Matrix (High Density)

```
┌──────────────────────────┐
│ Cluster Status Overview  │
├──────────────────────────┤
│ ●●●●●●●●●●●●●●●●●●●●●●  │ 2x2 dots
│ ●●●●●●●●●●●●●●●●●●●●●●  │ 1px gaps
│ ●●●●●●●●●●●●●●●●●●●●●●  │
│ ●●●●●●●●●●●●●●●●●●●●●●  │
│ ●●●●●●●●●●●●●●●●●●●●●●  │
└──────────────────────────┘
```

### Sparklines

#### Inline Sparkline (16×8 minimum)

```
CPU: ▁▂▄█▆▃▁▂ 45%   (Single pixel height variations)
MEM: ▄▄▅▆▇███ 92%   (8 data points in 16 pixels)
NET: ▁▁▂▁▃▂▁▁ 12%   
```

**Height Mapping** (8px tall):
- ▁ = 1px (0-12.5%)
- ▂ = 2px (12.5-25%)
- ▃ = 3px (25-37.5%)
- ▄ = 4px (37.5-50%)
- ▅ = 5px (50-62.5%)
- ▆ = 6px (62.5-75%)
- ▇ = 7px (75-87.5%)
- █ = 8px (87.5-100%)

#### Dashboard Sparkline Array

```
┌─────────────────────────────────┐
│ 24-Hour Overview                │
├─────────────────────────────────┤
│ CPU ▁▂▄▅▇█▇▅▄▃▂▁▁▂▃▄▅▆▇▆▅▄▃▂ │
│ MEM ▄▄▄▄▄▅▅▅▅▆▆▆▇▇▇▇███▇▇▆▆▅ │
│ NET ▁▁▁▂▃▄▅▆▇▆▅▄▃▂▁▁▁▁▂▂▃▃▂▁ │
│ DSK ▂▂▂▂▂▂▂▂▂▂▂▂▃▃▃▃▃▃▃▃▃▃▃▃ │
└─────────────────────────────────┘
```

## Dithering Patterns

### Basic Patterns (4×4 tiles)

```
12.5%:      25%:        37.5%:      50%:
●···        ●···        ●·●·        ●·●·
····        ··●·        ····        ·●·●
··●·        ····        ●·●·        ●·●·
····        ·●··        ··●·        ·●·●

62.5%:      75%:        87.5%:      Gradient:
●●●·        ●●●·        ●●●●        ●···
·●·●        ●·●●        ●●·●        ●●··
●·●●        ●●●·        ●●●●        ●●●·
●●·●        ●●·●        ●●●·        ●●●●
```

### Area Fill with Dithering

```
Graph with gradient fill using dithering:
│     ╱████████╲     ← 100% solid
│    ╱██●●●●●●██╲    ← 87.5% dither
│   ╱██●●●●●●●●██╲   ← 75% dither  
│  ╱●●●●●●●●●●●●●╲  ← 62.5% dither
│ ╱●·●·●·●·●·●·●·╲ ← 50% dither
│╱·················╲ ← 25% dither
```

## Scaling Specifications

### Scale Factor Decision Matrix

| Display Resolution | Graph Scale | Font Scale | Minimum Graph Size |
|-------------------|-------------|------------|-------------------|
| 720p (1280×720)   | 2x          | 3×5 → 6×10 | 160×120          |
| 1080p (1920×1080) | 3x          | 3×5 → 9×15 | 240×180          |
| 1440p (2560×1440) | 4x          | 5×7 → 20×28| 320×240          |
| 4K (3840×2160)    | 6x          | 5×7 → 30×42| 480×360          |

### Responsive Breakpoints

```
if (screenWidth >= 3840) {
    scale = 6;
    useFont = FONT_5x7;
} else if (screenWidth >= 2560) {
    scale = 4;
    useFont = FONT_5x7;
} else if (screenWidth >= 1920) {
    scale = 3;
    useFont = FONT_3x5;
} else {
    scale = 2;
    useFont = FONT_3x5;
}
```

## Technical Implementation

### Memory Layout

```rust
// Graph component base structure
struct Graph {
    width: u16,          // Base width (before scaling)
    height: u16,         // Base height (before scaling)
    scale: u8,           // 2, 3, 4, or 6
    buffer: Vec<u8>,     // RGBA pixel buffer
    palette: [Color; 16], // SWEETIE-16 colors
}

// Efficient pixel plotting
fn plot_pixel(x: u16, y: u16, color_index: u8) {
    let color = PALETTE[color_index as usize];
    let base_offset = (y * width + x) * 4;
    
    // Plot scaled pixel
    for sy in 0..scale {
        for sx in 0..scale {
            let offset = ((y * scale + sy) * (width * scale) + 
                         (x * scale + sx)) * 4;
            buffer[offset] = color.r;
            buffer[offset + 1] = color.g;
            buffer[offset + 2] = color.b;
            buffer[offset + 3] = 255;
        }
    }
}
```

### Drawing Order

1. Clear background (White #12)
2. Draw grid if enabled (Light Gray #13)
3. Render data series (back to front)
4. Draw axes (Black #0)
5. Render axis labels (Black #0)
6. Draw border (Black #0)
7. Add title/legend
8. Apply any UI overlays

### Performance Optimizations

1. **Pre-calculate scaled coordinates**
   ```rust
   let scaled_points: Vec<(u16, u16)> = data_points
       .iter()
       .map(|p| (p.x * scale, p.y * scale))
       .collect();
   ```

2. **Use lookup tables for dithering**
   ```rust
   const DITHER_PATTERNS: [[bool; 16]; 8] = [
       // Pre-computed 4x4 patterns for each density level
   ];
   ```

3. **Batch similar color operations**
   ```rust
   // Draw all pixels of one color before switching
   for color_index in 0..16 {
       draw_all_pixels_of_color(color_index);
   }
   ```

### Component Interface

```typescript
interface RetroGraph {
    // Core configuration
    type: 'line' | 'bar' | 'matrix' | 'sparkline';
    width: number;   // Base resolution
    height: number;  // Base resolution
    scale: 2 | 3 | 4 | 6;
    
    // Data
    data: GraphData;
    
    // Styling
    showGrid: boolean;
    showLegend: boolean;
    colorScheme: 'default' | 'alert' | 'mono';
    
    // Update methods
    update(data: GraphData): void;
    render(): Uint8Array; // Returns pixel buffer
}
```

## Edge Cases

### Empty Data
```
┌────────────────────────┐
│ No Data Available      │
├────────────────────────┤
│                        │
│    ┌─────────────┐     │
│    │      ?      │     │ ← Purple (1)
│    │   No Data   │     │ ← 5x7 font
│    └─────────────┘     │
│                        │
└────────────────────────┘
```

### Single Data Point
```
Show as dot with value label:
│100%┤                   │
│    │        ●          │ ← 3x3 dot
│    │      45.2%        │ ← Value label
│  0%└───────────────────┘
```

### Overflow Values
```
Values exceeding scale show peak indicator:
│100%┤════════▲═════════ │ ← Red (2) line with arrow
│    │     ╱██╲          │
│    │    ╱████╲         │ ← Clipped at top
```

## Summary

These specifications provide a complete blueprint for implementing pixel-perfect, retro-styled graphs using TIC-80's SWEETIE-16 palette. Every element has been designed to scale perfectly while maintaining the nostalgic aesthetic of 90s monitoring tools with modern clarity and usability.

Key implementation points:
- Always use integer coordinates
- Scale at the rendering layer, not the data layer
- Maintain consistent pixel density across all elements
- Test at all target resolutions
- Optimize for WebAssembly performance

Remember: **Every pixel has purpose. Constraints create consistency.**
