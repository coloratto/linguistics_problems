# -*- coding: utf-8 -*-


class RussianCaser(object):
    @staticmethod
    def is_vowel(symbol):
        return symbol in "аеиоуыэя"

    @staticmethod
    def is_without_ending(word):
        # see words list: http://morphemeonline.ru/words-without-ending.html
        return word in "адажио ассорти денди депо дефиле дзюдо жалюзи " \
                       "кабаре каратэ кафе кино колибри кофе лото " \
                       "метро кенгуру пальто панно паспарту пенсне пианино " \
                       "табу такси тире фламинго фортепиано фото хачапури шимпанзе шоссе эскимо эссе".split()

    """ Return word in Russian dative case
        :param word is Russian lemma
        :param gen is gender of word, if gen is None then first word of non-defined gender, otherwise male of female
        :return word in Russian dative case
    """

    def find_last_vowel_index(self, word):
        return [i for i in range(len(word)) if self.is_vowel(word[i])][-1]

    def dative_single(self, word, gen=None):
        if self.is_without_ending(word):
            return word
        else:
            if gen == 'f':
                if word in ['мать', 'дочь']:
                    return word[:-1] + 'ери'
                elif word.endswith('ожь'):
                    if word == 'дрожь':
                        return word[:-1] + 'и'
                    else:
                        return word[:-3] + 'жи'
                elif word[-1] == 'ь':
                    return word[:-1] + 'и'
                elif word[-1] in 'ая':
                    return word[:-1] + 'е'
            elif gen == 'm':
                if word in 'мох рот ров узел ветер огонь корень пень ноготь'.split():
                    last_vowel_index = self.find_last_vowel_index(word)
                    if word[-1] == 'ь':
                        return word[:last_vowel_index] + word[-2] + 'ю'
                    else:
                        return word[:last_vowel_index] + word[-1] + 'у'
                elif word in 'улей лёд'.split():
                    return word[:-2] + 'ью' if word[-1] == 'ь' else word[:-2] + 'ь' + word[-1] + 'у'
                elif word[-1] in 'йь':
                    if word[-2] == 'о':
                        return word[:-1] + 'му'
                    return word[:-1] + 'ю'
                elif word.endswith('ек') and word[-3] in 'жчш' and word != 'чек':
                    return word[:-2] + 'ку'
                elif word.endswith('ёк'):
                    return word[:-2] + 'ьку'
                elif word.endswith('ок') and word[-3] in 'жнтчш' and len(word) > 4:
                    return word[:-2] + 'ку'
                elif word.endswith('ец'):
                    return word[:-2] + 'цу'
                else:
                    return word + 'у'
            else:
                if word[-1] == 'е' and word[-2] in 'иь':
                    return word[:-1] + 'ю'
                return word[:-1] + 'у'

    """ Return word in Russian dative case
            :param word is Russian lemma
            :return word in Russian dative case

            !!! Method architecture has refactored due to incorrectly working with plural form !!!
        """
    def dative_plural(self, word):
        if self.is_without_ending(word):
            return word
        else:
            if word[-1] == 'ы':
                return word[:-1] + 'ам'
            elif word[-1] in 'ая':
                return word + 'м'
            else:
                if word[-2] in 'вилнрть':
                    return word[:-1] + 'ям'
                else:
                    return word[:-1] + 'ам'


if __name__ == "__main__":
    caser = RussianCaser()
    assert caser.dative_single('ложь', 'f') == "лжи"
    assert caser.dative_single('рожь', 'f') == "ржи"
    assert caser.dative_single('дрожь', 'f') == "дрожи"
    assert caser.dative_single("ванна", 'f') == "ванне"
    assert caser.dative_single("мать", 'f') == "матери"
    assert caser.dative_single("дочь", 'f') == "дочери"
    assert caser.dative_single("рать", 'f') == "рати"
    assert caser.dative_single("верёвка", 'f') == "верёвке"
    assert caser.dative_single("капля", 'f') == "капле"
    assert caser.dative_single("капель", 'f') == "капели"
    assert caser.dative_single("вонь", 'f') == "вони"
    assert caser.dative_single("апрель", 'm') == "апрелю"
    assert caser.dative_single("молодец", 'm') == "молодцу"
    assert caser.dative_single("замочек", 'm') == "замочку"
    assert caser.dative_single("ребёнок", 'm') == "ребёнку"
    assert caser.dative_single("чек", 'm') == "чеку"
    assert caser.dative_single("ключик", 'm') == "ключику"
    assert caser.dative_single("горшок", 'm') == "горшку"
    assert caser.dative_single("шок", 'm') == "шоку"
    assert caser.dative_single("станок", 'm') == "станку"
    assert caser.dative_single("завиток", 'm') == "завитку"
    assert caser.dative_single("старичок", 'm') == "старичку"
    assert caser.dative_single("конёк", 'm') == "коньку"
    assert caser.dative_single("варенье") == "варенью"
    assert caser.dative_single("общение") == "общению"
    assert caser.dative_single("конь", 'm') == "коню"
    assert caser.dative_single("мотылёк", 'm') == "мотыльку"
    assert caser.dative_single("огонь", 'm') == "огню"
    assert caser.dative_single("лоток", 'm') == "лотку"
    # assert caser.dative_single("отток", 'm') == "оттоку"
    assert caser.dative_single("ток", 'm') == "току"
    assert caser.dative_single("ров", 'm') == "рву"
    assert caser.dative_single("ларёк", 'm') == "ларьку"
    assert caser.dative_single("харёк", 'm') == "харьку"
    assert caser.dative_single("порок", 'm') == "пороку"
    assert caser.dative_single("санаторий", 'm') == "санаторию"
    assert caser.dative_single("ковчег", 'm') == "ковчегу"
    assert caser.dative_single("такт", 'm') == "такту"
    assert caser.dative_single("село") == "селу"
    assert caser.dative_single("пальто") == "пальто"
    assert caser.dative_plural("ковчеги") == "ковчегам"
    assert caser.dative_plural("братья") == "братьям"
    assert caser.dative_plural("деревья") == "деревьям"
    assert caser.dative_plural("матери") == "матерям"
    assert caser.dative_plural("санатории") == "санаториям"
    assert caser.dative_plural("двери") == "дверям"
    assert caser.dative_plural("ванны") == "ваннам"
    assert caser.dative_plural("цветы") == "цветам"
    assert caser.dative_plural("старики") == "старикам"
    assert caser.dative_plural("ветви") == "ветвям"
    assert caser.dative_plural("метро") == "метро"
