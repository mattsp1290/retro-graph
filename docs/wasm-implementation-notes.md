# WebAssembly Implementation Notes

## Overview

This document outlines technical considerations for implementing retro-graph's pixel-perfect rendering system as WebAssembly components. The focus is on achieving optimal performance while maintaining the aesthetic constraints of TIC-80's SWEETIE-16 palette and pixelated graphics.

## Architecture Overview

### Component Structure
```
retro-graph/
├── core/
│   ├── pixel-renderer/      # Base pixel manipulation
│   ├── palette/            # TIC-80 SWEETIE-16 color management
│   ├── font-renderer/      # Bitmap font rendering
│   └── scaler/            # Integer scaling engine
├── graphs/
│   ├── line-graph/        # MRTG-style line graphs
│   ├── status-matrix/     # Big Brother-style status grids
│   └── bar-chart/         # Simple bar charts
└── adapters/
    ├── hugo/              # Hugo shortcode integration
    ├── spin/              # Fermyon Spin adapter
    └── browser/           # Direct browser usage
```

## Memory Management

### Pixel Buffer Layout
```rust
// Flat RGBA buffer for efficient manipulation
pub struct PixelBuffer {
    width: u32,
    height: u32,
    pixels: Vec<u8>, // width * height * 4 bytes
}

impl PixelBuffer {
    pub fn new(width: u32, height: u32) -> Self {
        Self {
            width,
            height,
            pixels: vec![0; (width * height * 4) as usize],
        }
    }
    
    #[inline(always)]
    pub fn set_pixel(&mut self, x: u32, y: u32, color: u8) {
        let idx = ((y * self.width + x) * 4) as usize;
        let rgba = SWEETIE16_PALETTE[color as usize];
        self.pixels[idx..idx + 4].copy_from_slice(&rgba);
    }
}
```

### TIC-80 SWEETIE-16 Palette as Constants
```rust
// Store palette as compile-time constants for zero-overhead access
const SWEETIE16_PALETTE: [[u8; 4]; 16] = [
    [0x1a, 0x1c, 0x2c, 0xFF], // 0: Black
    [0x5d, 0x27, 0x5d, 0xFF], // 1: Purple
    [0xb1, 0x3e, 0x53, 0xFF], // 2: Red
    [0xef, 0x7d, 0x57, 0xFF], // 3: Orange
    [0xff, 0xcd, 0x75, 0xFF], // 4: Yellow
    [0xa7, 0xf0, 0x70, 0xFF], // 5: Lime
    [0x38, 0xb7, 0x64, 0xFF], // 6: Green
    [0x25, 0x71, 0x79, 0xFF], // 7: Dark Cyan
    [0x29, 0x36, 0x6f, 0xFF], // 8: Dark Blue
    [0x3b, 0x5d, 0xc9, 0xFF], // 9: Blue
    [0x41, 0xa6, 0xf6, 0xFF], // 10: Light Blue
    [0x73, 0xef, 0xf7, 0xFF], // 11: Cyan
    [0xf4, 0xf4, 0xf4, 0xFF], // 12: White
    [0x94, 0xb0, 0xc2, 0xFF], // 13: Light Gray
    [0x56, 0x6c, 0x86, 0xFF], // 14: Gray
    [0x33, 0x3c, 0x57, 0xFF], // 15: Dark Gray
];
```

## Performance Optimizations

### Integer-Only Arithmetic
```rust
// All calculations use integers to avoid floating-point overhead
pub fn draw_line(buffer: &mut PixelBuffer, x0: i32, y0: i32, x1: i32, y1: i32, color: u8) {
    // Bresenham's line algorithm - integer only
    let dx = (x1 - x0).abs();
    let dy = (y1 - y0).abs();
    let sx = if x0 < x1 { 1 } else { -1 };
    let sy = if y0 < y1 { 1 } else { -1 };
    let mut err = dx - dy;
    let mut x = x0;
    let mut y = y0;
    
    loop {
        buffer.set_pixel(x as u32, y as u32, color);
        
        if x == x1 && y == y1 { break; }
        
        let e2 = 2 * err;
        if e2 > -dy {
            err -= dy;
            x += sx;
        }
        if e2 < dx {
            err += dx;
            y += sy;
        }
    }
}
```

