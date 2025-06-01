# Big Brother Visual Patterns

## Overview
Big Brother revolutionized system monitoring by introducing the status matrix - a grid of colored dots that provided instant visibility into infrastructure health. Its genius lay in making complex system states immediately understandable through color alone.

## Core Visual Elements

### 1. The Status Matrix
```
┌─────────────────┬─────┬─────┬─────┬─────┬─────┐
│ Hostname        │ CPU │ MEM │ DISK│ NET │ HTTP│
├─────────────────┼─────┼─────┼─────┼─────┼─────┤
│ web-server-01   │  ●  │  ●  │  ●  │  ●  │  ●  │
│ web-server-02   │  ●  │  ●  │  ●  │  ●  │  ●  │
│ db-master       │  ●  │  ●  │  ●  │  ●  │  ●  │
│ db-slave        │  ●  │  ●  │  ●  │  ●  │  ●  │
│ mail-server     │  ●  │  ●  │  ●  │  ●  │  ●  │
│ backup-server   │  ●  │  ●  │  ●  │  ●  │  ●  │
└─────────────────┴─────┴─────┴─────┴─────┴─────┘
```

### 2. Color States
Big Brother's original colors mapped to TIC-80 SWEETIE-16:

| Status | Original | TIC-80 SWEETIE-16 | Hex | Meaning |
|--------|----------|---------|-----|---------|
| Green | #00FF00 | Lime | #a7f070 | All OK |
| Yellow | #FFFF00 | Yellow | #ffcd75 | Warning |
| Red | #FF0000 | Red | #b13e53 | Critical |
| Purple | #FF00FF | Purple | #5d275d | No data/Error |
| Clear | #FFFFFF | White | #f4f4f4 | Disabled |
| Blue | #0000FF | Blue | #3b5dc9 | Informational |

### 3. Status Dot Rendering
```
3x3 Base Dot:     6x6 at 2x:       9x9 at 3x:
 ●●●              ●●●●●●           ●●●●●●●●●
 ●●●              ●●●●●●           ●●●●●●●●●
 ●●●              ●●●●●●           ●●●●●●●●●
                  ●●●●●●           ●●●●●●●●●
                  ●●●●●●           ●●●●●●●●●
                  ●●●●●●           ●●●●●●●●●
                                   ●●●●●●●●●
                                   ●●●●●●●●●
                                   ●●●●●●●●●
```

### 4. Header Styling
```
╔═══════════════════════════════════════════╗
║     BIG BROTHER IS WATCHING YOUR SYSTEMS  ║
║            Last Update: 12:34:56          ║
╚═══════════════════════════════════════════╝
```
- Double-line borders for emphasis
- Centered title in 5x7 font
- Update timestamp for freshness

### 5. Drill-Down Detail View
When clicking a status dot:
```
┌──────────────────────────────────┐
│ web-server-01 - CPU Status       │
├──────────────────────────────────┤
│ Current Load: 45%                │
│ 5 min avg: 42%                   │
│ 15 min avg: 38%                  │
│                                  │
│ Status History:                  │
│ ●●●●●●●●●●●●●●●●●●●●            │
│ └─────────────────┘              │
│ 24h                              │
└──────────────────────────────────┘
```

## Visual Hierarchy

### Primary View Elements
1. **Title Bar** - System identification
2. **Status Matrix** - At-a-glance health
3. **Legend** - Color meanings
4. **Update Time** - Data freshness

### Information Density
- Minimum 20 hosts visible without scrolling
- 5-10 service columns typical
- Compact 3x5 font for host names
- Clear 5x7 font for headers

## Grid Patterns

### Standard Layout
```
Column Width: 5 characters (30 pixels at 2x scale)
Row Height: 1 line (8 pixels at 2x scale)
Dot Size: 3x3 base (scales with display)
Padding: 1 pixel between elements
```

### Responsive Scaling
| Display | Scale | Dots/Screen | Font |
|---------|-------|-------------|------|
| 1080p | 3x | 30x20 | 9x15 |
| 1440p | 4x | 32x22 | 12x20 |
| 4K | 6x | 35x24 | 18x30 |

## Status Propagation

### Worst-Status Wins
If any service is red, host shows red:
```
Host Status = MAX(all service statuses)
Group Status = MAX(all host statuses)
Overall Status = MAX(all group statuses)
```

### Visual Indicators
- Blinking for critical alerts (2Hz)
- Solid colors for stable states
- Fade effect for stale data

## Modern Enhancements

### Hover Effects
```
Normal:     Hover:      Active:
  ●          ●●●         ███
             ●●●         ███
             ●●●         ███
```
Using TIC-80 SWEETIE-16 colors:
- Hover: Add cyan (#73eff7) outline
- Active: Add white (#f4f4f4) border

### Grouping
```
┌─ Web Servers ──────────────────┐
│ web-01  ● ● ● ● ●              │
│ web-02  ● ● ● ● ●              │
├─ Database Servers ─────────────┤
│ db-01   ● ● ● ● ●              │
│ db-02   ● ● ● ● ●              │
└────────────────────────────────┘
```

### Status History Sparklines
Tiny graphs showing 24h history:
```
▁▂▃▄▅▆▇█  (CPU usage over time)
████▇▆▅▄  (Memory trend)
```

## Implementation Patterns

### Efficient Rendering
1. Pre-render status dots at each scale
2. Cache rendered text strings
3. Use dirty rectangles for updates
4. Batch similar color operations

### Memory Layout
```rust
struct StatusMatrix {
    hosts: Vec<Host>,
    services: Vec<Service>,
    states: Vec<Vec<StatusColor>>,
    last_update: u64,
}

enum StatusColor {
    Green = 5,    // TIC-80 SWEETIE-16 palette index (Lime)
    Yellow = 4,   // Yellow
    Red = 2,      // Red
    Purple = 1,   // Purple
    Clear = 12,   // White
    Blue = 9,     // Blue
}
```

### Update Strategy
- Poll every 30 seconds
- Stagger updates to avoid spikes
- Show update progress indicator
- Maintain previous state during updates

## Big Brother's Innovation

Big Brother proved that complex system states could be represented simply:
- **Color = Status**: No interpretation needed
- **Grid = Scale**: Handles 10 or 1000 hosts
- **Simplicity = Speed**: Instant comprehension
- **Consistency = Trust**: Same patterns everywhere

## TIC-80 Aesthetic Integration

### Enhanced Dot Styles
```
Standard:   Pulsing:    Alert:
   ●         ●→◐→○      ●◐○●
                        (rapid)
```

### Border Variations
- Normal: 1px black
- Warning: 1px orange
- Critical: 2px red with 1Hz blink
- Disabled: 1px dark gray

### Background Patterns
Subtle dithering for visual interest:
```
Normal:     Hover:      Selected:
········    ·█·█·█·█    ████████
········    █·█·█·█·    ████████
········    ·█·█·█·█    ████████
```

## Accessibility Considerations

### Color-Blind Friendly
Add patterns to colors:
- Green: Solid fill
- Yellow: Horizontal lines
- Red: Diagonal lines
- Purple: Dots
- Blue: Vertical lines

### Text Alternatives
Each dot includes hover text:
```
"web-01 CPU: OK (15% usage)"
"db-master Disk: WARNING (85% full)"
"mail-server Network: CRITICAL (unreachable)"
```

## Legacy and Evolution

Big Brother's matrix view remains influential because it solves a fundamental problem: how to show the health of many things at once. By combining this proven pattern with TIC-80's constrained SWEETIE-16 palette, we create monitoring that is both functional and delightful.

The key insight: **Less information displayed better beats more information displayed poorly.**
