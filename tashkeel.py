import os

import numpy as np
import tensorflow as tf
from tensorflow.compat.v1.keras.models import load_model
from tensorflow.compat.v1.keras.preprocessing.sequence import pad_sequences

import tashkeel.tashkeel_helper as tashkeel_helper


class Tashkeel:
    """
    A Tashkeel class that is intended to apply diacritics (tashkeel) on arabic text for any input text.

    Args:
        folder_location (:obj:`str`): absolute or relative folder path

    Returns:
        Tashkeel: A Tashkeel instance.

    Example:
        from tashkeel import Tashkeel
        tashkeel = Tashkeel(folder_location)
        input_int = sh.prepare_input(input_text)
        model, graph = sh.get_model()
        logits = model.predict(input_int)[0]
        predicted_harakat = sh.logits_to_text(logits)
        final_output = sh.get_final_text(input_text, predicted_harakat)
    """

    def __init__(self, folder_location):
        assert folder_location != None, "model_location cant be empty, send location of keras model"

        model_folder = os.path.join(folder_location, 'model')
        self.max_sentence = 315
        self.model_location = os.path.join(model_folder, ('second_model6' + '.h5'))

        dictionary_folder = os.path.join(folder_location, 'dictionary')
        input_vocab_to_int = tashkeel_helper.load_binary('input_vocab_to_int', dictionary_folder)
        output_int_to_vocab = tashkeel_helper.load_binary('output_int_to_vocab', dictionary_folder)

        self.dictionary = {
            "input_vocab_to_int": input_vocab_to_int,
            "output_int_to_vocab": output_int_to_vocab}

    def get_model(self):
        """
        A function that returns the tensorflow model and its graph.

        Returns:
            the tensorflow model and its graph.
        """
        print('start load model')
        model = load_model(self.model_location)
        print('end load model')
        graph = tf.compat.v1.get_default_graph()

        return model, graph

    def prepare_input(self, input_sent):
        """
        A function that returns a prepared version of a given input text.

        Args:
            input_sent (:obj:`str`): a text string.

        Returns:
            a processed version of a given input text.
        """
        assert input_sent != None and len(input_sent) < self.max_sentence, \
            "max length for input_sent should be {} characters, you can split the sentence into multiple sentecens " \
            "and call the function".format(
                self.max_sentence)

        input_sent = [input_sent]

        return self.__preprocess(input_sent)

    def __preprocess(self, input_sent):
        """
        A function that returns a letter id matrix of a given input text.

        Args:
            input_sent (:obj:`str`): a text string.

        Returns:
            a letter id matrix.
        """

        input_vocab_to_int = self.dictionary["input_vocab_to_int"]

        input_letters_ids = [[input_vocab_to_int.get(ch, input_vocab_to_int['<UNK>']) for ch in sent] for sent in
                             input_sent]

        input_letters_ids = self.__pad_size(input_letters_ids, self.max_sentence)

        return input_letters_ids

    def logits_to_text(self, logits):
        """
        A function that returns a text converted from logits.

        Args:
            logits (:obj:`int`): logit.

        Returns:
            converted text.
        """
        text = []
        for prediction in np.argmax(logits, 1):
            if self.dictionary['output_int_to_vocab'][prediction] == '<PAD>':
                continue
            text.append(self.dictionary['output_int_to_vocab'][prediction])
        return text

    def get_final_text(self, input_sent, output_sent):
        """
        A function that returns the final text with diacritics.

        Args:
            input_sent (:obj:`str`): a text string.
            output_sent (:obj:`str`): a text string.

        Returns:
            the final text with diacritics.
        """
        return tashkeel_helper.combine_text_with_harakat(input_sent, output_sent)

    def clean_harakat(self, input_sent):
        """
        A function that returns a cleaned text from diacritics.

        Args:
            input_sent (:obj:`str`): a text string.

        Returns:
             cleaned text from diacritics.
        """
        return tashkeel_helper.clear_tashkel(input_sent)

    def __pad_size(self, matrix, length=None):
        """
        A function that returns the padding sequence of the text id matrix.

        Args:
            matrix (:list:`int`): text id matrix.

        Returns:
             the padding sequence of the text id matrix.
        """
        return pad_sequences(matrix, maxlen=length, padding='post')
