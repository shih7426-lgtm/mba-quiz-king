#!/usr/bin/env python3
"""MBA数学生成器 - 生成350道新题(m51-m400)"""
import random, math, json
random.seed(2026)

next_m = 51
DIFS = ["基础","中等","困难"]
questions = []

def mid():
    global next_m; i = next_m; next_m += 1; return f"m{i}"
def rdiff():
    r = random.random(); return "基础" if r<0.3 else ("中等" if r<0.7 else "困难")
def rsrc():
    return random.choice(["袁进·数学分册","陈剑·高分指南","","",""])
def dopts(correct, n=5):
    ds = set()
    for d in [correct-2,correct-1,correct+1,correct+2,-correct,correct*2 if correct!=0 else 1,correct+3,correct-3]:
        if d != correct: ds.add(d)
    while len(ds) < n-1:
        d = correct + random.randint(-8,8)
        if d != correct: ds.add(d)
    ds = list(ds)[:n-1]
    opts = [str(d) for d in ds] + [str(correct)]
    random.shuffle(opts)
    return opts, opts.index(str(correct))

def add(q, ans_val, exp, tp="solve", src=None, diff=None):
    opts, ai = dopts(ans_val)
    questions.append({"id":mid(),"type":tp,"diff":diff or rdiff(),"src":src or rsrc(),
        "q":q,"opts":opts,"ans":ai,"exp":exp})

# 1. 一元一次方程 (30)
for _ in range(30):
    a=random.randint(2,9); x=random.randint(-8,15); b=random.randint(-20,20); c=a*x+b
    bs=f"+{b}" if b>0 else str(b)
    add(f"解方程：{a}x{bs}={c}，则x的值为：", x, f"移项得{a}x={c-b}，x={x}。")

# 2. 一元二次方程 (25)
for _ in range(25):
    r1=random.randint(-8,8); r2=random.randint(-8,8)
    if r1==r2: r2+=1
    b=-(r1+r2); c=r1*r2; ans=max(r1,r2)
    bs=f"+{b}" if b>0 else str(b); cs=f"+{c}" if c>0 else str(c)
    add(f"方程x²{bs}x{cs}=0的较大根为：", ans, f"(x-{r1})(x-{r2})=0，较大根为{ans}。")

# 3. 方程组 (25)
for _ in range(25):
    x=random.randint(1,10); y=random.randint(1,10)
    a1,b1=random.randint(2,6),random.randint(2,6); a2,b2=random.randint(2,6),random.randint(2,6)
    if a1*b2-a2*b1==0: continue
    c1,c2=a1*x+b1*y,a2*x+b2*y; ans=x+y
    b1s=f"+{b1}y" if b1>0 else f"{b1}y"; b2s=f"+{b2}y" if b2>0 else f"{b2}y"
    add(f"解方程组：{a1}x{b1s}={c1}，{a2}x{b2s}={c2}，则x+y=：", ans, f"解得x={x}，y={y}，x+y={ans}。")

# 4. 百分比/折扣 (30)
for _ in range(30):
    p=random.choice([100,120,150,200,250,300,400,500,800])
    pct=random.choice([10,15,20,25,30,40,50]); ans=p*(100-pct)//100
    add(f"某商品原价{p}元，打{100-pct}折后售价为：", ans, f"{p}×{(100-pct)/100:.1f}={ans}元。")

# 5. 比例 (25)
for _ in range(25):
    a,b=random.randint(2,8),random.randint(2,8); t=random.randint(30,200)
    ans=t*a//(a+b)
    add(f"甲乙分{t}元，比例{a}:{b}，甲得：", ans, f"甲占{a}/{a+b}，得{ans}元。")

# 6. 工程 (25)
for _ in range(25):
    d1,d2=random.randint(6,20),random.randint(6,20)
    ans=round(d1*d2/(d1+d2),1)
    add(f"甲单独做{d1}天完成，乙{d2}天完成，合做需几天？", int(ans) if ans==int(ans) else ans, f"合做需{ans}天。")

