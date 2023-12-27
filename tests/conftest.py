import pytest

from credit_scoring_model.config.core import config
from credit_scoring_model.processing.data_manager import load_test_dataset


@pytest.fixture()
def sample_input_data():
    return load_test_dataset(file_name=config.app_config.data_file_test)
