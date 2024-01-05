import os
import string
import pprint


def tokenize(content: str) -> list[str]:
    return [word.strip(string.punctuation) for word in content.split(" ")]


def normalize(tokens: list[str]) -> list[str]:
    """This only converts everything to lowercase and removes punctuation"""
    return [i.lower() for i in tokens]


def generate_pairs(terms, doc_name):
    pass


def generate_incidence_matrix():
    directory_path = './corpus'
    dictionary = set()
    documents = os.listdir(directory_path)
    incidence_matrix = {}
    for doc in documents:
        doc_id = int(doc.split('_')[1]) - 1
        file_path = os.path.join(directory_path, doc)
        with open(file_path, 'r') as f:
            content = f.read()
            tokens = tokenize(content)
            normalized_tokens = normalize(tokens)
            unique_tokens = set(normalized_tokens)
            for token in unique_tokens:
                if token not in incidence_matrix:
                    if token == 'in':
                        print(f'in not in matrix, adding in for {doc}-{doc_id}')
                    incidence_matrix[token] = [0 for i in documents]
                    incidence_matrix[token][doc_id] = 1
                else:
                    if token == 'in':
                        print(f'in already in matrix, incrementing for {doc}-{doc_id}')
                    incidence_matrix[token][doc_id] = 1
    return incidence_matrix


if __name__ == '__main__':
    matrix = generate_incidence_matrix()
    pprint.pprint(matrix)
