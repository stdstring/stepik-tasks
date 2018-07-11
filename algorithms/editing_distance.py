def main():
    word1 = input()
    word2 = input()
    prev_row = []
    current_row = [value for value in range(0, len(word1) + 1)]
    for row in range(1, len(word2) + 1):
        prev_row = current_row
        current_row = [row]
        for column in range(1, len(word1) + 1):
            insert_cost = current_row[column - 1] + 1
            delete_cost = prev_row[column] + 1
            char_diff = 0 if word1[column - 1] == word2[row - 1] else 1
            subst_cost = prev_row[column - 1] + char_diff
            current_row.append(min(insert_cost, delete_cost, subst_cost))
    print(current_row[-1])

if __name__ == "__main__":
    main()