import timeit
from tabulate import tabulate, SEPARATING_LINE

from boyer_moore import boyer_moore_search
from knuth_morris_pratt import kmp_search
from rabin_karp import rabin_karp_search


def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()
    
def measure_time(algorithm, text, pattern):
    time = round(timeit.timeit(lambda: algorithm(text, pattern), number=5), 6)

    return time

def benchmark_search_algorithms(text, real_pattern, fake_pattern):
    boyer_moore_position_real = boyer_moore_search(text, real_pattern)
    boyer_moore_position_fake = boyer_moore_search(text, fake_pattern)
    boyer_moore_time_real = measure_time(boyer_moore_search, text, real_pattern)
    boyer_moore_time_fake = measure_time(boyer_moore_search, text, fake_pattern)

    kmp_position_real = kmp_search(text, real_pattern)
    kmp_position_fake = kmp_search(text, fake_pattern)
    kmp_time_real = measure_time(kmp_search, text, real_pattern)
    kmp_time_fake = measure_time(kmp_search, text, fake_pattern)

    rabin_karp_position_real = rabin_karp_search(text, real_pattern)
    rabin_karp_position_fake = rabin_karp_search(text, fake_pattern)
    rabin_karp_time_real = measure_time(rabin_karp_search, text, real_pattern)
    rabin_karp_time_fake = measure_time(rabin_karp_search, text, fake_pattern)

    headers = ["\nAlgorithm", "\nPosition", "\nTime, sec"]
    table = [["Boyer-Moore real", boyer_moore_position_real, boyer_moore_time_real], ["Boyer-Moore fake", boyer_moore_position_fake, boyer_moore_time_fake], ["Total time", "", boyer_moore_time_real + boyer_moore_time_fake], SEPARATING_LINE,
             ["KMP real", kmp_position_real, kmp_time_real], ["KMP fake", kmp_position_fake, kmp_time_fake], ["Total time", "", kmp_time_real + kmp_time_fake], SEPARATING_LINE,
             ["Rabin-Karp real", rabin_karp_position_real, rabin_karp_time_real], ["Rabin-Karp fake", rabin_karp_position_fake, rabin_karp_time_fake], ["Total time", "", rabin_karp_time_real + rabin_karp_time_fake], SEPARATING_LINE,]

    return(tabulate(table, headers, tablefmt="simple"))

text = read_file('article1.txt')
real_pattern = "public static int linearSearch"
fake_pattern = "fake"

text_2 = read_file('article2.txt')
real_pattern_2 = "Editors Ricci F"
fake_pattern_2 = "fake"

print("\nARTICLE 1")
print(benchmark_search_algorithms(text, real_pattern, fake_pattern))
print("\nARTICLE 2")
print(benchmark_search_algorithms(text_2, real_pattern_2, fake_pattern_2))




