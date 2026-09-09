# Nested-(TTSS)True Team Success Statistics-Sports-Framework
A 3-tier sports analytics framework designed to # The 3-Tier Nested TTSS Sports Analytics Framework
**Created by:** Shivam Sharma 
**Release Date:** September 2026  
**License:** MIT Open-Source License  

## 1. Overview & Problem Statement
Traditional tournament analytics suffer heavily from **Expansion Bias**. When sports leagues expand their brackets over time (e.g., FIFA expanding from the Round of 16 to the Round of 32) or introduce new franchises at different eras, older teams artificially accumulate larger data pools. This framework introduces a three-tiered, sport-agnostic metric architecture that evaluates teams purely on **round-by-round efficiency** and enforces a **longevity accountability tax** to treat all eras and team lifespans identically.

In this system, **lower scores represent higher performance/efficiency**, with a theoretical perfect run approaching zero.

---

## 2. The 3-Tier Architectural Hierarchy

### Tier 1: Team Success Stat (TSS)
Measures a team's performance inside a single, isolated tournament cycle using a descending geometric penalty scale ($32 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$).
$$\text{TSS} = \frac{\sum(\text{Geometric Knockout Round Penalties})}{\text{Adjusted Denominator}}$$
* **Modern Expansion Rule:** To resolve modern format shifts where teams play the same amount of games but finish in different ranks (e.g., 3rd-place matches), the denominator is calculated as:
  $$\text{Adjusted Denominator} = \text{Average}(\text{Final Placement Rank}, \text{Knockout Rounds Achieved})$$

### Tier 2: Nested TSS
Evaluates macro organizational capability across multiple years by passing the compiled historical data pool through the core TSS blueprint:
$$\text{Nested TSS} = \frac{\sum_{i=1}^{n} \text{TSS}_i}{\text{Total Lifespan Knockout Rounds Played}}$$

### Tier 3: Nested True Team Success Stat (Nested TTSS)
The ultimate macro-index engine. It applies a longevity accountability tax by multiplying the Nested TSS by the team's total active operational lifespan, completely flattening era expansion and playground bias:
$$\text{Nested TTSS} = \text{Nested TSS} \times \text{Active Years Competed}$$

---

## 3. Proven Empirical Implementations

### Case Study A: FIFA World Cups (2006–2026)
*Evaluates absolute international football performance across changing tournament architectures, specifically penalizing systemic qualification failures and early chokes while capturing the expanded 48-team, Round of 32 architecture of the 2026 iteration.*

#### Macro Historical Leaderboard
*Sorted strictly by: Lowest Nested TTSS = 1st Rank.*

| Rank | Country | Years Active | Sum of All Years TSS | Total Knockout Rounds Played | Nested TSS (Sum ÷ Rounds) | **Nested TTSS (Nested TSS × Years)** | Ultimate Performance Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 🥇 **1** | 🇫🇷 France | 6 | 63.20 | 21 | 3.0095 | **18.05** | **Absolute Global Leader.** High round-density cushions tournament tax. |
| 🥈 **2** | 🇦🇷 Argentina | 6 | 71.41 | 19 | 3.7584 | **22.55** | Elite dynasty heavily anchored by multi-finals appearances. |
| 🥉 **3** | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England | 6 | 81.08 | 14 | 5.7914 | **34.74** | Consistent runner-up; avoids early catastrophic chokes. |
| **4** | 🇪🇸 Spain | 6 | 88.20 | 15 | 5.8800 | **35.28** | Double champions whose mid-era drops create massive penalty drag. |
| **5** | 🇧🇷 Brazil | 6 | 81.33 | 13 | 6.2561 | **37.53** | Historically stable giant choked by opening-knockout bottlenecks. |
| **6** | 🇩🇪 Germany | 6 | 88.87 | 14 | 6.3478 | **38.08** | Exceptional early era completely undone by group/R32 collapses. |
| **7** | 🇭🇷 Croatia | 6 | 88.83 | 12 | 7.4025 | **44.41** | Massive podium spikes balanced by extreme dry spell cycles. |
| **8** | 🇳🇱 Netherlands | 6 | 92.83 | 12 | 7.7358 | **46.41** | High efficiency density hindered by failure to qualify in full cycles. |
| **9** | 🇵🇹 Portugal | 6 | 93.33 | 10 | 9.3330 | **55.99** | Complete baseline failure; unable to generate top-tier round volume. |
| **10** | 🇮🇹 Italy | 6 | 102.20 | 10 | 10.2200 | **61.32** | **Systemic Decay.** Historical trophy completely erased by qualification absences. |

---

### Case Study B: UEFA Champions League (2006–2026)
*Applies the 3-tier structure to 21 consecutive cycles of elite European club football, adjusting metrics seamlessly for the 2025/2026 Knockout Play-off expansion formats using the custom Rank + Rounds calculation method.*

#### Macro Historical Leaderboard
*Sorted strictly by: Lowest Nested TTSS = 1st Rank.*

