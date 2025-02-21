# Orthogonal Capacity

This program explores the geometric properties of high-dimensional spaces by:
1. Analyzing angular relationships between random unit vectors
2. Finding sets of nearly orthogonal vectors

## Overview

The program operates in two phases:

### Phase 1: Random Vector Analysis
Generates random unit vectors in spaces of increasing dimensionality (2D, 3D, and powers of 2 up to 2¹⁶) and analyzes their angular relationships. For each dimension:
- Generates 1000 random unit vectors using Gaussian distribution
- Computes angles between all pairs (499,500 unique pairs)
- Provides statistical analysis of the angles

### Phase 2: Orthogonal Vector Finding
Attempts to find sets of nearly orthogonal vectors in each dimension by:
- Generating random unit vectors one at a time
- Keeping vectors that are nearly orthogonal to all previous ones (90° ± 1°)
- Continuing until 1000 consecutive failures to find a new orthogonal vector

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

Dim     Min    Max    Mean±Std    Median   Time(ms)
------------------------------------------------------------
    2    0.0  180.0   90.0±51.9    90.0    1312.9
    3    0.1  179.9   89.9±39.1    89.9    1299.8
    4    1.2  179.2   90.0±32.5    89.9    1299.9
    8    8.6  168.1   90.0±21.6    90.0    1297.0
   16   27.8  149.2   90.0±14.7    90.0    1301.0
   32   41.2  134.5   90.0±10.3    90.0    1303.0
   64   57.8  124.4   90.0± 7.2    90.0    1304.4
  128   66.9  113.6   90.0± 5.1    90.0    1306.7
  256   73.1  106.8   90.0± 3.6    90.0    1320.5
  512   78.6  101.2   90.0± 2.5    90.0    1342.9
 1024   81.1   98.5   90.0± 1.8    90.0    1401.4
 2048   84.5   96.0   90.0± 1.3    90.0    1539.3
 4096   86.0   94.0   90.0± 0.9    90.0    1820.1
 8192   86.5   93.6   90.0± 0.6    90.0    2549.3
16384   88.0   92.0   90.0± 0.4    90.0    3556.9
32768   88.5   91.4   90.0± 0.3    90.0    5455.8
65536   88.9   91.1   90.0± 0.2    90.0    9225.5

Phase 2: Finding nearly orthogonal vectors (±1.0° from 90°, max 1000 attempts)

Dim    Found
------------
    2      2
    3      2
    4      3
    8      3
   16      4
   32      3
   64      4
  128      5
  256      7
  512      6
 1024     10
 2048     14
 4096     22
 8192     58
16384    100...
16384    200...
16384    207
32768    100...
32768    200...
32768    300...
32768    400...
32768    500...
32768    600...
32768    700...
32768    800...
32768    900...
32768   1000...
...
```

## Configuration

Constants in `main.py`:
- `NUM_VECTORS`: Number of random vectors for Phase 1 (1000)
- `ORTHOGONAL_TOLERANCE`: Allowed deviation from 90° (±1°)
- `MAX_ATTEMPTS`: Maximum consecutive failures before stopping (1000)
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
- Uses Rankin bound for spherical codes (2^(0.401 * dim))
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
