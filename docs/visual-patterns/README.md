# Visual Patterns Documentation

This directory contains detailed analysis of visual patterns from 90s monitoring tools and their adaptation to TIC-80's aesthetic constraints.

## Pattern Documents

### 1. [MRTG Patterns](mrtg-patterns.md)
- Dual-line graph layouts
- Area fill techniques
- Time-based view scaling
- Statistics box design
- Grid and axis patterns

### 2. [Big Brother Patterns](bigbrother-patterns.md)
- Status matrix design
- Color state mapping
- Dot rendering at scales
- Grid layout strategies
- Status propagation logic

## Common Patterns Across Tools

### Color Usage
All tools converged on similar color semantics:
- **Green**: Good/Normal/OK
- **Yellow**: Warning/Caution
- **Red**: Error/Critical/Down
- **Blue**: Informational/Secondary
- **Gray**: Disabled/Unknown
- **White**: Background/Clear

### Information Hierarchy
1. **Overview First**: Status at a glance
2. **Details on Demand**: Drill-down capability
3. **Context Preserved**: Time ranges, comparisons
4. **Consistent Layout**: Predictable placement

### Data Density Techniques
- Compact fonts (3x5 pixels)
- Minimal borders (1 pixel)
- Efficient use of color
- No decorative elements
- Maximum data per pixel

## TIC-80 SWEETIE-16 Adaptations

### Palette Mapping Summary
| 90s Convention | TIC-80 SWEETIE-16 | Index | Use Case |
|----------------|-------------------|-------|----------|
| CGA Green | Green | 6 | Input/Success |
| CGA Blue | Blue | 9 | Output/Info |
| VGA Red | Red | 2 | Errors/Alerts |
| VGA Yellow | Yellow | 4 | Warnings |
| DOS Gray | Light Gray | 13 | Grids/Inactive |

### Scaling Strategy
- **Base Resolution**: 240x136 (TIC-80 native, close to 16:9)
- **Alternative**: 640x360 (perfect 16:9)
- **Integer Scales**: 2x, 3x, 4x, 6x, 7x, 10x, 15x
- **Font Scaling**: Matches display scale
- **Dot Scaling**: Perfect squares only

## Implementation Priorities

### Must Have
1. MRTG-style line graphs
2. Big Brother status matrix
3. 3x5 and 5x7 bitmap fonts
4. TIC-80 SWEETIE-16 palette
5. Integer scaling support

### Nice to Have
1. Cricket-style advanced graphs
2. HP OpenView enterprise layouts
3. Animated transitions (10 FPS)
4. Dithering patterns
5. Sound effects (optional)

## Visual Pattern Insights

### Why These Patterns Work
1. **Instant Recognition**: Colors convey meaning immediately
2. **Scalability**: Same patterns work for 10 or 10,000 data points
3. **Efficiency**: Every pixel serves a purpose
4. **Consistency**: Learn once, use everywhere
5. **Timelessness**: Still effective 30 years later

### Modern Enhancements
While preserving retro aesthetics:
- Responsive scaling for modern displays
- Hover states using TIC-80 SWEETIE-16 colors
- Keyboard navigation support
- Touch-friendly hit targets
- Accessibility improvements

## Design Principles

### From 90s Tools
- Function over form
- Data density matters
- Color has meaning
- Consistency builds trust
- Simplicity scales

### From TIC-80
- Constraints spark creativity
- 16 colors are enough
- Pixels should be visible
- Charm through limitation
- Joy in simplicity

## Conclusion

The fusion of 90s monitoring tool patterns with TIC-80's aesthetic creates a unique visual language that is:
- **Functional**: Solves real monitoring needs
- **Beautiful**: Cohesive and charming
- **Efficient**: Fast to render and read
- **Nostalgic**: Honors computing history
- **Modern**: Works on today's displays

These patterns form the foundation for retro-graph's component system, ensuring every graph and display honors both traditions while serving contemporary needs.
