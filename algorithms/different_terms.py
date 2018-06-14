def calc_terms(n):
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    terms = [1]
    n -= 1
    while terms[-1] < n:
        terms.append(terms[-1] + 1)
        n -= terms[-1]
    terms[-1] += n
    return terms

def main():
    n = int(input())
    terms = calc_terms(n)
    print (len(terms))
    print (' '.join(map(str, terms)))

if __name__ == "__main__":
    main()