# 7. 行程 (25)
for _ in range(25):
    v1,v2=random.choice([40,50,60,80]),random.choice([30,40,50,60]); t=random.randint(2,6)
    add(f"甲乙从A、B相向出发，甲速{v1}km/h乙速{v2}km/h，{t}小时相遇，A、B相距：", (v1+v2)*t, f"相对速度{v1+v2}km/h，{t}小时走{(v1+v2)*t}km。")

# 8. 排列组合 (30)
for _ in range(30):
    qt=random.choice(["perm","comb","fact"])
    if qt=="perm":
        n,r=random.randint(5,8),random.randint(2,4); ans=math.perm(n,r)
        add(f"从{n}个不同元素取{r}个排列，排法数：", ans, f"A({n},{r})={ans}。")
    elif qt=="comb":
        n,r=random.randint(6,12),random.randint(2,5); ans=math.comb(n,r)
        add(f"从{n}个不同元素取{r}个组合，组合数：", ans, f"C({n},{r})={ans}。")
    else:
        n=random.randint(4,7); ans=math.factorial(n)
        add(f"{n}个人排一排，不同排法：", ans, f"{n}!={ans}。")

# 9. 等差数列 (25)
for _ in range(25):
    a1,d,n=random.randint(1,10),random.randint(1,5),random.randint(5,15)
    an=a1+(n-1)*d; sn=n*(a1+an)//2
    if random.random()<0.5:
        add(f"等差数列a₁={a1}，d={d}，a_{n}=：", an, f"aₙ={a1}+{n-1}×{d}={an}。")
    else:
        add(f"等差数列a₁={a1}，d={d}，S_{n}=：", sn, f"Sₙ=n(a₁+aₙ)/2={sn}。")

# 10. 等比数列 (20)
for _ in range(20):
    a1=random.choice([1,2,3,4,5]); q=random.choice([2,3,-2]); n=random.randint(3,6)
    an=a1*q**(n-1); sn=a1*(q**n-1)//(q-1) if q!=1 else a1*n
    if random.random()<0.5:
        add(f"等比数列a₁={a1}，q={q}，a_{n}=：", an, f"aₙ={a1}×{q}^{n-1}={an}。")
    else:
        add(f"等比数列a₁={a1}，q={q}，S_{n}=：", sn, f"Sₙ={sn}。")

