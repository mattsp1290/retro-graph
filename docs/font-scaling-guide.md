# Pixel Font Scaling Guide

## Introduction

This guide details the implementation and scaling strategies for bitmap fonts in the retro-graph system. Following TIC-80's philosophy of deliberate constraints, we use simple pixel fonts that scale perfectly at integer multiples while maintaining absolute clarity.

## Font Specifications

### Primary Font: 3x5 Pixels

The workhorse font for compact displays and data labels.

#### Character Set Definition
```
A: ·█·    B: ██·    C: ·██    D: ██·    E: ███
   █·█       █·█       █··       █·█       █··
   ███       ██·       █··       █·█       ██·
   █·█       █·█       █··       █·█       █··
   █·█       ██·       ·██       ██·       ███

F: ███    G: ·██    H: █·█    I: ███    J: ··█
   █··       █··       █·█       ·█·       ··█
   ██·       █·█       ███       ·█·       ··█
   █··       █·█       █·█       ·█·       █·█
   █··       ·██       █·█       ███       ·█·
```

#### Numeric Characters
```
0: ·█·    1: ·█·    2: ██·    3: ██·    4: █·█
   █·█       ██·       ··█       ··█       █·█
   █·█       ·█·       ·█·       ·█·       ███
   █·█       ·█·       █··       ··█       ··█
   ·█·       ███       ███       ██·       ··█
```

#### Scaling Properties
- **Base size**: 3x5 pixels per character
- **Character spacing**: 1 pixel
- **Line height**: 6 pixels (5 + 1)
- **Effective character width**: 4 pixels (3 + 1 spacing)

### Secondary Font: 5x7 Pixels

For headers and improved readability at larger sizes.

#### Sample Characters
```
A: ··█··    B: ████·    C: ·███·
   ·█·█·       █···█       █···█
   █···█       █···█       █····
   █···█       ████·       █····
   █████       █···█       █····
   █···█       █···█       █···█
   █···█       ████·       ·███·
```

#### Scaling Properties
- **Base size**: 5x7 pixels per character
- **Character spacing**: 1 pixel  
- **Line height**: 9 pixels (7 + 2)
- **Effective character width**: 6 pixels (5 + 1 spacing)

## Scaling Strategies

### Integer Scaling Table

| Base Font | Scale | Result Size | Use Case |
|-----------|-------|-------------|----------|
| 3x5 | 2x | 6x10 | Small displays, tooltips |
| 3x5 | 3x | 9x15 | Standard UI text |
| 3x5 | 4x | 12x20 | Large displays, headers |
| 5x7 | 2x | 10x14 | Readable body text |
| 5x7 | 3x | 15x21 | Large headers |
| 5x7 | 4x | 20x28 | Display titles |

### Implementation Algorithm

```rust
pub struct PixelFont {
    glyphs: HashMap<char, Vec<u8>>,
    width: u8,
    height: u8,
}

impl PixelFont {
    pub fn render_scaled(
        &self,
        text: &str,
        scale: u8,
        color_index: u8,
        buffer: &mut [u8],
        buffer_width: usize,
        x: usize,
        y: usize,
    ) {
        let mut cursor_x = x;
        
        for ch in text.chars() {
            if let Some(glyph) = self.glyphs.get(&ch) {
                self.render_glyph_scaled(
                    glyph,
                    scale,
                    color_index,
                    buffer,
                    buffer_width,
                    cursor_x,
                    y,
                );
                cursor_x += (self.width + 1) as usize * scale as usize;
            }
        }
    }
    
    fn render_glyph_scaled(
        &self,
        glyph: &[u8],
        scale: u8,
        color_index: u8,
        buffer: &mut [u8],
        buffer_width: usize,
        x: usize,
        y: usize,
    ) {
        for gy in 0..self.height {
            for gx in 0..self.width {
                let bit_index = gy * self.width + gx;
                let byte_index = bit_index / 8;
                let bit_offset = bit_index % 8;
                
                if glyph[byte_index as usize] & (1 << bit_offset) != 0 {
                    // Render scaled pixel
                    for sy in 0..scale {
                        for sx in 0..scale {
                            let px = x + (gx as usize * scale as usize) + sx as usize;
                            let py = y + (gy as usize * scale as usize) + sy as usize;
                            let idx = (py * buffer_width + px) * 4;
                            
                            // Set pixel using TIC-80 SWEETIE-16 palette
                            set_pixel_from_palette(
                                &mut buffer[idx..idx + 4],
                                color_index
                            );
                        }
                    }
                }
            }
        }
    }
}
```

## Font Data Storage

### Compact Binary Format

Store font data efficiently using bit packing:

```rust
// 3x5 font = 15 bits per character
// Pack into 2 bytes (16 bits) with 1 unused bit
const FONT_3X5: [(char, u16); 95] = [
    ('A', 0b010101111101101),  // ·█·█·████·█·█
    ('B', 0b110101110101110),  // ██·█·███·█·███·
    ('C', 0b011100100100011),  // ·███··█··█···██
    // ... etc
];

// 5x7 font = 35 bits per character  
// Pack into 5 bytes (40 bits) with 5 unused bits
const FONT_5X7: [(char, [u8; 5]); 95] = [
    ('A', [0x04, 0x0A, 0x11, 0x1F, 0x11]), // ··█··/·█·█·/█···█/█████/█···█
    // ... etc
];
```

