#!/usr/bin/python3
import sys


def get_yuegong(loan, loan_nyears, m_lilv):
    """ Get YueGong if loan from bank via cash-instalment
        o http://money.qq.com/a/20170506/002967.htm
    """
    m_benjin = loan / (loan_nyears * 12)
    m_lixi = loan * m_lilv;
    m_yuegong = m_benjin + m_lixi;
    return (m_yuegong, m_lixi)


def get_tag(nid, bid=None):
    if bid is None:
        return '[ %02d ]' % nid
    else:
        bank_id = bid.upper()
        d_bank = {
            'GF': 'GuangFa ',
            'ZH': 'ZhaoHang',
            'MS': 'MingShen',
            'JH': 'JianHang',
            'GH': 'GongHang',
            'NA': 'Unknown '
        }
        if bank_id in d_bank:
            return '[ %s ]' % d_bank[bank_id]
        else:
            return '[ %s ]' % bank_id


def do_sum(l_loan):
    d_sum = dict()
    d_sum['loan'] = 0
    d_sum['lixi'] = 0
    d_sum['m_benjin'] = 0
    d_sum['m_lixi'] = 0
    d_sum['m_yuegong'] = 0

    i = 0
    for cell in l_loan:
        i += 1
        l_cell = cell.split(':')
        e_loan = int(l_cell[0])
        e_mlilv = float(l_cell[1])
        e_nyears = float(l_cell[2])
        if len(l_cell) > 3:
            tag = get_tag(i, l_cell[3])
        else:
            tag = get_tag(i)

        (m_yuegong, m_lixi) = get_yuegong(e_loan * 10000,
                                          e_nyears,
                                          e_mlilv / 100)
        sum_lixi = m_lixi * 12 * e_nyears
        print("%s Total Loan = %dw"  % (tag, e_loan))
        print("%s Total Lixi = %d"   % (tag, sum_lixi))
        print("%s YueLilv    = %.3f" % (tag, e_mlilv))
        print("%s nYears     = %d"   % (tag, e_nyears))
        print("%s YueBenjin  = %d"   % (tag, m_yuegong - m_lixi))
        print("%s YueLixi    = %d"   % (tag, m_lixi))
        print("%s Yuegong    = %d"   % (tag, m_yuegong))
        print("")

        d_sum['loan'] += e_loan
        d_sum['lixi'] += m_lixi * e_nyears * 12
        d_sum['m_benjin'] += (m_yuegong - m_lixi)
        d_sum['m_lixi'] += m_lixi
        d_sum['m_yuegong'] += m_yuegong

    prefix = ' ' * (len(tag) - 2)
    print('#' * 79)
    print("# %s Total Loan      = %dw" % (prefix, d_sum['loan']))
    print("# %s Total Lixi      = %d"  % (prefix, d_sum['lixi']))
    print("# %s Total YueBenjin = %d"  % (prefix, d_sum['m_benjin']))
    print("# %s Total YueLixi   = %d"  % (prefix, d_sum['m_lixi']))
    print("# %s Total Yuegong   = %d"  % (prefix, d_sum['m_yuegong']))
    print("#" * 79)


def main(argc, argv):
    if argc < 2:
        sys.stderr.write("Usage: %s <Loan:m_lilv%%:N> [...]\n" % argv[0])
        sys.stderr.write("e.g.   %s 20:0.67:3  # Guangfa \n" % argv[0])
        sys.stderr.write("       %s 18:0.375:2 # Zhaohang\n" % argv[0])
        sys.stderr.write("       %s 20:0.75:2  # Minsheng\n" % argv[0])
        sys.stderr.write("       %s 12:0.67:3  18:0.375:2\n" % argv[0])
        sys.stderr.write("       %s 12:0.67:3:GF  18:0.375:2:ZH\n" % argv[0])
        sys.stderr.write("       %s 20:0.67:3:GF  18:0.375:2:zh\n" % argv[0])
        return 1

    do_sum(argv[1:])
    return 0


if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
