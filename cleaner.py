# -*- coding: utf-8 -*-

import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk import word_tokenize


from appos.appos import appos_dict
from slangs.slangs import slangs_dict
from stopwords.stopwords import stop_words_list
from emoticons.emo import emo


sb_stem = SnowballStemmer("english", ignore_stopwords=True)
pt_stem = PorterStemmer()

lmtzr = WordNetLemmatizer()

def appos_look_up(text):
    """
    Convert apostrophes word to original form
    Example: I don't know what is going on?  => I do not know what is going on? 
    Args:
        text (str): text 

    Returns:
        apposed (str) : text with converted apostrophes
    """
    words = text.split()
    new_text = []
    for word in words:
        word_s = word.lower()
        if word_s in appos_dict:
            new_text.append(appos_dict[word_s])
        else:
            new_text.append(word)
    apposed = " ".join(new_text)
    return apposed


def remove_repeated_characters(text):
    """
    Remove repeated characters (>2) in words to max limit of 2
    Example: I am verrry happpyyy today => I am verry happyy today
    Args:
        text (str): text

    Returns:
        clean_text (str): cleaned text with removed repeated chars
    """
    regex_pattern = re.compile(r'(.)\1+')
    clean_text = regex_pattern.sub(r'\1\1', text)
    return clean_text


def separate_digit_text(text):
    """
    Separate digit and words with space in text
    Example: I will be booking tickets for 2adults => I will be booking tickets for 2 adults   
    Args:
        text (str): text
    Returns:
        clean_text (str): cleaned text with separated digits and words
    """
    regex_patter = re.compile(r'([\d]+)([a-zA-Z]+)')
    clean_text = regex_patter.sub(r'\1 \2', text)
    return clean_text


def slang_look_up(text):
    """
    Replace slang word in text to their original form
    Example: hi, thanq so mch => hi, thank you so much
    Args:
        text (str): text
    Returns:
        slanged (str): cleaned text with replaced slang
    """
    words = text.split()
    new_text = []

    for word in words:
        word_s = word.lower()
        if word_s in slangs_dict:
            new_text.append(slangs_dict[word_s])
        else:
            new_text.append(word)
    slanged = " ".join(new_text)
    return slanged


def stem_text(text, stemmer='snowball'):
    """
    Convert words in text into their root form
    Example: I am playing in ground => I am play in ground 
    Args:
        text (str): text
        
    Returns:
        text_stem (str): cleaned text with replaced stem words
    """
    text = remove_inside_braces(text)
    tokens = word_tokenize(text)
    if stemmer == 'snowball':
        text_stem = " ".join([sb_stem.stem(w) for w in tokens])
    else:
        text_stem = " ".join([pt_stem.stem(w) for w in tokens])
    
    return text_stem


def remove_single_char_word(text):
    """
    Remove single character word from text
    Example: I am in a home for 2 years => am in home for years 
    Args:
        text (str): text
         
    Returns:
        (str): text with single char removed
    """
    words = text.split()
    filter_words = [word for word in words if len(word) > 1]
    return " ".join(filter_words)


def remove_punctuations(text):
    """
    Removed special characters from text
    Example: he: I am going. are you coming? => he I am going. are you coming
   
    Args:
        text (str): text
   
    Returns:
        clean_text (str): cleaned text with removed special characters
    """
    regex_pattern = re.compile(r'[\,+\:\?\!\"\(\)!\'\.\%\[\]]+')
    clean_text = regex_pattern.sub(r' ', text)
    clean_text = clean_text.replace('-', '')
    return clean_text


def remove_extra_space(text):
    """
    Remove extra white spaces space from text
    Example: hey are   you coming. ? => he are you coming. ?
    Args:
        text (str): text
    Returns:
        clean_text (str): clean text with removed extra white spaces
    """
    clean_text = ' '.join(text.strip().split())
    return clean_text


def replace_digits_with_char(text, replace_char='d'):
    """
    Replace digits to `replace_char`
    Example: I will be there on 22 april. => I will be there on dd april.
    Args:
        text (str): text
        replace_char (str): character with which digit has to be replaced
    Returns:
        clean_text (str): clean text with replaced char for digits
    """
    regex_pattern = re.compile(r'[0-9]')
    clean_text = regex_pattern.sub(replace_char, text)
    return clean_text


def emoticons_look_up(text):
    """
    Remove emoticons from text and returns list of emotions present in text
    Example: Sure, you are welcome :) => Sure, you are welcome.
    Args:
        text (str): text
    Returns:
        text (str): text with removed emoticons sign
        emolist (list) : list of emotions from text
    """

    words = text.split()
    emolist = []
    for word in words:
        if word in emo:
            emolist.append(str(emo[word]))
            text = text.replace(word," ")
    return text, emolist


def remove_url(text):
    """
    Remove urls from text
    Example: link to latest cricket score. https://xyz.com/a/b => link to latest cricket score.
    Args:
        text (str): text
    Returns:
        text (str): text with removed urls
    """

    urlfree = []
    for word in text.split():
        if not word.startswith("www"):
            urlfree.append(word)
        elif not word.startswith("http"):
            urlfree.append(word)
        elif not word.endswith(".html"):
            urlfree.append(word)
    urlfree = " ".join(urlfree)

    urls = re.finditer(r'http[\w]*:\/\/[\w]*\.?[\w-]+\.+[\w]+[\/\w]+', urlfree)
    for i in urls:
        urlfree = re.sub(i.group().strip(), '', urlfree)
    return urlfree


def remove_alphanumerics(text):
    """
    Remove alphanumeric words from text
    Example: hello man whatsup123 => hello man
    Args:
        text (str): text
    Returns:
        text (str): text with removed alphanumeric words
    """
    txt = []
    for each in text.split():
        if not any(x in each.lower() for x in "0123456789"):
            txt.append(each)
    txtsent = " ".join(txt)
    return txtsent 


def remove_words_start_with(text, starts_with_char):
    """
    Remove words start with character `starts_with_char`
    Example: dhoni rocks with last ball six #dhoni #six => dhoni rocks with last ball six (start_char_with='#')
    Args:
        text (str): text
        starts_with_char (str): starting characters of word, which to be removed from text

    Returns:
        text (str): text with removed words start with given chars
    """
    urls = re.finditer(starts_with_char + r'[A-Za-z0-9\w]*', text)
    for i in urls:
        text = re.sub(i.group().strip(), '', text)
    return text.strip()

def remove_stop_words(text, stop_words=stop_words_list):
    """
    This function removes stop words from text
    Example: I am very excited for today's football match => very excited today's football match
    Params
        text (str) :text on which processing needs to done
        stop_words (list) : stop words which needs to be removed
    Returns
        text(str): text after stop words removal
    """
    stop_words = set(stop_words)
    split_list = text.split(" ")
    split_list = [word for word in split_list if word not in stop_words]
    return " ".join(split_list)
