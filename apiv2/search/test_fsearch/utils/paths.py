import os

TXT_FILE = os.path.join(os.path.dirname(__file__),
                        '../data/new_test_q.txt')
MQID_PICKLE_FILE = os.path.join(os.path.dirname(__file__),
                                '../data/new_map_qids.pickle')
QID_PICKLE_FILE = os.path.join(os.path.dirname(__file__),
                               './data/new_qids.pickle')
INFO_FILE = os.path.join(os.path.dirname(__file__),
                         '../data/testdata_info.txt')
JSON_FILE = os.path.join(os.path.dirname(__file__), '../data/%s') + ".json"