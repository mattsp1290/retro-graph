# MRTG Visual Patterns

## Overview
Multi Router Traffic Grapher (MRTG) established many of the visual conventions for network monitoring that persist today. Its design philosophy emphasized clarity, data density, and utilitarian aesthetics.

## Key Visual Elements

### 1. Dual-Line Graph Layout
```
┌─────────────────────────────────────────┐
│ Title: Traffic Analysis for eth0        │
├─────────────────────────────────────────┤
│ 100%│                                   │
│     │     ╱╲      In (Green Area)      │
│  75%│    ╱  ╲                          │
│     │   ╱    ╲    Out (Blue Line)      │
│  50%│  ╱      ╲  ────────              │
│     │ ╱        ╲                       │
│  25%│╱                                 │
│     └───────────────────────────────→  │
│      0  6  12  18  24 (hours)         │
└─────────────────────────────────────────┘
```

**TIC-80 SWEETIE-16 Adaptation:**
- Input traffic: Green (#38b764) filled area
- Output traffic: Blue (#3b5dc9) line only
- Background: White (#f4f4f4)
- Grid: Light Gray (#94b0c2)

### 2. Time-Based Views
MRTG's signature feature: Multiple time scales for the same data
- Daily (5-minute averages)
- Weekly (30-minute averages)
- Monthly (2-hour averages)
- Yearly (1-day averages)

### 3. Statistics Box
```
┌──────────────────────────┐
│ Max In:  156.3 kb/s      │
│ Average: 45.2 kb/s       │
│ Current: 52.1 kb/s       │
│                          │
│ Max Out: 89.4 kb/s       │
│ Average: 23.1 kb/s       │
│ Current: 31.2 kb/s       │
└──────────────────────────┘
```

**Font Choice:** 3x5 pixel font for data density
**Colors:** Black text on white background

### 4. Grid Pattern
- Horizontal lines at 0%, 25%, 50%, 75%, 100%
- Vertical lines at time intervals
- 1-pixel width, dashed pattern
- Light gray color for subtlety

### 5. Title Bar
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Traffic Analysis - eth0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
- Bold horizontal lines
- Centered text
- 5x7 font for readability

## Color Mapping from MRTG to TIC-80 SWEETIE-16

| MRTG Original | TIC-80 SWEETIE-16 | Usage |
|---------------|-------------------|--------|
| #00CC00 (Green) | #38b764 (Green) | Input/Inbound traffic |
| #0000FF (Blue) | #3b5dc9 (Blue) | Output/Outbound traffic |
| #FF0000 (Red) | #b13e53 (Red) | Peak/Maximum lines |
| #000000 (Black) | #1a1c2c (Black) | Text, borders |
| #FFFFFF (White) | #f4f4f4 (White) | Background |
| #CCCCCC (Gray) | #94b0c2 (Light Gray) | Grid lines |

## Distinctive Features

### Area Fill Pattern
MRTG fills the area under the input line:
```
████████████████
███████████████▀
██████████████▀ 
█████████████▀  
████████████▀   
```

### Legend Placement
Always bottom or right side:
- Clear color coding
- Minimal text
- Direct data association

### Scale Indicators
- Always show 0 and max
- Intermediate values at regular intervals
- Right-aligned numbers
- Units clearly marked (kb/s, %, etc.)

## Modern Adaptations

### Responsive Scaling
At different pixel scales:
- 2x: Minimum viable for readability
- 3x: Optimal for 1080p displays
- 4x: Perfect for 1440p
- 6x: 4K displays

### Enhanced Grid Options
- Toggle grid on/off
- Adjust grid density
- Weekend shading (subtle gray)

### Interactive Elements
While keeping static aesthetic:
- Hover tooltips with exact values
- Click to zoom time ranges
- Maintain pixel alignment

## Implementation Notes

### Efficient Rendering Order
1. Clear background (white)
2. Draw grid if enabled
3. Fill input area (back to front)
4. Draw output line
5. Draw axes and labels
6. Add statistics box
7. Draw border frame

### Memory Optimization
- Pre-calculate common values
- Reuse pixel buffers
- Cache rendered text

### Pixel-Perfect Alignment
- All coordinates must be integers
- Scale at rendering, not data level
- Maintain consistent line weights

## MRTG's Legacy

MRTG's visual language persists because it solves fundamental problems:
1. **Data density** - Maximum information in minimum space
2. **Clarity** - Instantly understandable
3. **Consistency** - Same patterns everywhere
4. **Efficiency** - Fast to render and read

By adapting these patterns with TIC-80's SWEETIE-16 palette, we honor this legacy while adding charm and modern polish.
