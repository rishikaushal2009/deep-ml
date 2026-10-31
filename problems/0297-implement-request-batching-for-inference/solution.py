def batch_requests(requests: list, max_batch_size: int, max_wait_time: float) -> list:
    """
    Group inference requests into batches based on size and time constraints.
    
    Args:
        requests: List of dicts with 'id', 'timestamp', 'features'
        max_batch_size: Maximum number of requests per batch
        max_wait_time: Maximum time to wait before processing a batch
    
    Returns:
        List of tuples: (request_ids, batched_features, process_time)
    """
    if not requests:
        return []

    # Step 1: Sort requests by arrival timestamp
    requests = sorted(requests, key=lambda r: r["timestamp"])

    batches = []
    current_batch = []
    batch_start_time = None

    # Step 2: Process requests in timestamp order
    for request in requests:
        timestamp = request["timestamp"]

        # Step 3: Check whether adding this request exceeds the wait limit
        if current_batch and timestamp - batch_start_time > max_wait_time:
            # Finalize the existing batch
            request_ids = [r["id"] for r in current_batch]
            batched_features = [r["features"] for r in current_batch]
            process_time = round(current_batch[-1]["timestamp"], 4)

            batches.append((request_ids, batched_features, process_time))

            # Start a new batch
            current_batch = []
            batch_start_time = None

        # Step 4: Start a batch if necessary
        if not current_batch:
            batch_start_time = timestamp

        # Step 5: Add the request to the current batch
        current_batch.append(request)

        # Step 6: Finalize the batch if it reaches maximum size
        if len(current_batch) >= max_batch_size:
            request_ids = [r["id"] for r in current_batch]
            batched_features = [r["features"] for r in current_batch]
            process_time = round(current_batch[-1]["timestamp"], 4)

            batches.append((request_ids, batched_features, process_time))

            current_batch = []
            batch_start_time = None

    # Step 7: Process any remaining requests
    if current_batch:
        request_ids = [r["id"] for r in current_batch]
        batched_features = [r["features"] for r in current_batch]
        process_time = round(current_batch[-1]["timestamp"], 4)

        batches.append((request_ids, batched_features, process_time))

    return batches