# Vector Angle Distribution Analysis Specification

## 1. Overview
This program analyzes the angular relationships between random unit vectors in high-dimensional spaces. It generates multiple random vectors in spaces of increasing dimensionality and computes statistical properties of the angles between all possible vector pairs.

## 2. Input Parameters

### 2.1 Constants
- `NUM_VECTORS`: Number of random vectors to generate (fixed at 1000)
- `ABS_FLAG`: Boolean flag determining angle interpretation (fixed at False)
- `ORTHOGONAL_TOLERANCE`: Allowed deviation from 90° (fixed at ±1°)
- `MAX_ATTEMPTS`: Maximum attempts to find orthogonal vectors (fixed at 1000)
- Dimensions analyzed: 
  - Powers of 2 from 2¹ to 2¹⁶ (2 to 65536)
  - Special focus on 2D, 3D, and higher dimensions

## 3. Functional Requirements

### 3.1 Vector Generation
- The system shall generate `NUM_VECTORS` random vectors for each dimension
- Vectors shall be:
  - Initially generated using uniform distribution (-1 to 1)
  - Normalized to unit length
  - Generated independently for each dimension

### 3.2 Angle Computation
- The system shall:
  - Compute angles between all possible pairs of vectors
  - Express angles in degrees
  - When `ABS_FLAG` is True: Consider only acute angles (0° to 90°)
  - When `ABS_FLAG` is False: Consider full angle range (0° to 180°)
  - Use arccos of dot product for angle calculation
  - Clip dot products to [-1.0, 1.0] to prevent numerical errors

### 3.3 Statistical Analysis
For each dimension, the system shall compute:
- Mean angle
- Standard deviation of angles
- Median angle
- Minimum angle
- Maximum angle

### 3.4 Performance Measurement
- The system shall measure and report the execution time for each dimension
- Timing shall:
  - Include vector generation, angle computation, and statistical analysis
  - Be measured in milliseconds
  - Use high-precision timer (perf_counter)

### 3.5 Orthogonal Vector Finding
- The system shall attempt to find sets of nearly orthogonal vectors
- For each dimension N:
  - Try to find N+1 vectors that are nearly orthogonal to each other
  - Consider vectors orthogonal if their angle is 90° ± ORTHOGONAL_TOLERANCE
  - Stop after finding N+1 vectors or reaching MAX_ATTEMPTS
  - Report the number of orthogonal vectors found

## 4. Output Requirements

### 4.1 Phase 1 Display Format
The system shall display:
- The number of random vectors used for each dimension size
- A header row with column labels
- One row per dimension containing:
  - Dimension size (5 characters, right-aligned)
  - Minimum angle (5 characters)
  - Maximum angle (6 characters)
  - Mean ± Standard deviation (10 characters total)
  - Median (6 characters)
  - Execution time in milliseconds (8 characters)

### 4.2 Phase 2 Display Format
The system shall display:
- A header indicating Phase 2, the orthogonal tolerance, and maximum attempts
- Column headers for dimension and found count
- One row per dimension containing:
  - Dimension size (5 characters, right-aligned)
  - Number of orthogonal vectors found (5 characters)

## 5. Performance Requirements
- The system shall handle vector dimensions up to 2¹⁶ (65536)
- The system shall process 1000 vectors (499500 unique pairs) per dimension

## 6. Mathematical Constraints
- All vectors must be unit vectors (length = 1)
- Dot products must be constrained to [-1, 1]
- Angles must be converted from radians to degrees for display
- Upper bounds must follow Rankin's spherical code bound

## 7. Dependencies
- NumPy library for numerical computations
- Python standard library (itertools for combinations)
- Python standard library (time for performance measurement)

## 8. Error Handling
- The system shall handle numerical precision issues in dot product calculations
- The system shall prevent invalid angle calculations through dot product clipping 