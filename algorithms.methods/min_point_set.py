def main():
    n = int(input())
    segments = []
    while (len(segments) < n):
        l, r = map(int, input().split())
        segments.append((l, r))
    segments.sort(key=lambda value: value[1])
    result = []
    current_segment = None
    for segment in segments:
        if current_segment is None:
            current_segment = segment
        if current_segment[1] < segment[0]:
            result.append(current_segment[1])
            current_segment = segment
    if current_segment is not None:
        result.append(current_segment[1])
    print (len(result))
    print (' '.join(map(str, result)))

if __name__ == "__main__":
    main()