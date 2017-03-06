const BASE_URL = "http://localhost:8000/apiv2"
const URL = {
    URL_BASE: BASE_URL,
    TEST_QUESTION: BASE_URL + '/test_questions',
    SEARCH_TEXT: BASE_URL + '/questions/search/q?=',
    SEARCH_FORMULA: BASE_URL + '/questions/search/type=f&q?=',
    TESTSEARCH_TEXT: BASE_URL + '/questions/search/q?=',
    TESTSEARCH_FORMULA: BASE_URL + '/questions/search/type=f&q?=',
    GET_FORMULA_CATEGORIES: BASE_URL + '/test_formula_categories/',
    GET_TEST_FORMULAS: BASE_URL + '/test_formulas/',
    CHECK_MATHML: BASE_URL + '/check_mathml/',
    CREATE_UPDATE_TEST_FORMULA: BASE_URL + '/create_update_test_formula/',
    DELETE_TEST_FORMULA: BASE_URL + '/delete_test_formula/',
    REINDEX_TEST_FORMULA: BASE_URL + '/reindex_test_formula/',
    LOGIN: BASE_URL + '/auth/login/',
    LOGOUT: BASE_URL + '/auth/logout/',
    SEARCH_TEST_FORMULA: BASE_URL + '/search_test_formula/'
}

export default URL;