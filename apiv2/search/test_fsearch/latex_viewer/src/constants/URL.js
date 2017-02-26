const BASE_URL = "http://localhost:8000/apiv2"
const URL = {
    TEST_QUESTION: BASE_URL + '/test_questions',
    SEARCH_TEXT: BASE_URL + '/questions/search/q?=',
    SEARCH_FORMULA: BASE_URL + '/questions/search/type=f&q?=',
    TESTSEARCH_TEXT: BASE_URL + '/questions/search/q?=',
    TESTSEARCH_FORMULA: BASE_URL + '/questions/search/type=f&q?=',
    GET_FORMULA_CATEGORIES: BASE_URL + '/test_formula_categories/',
    GET_TEST_FORMULAS: BASE_URL + '/test_formulas/',
    UPDATE_TEST_FORMULA: BASE_URL + '/update_test_formula/',
    CHECK_MATHML: BASE_URL + '/check_mathml/',
    // CHECK_FORMULA_TOKEN: BASE_URL + '/check_formula_token/',
    // POST_TEST_FORMULA: BASE_URL + '/create_test_formula/',
    CUD_TEST_FORMULA: BASE_URL + '/cud_test_formula/',
}

export default URL;