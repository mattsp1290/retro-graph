# Sparkline Mockups - Pixel Perfect Designs

## Inline Sparklines

### Base Resolution (16×8 pixels)

```
Single Metrics:
CPU: ▁▂▄█▆▃▁▂ 45%
MEM: ▄▄▅▆▇███ 92%
NET: ▁▁▂▁▃▂▁▁ 12%
DSK: ▂▂▂▂▃▃▃▃ 28%

Each character represents 1-2 data points
Height: 8 pixels divided into 8 levels
Width: 16 pixels (2px per data point)
```

### Height Level Mapping
```
█ = 8px = 87.5-100%
▇ = 7px = 75-87.5%
▆ = 6px = 62.5-75%
▅ = 5px = 50-62.5%
▄ = 4px = 37.5-50%
▃ = 3px = 25-37.5%
▂ = 2px = 12.5-25%
▁ = 1px = 0-12.5%
```

### 2x Scale (32×16 pixels)

```
CCPPUU::  ▁▁▂▂▄▄██▆▆▃▃▁▁▂▂  4455%%
        ││││││████││││││││
        ││││████████││││││
        ││████████████││││
        ████████████████││

Each bar is 2px wide at 2x scale
Spacing maintained for clarity
```

### 3x Scale with Grid (48×24 pixels)

```
CCCPPPUUU:::  ▁▁▁▂▂▂▄▄▄███▆▆▆▃▃▃▁▁▁▂▂▂  444555%%%
           ┊┊┊┊┊┊█████████┊┊┊┊┊┊┊┊┊
           ┊┊┊┊┊┊█████████┊┊┊┊┊┊┊┊┊
           ┊┊┊┊┊┊█████████┊┊┊┊┊┊┊┊┊
           ┊┊┊┊███████████████┊┊┊┊┊┊
           ┊┊┊┊███████████████┊┊┊┊┊┊
           ┊┊┊┊███████████████┊┊┊┊┊┊
           ┊┊┊█████████████████████┊┊┊
           ┊┊┊█████████████████████┊┊┊
           ┊┊┊█████████████████████┊┊┊
           ┊┊┊█████████████████████┊┊┊
           ┊┊┊█████████████████████┊┊┊
           ┊┊┊█████████████████████┊┊┊
           ┊███████████████████████████
           ┊███████████████████████████
           ┊███████████████████████████
           █████████████████████████████
           █████████████████████████████
           █████████████████████████████

Grid lines (┊) in Light Gray (13)
Bars in appropriate status colors
```

## Dashboard Sparkline Array

### Base Resolution (80×32 pixels)

```
┌────────────────────────────────────────────────────────────────────────────┐
│ System Overview - Last 24 Hours                                            │
├────────────────────────────────────────────────────────────────────────────┤
│ CPU ▁▂▄▅▇█▇▅▄▃▂▁▁▂▃▄▅▆▇▆▅▄▃▂▁▂▃▄▅▆▇█▇▆▅▄▃▂▁▁▂▃▄ 65% avg              │
│ MEM ▄▄▄▄▄▅▅▅▅▆▆▆▇▇▇▇███▇▇▆▆▅▅▅▅▆▆▇▇███████▇▇▆▅▄ 78% avg              │
│ NET ▁▁▁▂▃▄▅▆▇▆▅▄▃▂▁▁▁▁▂▂▃▃▂▁▁▂▃▄▅▆▇█▇▆▅▄▃▂▁▁▁▁▂ 35% avg              │
│ DSK ▂▂▂▂▂▂▂▂▂▂▂▂▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▄ 42% avg              │
└────────────────────────────────────────────────────────────────────────────┘

48 data points per metric (30-minute intervals)
Color coding based on thresholds
```

### 2x Scale Dashboard (160×64 pixels)

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  SSyysstteemm  OOvveerrvviieeww  --  LLaasstt  2244  HHoouurrss                                                                                                │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  CCPPUU  ▁▁▂▂▄▄▅▅▇▇██▇▇▅▅▄▄▃▃▂▂▁▁▁▁▂▂▃▃▄▄▅▅▆▆▇▇▆▆▅▅▄▄▃▃▂▂▁▁▂▂▃▃▄▄▅▅▆▆▇▇██▇▇▆▆▅▅▄▄▃▃▂▂▁▁▁▁▂▂▃▃▄▄  6655%%  aavvgg                      │
│                                                                                                                                                                │
│  MMEEMM  ▄▄▄▄▄▄▄▄▅▅▅▅▅▅▅▅▆▆▆▆▆▆▆▆▇▇▇▇▇▇▇▇████████▇▇▇▇▆▆▆▆▅▅▅▅▅▅▅▅▆▆▆▆▇▇▇▇████████████████▇▇▇▇▆▆▅▅▄▄  7788%%  aavvgg                      │
│                                                                                                                                                                │
│  NNEETT  ▁▁▁▁▁▁▂▂▃▃▄▄▅▅▆▆▇▇▆▆▅▅▄▄▃▃▂▂▁▁▁▁▁▁▁▁▂▂▂▂▃▃▃▃▂▂▁▁▁▁▂▂▃▃▄▄▅▅▆▆▇▇██▇▇▆▆▅▅▄▄▃▃▂▂▁▁▁▁▁▁▁▁▂▂  3355%%  aavvgg                      │
│                                                                                                                                                                │
│  DDSSKK  ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▄▄  4422%%  aavvgg                      │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Micro Sparklines (Embedded in Tables)

