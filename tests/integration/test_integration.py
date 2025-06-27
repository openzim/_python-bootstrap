# pyright: strict, reportUnusedExpression=false

from great_project import get_env_value


# a fake test needing a value from environment variable secret to complete properly
def test_environ():
    assert get_env_value("A_SECRET_VALUE_FROM_ENV") == "A_SECRET_VALUE_FROM_ENV"
