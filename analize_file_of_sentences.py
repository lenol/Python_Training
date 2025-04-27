# Open the file
with open("phrases.txt") as f:
  number_of_sentences=0
  total_length=0
  maximum_sentence_length=0
  minimum_sentence_length=float('inf')
  for line in f:
        sentence_length=len(line.strip())
        print(sentence_length)
        number_of_sentences+=1
        total_length+=sentence_length
        if sentence_length>maximum_sentence_length:
            maximum_sentence_length=sentence_length
        if minimum_sentence_length>sentence_length:
            minimum_sentence_length=sentence_length
print(f"Total number of sentences: {number_of_sentences}")
print(f"Average sentence length: {total_length / number_of_sentences:} characters")
print(f"Longest sentence length: {maximum_sentence_length} characters")
print(f"Shortest sentence length: {minimum_sentence_length} characters")