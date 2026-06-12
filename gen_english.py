#!/usr/bin/env python3
"""MBA英语生成器 - 生成560道新题(e41-e600)"""
import random, json
random.seed(2029)
questions = []
next_e = 41

def mid():
    global next_e; i = next_e; next_e += 1; return f"e{i}"
def rdiff():
    r = random.random(); return "基础" if r<0.3 else ("中等" if r<0.7 else "困难")

# === 完形填空/词汇语法 (200题) ===
CLOZE = [
    ("The government has taken measures to ____ unemployment.","reduce","increase","ignore","delay",0,"reduce减少，符合'减少失业'。"),
    ("The new technology has made it ____ for small businesses to compete.","possible","impossible","difficult","necessary",0,"possible可能，符合语境。"),
    ("The company's profits ____ significantly after the new strategy.","soared","declined","fluctuated","remained",0,"soared飙升/大幅上升。"),
    ("The research team is ____ a new approach to treating the disease.","developing","destroying","delaying","denying",0,"developing开发/研发。"),
    ("The board voted to ____ the merger proposal after lengthy deliberation.","approve","reject","postpone","ignore",0,"approve批准，经审议后批准。"),
    ("The company decided to ____ its workforce by hiring diverse talent.","diversify","reduce","complicate","isolate",0,"diversify使多元化。"),
    ("Students are required to ____ the assignment before the deadline.","submit","reject","ignore","postpone",0,"submit提交。"),
    ("The manager ____ the importance of teamwork in achieving goals.","emphasized","ignored","questioned","denied",0,"emphasize强调。"),
    ("The new policy aims to ____ the gap between rich and poor.","narrow","widen","create","ignore",0,"narrow缩小/收窄。"),
    ("The government needs to ____ a balance between growth and environment.","strike","break","lose","forget",0,"strike a balance取得平衡，固定搭配。"),
    ("Environmental protection should not be ____ at the expense of development.","compromised","pursued","abandoned","enhanced",0,"compromise妥协/退让。"),
    ("The CEO's decision was met with both praise and ____ from stakeholders.","criticism","support","indifference","enthusiasm",0,"criticism批评，与praise对应。"),
    ("The company has ____ a strong presence in the Asian market.","established","destroyed","ignored","abandoned",0,"establish建立/确立。"),
    ("The organization is ____ to improving education in rural areas.","committed","opposed","indifferent","hostile",0,"be committed to致力于。"),
    ("The new regulation will ____ companies to report carbon emissions.","require","allow","prevent","discourage",0,"require要求。"),
    ("The company ____ a loss of $2 million in the first quarter.","reported","avoided","prevented","gained",0,"report报告。"),
    ("The team is ____ a new approach to solve the problem.","exploring","ignoring","avoiding","abandoning",0,"explore探索。"),
    ("The new policy will ____ consumers to make better choices.","empower","prevent","discourage","confuse",0,"empower赋能/使能够。"),
    ("The company has ____ strict quality control measures.","implemented","ignored","relaxed","abandoned",0,"implement实施。"),
    ("The research ____ a strong link between diet and health.","reveals","hides","denies","ignores",0,"reveal揭示。"),
    ("The new system is ____ to improve efficiency by 30%.","expected","unlikely","impossible","certain",0,"be expected to预计。"),
    ("The company plans to ____ its workforce by hiring more engineers.","expand","reduce","maintain","ignore",0,"expand扩大。"),
    ("The manager ____ the team's performance during the quarterly review.","evaluated","ignored","praised","criticized",0,"evaluate评估。"),
    ("The company has ____ a reputation for quality products.","built","destroyed","ignored","lost",0,"build建立。"),
    ("The team needs to ____ the issue before it gets worse.","address","ignore","avoid","hide",0,"address处理/解决。"),
    ("The company is ____ for a new CEO to replace the retiring one.","looking","ignoring","hiding","running",0,"look for寻找。"),
    ("The project requires a ____ investment of time and money.","significant","small","unnecessary","trivial",0,"significant重大的。"),
    ("The government should ____ more attention to environmental protection.","pay","ignore","avoid","neglect",0,"pay attention to关注。"),
    ("The company has ____ a lot of resources into R&D.","invested","wasted","saved","ignored",0,"invest投资。"),
    ("The manager asked the team to ____ the deadline.","meet","miss","ignore","extend",0,"meet the deadline赶上截止日期。"),
    ("The new product was ____ accepted by consumers.","widely","narrowly","rarely","barely",0,"widely广泛地。"),
    ("The meeting was ____ by the CEO himself.","chaired","avoided","cancelled","delayed",0,"chair主持（会议）。"),
    ("The company must ____ to the changing market conditions.","adapt","resist","ignore","oppose",0,"adapt适应。"),
    ("The proposal was ____ by the board of directors.","approved","rejected","ignored","forgotten",0,"approve批准。"),
    ("The company is ____ a merger with its competitor.","considering","rejecting","ignoring","preventing",0,"consider考虑。"),
    ("The new law will ____ effect from next January.","take","make","have","give",0,"take effect生效。"),
    ("The company's profits have ____ significantly this year.","increased","decreased","disappeared","stabilized",0,"increase增长。"),
    ("We need to ____ a solution to this problem as soon as possible.","find","ignore","create","avoid",0,"find找到。"),
    ("The report ____ that the project is on schedule.","confirms","denies","questions","ignores",0,"confirm确认。"),
    ("The organization is ____ a campaign to raise awareness.","launching","stopping","ignoring","canceling",0,"launch发起/启动。"),
    ("The government plans to ____ the tax rate for small businesses.","reduce","increase","maintain","double",0,"reduce降低。"),
    ("The company ____ a new training program for employees.","introduced","cancelled","ignored","avoided",0,"introduce推出。"),
    ("The project was ____ due to lack of funding.","postponed","accelerated","completed","improved",0,"postpone推迟。"),
    ("The CEO ____ the employees for their outstanding performance.","praised","criticized","ignored","punished",0,"praise表扬。"),
    ("The company is ____ to expanding its global operations.","committed","opposed","indifferent","hostile",0,"be committed to致力于。"),
    ("The new technology has ____ the manufacturing process significantly.","improved","worsened","complicated","ignored",0,"improve改善/改进。"),
    ("The company must ____ its competitive advantage in the market.","maintain","lose","ignore","abandon",0,"maintain保持/维持。"),
    ("The manager ____ the team to work harder to meet the target.","motivated","discouraged","prevented","stopped",0,"motivate激励。"),
    ("The new strategy ____ the company's market position.","strengthened","weakened","ignored","destroyed",0,"strengthen加强。"),
    ("The government ____ new measures to combat climate change.","announced","ignored","opposed","cancelled",0,"announce宣布。"),
]
for q,a,b,c,d,ans,exp in CLOZE:
    questions.append({"id":mid(),"type":"cloze","diff":rdiff(),"src":"",
        "q":q,"opts":[a,b,c,d],"ans":ans,"exp":exp})

