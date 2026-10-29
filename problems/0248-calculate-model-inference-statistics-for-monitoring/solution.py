def calculate_inference_stats(latencies_ms):
    if not latencies_ms:
        return {}

    latencies = sorted(latencies_ms)
    n = len(latencies)

    # Average latency
    avg_latency = sum(latencies) / n

    # Throughput for sequential processing
    throughput = 1000 / avg_latency if avg_latency > 0 else float("inf")

    # Calculate a percentile using linear interpolation
    def percentile(p):
        index = p * (n - 1)

        lower = int(index)
        upper = min(lower + 1, n - 1)

        fraction = index - lower

        return (
            latencies[lower]
            + fraction * (latencies[upper] - latencies[lower])
        )

    return {
        "throughput_per_sec": round(throughput, 2),
        "avg_latency_ms": round(avg_latency, 2),
        "p50_ms": round(percentile(0.50), 2),
        "p95_ms": round(percentile(0.95), 2),
        "p99_ms": round(percentile(0.99), 2),
    }


# Example
#latencies_ms = [10, 20, 30, 40, 50]

#print(calculate_inference_stats(latencies_ms))