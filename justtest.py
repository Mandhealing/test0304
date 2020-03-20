def test_passing():
    print('要开始测试了哈')

    yield

    print('测试结束')

    
    assert (1, 2, 3) == (1, 2)