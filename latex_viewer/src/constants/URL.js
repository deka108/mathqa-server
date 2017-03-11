const BASE_URL = "http://localhost:8000/apiv2"
const URL = {
    URL_BASE: BASE_URL,

    SEARCH: BASE_URL + '/search/',
    GET_SOLUTIONS: BASE_URL + '/solutions/',
    GET_QUESTIONS: BASE_URL + '/questions/',
    GET_KEYPOINTS: BASE_URL + '/keypoints/',
    SEARCH_DB: BASE_URL + '/search/?type=d&query=',
    SEARCH_FULL_TEXT: BASE_URL + '/search/?type=t&query=',
    SEARCH_FORMULA: BASE_URL + '/search/?type=f&query=',
    SEARCH_FORMULA_POST: BASE_URL + '/search_formula_post/',
    SEARCH_FORMULA_GET: BASE_URL + '/search_formula_get/?query=',
    GET_FORMULA_CATEGORIES: BASE_URL + '/formula_categories/',
    GET_FORMULAS: BASE_URL + '/formulas/',
    CREATE_UPDATE_FORMULA: BASE_URL + '/create_update_formula/',
    UPDATE_QUESTION: BASE_URL + '/update_question/',
    UPDATE_SOLUTION: BASE_URL + '/update_solution/',
    UPDATE_KEYPOINT: BASE_URL + '/update_keypoint/',
    DELETE_FORMULA: BASE_URL + '/delete_formula/',
    REINDEX_FORMULA: BASE_URL + '/reindex_all_formula/',

    TEST_QUESTION: BASE_URL + '/test_questions/',
    TESTSEARCH_TEXT: BASE_URL + '/test_questions/search/query?=',
    SEARCH_TEST_FORMULA: BASE_URL + '/search_test_formula/',
    GET_TEST_FORMULA_CATEGORIES: BASE_URL + '/test_formula_categories/',
    GET_TEST_FORMULAS: BASE_URL + '/test_formulas/',
    CREATE_UPDATE_TEST_FORMULA: BASE_URL + '/create_update_test_formula/',
    DELETE_TEST_FORMULA: BASE_URL + '/delete_test_formula/',
    REINDEX_TEST_FORMULA: BASE_URL + '/reindex_test_formula/',

    GET_FORMULA_CATEGORIES: BASE_URL + '/formula_categories/',
    CHECK_MATHML: BASE_URL + '/check_mathml/',

    LOGIN: BASE_URL + '/auth/login/',
    LOGOUT: BASE_URL + '/auth/logout/',
}

export default URL;