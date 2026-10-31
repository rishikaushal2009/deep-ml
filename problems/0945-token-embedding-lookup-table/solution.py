import numpy as np

def token_embedding_lookup(vocab_size: int, embed_dim: int, token_ids: list, seed: int = 0) -> list:
    """
    Build a random embedding table of shape (vocab_size, embed_dim) using
    np.random.default_rng(seed).standard_normal(...), then return the rows
    corresponding to token_ids as a nested list.
    """
   # Step 1: Create a random number generator
    rng = np.random.default_rng(seed)

    # Step 2: Generate the embedding matrix
    embeddings = rng.standard_normal((vocab_size, embed_dim))

    # Step 3: Select the rows corresponding to token IDs
    selected_embeddings = embeddings[token_ids]

    # Step 4: Convert the NumPy array to a Python list
    return selected_embeddings.tolist()