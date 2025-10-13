from src import irat_library as irat

text = "Information science helps people retrieve knowledge from data."

tokens = irat.tokenize_text(text)
print("Tokens:", tokens)

counts = irat.count_word_frequency(tokens)
print("Word counts:", counts)

print("Contains 'science'?", irat.find_keyword_in_text(text, "science"))

print("Snippet example:", irat.make_snippet(text, "science"))
