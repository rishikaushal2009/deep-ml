import numpy as np

def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:

    points_array = np.array(points, dtype=float)
    centroids = np.array(initial_centroids, dtype=float)

    for _ in range(max_iterations):
        # Calculate distance from every point to every centroid
        distances = np.linalg.norm(
            points_array[:, None, :] - centroids[None, :, :],
            axis=2
        )

        # Assign each point to its nearest centroid
        assignments = np.argmin(distances, axis=1)

        # Recalculate each centroid
        new_centroids = centroids.copy()

        for i in range(k):
            cluster_points = points_array[assignments == i]

            if len(cluster_points) > 0:
                new_centroids[i] = cluster_points.mean(axis=0)

        # Stop if centroids no longer change
        if np.allclose(centroids, new_centroids):
            centroids = new_centroids
            break

        centroids = new_centroids

    # Return a list of tuples containing floating-point coordinates
    return [tuple(row) for row in centroids]

