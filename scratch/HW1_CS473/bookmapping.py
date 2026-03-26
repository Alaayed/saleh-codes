import os, sys, csv, re, string
from pathlib import Path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.similarities import MatrixSimilarity

def preprocess_text(text):
    ps = PorterStemmer()
    stop_words = set(stopwords.words("english"))
    text = text.lower()

    # remove punctuation directly, was that the issue??
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    clean_tokens = [ps.stem(w) for w in tokens if w not in stop_words]
    return clean_tokens


def read_chapters(folder_path):
    chapter_files = sorted(Path(folder_path).glob("*.txt"))
    chapters = []
    for fp in chapter_files:
        with open(fp, "r", encoding="utf-8", errors="ignore") as f:
            text = " ".join(line.strip() for line in f)
        chapters.append((fp.name, preprocess_text(text)))
    return chapters


def load_paths(input_file):
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines[0], lines[1]


def map_chapters(b1_chapters, b2_chapters, output_file="output.csv"):
    names1, docs1 = zip(*b1_chapters)
    names2, docs2 = zip(*b2_chapters)

    dictionary = Dictionary(docs1 + docs2)
    bow1 = [dictionary.doc2bow(doc) for doc in docs1]
    bow2 = [dictionary.doc2bow(doc) for doc in docs2]

    tfidf = TfidfModel(bow1 + bow2, dictionary=dictionary, smartirs="ltc", normalize=True)
    tfidf1 = [tfidf[bow] for bow in bow1]
    tfidf2 = [tfidf[bow] for bow in bow2]

    index = MatrixSimilarity(tfidf2, num_features=len(dictionary))

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i, vec in enumerate(tfidf1):
            sims = index[vec]
            j_best = int(sims.argmax())
            writer.writerow([names1[i], names2[j_best], f"{sims[j_best]:.8f}"])


def solve():
    b1_path, b2_path = load_paths(sys.argv[1])
    b1_chaps = read_chapters(b1_path)
    b2_chaps = read_chapters(b2_path)
    map_chapters(b1_chaps, b2_chaps, "output.csv")
solve()

