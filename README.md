# Custom Tokenizer

## Overview

This project implements a custom tokenizer using Byte Pair Encoding (BPE). The tokenizer is designed to efficiently encode and decode text by merging frequently occurring pairs of characters or byte sequences. It can handle input text by converting it into a list of integer representations, allowing for easier processing in machine learning tasks and natural language processing.

## Project Structure

The project contains the following files:

1. **`tokenizer.py`**: This file contains the core functionality of the tokenizer, including:
   - **`Tokenizer` class**: The base class for the tokenizer, which includes methods for merging sequences, gathering statistics on occurrences, and building a vocabulary.
   - **`get_stats` function**: Computes the frequency of adjacent pairs in a given list of integers.
   - **`merge` function**: Merges two adjacent numbers in the list with a specified index.
   
2. **`gpt4_tokenizer.py`**: This file contains a subclass of `Tokenizer` designed specifically for use with the GPT-4 model. It implements:
   - **`train` method**: Trains the tokenizer on the provided text and updates the vocabulary.
   - **`encode` method**: Encodes input text into integer sequences based on the trained merges.
   - **`decode` method**: Decodes the integer sequences back into text.

3. **`basic_tokenizer.py`**: This file includes another subclass of `Tokenizer` that implements basic functionalities for training, encoding, and decoding text using BPE.

## Features

- **Byte Pair Encoding (BPE)**: Merges pairs of characters based on their frequency of occurrence in the input text.
- **Encoding and Decoding**: Converts text to integer sequences and back to text using UTF-8 encoding.
- **Custom Vocabulary**: Builds a vocabulary based on the first 256 ASCII characters and dynamically updates it based on merged pairs.

## Future Plans

I plan to update the code in the future to handle special characters more effectively. This will enhance the tokenizer's ability to process a wider range of text inputs.

## Motivation

The motivation for this project stemmed from two insightful YouTube videos by [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy), which provided a deep dive into the principles of LLM, tokenization and BPE. I highly recommend watching these videos for a better understanding of the concepts discussed in this project:

1. [Video 1](https://www.youtube.com/watch?v=zduSFxRajkE&t=6s)
2. [Video 2](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=5s)

Credit for the inspiration behind this project goes to the creator of these videos, whose work has greatly motivated and inspired me to develop this code.

## Usage

To use the tokenizer, simply call the `train`, `encode`, or `decode` methods from the `Tokenizer` class. Ensure you have the required input text and specify the vocabulary size as needed.
