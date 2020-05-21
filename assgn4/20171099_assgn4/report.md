# 20171099 - Assignment 4 LD2
## URL of Model
[Model URL](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/harshita_sharma_research_iiit_ac_in/ET9pPPisEkxEtTfHWCzvygABl177uAf-lGgDUMCW-OPGTw?e=oTuEN9)

## How to run:
- [requirements.txt](./requirements.txt) attached
- Run `python3 test_file.py <location of modal> <location of test corpus>`
- If running in same folder: Run `python3 test_file.py ./annCorra_crf_all_features_model ./final_test_corpus.txt`

## Output:
- Output will be written to a file named `20171099_output.txt`.
- Attaching output file with a different name just for safety: [Output file](./output.txt)

## Evaluation scores:
- Accuracy: 0.876
- F1 score on Test Data: 0.873
- Precision score on Test Data: 0.873
- Recall score on Test Data: 0.876

## Features Used:
- word
- lemma
- isFirstWord
- isLastWord
- previous word
- next word
- prev to prev word
- next to next word
- isNumeric
- isAlphanumeric
- POS tag
- TAm label
- Gender
- Number
- Person