| Rank | Club | Years Active | Sum of All Years TSS | Total Knockout Rounds Played | Nested TSS (Sum ÷ Rounds) | **Nested TTSS (Nested TSS × Years)** | Ultimate Performance Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 🥇 **1** | 🇪🇸 Real Madrid | 21 | 215.30 | 73 | 2.9493 | **61.93** | **Unchallenged Dynastic Leader.** Record-breaking 73-round baseline. |
| 🥈 **2** | 🇩🇪 Bayern Munich | 21 | 231.20 | 62 | 3.7290 | **78.31** | High-efficiency organization; rarely exits at the baseline tier. |
| 🥉 **3** | 🇪🇸 Barcelona | 21 | 258.40 | 54 | 4.7852 | **100.48** | Massive initial era severely dragged down by post-2020 decline. |
| **4** | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Manchester City | 21 | 284.10 | 48 | 5.9187 | **124.28** | Modern powerhouse actively diluting past low-round decades. |
| **5** | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Liverpool | 21 | 290.30 | 41 | 7.0804 | **148.68** | Extreme peaks balanced by multi-year absences from the pool. |
| **6** | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Chelsea | 21 | 302.50 | 40 | 7.5625 | **158.80** | Modern institutional drop neutralizes deep multi-trophy history. |
| **7** | 🇫🇷 Paris Saint-Germain | 21 | 318.60 | 42 | 7.5857 | **159.28** | Back-to-back modern trophies barely rescue past round-of-16 chokes. |
| **8** | 🇮🇹 Juventus | 21 | 322.10 | 36 | 8.9472 | **187.89** | Suffers intensely from persistent baseline eliminations. |
| **9** | 🇮🇹 AC Milan | 21 | 344.00 | 28 | 12.2857 | **257.98** | **Sleeping Giant Exposed.** A full decade outside the knockouts explodes tax. |

---

---

### Case Study C: Indian Premier League Cricket (2008–2026)
*Evaluates franchise cricket organizational efficiency across 19 seasons, perfectly managing the structural change from the early 4-team Semifinals format to the modern Page Playoff matrix, and applying the longevity tax to evaluate new expansion teams side-by-side with founding franchises.*

#### Macro Historical Leaderboard
*Sorted strictly by: Lowest Nested TTSS = 1st Rank.*

| Rank | Franchise | Years Active | Sum of All Years TSS | Total Knockout Rounds Played | Nested TSS (Sum ÷ Rounds) | **Nested TTSS (Nested TSS × Years)** | Ultimate Performance Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 🥇 **1** | Gujarat Titans (GT) | 5 | 22.20 | 8 | 2.7750 | **13.87** | **Peak Efficiency Leader.** Highly protected by an explosive 5-year active lifespan. |
| 🥈 **2** | Chennai Super Kings (CSK) | 19 | 62.41 | 37 | 1.6867 | **32.03** | **Ultimate Old Dynasty.** Record-breaking 37-round pool absorbs longevity tax. |
| 🥉 **3** | Mumbai Indians (MI) | 19 | 66.01 | 34 | 1.9414 | **36.88** | Elite institutional strength backed heavily by their 5-trophy density. |
| **4** | Sunrisers Hyderabad (SRH) | 14 | 71.92 | 22 | 3.2690 | **45.76** | **Flaw Fixed.** Shorter operational lifespan allows them to cleanly defeat RCB. |
| **5** | Kolkata Knight Riders (KKR) | 19 | 69.11 | 27 | 2.5596 | **48.62** | Very steady macro-performer across two full operational decades. |
| **6** | Royal Challengers Bengaluru (RCB) | 19 | 68.31 | 26 | 2.6273 | **49.91** | Heavily taxed for early-era playoff droughts despite late-era dominance. |
| **7** | Rajasthan Royals (RR) | 19 | 73.13 | 21 | 3.4823 | **66.16** | Initial 2008 championship heavily diluted by long mid-era dry spells. |
| **8** | Delhi Capitals (DC) | 19 | 74.45 | 17 | 4.3794 | **83.20** | Suffers immense penalty accumulation from decades of missing playoffs. |
| **9** | Punjab Kings (PBKS) | 19 | 75.20 | 14 | 5.3714 | **102.05** | **Systemic Underperformance.** Consistently choked at the baseline tier. |

 ## 4. How to Use the Python Engine

You do not need to be a software engineer to run this framework. Follow these simple steps to calculate your own sports datasets:

### Prerequisites
Make sure you have **Python** installed on your computer. If you do not have it, download it for free from [python.org](https://python.org).

### Step-by-Step Guide
1. **Download the Engine:** Click on the `ttss_engine.py` file above in this repository, then click the **Download raw file** button (the small arrow icon at the top right of the code window) to save it to your computer.
2. **Open the File:** Open the `ttss_engine.py` file using any text editor (like Notepad on Windows or TextEdit on Mac).
3. **Input Your Data:** Scroll down to the `historical_db` section at the bottom of the script. Change the team names and plug in your own data numbers using this exact format:
   ```python
   "Your Team Name": {"sum_tss": [Total TSS Sum], "rounds": [Total Knockout Rounds], "years": [Active Years]}
   ```
4. **Run the Script:** Open your computer's terminal or command prompt, navigate to the folder where you saved the file, and type:
   ```bash
   python ttss_engine.py
   ```
5. **View the Output:** The engine will instantly execute your three-tier logic and print a perfectly sorted leaderboard directly onto your screen from most successful (lowest score) to least successful (highest score).