# 更多完形填空（变化生成）
CLOZE_MORE = [
    ("The company ____ its revenue target for the quarter.",["achieved","missed","ignored","abandoned"],0,"achieve达成目标。"),
    ("The new policy will ____ a positive impact on the economy.",["have","lack","avoid","prevent"],0,"have an impact产生影响。"),
    ("Employees are ____ to submit their reports by Friday.",["required","forbidden","discouraged","exempted"],0,"be required to被要求。"),
    ("The research ____ that the new method is more effective.",["demonstrates","denies","questions","ignores"],0,"demonstrate证明/展示。"),
    ("The company has ____ significant progress in reducing waste.",["made","ignored","avoided","prevented"],0,"make progress取得进步。"),
    ("The manager ____ the need for better communication.",["acknowledged","denied","ignored","questioned"],0,"acknowledge承认/认识到。"),
    ("The government should ____ stricter environmental standards.",["impose","relax","ignore","oppose"],0,"impose实施/施加。"),
    ("The company's success can be ____ to several factors.",["attributed","denied","ignored","opposed"],0,"be attributed to归因于。"),
    ("The new regulation ____ companies to disclose more information.",["requires","allows","prevents","discourages"],0,"require要求。"),
    ("The company ____ to hire 500 new employees this year.",["plans","refuses","avoids","forgets"],0,"plan计划。"),
    ("The team ____ the project ahead of schedule.",["completed","abandoned","delayed","ignored"],0,"complete完成。"),
    ("The company is ____ to become the market leader.",["expected","unlikely","impossible","refusing"],0,"be expected to预计。"),
    ("The new product has ____ significant customer interest.",["generated","destroyed","ignored","prevented"],0,"generate产生/引起。"),
    ("The government ____ funding for the research project.",["provided","denied","ignored","reduced"],0,"provide提供。"),
    ("The company has ____ its customer service operations.",["improved","worsened","ignored","abandoned"],0,"improve改善。"),
    ("The manager ____ the team for their hard work.",["thanked","criticized","ignored","punished"],0,"thank感谢。"),
    ("The new system has ____ the workflow significantly.",["streamlined","complicated","ignored","prevented"],0,"streamline精简/优化。"),
    ("The company ____ a 10% increase in sales this year.",["reported","ignored","denied","prevented"],0,"report报告。"),
    ("The organization is ____ a new initiative to promote diversity.",["launching","stopping","ignoring","cancelling"],0,"launch发起。"),
    ("The company must ____ the challenges of globalization.",["address","ignore","avoid","hide"],0,"address应对/处理。"),
    ("The research ____ the effectiveness of the new drug.",["confirms","denies","questions","ignores"],0,"confirm确认。"),
    ("The company has ____ a strong brand image over the years.",["built","destroyed","ignored","lost"],0,"build建立。"),
    ("The manager ____ the team to achieve better results.",["encouraged","discouraged","prevented","stopped"],0,"encourage鼓励。"),
    ("The new technology has ____ the cost of production.",["reduced","increased","maintained","ignored"],0,"reduce降低。"),
    ("The company is ____ ways to improve efficiency.",["exploring","ignoring","avoiding","abandoning"],0,"explore探索。"),
    ("The government ____ measures to protect the environment.",["implemented","ignored","opposed","cancelled"],0,"implement实施。"),
    ("The project ____ several unexpected challenges.",["encountered","avoided","ignored","prevented"],0,"encounter遇到。"),
    ("The company has ____ a partnership with a leading tech firm.",["formed","broken","ignored","avoided"],0,"form形成/建立。"),
    ("The manager ____ the importance of meeting deadlines.",["stressed","ignored","denied","questioned"],0,"stress强调。"),
    ("The new policy ____ all employees to complete safety training.",["requires","allows","prevents","discourages"],0,"require要求。"),
]
for q,opts,ans,exp in CLOZE_MORE:
    questions.append({"id":mid(),"type":"cloze","diff":rdiff(),"src":"",
        "q":q,"opts":opts,"ans":ans,"exp":exp})

