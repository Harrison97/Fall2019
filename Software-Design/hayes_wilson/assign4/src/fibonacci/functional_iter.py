functional_iter = lambda n: \
    1 if 0 <= n <= 1 \
    else functional_iter(n-1) + functional_iter(n-2) if n > 0 \
    else None