### Efficient Scaling
```rust
// Optimized nearest-neighbor scaling using memory copies
#[inline(always)]
pub fn scale_pixel_block(
    src: &[u8],
    dst: &mut [u8],
    src_stride: usize,
    dst_stride: usize,
    scale: usize,
) {
    // Copy first scaled row
    for x in 0..scale {
        dst[x * 4..x * 4 + 4].copy_from_slice(src);
    }
    
    // Copy first row to remaining rows
    for y in 1..scale {
        let src_offset = 0;
        let dst_offset = y * dst_stride * 4;
        dst[dst_offset..dst_offset + scale * 4]
            .copy_from_slice(&dst[src_offset..src_offset + scale * 4]);
    }
}
```

### Batch Operations
```rust
// Process multiple pixels at once when possible
pub fn fill_rect(buffer: &mut PixelBuffer, x: u32, y: u32, w: u32, h: u32, color: u8) {
    let rgba = SWEETIE16_PALETTE[color as usize];
    let row_size = (w * 4) as usize;
    let mut row = vec![0u8; row_size];
    
    // Fill one row
    for i in 0..w {
        let offset = (i * 4) as usize;
        row[offset..offset + 4].copy_from_slice(&rgba);
    }
    
    // Copy row to all rows in rectangle
    for dy in 0..h {
        let y_offset = ((y + dy) * buffer.width * 4) as usize;
        let x_offset = (x * 4) as usize;
        let dst_start = y_offset + x_offset;
        buffer.pixels[dst_start..dst_start + row_size].copy_from_slice(&row);
    }
}
```

## WebAssembly Interface Types (WIT)

### Core Renderer Interface
```wit
interface pixel-renderer {
    record color {
        index: u8,
    }
    
    record point {
        x: u32,
        y: u32,
    }
    
    record rect {
        x: u32,
        y: u32,
        width: u32,
        height: u32,
    }
    
    create-buffer: func(width: u32, height: u32) -> buffer-handle
    set-pixel: func(buffer: buffer-handle, pos: point, color: color)
    draw-line: func(buffer: buffer-handle, from: point, to: point, color: color)
    fill-rect: func(buffer: buffer-handle, area: rect, color: color)
    get-pixels: func(buffer: buffer-handle) -> list<u8>
}
```

### Graph Component Interface
```wit
interface line-graph {
    record graph-config {
        width: u32,
        height: u32,
        time-range: time-range-type,
        show-grid: bool,
        grid-color: u8,
        background-color: u8,
    }
    
    record data-point {
        timestamp: u64,
        value: f32,
    }
    
    variant time-range-type {
        minutes(u32),
        hours(u32),
        days(u32),
    }
    
    create-graph: func(config: graph-config) -> graph-handle
    add-series: func(graph: graph-handle, name: string, color: u8)
    update-data: func(graph: graph-handle, series: string, data: list<data-point>)
    render: func(graph: graph-handle, scale: u8) -> list<u8>
}
```

## Binary Size Optimization

### Compile Flags
```toml
[profile.release]
opt-level = "z"          # Optimize for size
lto = true              # Link-time optimization
codegen-units = 1       # Single codegen unit
strip = true            # Strip symbols
panic = "abort"         # No unwinding

[dependencies]
# Use no_std where possible
```

### Code Strategies
```rust
// Use const generics to eliminate runtime checks
pub struct ScaledRenderer<const SCALE: usize> {
    base_width: u32,
    base_height: u32,
}

impl<const SCALE: usize> ScaledRenderer<SCALE> {
    pub fn render_pixel(&mut self, x: u32, y: u32, color: u8, buffer: &mut [u8]) {
        // Compiler can optimize away the loop for known SCALE
        for dy in 0..SCALE {
            for dx in 0..SCALE {
                let px = x * SCALE as u32 + dx as u32;
                let py = y * SCALE as u32 + dy as u32;
                // ... set pixel
            }
        }
    }
}
```

## Integration Patterns

### Hugo Adapter
```javascript
// JavaScript bridge for Hugo shortcodes
async function loadRetrograph() {
    const module = await WebAssembly.instantiateStreaming(
        fetch('/wasm/retro-graph.wasm')
    );
    
    return {
        createGraph: (config) => {
            const ptr = module.exports.create_graph(
                config.width,
                config.height,
                config.timeRange,
                config.showGrid
            );
            return new GraphHandle(module, ptr);
        }
    };
}

// Hugo shortcode: {{< retro-graph type="line" data="metrics.json" >}}
```

