# ComputorV1

____

The purpose of this project is to make you code a program that solves simple equations. The program takes a polynomial equation. That is to say, involving only powers, no complicated functions. The program should display its solution(s).

## Run

	python3 computorv1.py <calculation string>

## Samples

	> python3 computorv1.py "5 * X^0 + 4 * X^1 = 4 * X^0"
	Reduced form: 1 * X^0 + 4 * X^1 = 0
	Polynomial degree: 1
	The solution is:
	-1 / 4 = -0.25

	> python3 computorv1.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
	Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
	Polynomial degree: 2
	Discriminant: 164.8
	Discriminant positive, the two solutions are:
	-16.837445228704972 / -18.6 = 0.9052389907905898
	8.83744522870497 / -18.6 = -0.47513146390886934

	> python3 computorv1.py "8 * X^0 - 6 * X^18 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
	Reduced form: 5 * X^0 -  5.6 * X^3 - 6 * X^18 = 0
	Polynomial degree: 18
	The polynomial degree is strictly greater than 2, I can't solve

____

If you have any questions or suggestions, feel free to send me an email at squiquem@student.42.fr
