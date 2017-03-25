# -*- coding: utf-8 -*-
from collections import Counter
import re
import string

printable = set(string.printable)
ORIGINAL_TEXT =  "A curve has the equation y = 2 sin 2 x - 3 cos x = 2 sin 2 x − 3 cos x.  (i) Find the gradient of the curve when x= ​π / ​6. (ii) Given that x is increasing at a constant rate of 0.0006 units per second, find the rate of change of y when x = ​π / 6​​​ ."

TEXTS = {
    "tesseract_nop": r"""A curve has the equation
:1] : 25in2x 7 3cosz

m Find the gradient of the curve when
7r
1 7 E

(ii) Given that x is increasing at a constant rnLn of 0.0006 units pm swund. ﬁnd aha mlr-”Mum , MM»

7 I
r ’ 6

""",
    "tesseract_leptonica": r"""
   A curve has the equation
y : 23mm; — 30052

0) Find the gradient of me curve when
1r
1 # 6

(ii) Given that x is increasing at a constant rate of 0.0006 units pnr second, ﬁnd the rate or Chung! oly when

7 I
a” ’ s
""",
    "tesseract_catalano": r"""
1A curve has the equation
3/ : 25in2z 7 36052

m Find the gradient of the curve when
7r
1 7 E

(ii) Given that x is increasing at a constant rain of 0.0006 units pm SUCUHLL ﬁnd :hv mu»Alfrhimur i v , w n

7 I
r ’ 6

""",
    "google_text_api": r""" 
   A curve has the equationee 2 sin 2r - 3 cos z(i) Find the gradient of the curve whenG) Given that x is increasing at a constant rate of 0.0006 units per second, find the rate of change of y when

"""
}

def compute_char_freq(text):
    text = ''.join(text.split())
    all_chars = list(text)
    char_counts = Counter(all_chars)
    return char_counts

def compute_precision(tp, fp):
    try:
        return tp * 1.0 / (tp + fp)
    except:
        return 0

def compute_recall(tp, fn):
    try:
        return tp * 1.0 / (tp + fn)
    except: 
        return 0

def compute_f1(tp, fp, fn):
    try:
        return 2 * tp / (2 * tp + fp + fn)
    except:
        return 0


def evaluate_text(original_text, ocr_text):
    original_text = filter(lambda x: x in printable, original_text)
    ocr_text = filter(lambda x: x in printable, ocr_text)
    ori_counts = compute_char_freq(original_text)
    ocr_counts = compute_char_freq(ocr_text)

    print(ori_counts)
    print(ocr_counts)

    for ch in ori_counts:
        if ch in ocr_counts:
            ocr_counts[ch] -= ori_counts[ch]
        else:
            ocr_counts[ch] = -ori_counts[ch]
    
    
    recognised = {}
    tp = "TP = {}"
    
    # filter = 0
    fully_recognised = {k:tp.format(ori_counts[k]) for k, v in ocr_counts.items() if v == 0}
    TP  = sum([ori_counts[k] for k,v in ocr_counts.items() if v == 0])
    
    # filter > 0
    fp = ", FP = {}"
    false_positives = {k:tp.format(ori_counts.get(k, 0)) + fp.format(v) for k, v in ocr_counts.items() if v > 0}
    FP  = sum([v for k,v in ocr_counts.items() if v > 0])
    TP += sum([ori_counts.get(k, 0) for k,v in ocr_counts.items() if v > 0])

    # # filter < 0    
    fn = ", FN = {}"
    false_negatives = {k:tp.format(ori_counts[k] + v) + fn.format(-v)  for k, v in ocr_counts.items() if v < 0}
    FN = sum([-v for k, v in ocr_counts.items() if v < 0])
    TP += sum([ori_counts.get(k) + v for k,v in ocr_counts.items() if v < 0])

    print("fully recognised")
    print(fully_recognised)
    print("false positives")
    print(false_positives)
    print("false negatives")
    print(false_negatives)

    print("True Positives: {}".format(TP))
    print("False Positives: {}".format(FP))
    print("False Negatives: {}".format(FN))

    print("Precision: {}".format(compute_precision(TP, FP)))
    print("Recall: {}".format(compute_precision(TP, FN)))
    print("F1: {}".format(compute_f1(TP, FP, FN)))


if __name__ == "__main__":
    for ocr_config in TEXTS:
        print("Results for {}".format(ocr_config))
        evaluate_text(ORIGINAL_TEXT, TEXTS[ocr_config])