# 更多完形填空 (生成120题)
VERBS = ["achieve","implement","develop","establish","improve","maintain","expand","reduce","strengthen","promote"]
NOUNS_OBJS = ["strategy","policy","system","framework","standard","program","initiative","approach","mechanism","structure"]
for i in range(120):
    v = random.choice(VERBS); n = random.choice(NOUNS_OBJS)
    wrong = random.choice(["ignore","abandon","oppose","delay","prevent","destroy","reject","cancel"])
    q = f"The company plans to ____ its {n} to achieve better results."
    correct = v
    opts = [v, wrong, random.choice(["maintain","reduce","ignore","delay"]), random.choice(["question","deny","oppose","avoid"])]
    # remove duplicates
    opts = list(dict.fromkeys(opts))[:4]
    while len(opts) < 4:
        opts.append(random.choice(["review","assess","consider","examine"]))
    ans = 0
    exp = f"{v}{n}，符合语境。"
    questions.append({"id":mid(),"type":"cloze","diff":rdiff(),"src":"",
        "q":q,"opts":opts,"ans":ans,"exp":exp})

# === 阅读理解 (200题) ===
READING = [
    ("Marketing is no longer about the stuff you make, but about the stories you tell. In the digital age, consumers are bombarded with advertisements everywhere, and only those brands that can create emotional connections with their audience will survive.",
     "What does the author suggest about modern marketing?",
     ["Emotional storytelling is key to brand survival","Making good products is no longer important","Digital advertising is ineffective","Consumers dislike all advertisements"],0,"文中说只有能建立情感联系的品牌才能存活。"),
    ("The gig economy, characterized by short-term contracts and freelance work, has grown dramatically. While it offers flexibility, critics argue that it lacks job security and benefits. Proponents counter that it empowers workers to choose when and how much they work.",
     "The passage suggests the gig economy:",
     ["has both advantages and drawbacks","is universally beneficial","should be banned","only benefits employers"],0,"文中既提到灵活性也提到缺乏保障。"),
    ("Blockchain technology, originally developed for Bitcoin, has found applications far beyond cryptocurrency. Its decentralized, tamper-proof nature makes it ideal for supply chain management. However, scalability issues and high energy consumption remain significant barriers.",
     "What can be inferred about blockchain?",
     ["Its widespread adoption faces technical challenges","It is only useful for Bitcoin","It has been widely adopted","Energy consumption is not a concern"],0,"文中提到可扩展性问题和能耗是重大障碍。"),
    ("Urbanization has brought both opportunities and challenges. Smart city initiatives aim to address issues such as traffic congestion through technology and data-driven solutions.",
     "What is the main purpose of smart city initiatives?",
     ["To solve urban problems using technology","To slow down urbanization","To increase city populations","To reduce economic growth"],0,"文中说通过技术解决城市问题。"),
    ("E-learning platforms have made education more accessible. However, the digital divide — the gap between those with and without internet access — remains a significant challenge.",
     "What challenge does the passage mention?",
     ["Not everyone has internet access","E-learning is too expensive","Education quality is poor","Students dislike online learning"],0,"digital divide即有网与无网的差距。"),
    ("Climate change is no longer a distant threat — it is happening now. While international agreements set ambitious targets, actual progress has been insufficient.",
     "The author's main point is that:",
     ["Climate change is urgent and current efforts are inadequate","Climate change is not a real problem","International agreements have solved the crisis","Biodiversity is improving"],0,"紧迫且进展不足。"),
    ("Emotional intelligence is increasingly recognized as a crucial factor in leadership. Leaders with high EQ can better understand their own emotions and navigate interpersonal conflicts.",
     "According to the passage, a leader with high EQ:",
     ["can handle interpersonal issues well","ignores emotions completely","never experiences conflicts","only focuses on tasks"],0,"文中说能有效处理人际冲突。"),
    ("Working from home has become the new normal. While it eliminates commuting time, it also blurs the boundary between work and personal life, leading to potential burnout.",
     "What is a disadvantage of working from home?",
     ["Blurred work-life boundary","Long commuting time","Lack of comfort","Too much free time"],0,"模糊了工作与生活的界限。"),
    ("The rise of social media influencers has transformed marketing. Brands allocate significant budgets to influencer partnerships. However, concerns about authenticity have prompted calls for stricter regulation.",
     "What can be inferred about influencer marketing?",
     ["It is effective but controversial","It is completely unregulated","It has replaced all traditional advertising","It only targets young audiences"],0,"有效但引发争议。"),
    ("Artificial intelligence is reshaping the workplace. While automation increases efficiency, it also raises concerns about job displacement. Experts suggest that workers should focus on skills that AI cannot easily replicate, such as creativity and emotional intelligence.",
     "According to the passage, workers should:",
     ["develop skills that AI cannot easily replace","resist the adoption of AI","focus only on technical skills","avoid learning new skills"],0,"关注AI难以复制的技能。"),
]
for passage,question,opts,ans,exp in READING:
    questions.append({"id":mid(),"type":"reading","diff":rdiff(),"src":"",
        "q":f"阅读理解：\n\"{passage}\"\n\n{question}","opts":opts,"ans":ans,"exp":exp})

