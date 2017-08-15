import tensorflow as tf
from numpy.random import choice as random_choice, randint as random_randint, rand
MAX_INPUT_LEN = 40
AMOUNT_OF_NOISE = 0.2 / MAX_INPUT_LEN
CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .")


tf.app.flags.DEFINE_string("raw_data", "", "Raw data path")
tf.app.flags.DEFINE_string("out_file", "", "File to write preprocessed data "
                                           "to.")

FLAGS = tf.app.flags.FLAGS

def add_noise_to_string(a_string, amount_of_noise):
    """Add some artificial spelling mistakes to the string"""
    if rand() < amount_of_noise * len(a_string):
        # Replace a character with a random character
        random_char_position = random_randint(len(a_string))
        a_string = a_string[:random_char_position] + random_choice(CHARS[:-1]) + a_string[random_char_position + 1:]
    if rand() < amount_of_noise * len(a_string):
        # Delete a character
        random_char_position = random_randint(len(a_string))
        a_string = a_string[:random_char_position] + a_string[random_char_position + 1:]
    if len(a_string) < MAX_INPUT_LEN and rand() < amount_of_noise * len(a_string):
        # Add a random character
        random_char_position = random_randint(len(a_string))
        a_string = a_string[:random_char_position] + random_choice(CHARS[:-1]) + a_string[random_char_position:]
    if rand() < amount_of_noise * len(a_string):
        # Transpose 2 characters
        random_char_position = random_randint(len(a_string) - 1)
        a_string = (a_string[:random_char_position] + a_string[random_char_position+1] + a_string[random_char_position] +
                    a_string[random_char_position + 2:])
    return a_string

def main(_):
    with open(FLAGS.raw_data, "r") as raw_data, \
            open(FLAGS.out_file, "w") as out:
        for line in raw_data:
            preprocessed_line = add_noise_to_string(line,3)
            out.write(preprocessed_line)

if __name__ == "__main__":
    tf.app.run()