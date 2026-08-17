from src.assistant import ask_nova


def test_nova_responds():
    response = ask_nova("Hello Nova")
    assert response
    
    
def test_ask_nova_returns_text():
    result = ask_nova("Say hello in one sentence.")
    assert isinstance(result, str)
    assert len(result) > 0