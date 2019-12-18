import collections


def topological_sort(nodes_map, nodes):
    def recursion(nodes_map, node, result, visited):
        if node in visited:
            return
        visited.add(node)
        if node in nodes_map:
            for c in nodes_map[node]:
                recursion(nodes_map, c, result, visited)
        result.append(node)

    visited, result = set(), []
    for node in nodes:
        recursion(nodes_map, node, result, visited)
    return reversed(result)

def find_characters(available_words):
    chars = set()
    for word in available_words:
        for c in word:
            chars.add(c)
    return chars

def process_word_list(words):
    chars = find_characters(words)
    nodes_map = collections.defaultdict(list)
    for i, word in enumerate(words[:-1]):
        nxt = words[i + 1]
        # Create an map of characters having a lexical greater than character `one`
        for one, two in zip(word, nxt):
            if one != two:
                nodes_map[one] += [two]
                break
    for val in topological_sort(nodes_map, chars):
        print(val)


if __name__ == '__main__':
    words = ("baa", "abcd", "abca", "cab", "cad")
    process_word_list(words)