# Text Preprocessing Tool

Here is a text preprocessing tool designed in python to save you from preprocessing tasks that you need to completed before performing any NLP task. 



## List of methods

- **appos_look_up** : Convert apostrophes word to original form  
  - `Example : I don't know what is going on => I do not know what is going on?`
- **remove_repeated_characters** : Remove repeated characters (>2) in words to max limit of 2
  - `Example: I am verrry happpyyy today => I am verry happyy today`
- **separate_digit_text** :  Splits alphanumeric words into digits and text.
  - `Example: I will be booking tickets for 2adults => I will be booking tickets for 2 adults`
- **slang_look_up** : Replace slang word in text to their original form
  - `Example: hi, thanq so mch => hi, thank you so much`
- **stem_text** : Convert words in text into their root form
  - `Example: I am playing in ground => I am play in ground`
- **remove_single_char_word**: Remove single character word from text
  - `Example: I am in a home for 2 years => am in home for`
- **remove_punctuations**:  Removed special characters from text
  - `Example: he: I am going. are you coming? => he I am going. are you coming`
- **remove_extra_space**: Remove extra white spaces space from text
  - `Example: hey are   you coming. ? => he are you coming. ?`
- **replace_digits_with_char**: Replace digits to `replace_char`
  - `Example: I will be there on 22 april. => I will be there on dd april.`
- **emoticons_look_up**: Remove emoticons from text and returns list of emotions present in text
  - `Example: Sure, you are welcome :) => Sure, you are welcome.`
- **remove_url**: Remove urls from text
  - `Example: link to latest cricket score. https://xyz.com/a/b => link to latest cricket score.`
- **remove_alphanumerics**: Remove alphanumeric words from text
  - `Example: hello man whatsup123 => hello man`
- **remove_words_start_with**: Remove words start with character `starts_with_char`
  - `Example: dhoni rocks with last ball six #dhoni #six => dhoni rocks with last ball six (start_char_with='#')`
- **remove_stop_words**: This function removes stop words from text
  - `Example: I am very excited for today's fotball match => very excited today's fotball match`


**Note**: Anyone can contribute to the project by adding more to the preprocessing module Thanks :)

