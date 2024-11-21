import pytest
import pyspark
from lib.Utils import get_spark_session


@pytest.fixture(scope='session')
def spark():
    #print("PySpark version in test: ", pyspark.__version__)
    return get_spark_session("LOCAL")


def test_blank_test(spark):
    print("PySpark version:::::::::::::::",spark.version)
    assert spark.version == "3.3.0"


