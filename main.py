import numpy as np
from itertools import combinations
import time
import math  # Add this import

# Constants
NUM_VECTORS = 1000
ABS_FLAG = False
ORTHOGONAL_TOLERANCE = 1.0  # +/- degrees from 90°
MAX_ATTEMPTS = 1000  # Maximum attempts to find orthogonal vector

def generate_random_vectors(dim):
    """Generate random unit vectors uniformly distributed on N-dimensional sphere
    
    Uses the Gaussian method which:
    - Generates values using normal distribution (mean=0, std=1)
    - Normalizes to get uniform distribution on unit sphere
    - This works because normal distribution has rotational symmetry
    """
    vectors = np.random.normal(0, 1, (NUM_VECTORS, dim))  # Normal/Gaussian distribution
    return vectors / np.linalg.norm(vectors, axis=1)[:, np.newaxis]

def compute_angles(vectors):
    """Compute angles between all pairs of vectors"""
    angles = []
    for v1, v2 in combinations(vectors, 2):
        dot_product = np.clip(np.dot(v1, v2), -1.0, 1.0)
        angle = np.arccos(dot_product) * 180 / np.pi
        
        if ABS_FLAG:
            angle = min(angle, 180 - angle)
        
        angles.append(angle)
    return np.array(angles)

def estimate_orthogonal_bounds(dim):
    """Estimate upper bound on number of almost orthogonal vectors
    
    Uses Rankin bound for spherical codes:
    - For angle θ near 90°, bound is approximately 2^(0.401 * dim)
    - More accurate than Kabatyanskii-Levenshtein bound
    - Matches known values well
    """
    if dim <= 1:
        return str(dim)
        
    # Use Rankin bound: approximately 2^(0.401 * dim) for nearly orthogonal vectors
    power = int(0.401 * dim)
    
    if power >= 6:  # 10^6 = 1M
        return f"~10^{power}"
    else:
        upper_bound = 2 ** power
        return str(upper_bound)

def find_orthogonal_vectors(dim):
    """Find a set of nearly orthogonal vectors
    
    Args:
        dim: Dimension of vectors
        
    Returns:
        List of vectors that are nearly orthogonal to each other
    """
    orthogonal_vectors = []
    attempts = 0
    
    # Try MAX_ATTEMPTS times to find as many orthogonal vectors as possible
    while attempts < MAX_ATTEMPTS:
        # Generate a new random vector
        new_vector = np.random.normal(0, 1, dim)
        new_vector = new_vector / np.linalg.norm(new_vector)
        
        # Check if this vector is nearly orthogonal to all existing vectors
        is_orthogonal = True
        for existing_vector in orthogonal_vectors:
            angle = np.arccos(np.clip(np.dot(new_vector, existing_vector), -1.0, 1.0)) * 180 / np.pi
            if abs(angle - 90) > ORTHOGONAL_TOLERANCE:
                is_orthogonal = False
                break
                
        if is_orthogonal:
            attempts = 0  # Reset attempts when we find a good vector
            orthogonal_vectors.append(new_vector)
            if len(orthogonal_vectors) % 100 == 0:
                print(f"{dim:5d}  {len(orthogonal_vectors):5d}...")
        else:
            attempts += 1
    
    return np.array(orthogonal_vectors)

def main():
    # Phase 1: Random vector analysis
    n_pairs = NUM_VECTORS * (NUM_VECTORS - 1) // 2
    print(f"\nPhase 1: Analyzing {NUM_VECTORS} random vectors ({n_pairs} unique pairs) per dimension")
    
    print("\nDim     Min    Max    Mean±Std    Median   Time(ms)")
    print("-" * 60)
    
    dimensions = [2, 3] + [2 ** power for power in range(2, 17)]
    
    for dim in dimensions:
        start_time = time.perf_counter()
        vectors = generate_random_vectors(dim)
        angles = compute_angles(vectors)
        
        mean = np.mean(angles)
        std = np.std(angles)
        median = np.median(angles)
        min_angle = np.min(angles)
        max_angle = np.max(angles)
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        
        print(f"{dim:5d}  {min_angle:5.1f} {max_angle:6.1f}  {mean:5.1f}±{std:4.1f}  {median:6.1f}  {elapsed_ms:8.1f}")
    
    # Phase 2: Finding orthogonal vectors
    print(f"\nPhase 2: Finding nearly orthogonal vectors (±{ORTHOGONAL_TOLERANCE}° from 90°, max {MAX_ATTEMPTS} attempts)")
    print("\nDim    Found")
    print("-" * 12)
    
    for dim in dimensions:
        orthogonal_vectors = find_orthogonal_vectors(dim)
        count = len(orthogonal_vectors)
        print(f"{dim:5d}  {count:5d}")

if __name__ == "__main__":
    main()