### Fermyon Spin Adapter
```rust
use spin_sdk::http::{Request, Response};

#[spin_sdk::http_component]
fn handle_graph_request(req: Request) -> Result<Response> {
    let config = parse_config(&req)?;
    let data = fetch_metrics(&config)?;
    
    let mut graph = LineGraph::new(config);
    graph.update_data(data);
    
    let pixels = graph.render(determine_scale(&req));
    let png = encode_png(&pixels, graph.width(), graph.height());
    
    Ok(Response::builder()
        .status(200)
        .header("content-type", "image/png")
        .body(Some(png.into()))?)
}
```

## Memory Layout Optimization

### Structure Packing
```rust
#[repr(C)]
pub struct GraphData {
    // Group by size to minimize padding
    timestamps: Vec<u64>,    // 8-byte aligned
    values: Vec<f32>,       // 4-byte aligned
    width: u32,             // 4-byte aligned
    height: u32,            // 4-byte aligned
    colors: Vec<u8>,        // 1-byte aligned
    flags: u8,              // 1-byte aligned
}
```

### Cache-Friendly Access
```rust
// Process data in cache-friendly order
pub fn render_graph_data(data: &GraphData, buffer: &mut PixelBuffer) {
    // Process by rows to maximize cache hits
    for y in 0..data.height {
        for x in 0..data.width {
            // Process pixel
        }
    }
}
```

## Error Handling

### No Panics Policy
```rust
// Use Result types everywhere
pub fn safe_set_pixel(
    buffer: &mut PixelBuffer,
    x: u32,
    y: u32,
    color: u8
) -> Result<(), PixelError> {
    if x >= buffer.width || y >= buffer.height {
        return Err(PixelError::OutOfBounds);
    }
    if color >= 16 {
        return Err(PixelError::InvalidColor);
    }
    
    buffer.set_pixel(x, y, color);
    Ok(())
}
```

## Testing in WASM Environment

### Unit Tests
```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_pixel_scaling() {
        let mut buffer = PixelBuffer::new(2, 2);
        buffer.set_pixel(0, 0, 2); // Red pixel
        
        let scaled = scale_buffer(&buffer, 2);
        assert_eq!(scaled.width, 4);
        assert_eq!(scaled.height, 4);
        
        // Check all 4 pixels are red
        for y in 0..2 {
            for x in 0..2 {
                let idx = ((y * 4 + x) * 4) as usize;
                assert_eq!(&scaled.pixels[idx..idx + 4], &SWEETIE16_PALETTE[2]);
            }
        }
    }
}
```

### Integration Tests
```javascript
// Test from JavaScript side
describe('Retro Graph WASM', () => {
    it('should render line graph', async () => {
        const retro = await loadRetrograph();
        const graph = retro.createGraph({
            width: 320,
            height: 180,
            timeRange: 'hour',
            showGrid: true
        });
        
        graph.addSeries('cpu', 6); // Green
        graph.updateData('cpu', testData);
        
        const pixels = graph.render(2); // 2x scale
        expect(pixels.length).toBe(320 * 180 * 4 * 4); // RGBA * scale²
    });
});
```

## Deployment Considerations

### File Size Targets
- Core renderer: < 50KB
- Font renderer: < 20KB
- Graph components: < 30KB each
- Total bundle: < 150KB

### Loading Strategy
```javascript
// Lazy load components as needed
const components = {
    line: () => import('./line-graph.wasm'),
    matrix: () => import('./status-matrix.wasm'),
    bar: () => import('./bar-chart.wasm')
};

async function createGraph(type, config) {
    const module = await components[type]();
    return module.create(config);
}
```

## Future Optimizations

### SIMD Support
When available, use SIMD for parallel pixel operations:
```rust
#[cfg(target_feature = "simd128")]
pub fn fill_rect_simd(buffer: &mut PixelBuffer, rect: Rect, color: u8) {
    // Use v128 operations for 4 pixels at once
}
```

### Shared Memory
For real-time updates:
```rust
// Use SharedArrayBuffer when available
pub fn create_shared_buffer(width: u32, height: u32) -> SharedPixelBuffer {
    // Implementation for shared memory between WASM and JS
}
```

## Conclusion

These implementation notes provide a foundation for building high-performance, pixel-perfect WebAssembly components. The key principles are:

1. Integer-only arithmetic for speed
2. Const arrays for palette data
3. Efficient memory layout
4. Minimal allocations
5. Cache-friendly algorithms
6. No runtime panics

By following these guidelines, retro-graph can deliver authentic retro aesthetics with modern performance.
