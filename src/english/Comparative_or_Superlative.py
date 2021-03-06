# -*- coding: utf-8 -*-
from russian.Syllables import SyllableModule


class AdjectiveComparisoner(object):
    def __init__(self):
        self.irregular_adjectives = {"good": ["better", "best"], "bad": ["worse", "worst"],
                                     "far": ["farther", "farthest"], "little": ["less", "least"],
                                     "much": ["more", "most"]}

        self.irreg_comp_adj = {}
        with open("resources/irregular_adjectives.txt", "r") as f:
            for line in f:
                comparative, adjective = line.strip().split()
                self.irreg_comp_adj[comparative] = adjective

    @staticmethod
    def is_english_vowel(symbol):
        return symbol in "aeiouy"

    @staticmethod
    def is_english_consonant(symbol):
        return symbol in "bcdfghjklmnpqrstvwxz"

    @staticmethod
    def has_e_ending(word):
        # see words list: http://www.enchantedlearning.com/wordlist/adjectives.shtml
        return (word + "e") in "able active agile alive ample aware bare brave bronze " \
                               "close cute dense discrete edible fake false fickle feline female fine free " \
                               "gentle genuine grave gruesome handmade handsome hoarse huge humble " \
                               "idle impure lame late large live lone loose male massive mature naive nice nimble " \
                               "obese orange ornate pale polite prime pristine private prize profuse pure purple " \
                               "rare ripe rude safe same sane scarce serene severe simple single some sore sparse " \
                               "square stable stale strange subtle svelte tame tense unique unripe untrue vague " \
                               "wee welcome white whole wide wise"

    def get_comparative_degree(self, word, superlative=False):
        """Return adjective in the comparative degree"""
        def get_prefix(is_superlative):
            if not is_superlative:
                return "more"
            else:
                return " ".join([prefix, "most"])

        word = word.lower()
        prefix = "" if not superlative else "the"

        if word in self.irregular_adjectives:
            word = self.irregular_adjectives[word][0] if not superlative else self.irregular_adjectives[word][1]
        else:
            suffix = ""
            sm = SyllableModule()
            if word.endswith("y") and sm.english_syllables_count(word) <= 2:
                word = word[:-1] + "i" + ("er" if not superlative else "est")
            elif sm.english_syllables_count(word) == 1:
                suffix = "er" if not superlative else "est"
                if word.endswith("e"):
                    suffix = suffix[1:]

                if self.is_english_consonant(word[-1]) and self.is_english_vowel(word[-2]) and \
                        self.is_english_consonant(word[-3]):
                    word += word[-1]

                word += suffix
            elif sm.english_syllables_count(word) == 2:
                if word.endswith("e"):
                    suffix = "r" if not superlative else "st"
                elif word.endswith("ow") or word.endswith("er"):
                    suffix = "er" if not superlative else "est"
                else:
                    prefix = get_prefix(superlative)
                word += suffix
            else:
                prefix = get_prefix(superlative)

        return " ".join([prefix, word]).strip()

    def get_normalize_adjective(self, text):
        """Return normalized adjective"""
        words = text.strip().split()
        word = words[-1]
        if word in self.irreg_comp_adj:
            return self.irreg_comp_adj[word]
        elif "more" in words or "most" in words:
            return word
        else:
            ind = -2 if word.endswith("er") else -3
            word = word[:ind]
            if word.endswith("i"):
                return word[:-1] + "y"
            elif word.endswith("ll"):
                return word
            elif word.endswith(word[-1] + word[-1]):
                return word[:-1]
            elif self.has_e_ending(word):
                return word + "e"
            else:
                return word

    def get_all_comparisons(self, word):
        return [self.get_comparative_degree(word),
                self.get_comparative_degree(word, True)]

if __name__ == "__main__":
    ac = AdjectiveComparisoner()
    assert ac.get_comparative_degree("nice") == "nicer"
    assert ac.get_comparative_degree("impressive") == "more impressive"
    assert ac.get_comparative_degree("impressive", True) == "the most impressive"
    assert ac.get_comparative_degree("big") == "bigger"
    assert ac.get_comparative_degree("strange") == "stranger"
    assert ac.get_comparative_degree("happy") == "happier"
    assert ac.get_comparative_degree("far", True) == "the farthest"
    assert ac.get_normalize_adjective("the furthest") == "far"
    assert ac.get_normalize_adjective("smaller") == "small"
    assert ac.get_comparative_degree("simple", True) == "the simplest"
    assert ac.get_normalize_adjective("the hottest") == "hot"
    assert ac.get_normalize_adjective("the cheapest") == "cheap"
    assert ac.get_normalize_adjective("the cleverest") == "clever"
    assert ac.get_comparative_degree("clever", True) == "the cleverest"
    assert ac.get_comparative_degree("tangled") == "more tangled"
    assert ac.get_normalize_adjective("happier") == "happy"
    assert ac.get_normalize_adjective("the silliest") == "silly"
    assert ac.get_comparative_degree("strong", True) == "the strongest"
    assert ac.get_comparative_degree("narrow", True) == "the narrowest"
    assert ac.get_normalize_adjective("the strongest") == "strong"
    assert ac.get_normalize_adjective("bigger") == "big"
    assert ac.get_normalize_adjective("the nicest") == "nice"
    assert ac.get_normalize_adjective("stranger") == "strange"
