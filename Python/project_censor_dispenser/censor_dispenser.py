# 1. Censor some text and then return the censored text
def censor_text_single(text):
    proprietary_term = 'learning algorithms'
    return text.replace(proprietary_term, '*****')

# 3. Censor some text and return the censored text -- multiple items
def censor_text_multiple(text):
    proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
    return text.lower().replace(proprietary_terms[0], '*****').replace(proprietary_terms[1], '*****').replace(proprietary_terms[2], '*****').replace(proprietary_terms[3], '*****').replace(proprietary_terms[4], '*****').replace(proprietary_terms[5], '*****').replace(proprietary_terms[6], '*****')

# 4. Censor 'negative words', after two occurrences
def censor_negative_words(text):
    negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]


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
