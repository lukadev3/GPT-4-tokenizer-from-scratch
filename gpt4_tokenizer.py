from tokenizer import merge, get_stats, Tokenizer
import regex as re

# Function to update the statistics dictionary with counts from a new counts dictionary
def update_stats(stats: dict, counts: dict):
    for (pair1, pair2), count in counts.items():
        if stats.get((pair1, pair2)) is None:
            stats[pair1, pair2] = counts[pair1, pair2]
        else:
            stats[pair1, pair2] += counts[pair1, pair2]

# Class for the GPT-4 tokenizer
class Gpt4Tokenizer(Tokenizer):
    def __init__(self) -> None:
        super().__init__()
        # The pattern is copied from the official GitHub page for GPT tokenizers
        self.patern = r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""

    # Method to train the tokenizer on the given text with a specified vocabulary size
    def train(self, text , vocab_size):
        num_of_merges = vocab_size - 256  # Calculate the number of merges needed
        code = 256  # Initial code value
        text_chunks = re.findall(self.patern, text)  # Find text chunks using the specified pattern
        ids = [list(chunk.encode("utf-8")) for chunk in text_chunks]  # Encode chunks as lists of bytes
        print("PRE BPE ALGORITMA")  # Print a message before the BPE algorithm
        print(ids)  # Display the initial ids
        while num_of_merges > 0:
            stats = {}  # Initialize a statistics dictionary
            for chunk_id in ids:
                counts = get_stats(chunk_id)  # Get statistics for the current chunk
                update_stats(stats, counts)  # Update the statistics with new counts
            # Sort statistics in descending order based on the count
            stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=True))
            first_pair = next(iter(stats))  # Get the first pair from the sorted statistics
            # Merge the first pair across all chunk ids
            for i, chunk_id in enumerate(ids):
                new_id = merge(chunk_id, first_pair, code)
                ids[i] = new_id
                self.merges[first_pair] = code  # Update the merges dictionary
            code += 1  # Increment the code for the next merge
            num_of_merges -= 1  # Decrement the number of merges remaining
        self.vocab = self.build_vocab()  # Build the vocabulary based on the merges
        print("NAKON BPE ALGORITMA")  # Print a message after the BPE algorithm
        return ids  # Return the final ids
            
    
    # Method to decode a list of ids back to a string
    def decode(self, ids):
        word_list = []  # Initialize a list to store words
        for id in ids:
            text_bytes = b"".join(self.vocab[idx] for idx in list(id))  # Join bytes to form the text
            text = text_bytes.decode("utf-8", errors="replace")  # Decode bytes to string
            word_list.append(text)  # Append the decoded text to the word list
        result = ''.join(word_list)  # Join all words to form the final result
        return result  # Return the final decoded string

    # Method to encode a given text into a list of ids
    def encode(self, text):
        text_chunks = re.findall(self.patern, text)  # Find text chunks using the specified pattern
        ids = [list(chunk.encode("utf-8")) for chunk in text_chunks]  # Encode chunks as lists of bytes
        for (pair1, pair2), code in self.merges.items():  # Iterate through each pair in merges
            for i, id in enumerate(ids):
                id = merge(id, (pair1, pair2), code)  # Merge the current id with the pair
                ids[i] = id  # Update the ids list with the new id
        return ids  # Return the encoded ids
