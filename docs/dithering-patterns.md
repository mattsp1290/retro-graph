# 🎨 Dithering Pattern Library

## Overview

This document provides a comprehensive library of dithering patterns for creating gradients, textures, and visual effects using TIC-80's SWEETIE-16 palette. These patterns enable smooth visual transitions while maintaining the pixel-perfect aesthetic.

## What is Dithering?

Dithering is a technique that uses patterns of pixels to create the illusion of colors or gradients that aren't available in a limited palette. By alternating pixels of different colors, we can create perceived intermediate shades when viewed from a distance.

## Basic 4×4 Dithering Patterns

### Density Levels

```
0% (Empty):     6.25% (1/16):   12.5% (2/16):   18.75% (3/16):
····            ●···            ●···            ●···
····            ····            ··●·            ··●·
····            ····            ····            ····
····            ····            ····            ·●··

25% (4/16):     31.25% (5/16):  37.5% (6/16):   43.75% (7/16):
●···            ●·●·            ●·●·            ●·●·
··●·            ··●·            ··●·            ●·●·
·●··            ·●··            ●·●·            ●···
····            ····            ····            ····

50% (8/16):     56.25% (9/16):  62.5% (10/16):  68.75% (11/16):
●·●·            ●·●·            ●·●·            ●●●·
·●·●            ●●·●            ●●·●            ●●·●
●·●·            ●·●·            ●·●●            ●·●●
·●·●            ·●·●            ·●·●            ·●·●

75% (12/16):    81.25% (13/16): 87.5% (14/16):  93.75% (15/16):
●●●·            ●●●●            ●●●●            ●●●●
●·●●            ●·●●            ●●●●            ●●●●
●●●·            ●●●·            ●●●●            ●●●●
●●·●            ●●·●            ●●·●            ●●●·

100% (Full):
●●●●
●●●●
●●●●
●●●●
```

## Common Pattern Applications

### Gradient Fills

#### Vertical Gradient (Light to Dark)
```
████████████████  ← 100% fill
●●●●●●●●●●●●●●●●  ← 87.5%
●●●·●●●·●●●·●●●·  ← 75%
●·●·●·●·●·●·●·●·  ← 50%
●···●···●···●···  ← 25%
················  ← 0%
```

#### Horizontal Gradient
```
█ ● ● · · · · ·
█ ● ● · · · · ·
█ ● ● · · · · ·
█ ● ● · · · · ·
↑             ↑
100%          0%
```

### Area Fill Patterns for Graphs

#### MRTG-Style Graph Fill
```
Graph line with gradient fill below:
      ╱╲
     ╱██╲      ← Solid at peak
    ╱●●●●╲     ← 87.5% dither
   ╱●·●·●╲    ← 75% dither
  ╱·●·●·●·╲   ← 50% dither
 ╱●···●···╲  ← 25% dither
╱··········╲ ← 12.5% dither
```

### Shadow and Depth Effects

#### Drop Shadow Pattern
```
Main element:     With shadow:
████████         ████████
████████         ████████··
████████         ████████·●
████████         ████████●●
                 ··●●●●●●●●
                 ·●●●●●●●●●
```

## Color Combination Patterns

### Two-Color Dithering

#### Green to Blue Transition (for data series blending)
```
Color 1: Green (#38b764)  →  Color 2: Blue (#3b5dc9)

100% Green   75/25    50/50    25/75    100% Blue
████████    ●●●●●●●●  ●●●●●●●●  ●●●●●●●●  ████████
████████    ●●●●●●●●  ●●●●●●●●  ●●●●●●●●  ████████
████████    ●●●●●●●●  ●●●●●●●●  ●●●●●●●●  ████████
████████    ●●●●●●●●  ●●●●●●●●  ●●●●●●●●  ████████
```

### Alert State Transitions

#### Normal to Warning Gradient
```
Green → Yellow → Orange → Red
████  ●●●●  ●●●●  ●●●●  ████
████  ●●●●  ●●●●  ●●●●  ████
████  ●●●●  ●●●●  ●●●●  ████
```

## Advanced Patterns

### Noise Patterns (for texture)

#### Fine Noise
```
●··●·●··
·●··●··●
··●··●·●
●··●··●·
```

#### Coarse Noise
```
●●··●●··
●●··●●··
··●●··●●
··●●··●●
```

### Diagonal Patterns

#### 45° Lines (Sparse)
```
●···    ·●··    ··●·    ···●
···●    ●···    ·●··    ··●·
··●·    ···●    ●···    ·●··
·●··    ··●·    ···●    ●···
```

