# 双西二风险应对策略

因双西二存在着央产房上市交易风险，故拟定应对策略如下：

## 2.1 龙六现金分析

| # | ITEM                   | NUM   |
|-- | --                     | --    |
| A1|龙六                    | 420   |
| A2|定金                    |  10   |
| A3|户口押金(ToJiu)         |  `11` |
| A4|舍长120天               |  22   |
| A5|MEM第一年学费(+移动课堂)|  11   |
| A6|装修启动资金            |   `8` |
| >>|到九月底可用现金        |**358**|

## 2.2 双西二现金分析

| # | ITEM                   | NUM    |
|-- | --                     | --     |
| B1| 定金                   | 10     |
| B2| 中介费                 | 14.7   |
| >>| 合计                   |**24.7**|

* NOTE: 这里的24.7可作为最终的交易费用 (契税+中介费)

## 2.3 Anti-RISK

* 可以考虑的房子的成交价范围在**575-605**之间
* 需要收回**10**以交付新看房定金

```Bash
###################################################################
# 358 + 24.7 = 382.7 ~= 383 # <<< TOTAL CASH AVAILABLE BY0930 <<< #
###################################################################

#bash.610$ ./fang 610 0.95 20 Y # ** 383 - 401 = -18 #<< [A3+A6-1]
Raw total    =   610.00
Net total    =   579.50
Loan         =   231.00
Deed tax     =     5.79
Geshui       =     0.00
Zhongjiefee  =    15.65
Shoufu       =   401.00
Yuegong(#20) = 16390.04
Yuegong(#25) = 14714.38

#bash.605$ ./fang 605 0.95 20 Y # ** 383 - 397 = -14 #<< [A3+A6-5]
Raw total    =   605.00
Net total    =   574.75
Loan         =   229.00
Deed tax     =     5.75
Geshui       =     0.00
Zhongjiefee  =    15.52
Shoufu       =   397.00
Yuegong(#20) = 16248.13
Yuegong(#25) = 14586.98

#bash.600$ ./fang 600 0.95 20 Y # ** 383 - 393 = -10 #<< [A3+A6-8]
Raw total    =   600.00
Net total    =   570.00
Loan         =   228.00
Deed tax     =     5.70
Geshui       =     0.00
Zhongjiefee  =    15.39
Shoufu       =   393.00
Yuegong(#20) = 16177.18
Yuegong(#25) = 14523.28

#bash.595$ ./fang 595 0.95 20 Y # *** 383 - 390 = -7 #<< [A3-4]
Raw total    =   595.00
Net total    =   565.25
Loan         =   226.00
Deed tax     =     5.65
Geshui       =     0.00
Zhongjiefee  =    15.26
Shoufu       =   390.00
Yuegong(#20) = 16035.28
Yuegong(#25) = 14395.88

#bash.590$ ./fang 590 0.95 20 Y # *** 383 - 387 = -4 #<< [A3-7]
Raw total    =   590.00
Net total    =   560.50
Loan         =   224.00
Deed tax     =     5.61
Geshui       =     0.00
Zhongjiefee  =    15.13
Shoufu       =   387.00
Yuegong(#20) = 15893.37
Yuegong(#25) = 14268.49

#bash.585$ ./fang 585 0.95 20 Y # ****  383 - 384 = -1 #<< [A3-10] SAFE
Raw total    =   585.00
Net total    =   555.75
Loan         =   222.00
Deed tax     =     5.56
Geshui       =     0.00
Zhongjiefee  =    15.01
Shoufu       =   384.00
Yuegong(#20) = 15751.47
Yuegong(#25) = 14141.09

#bash.580$ ./fang 580 0.95 20 Y # ***** 383 - 381 = +2 #<< SAFE
Raw total    =   580.00
Net total    =   551.00
Loan         =   220.00
Deed tax     =     5.51
Geshui       =     0.00
Zhongjiefee  =    14.88
Shoufu       =   381.00
Yuegong(#20) = 15609.56
Yuegong(#25) = 14013.69
```

```bash
huanli@ThinkPad:scripts$ ./fang 610 0.95 20 Y # 383+18=401-401=0
Raw total    =   610.00
Net total    =   579.50
Loan         =   231.00
Deed tax     =     5.79
Geshui       =     0.00
Zhongjiefee  =    15.65
Shoufu       =   401.00
Yuegong(#20) = 16390.04
Yuegong(#25) = 14714.38

huanli@ThinkPad:scripts$ ./fang 615 0.95 20 Y #383+18=401-404=-3
Raw total    =   615.00
Net total    =   584.25
Loan         =   233.00
Deed tax     =     5.84
Geshui       =     0.00
Zhongjiefee  =    15.77
Shoufu       =   404.00
Yuegong(#20) = 16531.94
Yuegong(#25) = 14841.77

huanli@ThinkPad:scripts$ ./fang 620 0.95 20 Y #383+18=401-407=-6 **YELLOW**
Raw total    =   620.00
Net total    =   589.00
Loan         =   235.00
Deed tax     =     5.89
Geshui       =     0.00
Zhongjiefee  =    15.90
Shoufu       =   407.00
Yuegong(#20) = 16673.85
Yuegong(#25) = 14969.17

huanli@ThinkPad:scripts$ ./fang 625 0.95 20 Y #383+18=401-410=-9 **RED**
Raw total    =   625.00
Net total    =   593.75
Loan         =   237.00
Deed tax     =     5.94
Geshui       =     0.00
Zhongjiefee  =    16.03
Shoufu       =   410.00
Yuegong(#20) = 16815.75
Yuegong(#25) = 15096.57

huanli@ThinkPad:scripts$ ./fang 630 0.95 20 Y #383+18=401-413=-12 **VERYRED**
Raw total    =   630.00
Net total    =   598.50
Loan         =   239.00
Deed tax     =     5.99
Geshui       =     0.00
Zhongjiefee  =    16.16
Shoufu       =   413.00
Yuegong(#20) = 16957.66
Yuegong(#25) = 15223.97

huanli@ThinkPad:scripts$ ./fang 635 0.95 20 Y #401-416=-15 *UNREACHABLE*
Raw total    =   635.00
Net total    =   603.25
Loan         =   241.00
Deed tax     =     6.03
Geshui       =     0.00
Zhongjiefee  =    16.29
Shoufu       =   416.00
Yuegong(#20) = 17099.56
Yuegong(#25) = 15351.36
```

# 北京市双榆树中心小学2019年入学登记通知
![双榆树中心小学2019年入学登记通知](images/0901.jpg)
