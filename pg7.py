import nltk
from nltk import pos_tag, sent_tokenize, ne_chunk, word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

paragraph = """Scarface is a 1983 American crime drama film directed by Brian De Palma and written by Oliver Stone. \
    Loosely based on the 1929 novel of the same name and serving as a loose remake of the 1932 film,\
    it tells the story of Cuban refugee Tony Montana (Al Pacino), \
    who arrives penniless in Miami during the Mariel boatlift and becomes a powerful and extremely homicidal drug lord.\
    The film co-stars Steven Bauer, Michelle Pfeiffer, Mary Elizabeth Mastrantonio and Robert Loggia.\
    De Palma dedicated this version of Scarface to the memories of Howard Hawks and Ben Hecht, \
    """


for sentence in sent_tokenize(paragraph):
    for chunk in ne_chunk(pos_tag(word_tokenize(sentence))):
        if hasattr(chunk, 'label'):
            print(f"{''.join(c[0] for c in chunk):<35} {chunk.label()}")
