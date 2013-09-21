''' This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>. '''

# This is a basic English to Pig Latin translator with
# simple validation checks.

# First setup our varibles to be used later
pyg = 'ay'
word = ''
first = ''
vowels = ["a", "e", "i", "o", "u"]
word_length = ''
spliced_word = ''
new_word = ''

original = raw_input('Enter a word:')

# start our if condition and validate that the word supplied
# isn't empty and is only charcters with no numbers

if len(original) > 0 and original.isalpha():
    # convert the word to lower case
    word = original.lower()
    # splice the first letter from the word for checking against the list of vowels
    first = word[0]

    # Check if the first letter is a vowel then conentate it with 'pyg' varible
    if first in vowels:
        new_word = word + pyg

         # Print the translated word to the console
        print new_word

    # If the first letter is a consonant then translate directly to pig latin
    else:
        # Find the length of the word (total amount of characters)
        word_length = len(original)

        # Use the length to splice the word from the 2nd character to the last
        spliced_word = word[1:word_length]

        # Now re-arrange the word to complete the pig latin translation
        new_word = spliced_word + first + pyg

        # Print the translated word to the console
        print new_word
else:
    print "That's not an English word!"