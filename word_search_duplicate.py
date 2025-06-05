from collections import Counter


def find_duplicate_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]

        word_counts = Counter(words)
        duplicates = {word: count for word, count in word_counts.items() if count > 1}

        if duplicates:
            print("Duplicate words found:")
            for word, count in duplicates.items():
                print(f"{word}: {count} times")
        else:
            print("No duplicate words found.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    find_duplicate_words('feelings.txt')
