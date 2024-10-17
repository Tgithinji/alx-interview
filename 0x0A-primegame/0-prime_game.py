def sieve_of_eratosthenes(limit):
    """Sieve of Eratosthenes algorithms"""
    prime_numbers = [True] * (limit + 1)
    prime_numbers[0] = prime_numbers[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if prime_numbers[i]:
            for multiple in range(i * i, limit + 1, i):
                prime_numbers[multiple] = False

    # Return list of prime numbers
    return prime_numbers


def prime_game(n, prime_numbers):
    """Simulates one game and returns the winner"""
    moves = 0
    # True means the number is still in the set
    remaining = [True] * (n + 1)

    for i in range(2, n + 1):
        if prime_numbers[i] and remaining[i]:
            moves += 1
            # Remove p and all its multiples
            for multiple in range(i, n + 1, i):
                remaining[multiple] = False

    return 'Maria' if moves % 2 == 1 else 'Ben'


def isWinner(x, nums):
    """Determines who won the most games after x rounds."""
    if x == 0 or not nums:
        return None

    limit = max(nums)
    primes = sieve_of_eratosthenes(limit)

    maria_wins = 0
    ben_wins = 0

    # Simulate each game
    for n in nums:
        winner = prime_game(n, primes)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
