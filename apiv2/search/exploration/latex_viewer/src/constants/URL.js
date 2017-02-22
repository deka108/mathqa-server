const BASE_URL = "http://localhost:8000/apiv2"
const URL = {
    TEST_QUESTION: BASE_URL + '/test_questions',
    SEARCH_TEXT: BASE_URL + '/questions/search/q?=',
    SEARCH_FORMULA: BASE_URL + '/questions/search/type=f&q?=',
    TESTSEARCH_TEXT: BASE_URL + '/questions/search/q?=',
    TESTSEARCH_FORMULA: BASE_URL + '/questions/search/type=f&q?=',
}

export default URL;