from revscoring.datasources.meta import vectorizers, mappers
from revscoring.features import wikitext
from revscoring.features.meta import aggregators


kowiki_kvs = vectorizers.word2vec.load_gensim_kv(
    filename="kowiki-20200501-learned_vectors.50_cell.10k.kv", mmap='r')


def vectorize_words(words):
    return vectorizers.word2vec.vectorize_words(kowiki_kvs, words)


revision_text_vectors = vectorizers.word2vec(
    mappers.lower_case(wikitext.revision.datasources.words),
    vectorize_words,
    name="revision.text.ko_vectors")

w2v = aggregators.mean(
    revision_text_vectors,
    vector=True,
    name="revision.text.ko_vectors_mean"
)

drafttopic = [w2v]
articletopic = drafttopic
