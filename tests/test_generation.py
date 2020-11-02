import pytest

from soccergen.generate import gen_data


class TestDataGeneration:
    """ Class to test data generation
    """

    def setup_class(self):
        """ Setup class by creating base environment
        """
        pass

    def teardown_class(self):
        """ Teardown class
        """
        pass

    def test_list_output(self):
        """ Tests if outputted states are a list
        """
        output_list = gen_data()
        assert type(output_list) == list
