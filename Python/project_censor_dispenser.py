# 1. Censor some text and then return the censored text
def censor_text_single(text):
    proprietary_term = 'learning algorithms'
    return text.replace(proprietary_term, '*****')

# 3. Censor some text and return the censored text -- multiple items
def censor_text_multiple(text):
    proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
    return text.lower().replace(proprietary_terms[0], '*****').replace(proprietary_terms[1], '*****').replace(proprietary_terms[2], '*****').replace(proprietary_terms[3], '*****').replace(proprietary_terms[4], '*****').replace(proprietary_terms[5], '*****').replace(proprietary_terms[6], '*****')

# 4. Censor 'negative words', after two occurrences


# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# 2. censor the first email
email_one_censored = censor_text_single(email_one)
print(email_one_censored)

print('\n\n')

# 3. Cencsor email 2
email_two_censored = censor_text_multiple(email_two)
print(email_two_censored)

print('\n\n')

# 4. Tone down the negative words
print('Censoring negative words: ')

def censor_text_negative_words_multiple(text):
  negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

  # this string is meant for holding a modified version of itself; anytime we need to censor a word, we need to change the string somehow
  string_to_modify = ""
  # circulate through every word in the list and check if it occurs more than once. If so, censor the word.
  lst_of_strings = text.split(' ')
  for current_word in negative_words:
    # go through all of the text
    for val in lst_of_strings:
      count = 0
      if current_word == val.lower():
        count += 1
      if count > 1:
        string_to_modify = text.replace(current_word, '******')

  return string_to_modify
string_received = censor_text_negative_words_multiple(email_three)
if len(string_received) < 1:
  print('Nothing was received.')
