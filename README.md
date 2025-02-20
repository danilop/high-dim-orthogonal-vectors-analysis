# Vector Angle Distribution Analysis

This program analyzes the angular relationships between random unit vectors in high-dimensional spaces. It provides insights into how angles between vectors behave as dimensionality increases, which is particularly relevant for high-dimensional geometry and machine learning applications.

## Overview

The program generates random unit vectors in spaces of increasing dimensionality (from 2¹ to 2¹⁶) and computes statistical properties of the angles between all possible vector pairs. Each dimension is analyzed using 1000 random vectors, resulting in 499,500 unique pair comparisons.

## Features

- Phase 1: Random Vector Analysis
  - Generates 1000 random unit vectors using Gaussian distribution
  - Analyzes dimensions in powers of 2 from 2¹ to 2¹⁶ (2 to 65,536)
  - Supports 2D, 3D, and higher dimensional vector spaces
  - Computes angles between all possible vector pairs
  - Provides comprehensive statistical analysis including:
    - Mean angle
    - Standard deviation
    - Median angle
    - Minimum and maximum angles
  - Performance timing for each dimensional analysis

- Phase 2: Orthogonal Vector Finding
  - Attempts to find sets of orthogonal vectors in each dimension
  - Considers vectors orthogonal if their angle is 90° ± 1°
  - For dimension N, tries to find N+1 orthogonal vectors
  - Reports number of vectors found and attempts made

## Requirements

- Python 3.x
- NumPy
- Python standard library (itertools, time)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/vector-angle-analysis.git
cd vector-angle-analysis
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

The program will output a table showing the statistical analysis for each dimension, including:
- Dimension size (5 characters, right-aligned)
- Minimum angle (5 characters)
- Maximum angle (6 characters)
- Mean ± Standard deviation (10 characters total)
- Median angle (6 characters)
- Execution time in milliseconds (8 characters)

All angle values are displayed with one decimal place precision.

### Example Output
```
Phase 1: Analyzing 100 random vectors (4950 unique pairs) per dimension

Dim     Min    Max    Mean±Std    Median   Time(ms)   Est.Max
-----------------------------------------------------------------
    2   0.1  179.9   90.0±52.0    90.0      5.2          2
    3   8.2  171.8   90.0±41.8    90.0     10.1          4
    4  25.3  154.7   90.0±29.6    90.0     20.3          8
    8  42.1  137.9   90.0±20.9    90.0     40.6        128
   16  42.1  137.9   90.0±20.9    90.0     40.6      32768
   32  42.1  137.9   90.0±20.9    90.0     40.6      ~10^9
   64  42.1  137.9   90.0±20.9    90.0     40.6     ~10^18
  ...

Phase 2: Finding nearly orthogonal vectors (±1.0° from 90°, max 10000 attempts)

Dim    Count
------------
    2      2
    3      3
    4      5
  ...
```

## Configuration

You can modify the following constants in `main.py`:

- `NUM_VECTORS`: Number of random vectors to generate (fixed at 1000)
- `ABS_FLAG`: When True, considers only acute angles (0° to 90°); when False, considers full angle range (0° to 180°)

## Technical Details

### Vector Generation
- Vectors are initially generated using normal distribution (Gaussian)
- Each vector is normalized to unit length
- Vectors are generated independently for each dimension

### Angle Computation
- Uses arccos of dot product for angle calculation
- Dot products are clipped to [-1.0, 1.0] to prevent numerical errors
- Angles are expressed in degrees

### Mathematical Constraints
- All vectors must be unit vectors (length = 1)
- Dot products must be constrained to [-1, 1]
- Angles are converted from radians to degrees for display

## Error Handling

The program implements the following error handling measures:
- Numerical precision issues in dot product calculations
- Prevention of invalid angle calculations through dot product clipping

## License

[Specify license information]

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request