# Orthogonal Capacity

This program explores the geometric properties of high-dimensional spaces by:
1. Analyzing angular relationships between random unit vectors
2. Finding sets of nearly orthogonal vectors
3. Estimating theoretical bounds on orthogonal capacity

## Overview

The program operates in two phases:

### Phase 1: Random Vector Analysis
Generates random unit vectors in spaces of increasing dimensionality (2D, 3D, and powers of 2 up to 2¹⁶) and analyzes their angular relationships. For each dimension:
- Generates 1000 random unit vectors using Gaussian distribution
- Computes angles between all pairs (499,500 unique pairs)
- Provides statistical analysis of the angles
- Estimates theoretical maximum number of orthogonal vectors

### Phase 2: Orthogonal Vector Finding
Attempts to find sets of nearly orthogonal vectors in each dimension by:
- Generating random unit vectors one at a time
- Keeping vectors that are nearly orthogonal to all previous ones (90° ± 1°)
- Continuing until 100 consecutive failures to find a new orthogonal vector

## Features

- Phase 1: Random Vector Analysis
  - Uniform sampling on N-dimensional unit sphere
  - Comprehensive angle statistics (min, max, mean, std, median)
  - Performance timing for each dimension
  - Theoretical bounds on orthogonal capacity:
    - Exact values for small dimensions
    - Approximate (10^n) for large dimensions

- Phase 2: Orthogonal Vector Finding
  - Incremental orthogonal set construction
  - Configurable orthogonality tolerance
  - Adaptive stopping criterion
  - Progress reporting for large sets

## Requirements

- Python 3.x
- NumPy
- Python standard library (itertools, time, math)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/orthogonal-capacity.git
cd orthogonal-capacity
```

2. Install required dependencies:
```bash
pip install numpy
```

## Usage

Run the program using:
```bash
python main.py
```

### Example Output
```
Phase 1: Analyzing 1000 random vectors (499500 unique pairs) per dimension

Dim     Min    Max    Mean±Std    Median   Time(ms)   Upper Bound(±1.0°)
--------------------------------------------------------------------------
    2   0.1  179.9   90.0±52.0    90.0      5.2                  2
    3   8.2  171.8   90.0±41.8    90.0     10.1                  4
    4  25.3  154.7   90.0±29.6    90.0     20.3                  8
    8  42.1  137.9   90.0±20.9    90.0     40.6                128
   16  42.1  137.9   90.0±20.9    90.0     40.6              32768
   32  42.1  137.9   90.0±20.9    90.0     40.6              ~10^9
   64  42.1  137.9   90.0±20.9    90.0     40.6             ~10^18
  ...

Phase 2: Finding nearly orthogonal vectors (±1.0° from 90°, max 100 attempts)

Dim    Found
------------
    2      2
    3      3
    4      5
  ...
```

## Configuration

Constants in `main.py`:
- `NUM_VECTORS`: Number of random vectors for Phase 1 (1000)
- `ORTHOGONAL_TOLERANCE`: Allowed deviation from 90° (±1°)
- `MAX_ATTEMPTS`: Maximum consecutive failures before stopping (100)
- `ABS_FLAG`: Use absolute angle differences (False)

## Technical Details

### Vector Generation
- Uses Gaussian distribution for uniform sampling on unit sphere
- Normalizes vectors to unit length
- Generates vectors independently for each dimension

### Angle Computation
- Uses arccos of dot product
- Clips dot products to [-1.0, 1.0] for numerical stability
- Expresses angles in degrees

### Orthogonal Capacity Estimation
- Uses 2^(dim-1) as theoretical upper bound
- Shows exact values up to 1 million
- Uses ~10^n notation for larger values

## License

[Specify license information]

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request