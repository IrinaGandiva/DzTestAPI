def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Target url"
    )
    parser.addoption(
        "--status_code",
        default=200,
        type=int,
        help="Target status_code"
    )
