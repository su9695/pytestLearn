import pytest
def pytest_configure(config):
    marker_list = ["slower"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )

