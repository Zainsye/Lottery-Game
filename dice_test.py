import dice

def test_dice_game():
    total = 0
    n = 100
    for i in range(n):
        total += dice.simulate_game()
    average = total / n
    print(f'average = {average}')
    assert 0.31 <= average <= 0.33
