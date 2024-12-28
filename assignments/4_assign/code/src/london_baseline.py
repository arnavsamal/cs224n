# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    # Load the dev dataset
    dev_data = utils.load_birth_dev_data()

    # Predict "London" for every example and compute accuracy
    correct_predictions = 0
    total_examples = len(dev_data)

    for question, answer in dev_data:
        prediction = "London"
        if prediction == answer:
            correct_predictions += 1

    accuracy = (correct_predictions / total_examples) * 100.0
    ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
