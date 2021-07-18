#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" A handy script to evaluate school records of a student """

import sys
import json
import collections


NA = -1  # XXX: mark those items lack of scores because they are not available

FD01_UE  = "unit-exam"          # e.g. weight = 0.50
FD02_MME = "midterm-mock-exam"  #      weight = 0.05
FD03_ME  = "midterm-exam"       #      weight = 0.15
FD04_FME = "final-mock-exam"    #      weight = 0.05
FD05_FE  = "final-exam"         #      weight = 0.25


def get_raw_score_list(obj, field=FD01_UE):
    """e.g. field = 'final-exam'
    """
    l_out = []
    for e in obj[field]['scores']:
        if e == NA or e == 'NA' or e == 'N/A':
            continue
        l_out.append(e)
    return l_out


def get_raw_weight(obj, field=FD01_UE):
    return obj[field]['weight']


def fmt_score_list(in_score_list):
    tmp_list = []
    for score in in_score_list:
        if score == NA:
            continue
        tmp_list.append(score)

    avg = sum(tmp_list) / len(tmp_list)
    out_score_list = []
    for score in in_score_list:
        if score == NA:
            out_score_list.append(avg)
        else:
            out_score_list.append(score)

    print(">>> IN  >>>:", in_score_list, file=sys.stderr)
    print(">>> OUT >>>:", out_score_list, file=sys.stderr)

    return out_score_list


def get_mid_score_list(*args):
    mid_score_list = []
    for l in args:
        if l:
            avg = sum(l) / len(l)
            mid_score_list.append(avg)
        else:
            mid_score_list.append(NA)
    return mid_score_list


def get_final_score(mid_score_list, weight_list):
    x = []
    s = 0
    out = fmt_score_list(mid_score_list)
    for i in range(len(weight_list)):
        s += out[i] * weight_list[i]
        x.append("%.2f x %d%%" % (out[i], weight_list[i] * 100))
    print(">>> %s = %.2f ~= %d" % (' + '.join(x), s, round(s)),
          file=sys.stderr)
    return round(s)


def get_final_score_with_variance(final_score, vrnc_score):
    x = []
    s = 0
    score_list  = [final_score, vrnc_score]
    weight_list = [0.8,         0.2]
    for i in range(len(score_list)):
        s += score_list[i] * weight_list[i]
        x.append("%.2f x %d%%" % (score_list[i], weight_list[i] * 100))
    print(">>> %s = %.2f ~= %d" % (' + '.join(x), s, round(s)),
          file=sys.stderr)
    return round(s)


def get_grade(score):
    if score >= 60 and score <= 62:
        return (1.0, 'D')
    elif score >= 63 and score <= 66:
        return (1.3, 'D+')
    elif score >= 67 and score <= 69:
        return (1.7, 'C-')
    elif score >= 70 and score <= 72:
        return (2.0, 'C')
    elif score >= 73 and score <= 76:
        return (2.3, 'C+')
    elif score >= 77 and score <= 79:
        return (2.7, 'B-')
    elif score >= 80 and score <= 84:
        return (3.0, 'B')
    elif score >= 85 and score <= 89:
        return (3.3, 'B+')
    elif score >= 90 and score <= 94:
        return (3.7, 'A-')
    elif score >= 95 and score <= 97:
        return (4.0, 'A')
    elif score >= 98 and score <= 100:
        return (4.0, 'A+')
    elif score > 100:
        return (9.9, 'N/A')
    else:
        return (0, 'F')


def get_stability(variance):
    if variance >= 0 and variance <= 2:
        return (100, 'A+')
    elif variance >= 3 and variance <= 5:
        return (96, 'A')
    elif variance >= 6 and variance <= 9:
        return (92, 'A-')
    elif variance >= 10 and variance <= 12:
        return (85, 'B+')
    elif variance >= 13 and variance <= 15:
        return (80, 'B')
    elif variance >= 16 and variance <= 18:
        return (77, 'B-')
    elif variance >= 19 and variance <= 21:
        return (73, 'C+')
    elif variance >= 22 and variance <= 24:
        return (70, 'C')
    elif variance >= 25 and variance <= 27:
        return (67, 'C-')
    elif variance >= 28 and variance <= 30:
        return (63, 'D+')
    elif variance >= 31 and variance <= 33:
        return (60, 'D')
    else:
        return (0, 'F')


def get_full_score_list(*args):
    out = []
    for l in args:
        if l:
            out.extend(l)
    return out


def get_variance(l):
    s = sum(l)
    n = len(l)
    avg = s / n
    x = 0
    for i in l:
        x += (i - avg) ** 2
    v = x / n
    return round(v)


def main(argc, argv):
    if argc != 3:
        print("Usage: %s <json file> <subject>" % argv[0], file=sys.stderr)
        return 1

    json_file = argv[1]
    subject = argv[2].title()

    # loads school records
    with open(json_file, 'r') as f:
        txt = ''.join(f.readlines())
    obj = json.loads(txt, object_pairs_hook=collections.OrderedDict)

    # get score list and the related weight
    l_ue   = get_raw_score_list(obj[subject], FD01_UE)
    l_mme  = get_raw_score_list(obj[subject], FD02_MME)
    l_me   = get_raw_score_list(obj[subject], FD03_ME)
    l_fme  = get_raw_score_list(obj[subject], FD04_FME)
    l_fe   = get_raw_score_list(obj[subject], FD05_FE)
    ue_weight  = get_raw_weight(obj[subject], FD01_UE)
    mme_weight = get_raw_weight(obj[subject], FD02_MME)
    me_weight  = get_raw_weight(obj[subject], FD03_ME)
    fme_weight = get_raw_weight(obj[subject], FD04_FME)
    fe_weight  = get_raw_weight(obj[subject], FD05_FE)

    # get variance
    l_full = get_full_score_list(l_ue, l_mme, l_me, l_fme, l_fe)
    vrnc = get_variance(l_full)
    vrnc_score, vrnc_grade = get_stability(vrnc)
    vrnc_gpa, vrnc_grade2 = get_grade(round(vrnc_score))
    print('>>> VRNC:', vrnc, vrnc_score, vrnc_grade, vrnc_gpa, file=sys.stderr)

    # get mid score list
    l_mid = get_mid_score_list(l_ue, l_mme, l_me, l_fme, l_fe)
    l_mid_weight = [ue_weight, mme_weight, me_weight, fme_weight, fe_weight]

    # get final score
    final_score = get_final_score(l_mid, l_mid_weight)
    final_grade_a, final_grade_b = get_grade(round(final_score))
    print(final_score, final_grade_a, final_grade_b, file=sys.stderr)

    # get final score with variance
    final_scorev = get_final_score_with_variance(final_score, vrnc_score)
    final_gradev_a, final_gradev_b = get_grade(round(final_scorev))
    print(final_scorev, final_gradev_a, final_gradev_b, file=sys.stderr)

    # final output
    print("=======:S1:S1:S1::VRNC:VRNC:VRNC:S2:S2:S2:=====")
    print("SUBJECT:SCORES:GRADE:GPA:VRNC:SCORES:GRADE:GPA:SCORES:GRADE:GPA:#FER#")
    s_final = "%d:%s:%.1f" % (final_score, final_grade_b, final_grade_a)
    s_vrnc = "%d:%d:%s:%.1f" % (vrnc, vrnc_score, vrnc_grade, vrnc_gpa)
    s_finalv = "%d:%s:%.1f" % (final_scorev, final_gradev_b, final_gradev_a)
    print("%s:%s:%s:%s:%d" % (subject, s_final, s_vrnc, s_finalv, l_fe[0]))
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