## Kerning and Spacing

### Fixed-Width Simplicity
- All characters occupy same horizontal space
- Spacing is consistent and predictable
- No kerning pairs needed

### Spacing Rules
```
Character spacing = 1 pixel (at base scale)
Word spacing = 3 pixels (at base scale)
Line spacing = 1-2 pixels (at base scale)
```

### Monospace Grid Alignment
```
Text:  H E L L O   W O R L D
Grid:  ████·████·████·████·████···████·████·████·████·████
       3+1  3+1  3+1  3+1  3+1   3+1  3+1  3+1  3+1  3+1
```

## Special Characters

### Essential ASCII Subset
Focus on characters needed for monitoring:
- A-Z (uppercase only for 3x5)
- 0-9 (numerics)
- Common punctuation: . , : ; ! ? - + = / \ ( ) [ ] { }
- Special: % @ # $ & * < > | ~ ` ' "

### Graph-Specific Symbols
```
↑: ·█·    ↓: ·█·    →: ···    ←: ···    •: ···
   ███       ███       █··       ··█       ·█·
   ·█·       ·█·       ███       ███       ·█·
   ·█·       ·█·       █··       ··█       ···
   ···       ·█·       ···       ···       ···
```

## Rendering Optimizations

### Pre-Scaled Font Cache
```rust
pub struct FontCache {
    fonts: HashMap<(FontSize, Scale), PreScaledFont>,
}

impl FontCache {
    pub fn get_or_create(&mut self, size: FontSize, scale: u8) -> &PreScaledFont {
        self.fonts.entry((size, scale))
            .or_insert_with(|| PreScaledFont::new(size, scale))
    }
}
```

### Batch Text Rendering
```rust
pub struct TextBatch {
    commands: Vec<TextCommand>,
}

struct TextCommand {
    text: String,
    x: u16,
    y: u16,
    color: u8,
    font: FontSize,
    scale: u8,
}

impl TextBatch {
    pub fn render_all(&self, buffer: &mut [u8], width: usize) {
        for cmd in &self.commands {
            // Render each text command
        }
    }
}
```

## Shadow and Outline Effects

### Simple Drop Shadow
```rust
// Render shadow first (offset by 1 scaled pixel)
render_text(text, x + scale, y + scale, DARK_GRAY, scale);
// Then render text on top
render_text(text, x, y, color, scale);
```

### Pixel-Perfect Outline
```
Original:  ·█·     With outline:  ███
           █·█                    █·█
           ███                    ███
           █·█                    █·█
           █·█                    █·█
```

## Performance Considerations

### Memory Usage
```
3x5 font: 95 chars × 2 bytes = 190 bytes
5x7 font: 95 chars × 5 bytes = 475 bytes
Total base fonts: < 1KB

Pre-scaled cache (3x5 at 2x, 3x, 4x): ~2KB
Pre-scaled cache (5x7 at 2x, 3x, 4x): ~6KB
```

### Rendering Speed
- Pre-scaled fonts: ~10x faster than runtime scaling
- Bit manipulation: Use lookup tables for bit extraction
- SIMD: Vectorize pixel copying where possible

## Integration Examples

### Graph Labels
```rust
// Y-axis labels (right-aligned)
for (i, label) in labels.iter().enumerate() {
    let y = graph_top + (i * spacing);
    render_text_right_aligned(label, margin_left - 2, y, FONT_3X5, 2);
}

// X-axis labels (centered)
for (i, label) in time_labels.iter().enumerate() {
    let x = graph_left + (i * column_width) + (column_width / 2);
    render_text_centered(label, x, graph_bottom + 2, FONT_3X5, 2);
}
```

### Status Display
```rust
// Host status matrix
render_text("HOSTNAME", x, y, FONT_5X7, 2);
for (i, host) in hosts.iter().enumerate() {
    let row_y = y + header_height + (i * row_height);
    render_text(&host.name, x, row_y, FONT_3X5, 3);
}
```

## Font Design Guidelines

### Readability Rules
1. Minimum 1 pixel between strokes
2. Consistent stroke width (1 pixel)
3. Clear differentiation between similar chars (0/O, 1/I/l)
4. Avoid diagonal lines in 3x5 (except necessary)

### TIC-80 Aesthetic Alignment
- Simple, geometric shapes
- No unnecessary decoration
- Function over form
- Clarity at smallest size

## Testing and Validation

### Test Patterns
```
// All characters at each scale
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
!@#$%^&*()_+-=[]{}|;':",./<>?

// Common monitoring text
CPU: 45.2%
MEM: 1.2GB/4.0GB
NET: ↓152KB/s ↑48KB/s
DISK: 85% USED
STATUS: ●GREEN ●YELLOW ●RED
```

### Validation Checklist
- [ ] All ASCII characters render correctly
- [ ] Scaling maintains pixel alignment
- [ ] Text remains readable at all scales
- [ ] Performance meets targets (<1ms per frame)
- [ ] Memory usage within bounds
- [ ] Special characters display properly

## Conclusion

Pixel fonts are fundamental to retro-graph's aesthetic. By constraining ourselves to simple, scalable bitmap fonts and implementing them efficiently, we achieve both authentic retro appearance and modern performance. The key is embracing the grid, using only integer scaling, and ensuring every pixel serves a purpose.
