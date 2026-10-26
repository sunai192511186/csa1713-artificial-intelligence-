def alpha_beta(depth, node, maximizing, values, alpha, beta):
    if depth == 2:
        return values[node]
    if maximizing:
        best = -999
        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i,
                             False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i,
                             True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = [3, 5, 6, 9]
result = alpha_beta(0, 0, True, values, -999, 999)
print("Optimal value:", result)
