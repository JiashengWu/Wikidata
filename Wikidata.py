import glob
import os


class Wikidata:
    """Wikidata class, which provide a function of find_property().

    Attributes:
        data (dict): Data stored as {path: example_set}.
    """

    def __init__(self, relpath):
        """The constructor of Wikidata class.
        Read the input files only once, and store them in class attribute 'data'.

        Parameters:
            relpath (string): The relative path of the Wikidata property files.
        """
        self.data = {}
        for path in glob.glob(relpath):
            self.data[path] = set(self.file_to_list(path))

    def find_property(self, strings):
        """Find property score (the number of strings in the input that are contained in a file).

        Parameters:
            strings (list): The input list of strings.
        Returns:
            scores (list): A sorted list of tuples of the form (filename, score).
        """
        scores = []
        for path, examples in self.data.items():
            score = 0
            for string in strings:
                if string in examples:
                    score += 1
            scores.append((os.path.basename(path), score))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        return scores

    @ staticmethod
    def file_to_list(relpath):
        """Convert a Wikidata property file to a list of strings.

        Parameters:
            relpath (string): The relative path of ONE Wikidata property file.
        Returns:
            examples (list): A list contains all examples in the input file.
        """
        examples = []
        with open(relpath, mode='r') as property:  # Wikidata property
            for line in property:
                examples.append(line.strip())
        return examples


if __name__ == '__main__':
    wikidata = Wikidata(r'programming_challenge/P*.txt')
    strings = Wikidata.file_to_list('programming_challenge/sample1.txt')
    scores = wikidata.find_property(strings)
    print(scores)
