# 宁波银行20万信用分期36期

* **用于2020年学费和舅的第5个10万**
* 月利率0.7%, 折扣6.18, 折扣后月利率0.4326%, 年利率大约为5.2%
* 提前还款，收取剩余本金的3%手续费 (不做优惠活动的话是5%)
* 月本金5556.56, 月利息865.2, 月供6420.76, 不支持最低还款，故月存入6500即可
* 首次还款: 2020/8/1
* 办理时间: 2020/6/30
* **2022/1/1将宁波银行的尾款10w一次性结清为理想的时间节点**，
  **因为[未来36个月收入支出预算表](../../08Next36MPlanD.md)在第18个月
  正好盈余10w。**

-------------------------------------------------------------------------------

```
huanli@ThinkCentre:/tmp$ ./nb_bank 20 36 0.70:0.618 24:3
Total loan  :   200000
Total months:       36
Total lixi  :  31147.2
Yue Ben Jin :   5555.6
Yue Li  Xi  :    865.2
Yue Gong    :   6420.8
--------------------------------
Tiqian Huankuan months:       24
Yihuan Benjin         :  66666.7
WeihuanBenjin         : 133333.3
Yihuan Li Xi          :  10382.4
Tiqian Huankuan SXFei :   4000.0
Total Li Xi (A)       :  31147.2
Total Li Xi (B)       :  14382.4
Saved Li Xi (B-A)     :  16764.8
huanli@ThinkCentre:/tmp$
huanli@ThinkCentre:/tmp$ ./nb_bank 20 36 0.70:0.618 18:3
Total loan  :   200000
Total months:       36
Total lixi  :  31147.2
Yue Ben Jin :   5555.6
Yue Li  Xi  :    865.2
Yue Gong    :   6420.8
--------------------------------
Tiqian Huankuan months:       18
Yihuan Benjin         : 100000.0
WeihuanBenjin         : 100000.0
Yihuan Li Xi          :  15573.6
Tiqian Huankuan SXFei :   3000.0
Total Li Xi (A)       :  31147.2
Total Li Xi (B)       :  18573.6
Saved Li Xi (B-A)     :  12573.6
huanli@ThinkCentre:/tmp$
huanli@ThinkCentre:/tmp$ ./nb_bank 20 36 0.70:0.618 12:3
Total loan  :   200000
Total months:       36
Total lixi  :  31147.2
Yue Ben Jin :   5555.6
Yue Li  Xi  :    865.2
Yue Gong    :   6420.8
--------------------------------
Tiqian Huankuan months:       12
Yihuan Benjin         : 133333.3
WeihuanBenjin         :  66666.7
Yihuan Li Xi          :  20764.8
Tiqian Huankuan SXFei :   2000.0
Total Li Xi (A)       :  31147.2
Total Li Xi (B)       :  22764.8
Saved Li Xi (B-A)     :   8382.4
huanli@ThinkCentre:/tmp$
```
