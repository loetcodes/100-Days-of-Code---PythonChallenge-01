"""
Day 26 - Managing High scores

Exercism


Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive games of all time, and a classic of the arcade era. Your task is to write methods that return the highest score from the list, the last added score and the three highest scores.

In this exercise, you're going to use and manipulate lists. Python lists are very versatile, and you'll find yourself using them again and again in problems both simple and complex.

"""
def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
	best_scores = sorted(scores, reverse=True)
	if len(best_scores) > 3:
		return [best_scores[x] for x in range(3)]
	return best_scores


def test_case(given, expected):
	if given != expected:
		raise Exception ("Given", given, "Expected", expected)



def main():
	test_case(personal_top_three([20, 10, 30]), [30, 20, 10])
	test_case(personal_top_three([40]), [40])
	test_case(personal_top_three([40, 20, 40, 30]), [40, 40,30])
	test_case(personal_top_three([20, 10, 30]), [30, 20, 10])
	test_case(personal_top_three([30, 80, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]), [100, 80, 70])
	test_case(personal_top_three([40]), [40])
	test_case(personal_best([40, 100, 70]),100)
	test_case(latest([100, 0, 90, 30]),30)


if __name__ == "__main__":
	main()