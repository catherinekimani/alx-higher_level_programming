#!/usr/bin/python3

""" Reads from standard input and computes metrics """


def print_metrics(size, status_codes):
    """Print  metrics.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_counter = 0

    try:
        for line in sys.stdin:
            if line_counter == 10:
                print_metrics(size, status_codes)
                line_counter = 1
            else:
                line_counter += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_metrics(size, status_codes)

    except KeyboardInterrupt:
        print_metrics(size, status_codes)
        raise
