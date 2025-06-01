# 🎨 SWEETIE-16 Color Mapping Guide for Retro-Graph

## Overview

This guide provides detailed rules and recommendations for using TIC-80's SWEETIE-16 palette across all retro-graph components. Each color has been carefully mapped to specific use cases based on 90s monitoring tool conventions and modern accessibility standards.

## Color Index Reference

```
Index | Hex     | Name       | RGB           | HSL
------|---------|------------|---------------|------------------
0     | #1a1c2c | Black      | (26,28,44)    | 233°,26%,14%
1     | #5d275d | Purple     | (93,39,93)    | 300°,41%,26%
2     | #b13e53 | Red        | (177,62,83)   | 349°,48%,47%
3     | #ef7d57 | Orange     | (239,125,87)  | 15°,82%,64%
4     | #ffcd75 | Yellow     | (255,205,117) | 38°,100%,73%
5     | #a7f070 | Lime       | (167,240,112) | 134°,79%,69%
6     | #38b764 | Green      | (56,183,100)  | 141°,53%,47%
7     | #257179 | Dark Cyan  | (37,113,121)  | 186°,53%,31%
8     | #29366f | Dark Blue  | (41,54,111)   | 229°,46%,30%
9     | #3b5dc9 | Blue       | (59,93,201)   | 226°,57%,51%
10    | #41a6f6 | Light Blue | (65,166,246)  | 207°,91%,61%
11    | #73eff7 | Cyan       | (115,239,247) | 184°,88%,71%
12    | #f4f4f4 | White      | (244,244,244) | 0°,0%,96%
13    | #94b0c2 | Light Gray | (148,176,194) | 203°,28%,67%
14    | #566c86 | Gray       | (86,108,134)  | 208°,22%,43%
15    | #333c57 | Dark Gray  | (51,60,87)    | 225°,26%,27%
```

## Primary Color Assignments

### Data Visualization Colors

#### Time Series Data (Line Graphs)
- **Primary Series**: Green (6) - Input/Inbound/Positive metrics
- **Secondary Series**: Blue (9) - Output/Outbound/Neutral metrics
- **Tertiary Series**: Orange (3) - Additional metrics/Warnings
- **Quaternary Series**: Dark Cyan (7) - Fourth data series

#### Status Indicators
- **Healthy/OK**: Lime (5) - Maximum visibility for good states
- **Warning**: Yellow (4) - Caution without alarm
- **High/Alert**: Orange (3) - Elevated concern
- **Critical**: Red (2) - Immediate attention required
- **Error/No Data**: Purple (1) - System failures
- **Unknown/Disabled**: Gray (14) - Inactive states

### UI Framework Colors

#### Backgrounds
- **Primary Background**: White (12) - Clean, paper-like
- **Secondary Background**: Light Gray (13) - Panels, sections
- **Tertiary Background**: Dark Gray (15) - Headers, emphasis
- **Dark Mode Primary**: Black (0) - Alternative scheme

#### Text
- **Primary Text**: Black (0) on light backgrounds
- **Primary Text**: White (12) on dark backgrounds
- **Secondary Text**: Gray (14) - Muted information
- **Disabled Text**: Light Gray (13) - Inactive elements

#### Borders and Lines
- **Strong Borders**: Black (0) - 1px primary borders
- **Normal Borders**: Gray (14) - Standard UI borders
- **Subtle Borders**: Light Gray (13) - Dividers
- **Grid Lines**: Light Gray (13) - Graph grids

## Context-Specific Mappings

### Line Graphs

```
Component        | Color | Index | Notes
-----------------|-------|-------|------------------------
Background       | White | 12    | Clean canvas
Grid             | Lt Gray| 13   | 1px dashed lines
Primary Line     | Green | 6     | Solid 1px
Secondary Line   | Blue  | 9     | Solid or dashed
Area Fill        | Green | 6     | With dithering gradient
Peak Indicator   | Red   | 2     | Horizontal line at max
Axis Lines       | Black | 0     | 1px solid
Axis Labels      | Black | 0     | 3×5 or 5×7 font
Value Labels     | Black | 0     | On hover/selection
```

### Bar Charts

```
Component        | Color    | Index | Notes
-----------------|----------|-------|------------------------
Bars (Normal)    | Green    | 6     | < 60% of max
Bars (Warning)   | Orange   | 3     | 60-80% of max
Bars (Critical)  | Red      | 2     | > 80% of max
Grouped Bar 1    | Green    | 6     | Primary series
Grouped Bar 2    | Blue     | 9     | Secondary series
Empty Space      | Lt Gray  | 13    | Background of bars
```

### Status Matrix

```
Status          | Color    | Index | Use Case
----------------|----------|-------|------------------------
OK              | Lime     | 5     | All systems normal
Warning         | Yellow   | 4     | Attention needed
High            | Orange   | 3     | Elevated metrics
Critical        | Red      | 2     | Failures/Outages
Error           | Purple   | 1     | System errors
Unknown         | Gray     | 14    | No data received
Disabled        | Lt Gray  | 13    | Monitoring paused
```

### Interactive States

```
State           | Color      | Index | Application
----------------|------------|-------|------------------------
Hover           | Light Blue | 10    | Highlight on mouseover
Active          | Cyan       | 11    | Currently selected
Focus           | Cyan       | 11    | Keyboard navigation
Pressed         | Dark Blue  | 8     | Button/element pressed
```

