def main():
    n, total_w = map(int, input().split())
    things = []
    while len(things) < n:
        cost, w = map(int, input().split())
        things.append((cost, w))
    things.sort(key=lambda thing: thing[0]/thing[1], reverse=True)
    total_cost = 0
    while (total_w > 0) and things:
        (cost, w) = things.pop(0)
        if w <= total_w:
            total_w -= w
            total_cost += cost
        else:
            total_cost += cost * (total_w / w)
            total_w = 0
    print('%.3f' % total_cost)

if __name__ == "__main__":
    main()