#### 45° Lines (Dense)
```
●·●·    ·●·●    ●·●·    ·●·●
·●·●    ●·●·    ·●·●    ●·●·
●·●·    ·●·●    ●·●·    ·●·●
·●·●    ●·●·    ·●·●    ●·●·
```

### Crosshatch Patterns

#### Light Crosshatch
```
●···●···
········
········
●···●···
········
········
●···●···
········
```

#### Dense Crosshatch
```
●·●·●·●·
·●·●·●·●
●·●·●·●·
·●·●·●·●
●·●·●·●·
·●·●·●·●
```

## Implementation Code Examples

### Pattern Definition in Code

```rust
// Define patterns as 2D arrays
const DITHER_25: [[bool; 4]; 4] = [
    [true,  false, false, false],
    [false, false, true,  false],
    [false, true,  false, false],
    [false, false, false, true],
];

const DITHER_50: [[bool; 4]; 4] = [
    [true,  false, true,  false],
    [false, true,  false, true],
    [true,  false, true,  false],
    [false, true,  false, true],
];

// Function to apply dithering
fn apply_dither(x: u32, y: u32, pattern: &[[bool; 4]; 4]) -> bool {
    pattern[(y % 4) as usize][(x % 4) as usize]
}
```

### Gradient Fill Algorithm

```rust
fn fill_gradient_area(
    start_y: u32,
    end_y: u32,
    color1: u8,
    color2: u8,
) {
    let height = end_y - start_y;
    
    for y in start_y..end_y {
        let progress = (y - start_y) as f32 / height as f32;
        let dither_level = (progress * 16.0) as u8;
        
        for x in 0..width {
            let use_color2 = should_dither(x, y, dither_level);
            let color = if use_color2 { color2 } else { color1 };
            plot_pixel(x, y, color);
        }
    }
}
```

## Pattern Usage Guidelines

### When to Use Each Pattern

1. **0-25% Dithering**
   - Subtle shadows
   - Light overlays
   - Barely visible grids

2. **50% Dithering**
   - Clear color mixing
   - Transparency effects
   - Equal blend of two states

3. **75-100% Dithering**
   - Strong overlays
   - Near-solid fills
   - Emphasis areas

### Performance Considerations

1. **Pre-compute patterns** - Store patterns in lookup tables
2. **Use bit operations** - `(x & 1) ^ (y & 1)` for checkerboard
3. **Tile patterns** - Use modulo to repeat 4×4 patterns
4. **Cache pattern results** - For static elements

## Visual Examples in Context

### Line Graph with Dithered Fill
```
100%┤                    
    │     ╱█╲        
 75%┤    ╱███╲       
    │   ╱█●●●█╲      
 50%┤  ╱●●●●●●●╲     
    │ ╱●·●·●·●·●╲    
 25%┤╱·●·●·●·●·●·╲   
    │··············  
  0%└────────────────
```

### Status Matrix with State Transitions
```
Normal → Warning (dithered transition)
 ●●●● → ●●●● → ●●●● → ●●●●
 ●●●●    ●●●●    ●●●●    ●●●●
 ●●●●    ●●●●    ●●●●    ●●●●
Green   G/Y mix  Y/O mix  Orange
```

### Bar Chart with Gradient Bars
```
████  ← 100% solid
●●●●  ← 87.5%
●●●·  ← 75%
●·●·  ← 50%
●···  ← 25%
····  ← 0%
```

## Best Practices

1. **Maintain Consistency**
   - Use the same dither patterns throughout your interface
   - Apply patterns at consistent densities

2. **Consider Viewing Distance**
   - Finer patterns work better at higher resolutions
   - Coarser patterns are more visible at lower resolutions

3. **Test at All Scales**
   - Ensure patterns look good at 2x, 3x, 4x, 6x
   - Some patterns may create moiré effects at certain scales

4. **Respect the Pixel Grid**
   - Always align patterns to the pixel grid
   - Never use sub-pixel positioning

5. **Use Sparingly**
   - Dithering is a tool, not a requirement
   - Solid colors often provide better clarity

## Pattern Quick Reference

| Effect | Pattern Type | Density |
|--------|-------------|---------|
| Subtle shadow | Fine noise | 12.5% |
| Transparency | Checkerboard | 50% |
| Gradient fill | Progressive | 0-100% |
| Texture | Diagonal lines | 25% |
| Color blend | Alternating | 50% |
| Emphasis | Dense fill | 75%+ |

## Conclusion

Dithering patterns are powerful tools for creating visual richness within the constraints of a 16-color palette. When used thoughtfully, they enhance the retro aesthetic while maintaining clarity and purpose. Remember: every pattern should serve the data, not obscure it.

The patterns in this library have been optimized for the specific colors in TIC-80's SWEETIE-16 palette and will render beautifully at all supported scaling factors.
