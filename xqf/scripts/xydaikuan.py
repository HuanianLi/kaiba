#!/usr/bin/python3
""" XinYong DaiKuan OR FangDai
    Deng E Ben Xi
"""

import sys


def get_yuegong(loan, loan_nyears, y_lilv):
    """ Deng E Ben Xi, to verify, please go to
        o http://www.edai.com/jsq/grdk/     OR
        o https://www.fangdaijisuanqi.com/
    """
    m_lilv = y_lilv / 12
    #
    # YueGong = Loan x YueLiLv x [ (1+YueLiLv)^N]
    #           ---------------------------------
    #               [ (1+YueLiLv)^N - 1 ]
    #
    #           where N is the FenQiZongShu = 12 * loan_nyears
    #
    n = 12 * loan_nyears
    x = loan * m_lilv * ((1 + m_lilv) ** n) / ((1 + m_lilv) ** n - 1)
    return x


def main(argc, argv):
    if argc != 4:
        sys.stderr.write("Usage: %s <total> <NianLilv> <NYears>\n" %
                         argv[0])
        sys.stderr.write("e.g.   %s 30 0.05 2\n" % argv[0])
        sys.stderr.write("       %s 30 0.05 3\n" % argv[0])
        return 1

    loan = int(argv[1])
    y_lilv = float(argv[2])
    loan_nyears = int(argv[3])

    yg = get_yuegong(10000 * loan, loan_nyears, y_lilv);
    total = yg * loan_nyears * 12
    total_lixi = total - loan * 10000
    print("Loan       = %7dw" % loan)
    print("Loan Years = %8d" % loan_nyears)
    print("Nian Lilv  = %7.2f%% # m%.2f%%" % (y_lilv * 100, y_lilv * 100 / 12))
    print("Total      = %7.2fw # %10.2f" % ((total/10000), total))
    print("Total lixi = %7.2fw # %10.2f" % ((total_lixi/10000), total_lixi))
    print("Yuegong    = %8.2f" % yg);
    return 0


if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
