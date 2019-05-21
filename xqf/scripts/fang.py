#!/usr/bin/python3
import sys

g_resv_yajin = 10
g_resv_xuefei = 16.8 / 2
g_resv_zhuanxiu = 20
g_cbc = 16 + 3
g_capital = 420 - 67 - g_resv_yajin - g_resv_xuefei - g_resv_zhuanxiu + g_cbc
g_ylilv = 0.049 * 1.2     # 2nd, increase 20%


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
        sys.stderr.write("Usage: %s <total> <eval_percent> <Nyears> <Y|N>\n" %
                         argv[0])
        sys.stderr.write("e.g.   %s 630 0.90 20 Y\n" % argv[0])
        sys.stderr.write("       %s 575 0.95 20 N\n" % argv[0])
        return 1

    raw_total    = int(argv[1])
    eval_percent = float(argv[2])
    loan_nyears  = int(argv[3])
    flag_manwuweiyi = argv[4]
    net_total    = raw_total * eval_percent
    loan         = int(net_total * 0.4)     # raw_total * eval_percent * 40%
    deed_tax     = net_total * 0.01         # net_total * 1%
    if flag_manwuweiyi == "N":
        geshui   = net_total * 0.01         # also net_total * 1%
    else:
        geshui   = 0
    zhongjiefee  = raw_total * 0.027 * 0.95 # raw_total * 2.7%
    others       = (600 + 1070) / 10000.0
    shoufu       = raw_total - loan + deed_tax + geshui +zhongjiefee + others
    print("Raw total    = %8.2f" % raw_total)
    print("Net total    = %8.2f" % net_total)
    print("Loan         = %8.2f" % loan)
    print("Deed tax     = %8.2f" % deed_tax)
    print("Geshui       = %8.2f" % geshui)
    print("Zhongjiefee  = %8.2f" % zhongjiefee)
    print("Shoufu       = %8.2f" % round(shoufu))
    print("XXCore       = %8.2f" % round(shoufu - g_capital))
    yg01 = get_yuegong(10000 * loan, loan_nyears, g_ylilv);
    print("Yuegong(#%2d) = %8.2f" % (loan_nyears, yg01));
    yg02 = get_yuegong(10000 * loan, loan_nyears + 5, g_ylilv);
    print("Yuegong(#%2d) = %8.2f" % (loan_nyears + 5, yg02));
    return 0

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