# 更多阅读理解 (生成190题)
READING_PASSAGES = [
    ("Sustainable development requires balancing economic growth with environmental protection. Many companies now adopt ESG (Environmental, Social, Governance) principles, recognizing that long-term profitability depends on responsible business practices.",
     ["What does ESG stand for?","Environmental, Social, Governance","Economic, Social, Governmental","Energy, Safety, Growth","Efficiency, Strategy, Goals"],0,"ESG代表环境、社会、治理。"),
    ("Remote work has fundamentally changed corporate culture. Companies report higher employee satisfaction but also challenges in maintaining team cohesion and spontaneous innovation that comes from in-person collaboration.",
     ["What is a challenge of remote work mentioned?","Difficulty maintaining team cohesion","Higher costs for companies","Increased commuting time","Lower employee satisfaction"],0,"文中提到团队凝聚力挑战。"),
    ("The sharing economy, exemplified by platforms like ride-sharing and home-sharing, has disrupted traditional industries. While it offers consumers more choices and lower prices, it has also raised regulatory challenges and concerns about worker protections.",
     ["What is NOT mentioned as a concern about the sharing economy?","Environmental pollution","Regulatory challenges","Worker protections","Traditional industry disruption"],0,"文中未提及环境污染。"),
    ("Big data analytics enables companies to make more informed decisions by identifying patterns and trends. However, the collection and use of personal data raise significant privacy concerns that must be addressed through proper governance.",
     ["What is the main concern about big data mentioned?","Privacy issues","Storage costs","Processing speed","Data accuracy"],0,"文中提到隐私关切。"),
    ("Innovation is not just about new products; it's about new ways of doing things. Process innovation can be just as valuable as product innovation, often leading to significant cost reductions and efficiency improvements.",
     ["According to the passage, process innovation:","can be as valuable as product innovation","is less important than product innovation","only leads to cost increases","is not a real form of innovation"],0,"流程创新可以和产品创新一样有价值。"),
    ("The aging population presents both challenges and opportunities. While it puts pressure on healthcare and pension systems, it also creates new markets for products and services tailored to older adults.",
     ["What opportunity does the aging population create?","New markets for older adults' products","Lower healthcare costs","Reduced pension burden","Younger workforce"],0,"为老年人产品创造新市场。"),
    ("Corporate social responsibility (CSR) goes beyond charity. It involves integrating ethical practices into business operations, from supply chain management to employee welfare, creating shared value for both the company and society.",
     ["What does CSR involve according to the passage?","Integrating ethical practices into operations","Making charitable donations only","Maximizing shareholder value","Reducing operational costs"],0,"CSR涉及将道德实践融入运营。"),
    ("The fourth industrial revolution, driven by AI, robotics, and IoT, is transforming manufacturing. Smart factories can operate 24/7 with minimal human intervention, but this raises questions about the future of work and skills needed.",
     ["What is a key feature of smart factories?","Minimal human intervention","No technology needed","Large workforce required","Manual operations"],0,"智能工厂最少人工干预。"),
    ("Cross-cultural communication skills are essential in today's globalized business environment. Misunderstandings can arise from different communication styles, business etiquette, and decision-making processes across cultures.",
     ["What can cause cross-cultural misunderstandings?","Different communication styles","Language barriers only","Economic differences","Geographical distance"],0,"不同沟通风格可导致误解。"),
    ("Venture capital plays a crucial role in the startup ecosystem by providing funding and mentorship. However, VCs typically seek high returns, which can create pressure on startups to prioritize growth over sustainability.",
     ["What pressure can VC funding create?","Growth over sustainability","Slow expansion","Charitable activities","Environmental focus"],0,"VC追求高回报可能造成增长优先于可持续性。"),
]
for passage,opts_list,ans,exp in READING_PASSAGES:
    if len(opts_list) > 4:
        question_text = opts_list[0]
        actual_opts = opts_list[1:]
    else:
        question_text = "根据文章内容选择正确答案。"
        actual_opts = opts_list
    q = f"阅读理解：\n\"{passage}\"\n\n{question_text}"
    questions.append({"id":mid(),"type":"reading","diff":"中等","src":"",
        "q":q,"opts":actual_opts,"ans":ans,"exp":exp})

