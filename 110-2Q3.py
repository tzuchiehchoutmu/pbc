import re
letterA, letterB = input().split(" ")
sentence_input = input()
def count_word_pairs_in_paragraph(word1, word2, paragraph):
    sentences = re.split(r'[.!?]',paragraph)
       
    total_sentences = len(sentences)
    word_pair_count = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            words = sentence.split()
            if word1 in words and word2 in words:
                word_pair_count += 1
    
    return total_sentences, word_pair_count, sentences

total_sentences, word_pair_count ,sentences= count_word_pairs_in_paragraph(letterA, letterB, sentence_input )
print(str(total_sentences-1), str(word_pair_count))
