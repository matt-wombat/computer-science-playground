def pattern_search(text, pattern):
  print("Text:", text, "\nPattern:", pattern, "\n")
  for it in range(len(text)):
    match_count = 0

    for ip in range(len(pattern)):
      if pattern[ip] == text[it + ip]:
        match_count += 1
      else:
        break
    
    if match_count == len(pattern):
      print(pattern, "found at index", it)


text = """
The most basic case of string searching involves one (often very long) string, 
sometimes called the haystack, and one (often very short) string, 
sometimes called the needle. The goal is to find one or more occurrences 
of the needle within the haystack. For example, one might search for to within:"""

pattern_search(text, "needle")
pattern_search(text, "haystack")
pattern_search(text, "sometime")