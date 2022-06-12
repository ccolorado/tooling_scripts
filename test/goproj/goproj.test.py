import unittest
import tempfile
from ...scripts.goproj import ProjectList

class GoprojTest(unittest.TestCase):

    def test_is_valid_uri_validates_path_exists(self):
        inexistent_path = '/notExistenDir/tmp'
        # existing_path = '/tmp'
        existing_path = tempfile.TemporaryFile()
        pprint.pprint(existing_path.name)

        should_be_false = ProjectList.is_valid_uri(inexistent_path)
        should_be_true = ProjectList.is_valid_uri(existing_path.name)

        self.assetFalse(should_be_false)
        self.assetTrue(should_be_true)

    def test_is_valid_url_validates_path_is_directory(self):

        existing_path = tempfile.TemporaryDirectory()
        pprint.pprint(existing_path.name)

        should_be_false = ProjectList.is_valid_uri(inexistent_path)
        should_be_true = ProjectList.is_valid_uri(existing_path.name)
        self.assetFalse(should_be_false)

        self.assetTrue(should_be_true)

    # def test_key_exists_validates_key_exists():
    # def test_save_stores_list_in_file():
    # def test_save_stores_list_in_correct_order():
    # def test_save_respect_commented_projects
    # def test_read_project_list_matches_source_file
    # def test_read_project_list_respects_commented_projects
    # def test_get_project_list_contains_project_number():
    # def test_get_project_list_contains_project_key():
    # def test_get_project_list_contains_project_url():
    # def test_print_list_matches_expected_output():
    #    """ https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
    # def test_project_number_to_project_key_finds_project_key_from_project_number
    # def test_get_projects_matching_only_match_projects_containing_word
    # def test_get_projects_matching_only_match_projects_containing_words
    # def test_add_project_adds_project_to_top_of_the_list
    # def test_delete_project
    # def test_get_opts_matches_-d
    # def test_get_opts_matches_--delte
    # def test_get_opts_matches_-a
    # def test_get_opts_matches_--add
    # def test_get_opts_matches_-b
    # def test_get_opts_matches_--bump
    # def test_get_opts_matches_GOTO

    # test:
    # find project
    # project exists
    # number to key
    # key to number




