import sys
import re
import pandas as pd

def word_count(text: str) -> int:
    return len(text.strip().split())

def sentence_count(text: str) -> int:
    # Count sentence-ending punctuation (. ! ?)
    return len(re.findall(r'[.!?]', text))

def is_question(text: str) -> bool:
    return text.strip().endswith('?')

def main(excel_path: str):
    df = pd.read_excel(excel_path)

    if "sentence" not in df.columns:
        raise ValueError("Excel file must contain a column named 'sentence'")

    # Ensure text
    df["sentence"] = df["sentence"].astype(str)

    df["gt_5_words"] = df["sentence"].apply(lambda x: word_count(x) > 5)
    df["le_5_words"] = df["sentence"].apply(lambda x: word_count(x) <= 5)
    df["more_than_1_sentence"] = df["sentence"].apply(lambda x: sentence_count(x) > 1)
    df["is_question"] = df["sentence"].apply(is_question)

    df.to_excel(excel_path, index=False)
    print("Analysis complete. File updated.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_sentences.py <path_to_excel_file>")
        sys.exit(1)

    main(sys.argv[1])
