# Lab 4 - Functions and Typing

Functions are a way to reduce code duplication, increase program modularity, and make it easier to debug and fix errors. The goal of this lab is get you comfortable with defining and invoking functions as well as a little bit of problem solving.

## Step 1 - Setup

The first thing I want you to do is to create a new folder in the `labs` folder called `functions`. In that folder I want you to create 2 new files; `functions.py` and `test_functions.py`. Copy all of the code in my version of `test_functions.py` into your file. Your `functions.py` file should be blank as we are going to define our functions in there.

## Step 2 - Functions

1. The first function I want you to define will be named `join_strings`. This function has a single parameter which is a list called `strings`. This goal of this function is to iterate through the list of strings and combine them into a single string with no spaces separating them and `return` it the caller.

2. Consider the following mad lib:

   > { name } is too cool for { noun } class. Instead she/he will be attending the { event }.

   Your task is to create a function called `mad_lib` that has three (3) string parameters; `name`, `noun`, and `event`. Using string concatenation or interpolation, this function is to return the mad lib above with parameters as substitution text.

3. In cryptography, one of the simplest forms of encryption is known as the _Caesar cipher_. The Caesar cipher is named after Julius Caesar and would use it to encrypt important military messages around the year 100 BC. The way the cipher works is letters in the message are shifted by positive or negative value. When encrypting, the letter `Y` with a shift of `+3` would then become `B`, a the letter `D` with a shift of `-3` will be `A`. Your task is to create a function called `caesar_cipher` that has two (2) parameters; `text` and `shift`. Encrypt the `text` by iterating through it and for each character find the shifted character and add it to a new string called `cipher_text` and once you are finished, return it. The decryption is done by passing in the encrypted text with the same shift used to encrypt it except negated.

   - For each character in the `text` passed in; find the index of it in the alphabet (0-25).
   - Calculate the shift of the index of that character and get the new character from the alphabet.
   - Concatenate that character to the end of our return value.

   __Note__: You are probably thinking; what happens if the shift is 4 and the character is `z`? Well you would have to wrap back around to the beginning of the alphabet. Use mod (or the % operator) to make sure you don't go out of bounds! For example: the index of the character `z` is 25 and if the shift is 4 that gives us 29, but there is not 29th character in the sequence! Well 29 % 26 will give us 3 which is the correct index of the character we want. The same goes for negatives; -3 % 26 gives us 23. Mod is an __incredibly powerful__ tool in cryptography.

   Now go be a hacker and encrypt/decrypt some text!

   ![hacker](https://i.imgflip.com/49h71v.png?a465168)

## Step 3 - Testing our work

If you want to test your work as you are developing; create a new file called `main.py` inside the `functions` folder and at the top of the `main.py` file, import your code from the functions module and test your functions. You can do this like so:

```py
# top of file.
from functions import *
plain_text = "hello, world!"
cipher_text = caesar_cipher(plain_text, -15)
deciphered_text = caesar_cipher(cipher_text, 15)

print(f"The cipher text of {plain_text} is {cipher_text}.")
print(f"When we decipher {cipher_text} we get {deciphered_text}.")
print(f"Are they equal?: {plain_text == deciphered_text}")
```

And then you can just simply run the code from the command line.

```sh
# cd'd into the functions folder in our repository.
python3 main.py
```

You can also test that your code is working properly by activating your python virtual environment and running the `pytest` command.

## Step 4 - Finishing up

Once your code passes all of the `pytest` unit tests you may now submit your work. Copy the output of the `pytest` command with all passing test cases from this lab and previous labs and paste the results in the submissions box for lab 4 on iLearn.

Good job everyone!

![Alt Text](https://i.imgur.com/plJGnCb.gif)