### Base Resolution in Status Table

```
┌─────────────┬────────┬──────────┬──────────┐
│ Server      │ Status │ CPU      │ Memory   │
├─────────────┼────────┼──────────┼──────────┤
│ web-01      │ ● OK   │ ▂▃▄▅▆▅▄▃ │ ▄▄▅▅▅▅▄▄ │
│ web-02      │ ● OK   │ ▁▂▃▄▃▂▁▁ │ ▅▅▆▆▆▆▅▅ │
│ db-master   │ ● WARN │ ▄▅▆▇██▇▆ │ ▆▇▇█████ │
│ cache-01    │ ● OK   │ ▂▂▃▃▂▂▂▂ │ ▃▃▃▃▃▃▃▃ │
└─────────────┴────────┴──────────┴──────────┘

8×8 pixel sparklines embedded in cells
Status dot + 8-point trend visualization
```

## Color-Coded Sparklines

### Threshold-Based Coloring

```
Normal (Green #6):     ▁▂▃▄▃▂▁▁
Warning (Yellow #4):   ▄▅▆▆▅▅▄▄
Critical (Red #2):     ▆▇███▇▆▅

Color changes based on value thresholds:
< 60% = Green
60-80% = Yellow  
> 80% = Red
```

### Multi-Color Sparkline (showing state changes)

```
Mixed states in one sparkline:
▁▂▃▄▅▆▇█  (gradient from green to red)
████████  Green section
████████  Yellow section
████████  Red section
```

## Animated Sparklines

### Sliding Window Animation

```
Frame 1: ▁▂▄▅▇▆▄▂│ (newest data)
Frame 2: ▂▄▅▇▆▄▂▃│
Frame 3: ▄▅▇▆▄▂▃▄│
Frame 4: ▅▇▆▄▂▃▄▅│

Slide left as new data arrives
Vertical line indicates current time
```

### Pulse Effect for Live Data

```
Normal:    ▁▂▃▄▅▆▇█
Pulse 1:   ▁▂▃▄▅▆▇█░  (fade in new point)
Pulse 2:   ▁▂▃▄▅▆▇█▓  (half brightness)
Pulse 3:   ▁▂▃▄▅▆▇██  (full brightness)

New data points pulse to show updates
```

## Implementation Details

### Sparkline Rendering Algorithm

```rust
fn render_sparkline(
    data: &[f32],
    x: u16,
    y: u16,
    width: u16,
    height: u16,
    color: u8,
) {
    let points_per_pixel = data.len() / width as usize;
    let max_val = data.iter().max();
    
    for i in 0..width {
        // Average multiple data points if needed
        let start = i as usize * points_per_pixel;
        let end = ((i + 1) as usize * points_per_pixel).min(data.len());
        let avg = average(&data[start..end]);
        
        // Map to height
        let bar_height = ((avg / max_val) * height as f32) as u16;
        
        // Draw vertical bar
        for j in 0..bar_height {
            plot_pixel(x + i, y + height - j - 1, color);
        }
    }
}
```

### Unicode Block Mapping

```
Height → Unicode Block Character
8/8 → █ (U+2588)
7/8 → ▇ (U+2587)
6/8 → ▆ (U+2586)
5/8 → ▅ (U+2585)
4/8 → ▄ (U+2584)
3/8 → ▃ (U+2583)
2/8 → ▂ (U+2582)
1/8 → ▁ (U+2581)
0/8 → (space)
```

### Memory-Efficient Storage

```rust
// Store sparkline as packed bytes
struct CompactSparkline {
    data: Vec<u8>,  // 3 bits per value (0-7)
    length: u8,     // Number of data points
}

impl CompactSparkline {
    fn get_value(&self, index: usize) -> u8 {
        // Extract 3-bit value from packed array
        let byte_index = (index * 3) / 8;
        let bit_offset = (index * 3) % 8;
        
        if bit_offset <= 5 {
            (self.data[byte_index] >> bit_offset) & 0b111
        } else {
            // Value spans two bytes
            let low = self.data[byte_index] >> bit_offset;
            let high = self.data[byte_index + 1] << (8 - bit_offset);
            (low | high) & 0b111
        }
    }
}
```

## Best Practices

1. **Data Density**: Show 8-24 data points for readability
2. **Update Frequency**: Refresh every 30-60 seconds for live data
3. **Color Usage**: Use color to indicate status, not just decoration
4. **Scaling**: Maintain 1:1 aspect ratio for each data point
5. **Context**: Always show current value alongside sparkline

## Summary

Sparklines provide dense, efficient visualization of trends in minimal space. When rendered with pixel-perfect precision using the SWEETIE-16 palette, they maintain both functionality and retro aesthetic charm.
