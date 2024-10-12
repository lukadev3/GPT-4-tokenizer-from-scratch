from tokenizer import merge, get_stats, Tokenizer

class BasicTokenizer(Tokenizer):
    def __init__(self) -> None:
        super().__init__()  # Initialize the parent class

    # Function in which we train our tokenizer; first we set how much we want to increase our vocabulary (num_of_merges)
    # and the code that we use to encode the sequences we merged;
    # we gather statistics to see how many times each sequence occurs and sort it so that the most frequent is first
    # (we always update this statistic after merging because it can happen that new codes in conjunction with old ones
    # occur the most frequently);
    # then for each pair in our statistics, as long as we do not exceed the set limit for merging,
    # we merge sequences and update our token array and our merge dictionary.
    def train(self, text, vocab_size):
        num_of_merges = vocab_size - 256  # Calculate number of merges based on desired vocabulary size
        code = 256  # Initialize code for new tokens
        ids = list(text.encode("utf-8"))  # Encode the input text to a list of integers
        tokens = ids.copy()  # Create a copy of the encoded list
        print("BEFORE BPE ALGORITHM")
        print(tokens)  # Display tokens before BPE
        counts = get_stats(ids)  # Get statistics of the current tokens
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))  # Sort counts by frequency
        while num_of_merges > 0:  # Continue merging until the limit is reached
            first_pair = next(iter(counts))  # Get the most frequent pair
            tokens = merge(tokens, first_pair, code)  # Merge the pair in tokens
            self.merges[first_pair] = code  # Update the merge dictionary
            counts = get_stats(tokens)  # Update counts after merging
            counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))  # Re-sort counts
            num_of_merges -= 1  # Decrease the number of merges left
            code += 1  # Increment the code for the next merge
        self.vocab = self.build_vocab()  # Build the vocabulary after training
        print("AFTER BPE ALGORITHM")
        return tokens  # Return the final list of tokens


    # Simple function that creates a byte array from our vocabulary
    # and then simply decodes it using utf-8
    def decode(self, ids):
        text_bytes = b"".join(self.vocab[idx] for idx in ids)  # Join bytes from vocab based on ids
        text = text_bytes.decode("utf-8", errors="replace")  # Decode bytes to string
        return text  # Return the decoded string
    

    # This function encodes text into a list of integers and then iterates through it (the condition is that the length of the list 
    # must be greater than two because if it is smaller, there are no pairs); then we go through our merging dictionary and 
    # merge sequences based on our merging list.
    def encode(self, text):
        ids = list(text.encode("utf-8"))  # Encode text to a list of integers
        if len(ids) > 2:  # Ensure there are enough ids to form pairs
            for (pair1, pair2) in self.merges.keys():  # Iterate through merge pairs
                idx = self.merges[(pair1, pair2)]  # Get the index for the current merge
                ids = merge(ids, (pair1, pair2), idx)  # Merge ids based on the pair
        return ids  # Return the encoded list of ids
