#!/usr/bin/python3
"""0-nqueens"""
import sys


def queens_prob(board_size):
    """Solves nqueens problem"""

    def valid_position(position, occupied_pos):
        """checks if position is valid"""
        for i in range(len(occupied_pos)):
            if (
                occupied_pos[i] == position or
                occupied_pos[i] == position - len(occupied_pos) or
                occupied_pos[i] + i == position + len(occupied_pos)
            ):
                return False
        return True

    def queens_pos(board_size, i, occupied_pos, solutions):
        """place queens"""
        if i == board_size:
            solutions.append(occupied_pos[:])
            return
        for i in range(board_size):
            if valid_position(i, occupied_pos):
                occupied_pos.append(i)
                queens_pos(board_size, i + 1, occupied_pos, solutions)
                occupied_pos.pop()

    solutions = []
    queens_pos(board_size, 0, [], solutions)
    return solutions


def main():
    """main function"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = queens_prob(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == '__main__':
    main()