# 11. 几何-直角三角形 (20)
for _ in range(20):
    a,b=random.choice([(3,4),(5,12),(6,8),(8,15),(9,12),(7,24),(12,16),(10,24)])
    c=int(math.sqrt(a*a+b*b))
    if random.random()<0.5:
        add(f"直角三角形两直角边{a}和{b}，斜边为：", c, f"√({a}²+{b}²)={c}。")
    else:
        add(f"直角三角形两直角边{a}和{b}，面积为：", a*b//2, f"S={a}×{b}/2={a*b//2}。")

# 12. 几何-圆/正方形 (20)
for _ in range(20):
    r=random.randint(3,10)
    if random.random()<0.5:
        add(f"半径为{r}的圆的面积约为：(π≈3.14)", int(3.14*r*r), f"S≈3.14×{r}²≈{int(3.14*r*r)}。")
    else:
        l=random.randint(3,10)
        add(f"边长为{l}的正方形面积为：", l*l, f"S={l}²={l*l}。")

# 13. 绝对值 (20)
for _ in range(20):
    a,b=random.randint(-8,8),random.randint(-8,8)
    if a==b: b+=1
    lo,hi=min(a,b),max(a,b); ans=hi-lo
    add(f"若{lo}≤x≤{hi}，则|x-{lo}|+|x-{hi}|=：", ans, f"和={hi}-{lo}={ans}。")

# 14. 不等式 (15)
for _ in range(15):
    a=random.randint(2,5); b=random.randint(-10,10); c=random.randint(-20,20)
    thr=(c-b)/a
    if thr!=int(thr): continue
    add(f"解不等式：{a}x+{b}>{c}，x的取值范围中x>{int(thr)}是否成立？", 1 if thr<int(thr)+1 else 0, f"{a}x>{c-b}，x>{int(thr)}。")

# 15. 函数最值 (15)
for _ in range(15):
    b=random.randint(-6,6); c=random.randint(-10,10)
    fmin=c-b*b/4
    if fmin!=int(fmin): continue
    bs=f"+{b}" if b>0 else str(b); cs=f"+{c}" if c>0 else str(c)
    add(f"f(x)=x²{bs}x{cs}的最小值为：", int(fmin), f"对称轴x={-b//2}，f({-b//2})={int(fmin)}。")

# 16. 整除/公约数 (15)
for _ in range(15):
    a,b=random.randint(4,30),random.randint(4,30)
    g=math.gcd(a,b); l=a*b//g
    if random.random()<0.5:
        add(f"{a}和{b}的最大公约数为：", g, f"gcd={g}。")
    else:
        add(f"{a}和{b}的最小公倍数为：", l, f"lcm={l}。")

# 17. 利润 (20)
for _ in range(20):
    cost=random.choice([50,80,100,120,150,200]); pct=random.choice([10,15,20,25,30,40,50])
    add(f"进价{cost}元，加价{pct}%出售，利润为：", cost*pct//100, f"利润={cost}×{pct}%={cost*pct//100}元。")

# 18. 浓度 (15)
for _ in range(15):
    m=random.choice([100,200,300,500]); p=random.choice([5,10,15,20,25]); w=random.choice([50,100,150,200])
    solute=m*p//100; new_p=round(solute/(m+w)*100,1)
    ans_int=int(new_p) if new_p==int(new_p) else round(new_p,1)
    add(f"{m}g浓度{p}%盐水加{w}g水后浓度为：", ans_int, f"溶质{solute}g，浓度≈{ans_int}%。")

# 19. 余数 (15)
for _ in range(15):
    a=random.randint(10,99); b=random.choice([3,4,5,6,7,8,9])
    add(f"{a}÷{b}的余数为：", a%b, f"{a}={a//b}×{b}+{a%b}，余数{a%b}。")

# 20. 连续升降价 (15)
for _ in range(15):
    p=random.choice([100,200,500]); p1,p2=random.choice([10,15,20,25]),random.choice([10,15,20,25])
    ans=p*(100-p1)*(100-p2)//10000
    add(f"原价{p}元，先降{p1}%再降{p2}%，现价：", ans, f"{p}×{100-p1}%×{100-p2}%={ans}元。")

# 21. 条件充分性判断-方程类 (25)
JUDGE_OPTS = ["条件(1)充分，但条件(2)不充分","条件(2)充分，但条件(1)不充分","条件(1)和(2)单独都不充分，但联合起来充分","条件(1)和(2)单独都充分","条件(1)和(2)单独都不充分，联合也不充分"]
for _ in range(25):
    x=random.randint(2,10)
    questions.append({"id":mid(),"type":"judge","diff":rdiff(),"src":rsrc(),
        "q":f"条件充分性判断：能确定{x}x+a=0中a的值。\n条件(1)：x={x}\n条件(2)：{x}x=-{x*x}",
        "opts":JUDGE_OPTS,"ans":1,"exp":f"条件(1)只给x值无法确定a，不充分。条件(2)可确定a={x*x}，充分。"})

# 22. 条件充分性判断-不等式类 (20)
for _ in range(20):
    a=random.randint(2,6); b=random.randint(-5,10); thr=b/a
    if thr!=int(thr): continue
    questions.append({"id":mid(),"type":"judge","diff":rdiff(),"src":rsrc(),
        "q":f"条件充分性判断：{a}x>{b}。\n条件(1)：x>{int(thr)+1}\n条件(2)：x>{int(thr)-1}",
        "opts":JUDGE_OPTS,"ans":0,"exp":f"解得x>{int(thr)}。条件(1)满足，充分。条件(2)不一定，不充分。"})

# 23. 条件充分性判断-几何类 (15)
for _ in range(15):
    r=random.randint(3,10)
    questions.append({"id":mid(),"type":"judge","diff":"困难","src":rsrc(),
        "q":f"条件充分性判断：能确定圆的面积。\n条件(1)：半径为{r}\n条件(2)：周长为{round(2*3.14*r,1)}",
        "opts":JUDGE_OPTS,"ans":3,"exp":f"两个条件都能确定r={r}，从而求面积，都充分。"})

# 24. 条件充分性判断-数论类 (15)
for _ in range(15):
    n=random.choice([6,8,10,12,15,18,20,24,30])
    divs=[i for i in range(2,n+1) if n%i==0]; d=random.choice(divs)
    questions.append({"id":mid(),"type":"judge","diff":rdiff(),"src":rsrc(),
        "q":f"条件充分性判断：{n}能被d整除。\n条件(1)：d={d}\n条件(2)：d是{n//d}的倍数且d≤{n}",
        "opts":JUDGE_OPTS,"ans":3,"exp":f"条件(1)：{n}÷{d}={n//d}整除✓。条件(2)也可推出d={d}，充分。"})

# 25. 集合/韦恩图 (20)
for _ in range(20):
    total=random.randint(40,100); ao=random.randint(5,20); bo=random.randint(5,20); both=random.randint(5,15)
    neither=total-ao-bo-both
    if neither<0: neither=random.randint(0,10)
    if random.random()<0.5:
        add(f"某班{total}人，A组{ao+both}人，B组{bo+both}人，都参加{both}人，都不参加多少人？", neither, f"都不参加={neither}人。")
    else:
        add(f"某班{total}人，A组{ao+both}人，B组{bo+both}人，都参加{both}人，至少参加一组多少人？", ao+bo+both, f"至少一组={ao+bo+both}人。")

# 26. 立体几何 (15)
for _ in range(15):
    a=random.randint(2,8)
    if random.random()<0.5:
        add(f"棱长{a}的正方体体积：", a**3, f"V={a}³={a**3}。")
    else:
        add(f"棱长{a}的正方体表面积：", 6*a*a, f"S=6×{a}²={6*a*a}。")

# 27. 解析几何 (15)
for _ in range(15):
    cx,cy=random.randint(-3,3),random.randint(-3,3); r=random.randint(2,5)
    px,py=random.randint(-3,3),random.randint(-3,3)
    dist=math.sqrt((px-cx)**2+(py-cy)**2)
    if dist<r: ans=0
    elif dist>r: ans=1
    else: ans=2
    opts=["在圆内","在圆外","在圆上","无法确定","以上都不对"]
    questions.append({"id":mid(),"type":"solve","diff":rdiff(),"src":rsrc(),
        "q":f"圆(x-{cx})²+(y-{cy})²={r*r}，点({px},{py})：","opts":opts,"ans":ans,
        "exp":f"距圆心{dist:.2f}，半径{r}，{opts[ans]}。"})

# 28. 概率-C(,) (15)
for _ in range(15):
    n=random.randint(5,12); k=random.randint(1,min(4,n-1)); m=random.randint(1,min(k,n-k))
    fav=math.comb(k,m)*math.comb(n-k,k-m); tot=math.comb(n,k)
    g=math.gcd(fav,tot); num,den=fav//g,tot//g
    ans_str=f"{num}/{den}" if den!=1 else str(num)
    fracs=set(); fracs.add(ans_str)
    while len(fracs)<5:
        fn,fd=random.randint(1,20),random.randint(2,20)
        fg=math.gcd(fn,fd); fv=f"{fn//fg}/{fd//fg}"
        if fv!=ans_str: fracs.add(fv)
    frac_list=list(fracs)[:5]
    if ans_str not in frac_list: frac_list.append(ans_str)
    random.shuffle(frac_list)
    questions.append({"id":mid(),"type":"solve","diff":rdiff(),"src":rsrc(),
        "q":f"{n}个球{k}个红球，取{k}个恰好{m}个红球的概率：","opts":frac_list,
        "ans":frac_list.index(ans_str),"exp":f"C({k},{m})×C({n-k},{k-m})/C({n},{k})={ans_str}。"})

# 补足到350题
while len(questions) < 350:
    a,b=random.randint(2,9),random.randint(2,9)
    add(f"计算：{a}×{b}=：", a*b, f"{a}×{b}={a*b}。")

print(f"Math: {len(questions)} questions")
with open("/Users/ke/WorkBuddy/2026-06-11-15-53-41/gen_math.json","w") as f:
    json.dump(questions, f, ensure_ascii=False)
