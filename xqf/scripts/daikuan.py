#!/usr/bin/python3
import sys

def get_yuegong(loan, loan_nyears, y_lilv):
    """ Deng E Ben Xi, to verify, please go to
        o https://www.rong360.com/calculator/fangdai.html
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
    x = loan * m_lilv * ((1 + m_lilv) ** n) / ((1 + m_lilv) ** n -1)
    return x


def main(argc, argv):
    if argc != 5:
        sys.stderr.write("Usage: %s <total> <base ylilv> <lilv+> <Nyears>\n" %
                         argv[0])
        sys.stderr.write("e.g.   %s 218 0.049 0.20 19\n" % argv[0])
        sys.stderr.write("       %s 218 0.049 0.15 19\n" % argv[0])
        return 1

    loan         = int(argv[1])
    yuelilv      = float(argv[2])
    lilvplus     = float(argv[3])
    loan_nyears  = int(argv[4])

    print("Loan         = %8.2f" % loan)
    print("BaseYueLilv  = %8.3f" % yuelilv)
    print("YueLilvFloat = %8d%%" % (lilvplus * 100))
    print("Yuelilv      = %8.4f" % (yuelilv * (1 + lilvplus)))
    yg01 = get_yuegong(10000 * loan, loan_nyears, yuelilv * (1+lilvplus));
    print("Yuegong(#%2d) = %8.2f" % (loan_nyears, yg01));
    nianlixi = (yg01 * 12 - loan  * 10000.0 / loan_nyears) / 10000.0
    print("Nian Lixi    = %8.2f" % nianlixi)
    print("Total Lixi   = %8.2f" % (nianlixi * loan_nyears))
    return 0

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
