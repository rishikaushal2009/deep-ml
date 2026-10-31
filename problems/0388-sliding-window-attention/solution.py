import numpy as np

def sliding_window_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray, window_size: int) -> np.ndarray:
    """
    Compute sliding window attention.
    
    Args:
        Q: Query matrix of shape (seq_len, d_k)
        K: Key matrix of shape (seq_len, d_k)
        V: Value matrix of shape (seq_len, d_v)
        window_size: Number of positions to the left and right each query can attend to
    
    Returns:
        Output matrix of shape (seq_len, d_v), rounded to 4 decimal places.
    """
     # Step 1: Calculate scaled attention scores
    d_k = Q.shape[1]
    scores = (Q @ K.T) / np.sqrt(d_k)

    # Step 2: Create the sliding-window mask
    n = Q.shape[0]
    rows, cols = np.indices((n, n))
    mask = np.abs(rows - cols) > window_size

    # Step 3: Mask positions outside the window
    masked_scores = scores.copy()
    masked_scores[mask] = -np.inf

    # Step 4: Calculate numerically stable softmax
    row_maxes = np.max(masked_scores, axis=1, keepdims=True)
    stable_scores = masked_scores - row_maxes

    exp_scores = np.exp(stable_scores)
    attention_weights = exp_scores / np.sum(
        exp_scores, axis=1, keepdims=True
    )

    # Step 5: Calculate attention output
    output = attention_weights @ V

    # Step 6: Round the final result
    return np.round(output, 4)