## Color Combination Rules

### High Contrast Pairs

These combinations ensure readability:

```
Background | Foreground | Use Case
-----------|------------|------------------
White (12) | Black (0)  | Primary text
Black (0)  | White (12) | Inverted text
White (12) | Red (2)    | Error messages
White (12) | Green (6)  | Success messages
Lt Gray(13)| Black (0)  | Secondary panels
```

### Avoid These Combinations

Low contrast pairs that reduce readability:

```
Background  | Foreground | Issue
------------|------------|------------------
Yellow (4)  | White (12) | Too bright
Lt Gray(13) | Gray (14)  | Insufficient contrast
Purple (1)  | Black (0)  | Too dark
Dark Blue(8)| Purple (1) | Poor visibility
```

## Semantic Color Groups

### Traffic Light Metaphor
```
Good    → Caution → Bad
Lime(5) → Yellow(4) → Red(2)
```

### Data Priority
```
Primary → Secondary → Tertiary → Quaternary
Green(6) → Blue(9) → Orange(3) → Dark Cyan(7)
```

### Severity Escalation
```
Normal → Attention → Warning → Critical → Error
Lime(5) → Yellow(4) → Orange(3) → Red(2) → Purple(1)
```

## Accessibility Considerations

### Color Blind Friendly Patterns

For users with color vision deficiencies, combine color with:

1. **Patterns**: Use dithering patterns to differentiate
2. **Icons**: Add symbolic indicators (↑↓⚠✓✗)
3. **Position**: Rely on spatial arrangement
4. **Labels**: Always provide text alternatives

### Example Accessible Status Indicators
```
OK:       ● (solid lime)      or ✓
Warning:  ◐ (half yellow)     or ⚠
Critical: ◯ (hollow red)      or ✗
Error:    ⊗ (crossed purple)  or !
```

## Implementation Examples

### CSS/JavaScript Palette Definition
```javascript
const SWEETIE_16 = {
  0:  { hex: '#1a1c2c', name: 'black',     rgb: [26,28,44] },
  1:  { hex: '#5d275d', name: 'purple',    rgb: [93,39,93] },
  2:  { hex: '#b13e53', name: 'red',       rgb: [177,62,83] },
  3:  { hex: '#ef7d57', name: 'orange',    rgb: [239,125,87] },
  4:  { hex: '#ffcd75', name: 'yellow',    rgb: [255,205,117] },
  5:  { hex: '#a7f070', name: 'lime',      rgb: [167,240,112] },
  6:  { hex: '#38b764', name: 'green',     rgb: [56,183,100] },
  7:  { hex: '#257179', name: 'darkCyan',  rgb: [37,113,121] },
  8:  { hex: '#29366f', name: 'darkBlue',  rgb: [41,54,111] },
  9:  { hex: '#3b5dc9', name: 'blue',      rgb: [59,93,201] },
  10: { hex: '#41a6f6', name: 'lightBlue', rgb: [65,166,246] },
  11: { hex: '#73eff7', name: 'cyan',      rgb: [115,239,247] },
  12: { hex: '#f4f4f4', name: 'white',     rgb: [244,244,244] },
  13: { hex: '#94b0c2', name: 'lightGray', rgb: [148,176,194] },
  14: { hex: '#566c86', name: 'gray',      rgb: [86,108,134] },
  15: { hex: '#333c57', name: 'darkGray',  rgb: [51,60,87] }
};
```

### Rust Implementation
```rust
const PALETTE: [(u8, u8, u8); 16] = [
    (0x1a, 0x1c, 0x2c), // 0: Black
    (0x5d, 0x27, 0x5d), // 1: Purple
    (0xb1, 0x3e, 0x53), // 2: Red
    (0xef, 0x7d, 0x57), // 3: Orange
    (0xff, 0xcd, 0x75), // 4: Yellow
    (0xa7, 0xf0, 0x70), // 5: Lime
    (0x38, 0xb7, 0x64), // 6: Green
    (0x25, 0x71, 0x79), // 7: Dark Cyan
    (0x29, 0x36, 0x6f), // 8: Dark Blue
    (0x3b, 0x5d, 0xc9), // 9: Blue
    (0x41, 0xa6, 0xf6), // 10: Light Blue
    (0x73, 0xef, 0xf7), // 11: Cyan
    (0xf4, 0xf4, 0xf4), // 12: White
    (0x94, 0xb0, 0xc2), // 13: Light Gray
    (0x56, 0x6c, 0x86), // 14: Gray
    (0x33, 0x3c, 0x57), // 15: Dark Gray
];
```

## Color Usage Checklist

Before finalizing any design:

- [ ] All 16 colors are utilized effectively
- [ ] Primary data uses Green (6) and Blue (9)
- [ ] Status indicators follow traffic light convention
- [ ] Text has sufficient contrast with backgrounds
- [ ] Interactive states are clearly differentiated
- [ ] Patterns supplement color for accessibility
- [ ] No more than 4 colors used in any single graph
- [ ] Grid lines use Light Gray (13) for subtlety
- [ ] Borders use appropriate weight (Black for emphasis)

## Summary

The SWEETIE-16 palette provides everything needed for effective data visualization. By following these mapping guidelines, retro-graph components will maintain visual consistency while honoring both the constraints of fantasy consoles and the proven patterns of 90s monitoring tools.

Remember: **Color serves function. Every hue has purpose.**
