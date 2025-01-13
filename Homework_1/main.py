from src.homework.search import binary_search_iterative, binary_search_recursive
from src.homework.text_ops import count_words, find_longest_word, format_sentences
from src.homework.number_ops import fibonacci_recursive, sum_of_digits_recursive, is_palindrome_number

def main():

    print("Exercise 1")
    # Exercise 1
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]
    result = binary_search_iterative(numbers, 7)
    result = binary_search_recursive(numbers, 7, 0, len(numbers) - 1)

    print("--------------------------------")

    print("Exercise 2")
    # Exercise 2
    text = """Python is an amazing programming language! It is easy to learn, 
              yet powerful enough for professional development. Python's syntax 
              is very readable."""

    word_count = count_words(text)
    longest = find_longest_word(text)
    sentences = format_sentences(text)

    print("--------------------------------")

    print("Exercise 3")
    # Exercise 3
    fib_8 = fibonacci_recursive(8)  # Should return 21
    print(fib_8)
    digit_sum = sum_of_digits_recursive(12345) # Should return 15
    print(digit_sum)
    is_pal = is_palindrome_number(12321)  # Should return True
    print(is_pal)

if __name__ == "__main__":
    main()