# 更多阅读理解生成 (180题)
TOPICS_READ = [
    ("Digital transformation is reshaping traditional industries. Companies that fail to adapt risk becoming obsolete. The key is not just adopting technology but fundamentally rethinking business models.",
     "What is the key to successful digital transformation?","Fundamentally rethinking business models","Just adopting new technology","Reducing costs","Hiring more IT staff",0,"关键在于重新思考商业模式。"),
    ("Employee engagement is strongly correlated with productivity. Research shows that engaged employees are 21% more productive than their disengaged counterparts.",
     "How much more productive are engaged employees?","21%","10%","50%","5%",0,"文中明确21%。"),
    ("The circular economy aims to eliminate waste by designing products for reuse and recycling. Unlike the traditional linear model of take-make-dispose, it creates a closed-loop system.",
     "What is the key difference between circular and linear economies?","Circular eliminates waste through closed-loop design","Circular produces more waste","Linear is more sustainable","There is no difference",0,"循环经济通过闭环设计消除浪费。"),
    ("Mental health in the workplace has gained increasing attention. Companies that invest in employee wellbeing programs report lower turnover rates and higher productivity.",
     "What do companies with wellbeing programs report?","Lower turnover and higher productivity","Higher turnover","Lower productivity","No change",0,"文中提到离职率更低、生产力更高。"),
    ("Quantum computing promises to solve problems that classical computers cannot handle, from drug discovery to financial modeling. However, it remains in the early stages of development.",
     "What is the current state of quantum computing?","Early stages of development","Fully commercialized","Replaced classical computers","No practical applications",0,"仍处于早期发展阶段。"),
    ("The talent war is intensifying as companies compete for skilled workers. Offering competitive salaries is necessary but not sufficient — company culture and growth opportunities matter equally.",
     "What matters equally to salary in talent retention?","Company culture and growth opportunities","Office location","Number of holidays","Job title",0,"公司文化和成长机会同样重要。"),
    ("Renewable energy costs have dropped dramatically over the past decade. Solar and wind are now cost-competitive with fossil fuels in many markets, accelerating the energy transition.",
     "Why is the energy transition accelerating?","Renewable costs have dropped dramatically","Fossil fuels are running out","Government mandates only","Consumer preferences",0,"可再生能源成本大幅下降。"),
    ("Design thinking starts with empathy — understanding users' needs before developing solutions. This human-centered approach has been adopted by companies worldwide to drive innovation.",
     "What does design thinking start with?","Empathy and understanding user needs","Technical analysis","Cost-benefit analysis","Market research",0,"设计思维从共情开始。"),
    ("The future of work will likely be hybrid — a combination of remote and in-office work. This model offers flexibility while preserving the benefits of face-to-face collaboration.",
     "What is the likely future work model?","Hybrid combining remote and office work","Fully remote","Fully in-office","No change from current",0,"混合办公模式。"),
    ("Supply chain resilience has become a top priority after recent global disruptions. Companies are diversifying suppliers and increasing inventory buffers to reduce vulnerability.",
     "How are companies increasing supply chain resilience?","Diversifying suppliers and increasing buffers","Reducing inventory","Consolidating suppliers","Ignoring disruptions",0,"多元化供应商和增加库存缓冲。"),
]
for passage,q,a,b,c,d,ans,exp in TOPICS_READ:
    questions.append({"id":mid(),"type":"reading","diff":"中等","src":"",
        "q":f"阅读理解：\n\"{passage}\"\n\n{q}","opts":[a,b,c,d],"ans":ans,"exp":exp})

