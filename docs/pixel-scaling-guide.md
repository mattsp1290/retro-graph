# Pixel Scaling Guide for Modern Displays

## Overview

This guide provides detailed strategies for scaling pixelated graphics from retro-graph's base resolution to modern displays while maintaining perfect pixel alignment and authentic retro aesthetics.

## Core Principle: Integer Scaling Only

The fundamental rule of pixel-perfect scaling is to use only integer multiples. This ensures each source pixel becomes a perfect square of pixels at the target resolution, with no blurring or artifacts.

## Base Resolution Design

### TIC-80 Native: 240x136
- **Why this resolution**: TIC-80's native resolution
- **Aspect ratio**: Close to 16:9 (1.76:1)
- **Flexibility**: Scales well to modern displays with integer multiples

### Recommended Scaling Strategy
- **For 1080p**: Use 7x scale (1680x952) with letterboxing
- **For 1440p**: Use 10x scale (2400x1360) with letterboxing
- **For 4K**: Use 15x scale (3600x2040) with letterboxing

### Alternative Base (for full coverage)
- **640x360**: Perfect 16:9 for modern displays
- **480x270**: Middle ground option
- **320x180**: Lower resolution option

## Scaling Factors by Display

### 1920x1080 (Full HD)
| Base Resolution | Scale Factor | Result | Coverage |
|----------------|--------------|---------|----------|
| 240x136 (TIC-80) | 7x | 1680x952 | 81.5% |
| 240x136 (TIC-80) | 8x | 1920x1088 | 100% height |
| 640x360 | 3x | 1920x1080 | 100% |
| 480x270 | 4x | 1920x1080 | 100% |

### 2560x1440 (QHD)
| Base Resolution | Scale Factor | Result | Coverage |
|----------------|--------------|---------|----------|
| 240x136 (TIC-80) | 10x | 2400x1360 | 91.1% |
| 640x360 | 4x | 2560x1440 | 100% |
| 480x270 | 5x | 2400x1350 | 87.9% |

### 3840x2160 (4K UHD)
| Base Resolution | Scale Factor | Result | Coverage |
|----------------|--------------|---------|----------|
| 240x136 (TIC-80) | 15x | 3600x2040 | 89.8% |
| 240x136 (TIC-80) | 16x | 3840x2176 | 100% width |
| 640x360 | 6x | 3840x2160 | 100% |
| 480x270 | 8x | 3840x2160 | 100% |

## Implementation Strategies

### 1. Nearest-Neighbor Scaling

The only acceptable scaling algorithm for pixel art:

```rust
fn scale_buffer(
    src: &[u8],
    src_width: usize,
    src_height: usize,
    scale: usize,
) -> Vec<u8> {
    let dst_width = src_width * scale;
    let dst_height = src_height * scale;
    let mut dst = vec![0u8; dst_width * dst_height * 4];
    
    for y in 0..src_height {
        for x in 0..src_width {
            let src_idx = (y * src_width + x) * 4;
            let pixel = &src[src_idx..src_idx + 4];
            
            // Copy pixel to scaled grid
            for dy in 0..scale {
                for dx in 0..scale {
                    let dst_x = x * scale + dx;
                    let dst_y = y * scale + dy;
                    let dst_idx = (dst_y * dst_width + dst_x) * 4;
                    dst[dst_idx..dst_idx + 4].copy_from_slice(pixel);
                }
            }
        }
    }
    
    dst
}
```

### 2. WebAssembly Optimization

For performance, implement scaling in WASM:

```rust
#[wasm_bindgen]
pub struct PixelScaler {
    scale: usize,
    src_width: usize,
    src_height: usize,
}

#[wasm_bindgen]
impl PixelScaler {
    pub fn new(src_width: usize, src_height: usize, scale: usize) -> Self {
        Self { scale, src_width, src_height }
    }
    
    pub fn scale(&self, src: &[u8]) -> Vec<u8> {
        // Optimized scaling with SIMD where available
        scale_buffer(src, self.src_width, self.src_height, self.scale)
    }
}
```

### 3. Canvas Rendering (Browser)

Configure canvas for pixel-perfect rendering:

```javascript
// Disable smoothing
ctx.imageSmoothingEnabled = false;
ctx.webkitImageSmoothingEnabled = false;
ctx.mozImageSmoothingEnabled = false;
ctx.msImageSmoothingEnabled = false;

// Set canvas size
canvas.width = baseWidth * scale;
canvas.height = baseHeight * scale;

// Apply CSS for crisp rendering
canvas.style.imageRendering = 'pixelated';
canvas.style.imageRendering = 'crisp-edges';
canvas.style.imageRendering = '-moz-crisp-edges';
```

