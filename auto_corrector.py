from collections import Counter


class AutoCorrection:
    """
    An AutoCorrection class that is intended to recommend an auto-corrected arabic text for any input text.

    Args:
        words (:list:`str`): words library for the model to rely on.
        alphabets (:obj:`str`): a string containing all alphabets to rely on.

    Returns:
        AutoCorrection: An AutoCorrection instance.

    Example:
        from auto_corrector import AutoCorrection
        auto_correct = AutoCorrection(words_lst, ar_letters)
        auto_correct.get_correction(word)
    """

    def __init__(self, words, alphabets):
        self.words = words
        self.alphabets = alphabets
        self.probs = {}  # The words probabilities
        self.words_cnt = {}  # The words frequencies
        self.vocabs = set(words)  # A set of the words

    def get_count(self):
        """
        A function that returns the frequency for each given word.

        Returns:
            a list of frequencies for each given word.
        """
        self.words_cnt = Counter(self.words)
        return self.words_cnt

    def get_probs(self):
        """
        A function that returns the relative probability for each given word.

        Returns:
            a list of relative probabilities for each given word.
        """
        sm = sum(self.words_cnt.values())
        for key, value in self.words_cnt.items():
            self.probs[key] = value / sm
        return self.probs

    def delete(self, word):
        """
        A function that returns a list of all possible combinations of one deleted character for a given word.

        Args:
            word (:list:`str`): a single piece of text, one word.

        Returns:
            a list of all combinations of one deleted character for a given word.
        """
        deleted = []
        for i in range(len(word)):
            deleted.append(word[:i] + word[i + 1:])
        return deleted

    def switch(self, word):
        """
        A function that returns a list of all possible combinations of one switch between two characters for a given
        word.

        Args:
            word (:list:`str`): a single piece of text, one word.

        Returns:
            a list of all possible combinations of one switch between two characters for a given word.
        """
        switched = []
        for i in range(len(word)):
            if len(word[i:]) >= 2:
                switched.append(word[:i] + word[i + 1] + word[i] + word[i + 2:])
        return switched

    def replace(self, word):
        """
        A function that returns a list of all possible combinations of one character replaced with another character
        for a given word.

        Args:
            word (:list:`str`): a single piece of text, one word.

        Returns:
            a list of all possible combinations of one character replaced with another character for a given word.
        """
        replaced = []
        for i in range(len(word)):
            for c in self.alphabets:
                if len(word) - i >= 1 and word[i] != c:
                    replaced.append(word[:i] + c + word[i + 1:])
            _replaced = sorted(replaced)
        return _replaced

    def insert(self, word):
        """
        A function that returns a list of all possible combinations of one character inserted for a given word.

        Args:
            word (:list:`str`): a single piece of text, one word.

        Returns:
            a list of all possible combinations of one character inserted for a given word.
        """
        inserted = []
        for i in range(len(word)):
            for c in self.alphabets:
                inserted.append(word[:i] + c + word[i:])
        return inserted

    def transform(self, word):
        """
        A function that returns a list of applied transformation for a given word using the functions: delete(word),
        switch(word), replace(word), and insert(word).

        Args:
            word (:list:`str`): a single piece of text, one word.

        Returns:
            a list of applied transformation for a given word.
        """
        deleted = self.delete(word)
        switched = self.switch(word)
        replaced = self.replace(word)
        inserted = self.insert(word)

        transformed = deleted + switched + replaced + inserted
        return transformed

    def edit_one_letter(self, word):
        """
        A function that returns a list of all possible combinations of an edited version of a word, if one letter needs
        to be corrected.

        Args:
            word (:list:`str`): a single piece of text, one word.

        Returns:
            a list of all possible combinations of an edited version of a word.
        """
        edit_set = set(self.transform(word))
        return edit_set

    def edit_two_letters(self, word):
        """
        A function that returns a list of all possible combinations of an edited version of a word, if two letters need
        to be corrected.

        Args:
            word (:list:`str`): a single piece of text, one word.

        Returns:
            a list of all possible combinations of an edited version of a word.
        """
        edit_set = set()
        for w1 in self.edit_one_letter(word):
            for w2 in self.edit_one_letter(word):
                edit_set.add(w2)
        return edit_set

    def get_correction(self, word):
        """
        A function that returns a list of the best suggestions of corrected version for a given word.

        Args:
            word (:list:`str`): a single piece of text, one word.

        Returns:
            a list of the best suggestions of corrected version for a given word.
        """
        best_suggestion = []
        # To check if this word in our vocabs
        in_vocabs = self.vocabs.intersection([word])

        # To see if this word in our editing method for one letter
        edited_to_1_letter = self.edit_one_letter(word)
        in_one_letter = self.vocabs.intersection(edited_to_1_letter)

        # To see if our word in our editing method for two letters
        edited_to_2_letters = self.edit_two_letters(word)
        in_two_letters = self.vocabs.intersection(edited_to_2_letters)

        # To obtain our suggestions words from in_vocabs,one_letter and two letters
        suggestion = {word: self.probs.get(word, 0) for word in in_vocabs or in_one_letter or in_two_letters}

        # To sort our suggestions by using values and obtain best two suggestions
        best_suggestion = sorted(suggestion.items(), key=lambda item: item[1], reverse=True)[:2]
        return best_suggestion
