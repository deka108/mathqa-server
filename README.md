# Meas Development

## Running Latex Viewer
1. Install Node.js and npm
2. Install jspm and live-server via npm
3. cd to latex_viewer directory
4. Run `jspm install`
5. Run `live-server .` -> starts a node.js server at http://localhost:8080
6. Navigate to different html views by clicking the link inside the side-navigator or by manually appending the html layout to the hostname:
http://localhost:8080/[page].html

## Loading data
1. The data used for this project is stored inside db_save.json
2. Load it using `python manage.py loaddata db_save.json` command

## Models and APIs
1. The model and the APIs are developed under apiv2 module
2. The REST APIs are available under the `apiv2/urls.py`
3. APIs for accessing models in general:
  - `/apiv2/[object]s/`: retrieve all objects from the database
  - `/apiv2/[object]s/[object_id]`: retrieve 1 object from the database based on object id
  - Advanced filtering methods are also available with the help of filters. To views the available filter, please look inside `apiv2/views.py` module. Example of this filtered contents:
  `/apiv2/questions/?concept=1` --> retrieve all questions that have the same concept id=1
4. APIs for Searching:
  - `/apiv2/search/?type=d&query=[query]` for database search
  - `/apiv2/search/?type=t&query=[query]` for full-text search (using Haystack)
  - `/apiv2/search/?type=f&query=[query]` for formula search

## Mathematical Document Retrieval
The three types of mathematical document retrieval are supported, which include `search_database`, `search_text` and `search_formula` methods.  These implementation can be found under `apiv2/views.py`
1. `search_database` method performs raw text retrieval using Django icontains queryset
2. `search_text` method performs full-text search using Django Haystack. Both the data and query is first preprocessed   using `apiv2/search/utils/text_util.py` module
3. The related formula search implementation methods is available under apiv2/search/fsearch directory. This module composed of 4 main modules:
  - `formula_features_extractor.py`: extract formula terms from raw latex syntax (excluding the delimiters such as $$ latex $$, $ latex $, \[ latex \] or \( latex \). If these delimiters exist, extract it first using formula_extractor module
  - `formula_extractor.py'`: extract raw latex string from latex delimiters
  - `formula_indexer.py`: creates inverted formula table (i.e. formula index table) based on existing formula data in the database. 
  - `formula_retriever.py`: performs formula query matching with the formula index table, ranks the results and serve the search results in the form of (formula, question) pair (please refer to the search_formula method under `views.py` and  `serializers.py` module for a better understanding).
