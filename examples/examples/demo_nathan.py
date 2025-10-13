from src.nathan_utils import word_count, average_word_length, clean_text

sample = "  Hello   Terps  from   Nathan  "
print("Words:", word_count(sample))
print("Average length:", average_word_length(sample))
print("Clean text:", clean_text(sample))
