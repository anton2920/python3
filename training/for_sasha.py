def F(n):
    if n > 2:
        return F(n - 1) + G(n - 2)
    else:
        return n


def G(n):
    if n > 2:
        return G(n - 1) + F(n - 2)
    else:
        return n + 1


if __name__ == '__main__':
    print(G(6))