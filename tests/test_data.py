from fruitpedia.data import get_fruit_info

def test_get_fruit_info():
    result = get_fruit_info("Banana")
    assert "potassium" in result["nutrients"]