## Handling Non-Integer Scales

When perfect scaling isn't possible:

### Option 1: Letterboxing
Center the scaled image with borders:

```rust
fn calculate_letterbox(
    screen_width: u32,
    screen_height: u32,
    base_width: u32,
    base_height: u32,
) -> (u32, u32, u32) {
    // Find largest integer scale that fits
    let scale_x = screen_width / base_width;
    let scale_y = screen_height / base_height;
    let scale = scale_x.min(scale_y);
    
    let scaled_width = base_width * scale;
    let scaled_height = base_height * scale;
    
    let offset_x = (screen_width - scaled_width) / 2;
    let offset_y = (screen_height - scaled_height) / 2;
    
    (scale, offset_x, offset_y)
}
```

### Option 2: Viewport Adjustment
Render more or less content to fill screen:

```rust
fn adjust_viewport(
    screen_width: u32,
    screen_height: u32,
    preferred_scale: u32,
) -> (u32, u32) {
    let viewport_width = screen_width / preferred_scale;
    let viewport_height = screen_height / preferred_scale;
    
    (viewport_width, viewport_height)
}
```

## Pixel Grid Alignment

### Subpixel Prevention
Always ensure coordinates are integers:

```rust
// Bad: Can cause blurring
let x = position * scale as f32;

// Good: Pixel-perfect positioning
let x = (position * scale) as i32;
```

### Grid Snapping for UI Elements
```rust
fn snap_to_grid(value: f32, grid_size: u32) -> u32 {
    ((value / grid_size as f32).round() * grid_size as f32) as u32
}
```

## Testing Methodology

### 1. Pattern Tests
Create test patterns to verify scaling:

```
1px checkerboard:
█ █ █ 
 █ █ █
█ █ █ 

Should remain crisp at all scales
```

### 2. Line Tests
Single pixel lines should scale uniformly:

```
Horizontal: ████████
Vertical:   █
            █
            █
Diagonal:   █
             █
              █
```

### 3. Text Rendering
Ensure fonts remain readable:
- 3x5 font at 3x scale = 9x15 pixels
- Each pixel should be a perfect square
- No interpolation artifacts

## Performance Considerations

### Memory Usage
```
TIC-80 Base: 240x136x4 = 130,560 bytes
7x scale: 1680x952x4 = 6,397,440 bytes
15x scale: 3600x2040x4 = 29,376,000 bytes

Alternative Base: 640x360x4 = 921,600 bytes
3x scale: 1920x1080x4 = 8,294,400 bytes
6x scale: 3840x2160x4 = 33,177,600 bytes
```

### Optimization Strategies
1. **Scale on GPU**: Use WebGL for scaling when possible
2. **Cache scaled sprites**: Pre-scale common elements
3. **Dirty rectangle**: Only scale changed regions
4. **Lower base resolution**: TIC-80's 240x136 for authentic retro graphics

## Platform-Specific Notes

### Web (Canvas/WebGL)
- Use `image-rendering: pixelated` CSS
- Disable all smoothing options
- Consider WebGL for better performance

### Native (SDL/Direct3D/Metal)
- Set texture filtering to "nearest"
- Use integer viewport scaling
- Disable multisampling

### WebAssembly
- Implement scaling in Rust for speed
- Use SIMD instructions where available
- Minimize memory allocations

## Common Pitfalls

### 1. Fractional Scaling
**Problem**: Using 1.5x or 2.5x scale
**Result**: Blurry pixels, uneven sizes
**Solution**: Always use integers

### 2. Misaligned Rendering
**Problem**: Drawing at fractional coordinates
**Result**: Pixel bleeding, artifacts
**Solution**: Round all positions

### 3. Mixed Resolutions
**Problem**: Combining different pixel sizes
**Result**: Inconsistent appearance
**Solution**: Use single base resolution

## Best Practices Checklist

- [ ] Choose base resolution that scales to target displays
- [ ] Use only integer scaling factors
- [ ] Disable all smoothing/interpolation
- [ ] Align all coordinates to pixel grid
- [ ] Test on actual target resolutions
- [ ] Profile performance at each scale
- [ ] Document supported resolutions
- [ ] Provide scaling options to users

## Conclusion

Pixel-perfect scaling is essential for maintaining the retro aesthetic of retro-graph. By following these guidelines and using only integer scaling with nearest-neighbor interpolation, we ensure every pixel remains crisp and deliberate at any display resolution.
