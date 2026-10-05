def promote_model(models: list) -> str:
    """
    Returns the model name as a string.
    """
    # Write code here
    best_mdl = max(
        models,
        key = lambda m: (m['accuracy'], -m['latency'],m['timestamp'])
    )

    return best_mdl['name']