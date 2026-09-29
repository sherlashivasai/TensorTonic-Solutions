import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    try:
        X_arr = np.asarray(X, dtype=float)
    except (ValueError, TypeError):
        return None

    # Validate dimensionality and minimum required samples (N >= 2)
    if X_arr.ndim != 2 or X_arr.size == 0:
        return None

    n_samples, n_features = X_arr.shape
    if n_samples < 2 or n_features == 0:
        return None

    # 1. Center the data by subtracting column means
    X_centered = X_arr - np.mean(X_arr, axis=0)

    # 2. Compute sample covariance matrix: Cov = (X_c^T @ X_c) / (N - 1)
    cov = (X_centered.T @ X_centered) / (n_samples - 1)

    # 3. Compute standard deviations: sigma = sqrt(diag(Cov))
    variances = np.diag(cov)
    std = np.sqrt(np.maximum(variances, 0.0))

    # Identify constant / zero-variance columns
    is_constant = np.all(X_arr == X_arr[0:1, :], axis=0)
    zero_var = is_constant | (std == 0) | np.isnan(std)

    # 4. Normalize: R = Cov / (sigma * sigma^T)
    denom = np.outer(std, std)
    with np.errstate(divide='ignore', invalid='ignore'):
        corr = cov / denom

    # 5. Set diagonal to 1.0 for valid features
    np.fill_diagonal(corr, 1.0)

    # 6. Assign NaN to all correlations involving zero-variance features
    corr[zero_var, :] = np.nan
    corr[:, zero_var] = np.nan

    # Guard against floating-point inaccuracies pushing values outside [-1.0, 1.0]
    corr = np.clip(corr, -1.0, 1.0)

    return corr