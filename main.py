import os
import pprint
import string


from definitions import PostingsList, Term, Posting


def tokenize(content: str) -> list[str]:
    return [word.strip(string.punctuation) for word in content.split(" ")]


def normalize(tokens: list[str]) -> list[str]:
    """This only converts everything to lowercase and removes punctuation"""
    return [i.lower() for i in tokens]


def generate_pairs() -> list[tuple]:
    directory_path = './corpus'
    documents = os.listdir(directory_path)
    pairs = []
    for doc in documents:
        doc_id = int(doc.split('_')[1]) - 1
        file_path = os.path.join(directory_path, doc)
        with open(file_path, 'r') as f:
            content = f.read()
            tokens = tokenize(content)
            normalized_tokens = normalize(tokens)
            for token in normalized_tokens:
                pairs.append((Term(token), doc_id))
    return pairs


def merge_pairs(pairs: list[tuple[Term, int]]) -> list[tuple[Term, int]]:
    unique_pairs_id = set()
    for pair in pairs:
        unique_pairs_id.add(f"{pair[0].item}:{pair[1]}")
    result = [(Term(i.split(":")[0]), int(i.split(":")[1])) for i in unique_pairs_id]
    result.sort(key=lambda x: x[0].item)
    return result


def generate_index(pairs: list[tuple[Term, int]]) -> tuple[dict[Term, PostingsList], dict[str, int]]:
    dictionary = {}
    counts = {}
    for pair in pairs:
        if pair[0].item not in dictionary:
            postings = PostingsList()
            dictionary[pair[0].item] = postings.append(Posting(pair[1]))
            counts[pair[0].item] = 1
        else:
            dictionary[pair[0].item] = dictionary[pair[0].item].append(Posting(pair[1]))
            counts[pair[0].item] = counts[pair[0].item] + 1
    return dictionary, counts


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
                    incidence_matrix[token] = [0 for i in documents]
                    incidence_matrix[token][doc_id] = 1
                else:
                    incidence_matrix[token][doc_id] = 1
    return incidence_matrix


if __name__ == '__main__':
    all_pairs = generate_pairs()
    uniq_pairs = merge_pairs(all_pairs)
    dictionar_e, counts = generate_index(uniq_pairs)
    pprint.pprint(dictionar_e)
    pprint.pprint(counts)