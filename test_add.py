import add


def test_add(mocker):
    # mocked_add = mocker.patch.object(Slackbot, "add")
    # mocked_add.return_value = 3

    assert add.add(2, 3) == 5
    assert add.add(0, 1) == 1
    assert add.add(-3, 3) == 0

    assert add.add("1", "2") == 3