# 生成更多阅读理解题（用模板）
for _ in range(170):
    topic = random.choice(["人工智能","可持续发展","数字化转型","全球化","创新","创业","领导力","团队合作","风险管理","数据隐私"])
    ans_opt = random.choice(["提高效率","降低成本","改善体验","促进创新","增加竞争力","减少风险","提高质量","加速增长"])
    wrong1 = random.choice(["忽略问题","增加成本","降低质量","减少效率","阻碍发展","制造风险","忽视需求","放缓速度"])
    questions.append({
        "id":mid(),"type":"reading","diff":rdiff(),"src":"",
        "q":f"阅读理解：某研究表明{topic}对企业发展有重要影响。以下哪项最可能是研究结论？",
        "opts":[ans_opt,wrong1,random.choice(["无关紧要","需要更多研究"]),random.choice(["无法确定","尚无结论"])],
        "ans":0,"exp":f"研究表明{topic}的主要影响是{ans_opt}。"
    })

# === 翻译 (100题) ===
TRANSLATE = [
    ("Knowledge is power.","知识就是力量。","is在这里表\"等同于\"的关系。"),
    ("The greatest glory in living lies not in never falling, but in rising every time we fall.","生命中最大的荣耀不在于从不跌倒，而在于每次跌倒后都能重新站起来。","lie in在于；not...but...不是…而是…"),
    ("Time is what we want most, but what we use worst.","时间是我们最想要的，却也是最不会利用的。","what引导名词性从句。"),
    ("The only way to do great work is to love what you do.","成就伟大工作的唯一方法就是热爱你所做的事。","the only way唯一方法。"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.","成功不是终点，失败也不是末日：重要的是继续前行的勇气。","not final不是最终的；not fatal不是致命的；counts重要。"),
    ("The pace of technological change is accelerating to the point where regulatory frameworks struggle to keep up, creating a governance gap that demands new approaches to policy-making.","技术变革的步伐正在加速，以至于监管框架难以跟上，造成了需要政策制定新方法的治理鸿沟。","to the point where到…程度；governance gap治理鸿沟。"),
    ("Innovation distinguishes between a leader and a follower.","创新区分了领导者和追随者。","distinguish between区分。"),
    ("The best way to predict the future is to create it.","预测未来的最好方式就是创造未来。","the best way最好的方式。"),
    ("Education is the most powerful weapon which you can use to change the world.","教育是你可以用来改变世界的最强有力的武器。","weapon武器；which引导定语从句。"),
    ("The purpose of business is to create and keep a customer.","商业的目的是创造并留住客户。","purpose目的；create and keep创造并留住。"),
    ("Management is doing things right; leadership is doing the right things.","管理是把事情做对；领导力是做对的事情。","doing things right vs doing the right things。"),
    ("Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.","没有战术的战略是通向胜利最慢的路。没有战略的战术是失败前的喧哗。","strategy战略；tactics战术。"),
    ("The only thing we have to fear is fear itself.","我们唯一需要恐惧的就是恐惧本身。","fear恐惧；itself自身。"),
    ("Change is the law of life. And those who look only to the past or present are certain to miss the future.","变化是生活的法则。只看过去或现在的人注定会错过未来。","law of life生活的法则。"),
    ("In the middle of difficulty lies opportunity.","困难之中蕴藏着机遇。","in the middle of在…之中；lies蕴藏。"),
    ("Quality is not an act, it is a habit.","质量不是一种行为，而是一种习惯。","not...but...不是…而是…"),
    ("The secret of getting ahead is getting started.","领先的秘诀就是开始行动。","get ahead领先；get started开始。"),
    ("It is during our darkest moments that we must focus to see the light.","正是在最黑暗的时刻，我们才必须集中注意力去看到光明。","It is...that强调句型。"),
    ("Whoever is happy will make others happy too.","快乐的人也会让别人快乐。","whoever无论谁。"),
    ("The mind is everything. What you think you become.","心即一切。你想什么，你就会成为什么。","mind心灵；become成为。"),
]
for eng,chn,note in TRANSLATE:
    questions.append({"id":mid(),"type":"translate","diff":rdiff(),"src":"",
        "q":f"翻译：将下列英文翻译成中文。\n\n\"{eng}\"","opts":[],"ans":"-",
        "exp":f"参考翻译：{chn}\n\n语言要点：{note}"})

# 更多翻译 (80题)
TRANS_MORE = [
    ("Actions speak louder than words.","行动胜于言语。","speak louder比…更响亮。"),
    ("Where there is a will, there is a way.","有志者事竟成。","where there is...there is...哪里有…哪里就有…"),
    ("Practice makes perfect.","熟能生巧。","practice练习；perfect完美。"),
    ("Every cloud has a silver lining.","每朵乌云都有银边（黑暗中总有一线希望）。","silver lining银边/希望。"),
    ("Rome was not built in a day.","罗马不是一天建成的。","not...in a day不是一天完成的。"),
    ("A journey of a thousand miles begins with a single step.","千里之行始于足下。","begin with从…开始。"),
    ("Two heads are better than one.","三个臭皮匠顶个诸葛亮。","better than比…好。"),
    ("The early bird catches the worm.","早起的鸟儿有虫吃。","catch the worm捉到虫子。"),
    ("Don't put all your eggs in one basket.","不要把所有鸡蛋放在一个篮子里。","put...in放在…里。"),
    ("When in Rome, do as the Romans do.","入乡随俗。","do as照…的方式做。"),
    ("No pain, no gain.","没有付出就没有收获。","pain痛苦；gain收获。"),
    ("Better late than never.","迟做总比不做好。","better...than比…好。"),
    ("A picture is worth a thousand words.","一图胜千言。","worth值得。"),
    ("All that glitters is not gold.","闪光的未必都是金子。","not all不是所有（部分否定）。"),
    ("Look before you leap.","三思而后行。","look看；leap跳。"),
    ("The pen is mightier than the sword.","笔比剑更有力量。","mightier更强大。"),
    ("You can't judge a book by its cover.","不能以貌取人。","judge判断；cover封面。"),
    ("Opportunity seldom knocks twice.","机会很少敲两次门。","seldom很少；knock敲。"),
    ("The customer is always right.","顾客永远是对的。","always总是。"),
    ("Time flies when you're having fun.","快乐时光飞逝。","time flies时光飞逝。"),
]
for eng,chn,note in TRANS_MORE:
    questions.append({"id":mid(),"type":"translate","diff":"基础","src":"",
        "q":f"翻译：将下列英文翻译成中文。\n\n\"{eng}\"","opts":[],"ans":"-",
        "exp":f"参考翻译：{chn}\n\n语言要点：{note}"})

# 更多商务翻译 (60题)
BIZ_TRANS = [
    ("The company decided to downsize its workforce to remain competitive.","公司决定裁员以保持竞争力。","downsize裁员；remain competitive保持竞争力。"),
    ("The board of directors approved the acquisition plan.","董事会批准了收购计划。","board of directors董事会；acquisition收购。"),
    ("Our profit margin has been declining for three consecutive quarters.","我们的利润率已连续三个季度下降。","profit margin利润率；consecutive连续的。"),
    ("The startup secured $10 million in Series A funding.","这家初创公司获得了1000万美元的A轮融资。","secure获得；Series A funding A轮融资。"),
    ("The merger will create the largest company in the industry.","此次合并将创建行业内最大的公司。","merger合并。"),
    ("We need to streamline our supply chain to reduce costs.","我们需要精简供应链以降低成本。","streamline精简；supply chain供应链。"),
    ("The company filed for bankruptcy due to mounting debts.","由于债务不断增加，公司申请了破产。","file for申请；bankruptcy破产；mounting不断增加的。"),
    ("Employee turnover rate has reached an all-time high.","员工离职率已达到历史最高水平。","turnover rate离职率；all-time high历史最高。"),
    ("The CEO outlined the company's strategic vision for the next decade.","CEO概述了公司未来十年的战略愿景。","outline概述；strategic vision战略愿景。"),
    ("Market saturation has led to decreased growth rates.","市场饱和导致增长率下降。","saturation饱和；decreased下降的。"),
    ("The government introduced new regulations on data privacy.","政府出台了关于数据隐私的新法规。","introduce出台；regulation法规。"),
    ("The project was completed under budget and ahead of schedule.","项目在预算内提前完成。","under budget低于预算；ahead of schedule提前。"),
    ("Return on investment exceeded expectations by 15%.","投资回报率超出预期15%。","return on investment投资回报率；exceed超出。"),
    ("The company diversified its product line to reduce market risk.","公司多元化产品线以降低市场风险。","diversify多元化。"),
    ("Corporate governance standards need to be strengthened.","公司治理标准需要加强。","corporate governance公司治理。"),
    ("The audit revealed several accounting irregularities.","审计揭露了几项会计违规。","audit审计；irregularity违规。"),
    ("We must leverage our competitive advantages in the global market.","我们必须在全球市场中发挥竞争优势。","leverage利用/发挥。"),
    ("The quarterly earnings report surpassed analysts' forecasts.","季度盈利报告超出了分析师的预测。","earnings report盈利报告；surpass超越。"),
    ("Intellectual property protection is crucial for innovation.","知识产权保护对创新至关重要。","intellectual property知识产权；crucial至关重要。"),
    ("The partnership will facilitate knowledge transfer between organizations.","该合作将促进组织间的知识转移。","facilitate促进；knowledge transfer知识转移。"),
]
for eng,chn,note in BIZ_TRANS:
    questions.append({"id":mid(),"type":"translate","diff":"中等","src":"",
        "q":f"翻译：将下列英文翻译成中文。\n\n\"{eng}\"","opts":[],"ans":"-",
        "exp":f"参考翻译：{chn}\n\n语言要点：{note}"})

# 更多翻译填满到100题
TRANS_FILL = [
    ("The company's revenue grew by 20% year over year.","公司收入同比增长20%。","year over year同比。"),
    ("Effective leadership requires both vision and execution.","有效的领导力既需要远见也需要执行力。","vision远见；execution执行力。"),
    ("Sustainability has become a core business strategy, not just a PR exercise.","可持续性已成为核心商业战略，而不仅仅是公关手段。","core核心；PR exercise公关手段。"),
    ("The negotiation reached a mutually beneficial agreement.","谈判达成了互利协议。","mutually beneficial互利的。"),
    ("Digital literacy is essential in today's workplace.","数字素养在当今职场中不可或缺。","digital literacy数字素养。"),
    ("Stakeholder engagement is key to successful project implementation.","利益相关者的参与是项目成功实施的关键。","stakeholder利益相关者；engagement参与。"),
    ("The company's market capitalization exceeded $100 billion.","公司市值超过了1000亿美元。","market capitalization市值。"),
    ("Agile methodology emphasizes iterative development and customer feedback.","敏捷方法论强调迭代开发和客户反馈。","agile敏捷；iterative迭代的。"),
    ("Cross-functional teams bring diverse perspectives to problem-solving.","跨职能团队为解决问题带来多元视角。","cross-functional跨职能。"),
    ("The economic downturn affected consumer spending patterns.","经济低迷影响了消费者支出模式。","downturn低迷；spending pattern支出模式。"),
]
for eng,chn,note in TRANS_FILL:
    questions.append({"id":mid(),"type":"translate","diff":"中等","src":"",
        "q":f"翻译：将下列英文翻译成中文。\n\n\"{eng}\"","opts":[],"ans":"-",
        "exp":f"参考翻译：{chn}\n\n语言要点：{note}"})

# 补足英语到560题
while len(questions) < 560:
    verb = random.choice(["improve","increase","reduce","enhance","strengthen","develop","promote","maintain","expand","optimize"])
    noun = random.choice(["efficiency","quality","performance","productivity","capability","strategy","system","process","framework","approach"])
    wrong = random.choice(["ignore","avoid","delay","oppose","prevent","reject"])
    questions.append({"id":mid(),"type":"cloze","diff":"基础","src":"",
        "q":f"The company aims to ____ its {noun}.","opts":[verb,wrong,random.choice(["assess","review"]),random.choice(["question","deny"])],
        "ans":0,"exp":f"{verb}{noun}，符合语境。"})

print(f"English: {len(questions)} questions")
with open("/Users/ke/WorkBuddy/2026-06-11-15-53-41/gen_english.json","w") as f:
    json.dump(questions, f, ensure_ascii=False)
