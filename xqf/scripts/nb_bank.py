#!/usr/bin/python3

import sys

def main(argc, argv):
    if argc != 5:
        print("Usage: %s <loan> <qishu> <yuelilv:zhekou> <tiqian:X>" % argv[0],
              file=sys.stderr)
        print("e.g.")
        print("# Ningbo: Yuelilv  = 0.75% if N <= 12 else 0.60%",
              file=sys.stderr)
        print("# Guangfa: Yuelilv = 0.60% if N <= 12 else 0.44%",
              file=sys.stderr)
        print("# Ningbo  bank #", file=sys.stderr)
        print("       %s  3 12 0.60:0.88   6:5" % argv[0], file=sys.stderr)
        print("       %s 20 36 0.60:0.88  12:5" % argv[0], file=sys.stderr)
        #
        # 2020/06/30: Ningbo Bank Promotional Activity
        # * Yue Lilv                 :         0.7% ==> 0.7% * 0.618
        # * Tiqian Huankuan Shouxufei: shengyu * 5% ==> shengyu * 3%
        #
        print("       %s 20 36 0.70:0.618 12:3" % argv[0], file=sys.stderr)
        print("       %s 20 36 0.70:0.618 18:3" % argv[0], file=sys.stderr)
        print("       %s 20 36 0.70:0.618 24:3" % argv[0], file=sys.stderr)
        print("# Guangfa bank #", file=sys.stderr)
        print("       %s  3 12 0.44:1.00   6:4" % argv[0], file=sys.stderr)
        print("       %s 20 36 0.44:1.00  12:4" % argv[0], file=sys.stderr)
        return 1

    loan = int(argv[1]) * 10000
    fqs = int(argv[2])
    list_argv3 = argv[3].split(':')
    yuelilv = float(list_argv3[0]) / 100
    lilv_zhekou = float(list_argv3[1])
    list_argv4 = argv[4].split(':')
    tqhkqs = int(list_argv4[0])
    tqhk_feilv = float(list_argv4[1]) / 100

    yuebenjin = loan / fqs
    yuelixi = loan * yuelilv * lilv_zhekou
    zonglixi = yuelixi * fqs
    yuegong = yuebenjin + yuelixi

    print("Total loan  : %8d" % loan)
    print("Total months: %8d" % fqs)
    print("Total lixi  : %8.1f" % zonglixi)
    print("Yue Ben Jin : %8.1f" % yuebenjin)
    print("Yue Li  Xi  : %8.1f" % yuelixi)
    print("Yue Gong    : %8.1f" % yuegong)

    yihuanqishu = fqs - tqhkqs
    yihuanlixi  = yuelixi * yihuanqishu
    daihuanlixi = yuebenjin * tqhkqs * tqhk_feilv  # Ningbo: 5% Guangfa: 4%
    zonglixi2 = yihuanlixi + daihuanlixi
    print('-' * 32)
    print("Tiqian Huankuan months: %8d" % tqhkqs)
    print("Yihuan Benjin         : %8.1f" % (yuebenjin * yihuanqishu))
    print("WeihuanBenjin         : %8.1f" % (yuebenjin * tqhkqs))
    print("Yihuan Li Xi          : %8.1f" % yihuanlixi)
    print("Tiqian Huankuan SXFei : %8.1f" % daihuanlixi)
    print("Total Li Xi (A)       : %8.1f" % zonglixi)
    print("Total Li Xi (B)       : %8.1f" % zonglixi2)
    print("Saved Li Xi (B-A)     : %8.1f" % (zonglixi - zonglixi2))

    return 0


if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))

"""
GF8/12$ ./nb_bank  3 12 0.44:1.00  4:4
Total loan  :    30000
Total months:       12
Total lixi  :   1584.0
Yue Ben Jin :   2500.0
Yue Li  Xi  :    132.0
Yue Gong    :   2632.0
--------------------------------
Tiqian Huankuan months:        4
Yihuan Benjin         :  20000.0
WeihuanBenjin         :  10000.0
Yihuan Li Xi          :   1056.0
Tiqian Huankuan SXFei :    400.0
Total Li Xi (A)       :   1584.0
Total Li Xi (B)       :   1456.0
Saved Li Xi (B-A)     :    128.0

GF6/12$ ./nb_bank  3 12 0.44:1.00  6:4
Total loan  :    30000
Total months:       12
Total lixi  :   1584.0
Yue Ben Jin :   2500.0
Yue Li  Xi  :    132.0
Yue Gong    :   2632.0
--------------------------------
Tiqian Huankuan months:        6
Yihuan Benjin         :  15000.0
WeihuanBenjin         :  15000.0
Yihuan Li Xi          :    792.0
Tiqian Huankuan SXFei :    600.0
Total Li Xi (A)       :   1584.0
Total Li Xi (B)       :   1392.0
Saved Li Xi (B-A)     :    192.0

===============================================================================

NB$ ./nb_bank 20 36 0.60:0.88 12:5
Total loan  :   200000
Total months:       36
Total lixi  :  43200.0
Yue Ben Jin :   5555.6
Yue Li  Xi  :   1200.0
Yue Gong    :   6755.6
--------------------------------
Tiqian Huankuan months:       12
Yihuan Benjin         : 133333.3
WeihuanBenjin         :  66666.7
Yihuan Li Xi          :  28800.0
Tiqian Huankuan SXFei :   3333.3
Total Li Xi (A)       :  43200.0
Total Li Xi (B)       :  32133.3
Saved Li Xi (B-A)     :  11066.7

GF$ ./nb_bank 20 36 0.44:1.00 12:4
Total loan  :   200000
Total months:       36
Total lixi  :  31680.0
Yue Ben Jin :   5555.6
Yue Li  Xi  :    880.0
Yue Gong    :   6435.6
--------------------------------
Tiqian Huankuan months:       12
Yihuan Benjin         : 133333.3
WeihuanBenjin         :  66666.7
Yihuan Li Xi          :  21120.0
Tiqian Huankuan SXFei :   2666.7
Total Li Xi (A)       :  31680.0
Total Li Xi (B)       :  23786.7
Saved Li Xi (B-A)     :   7893.3
"""
