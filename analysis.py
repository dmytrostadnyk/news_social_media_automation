# Analysis of the events received from the news feed or market changes performed by the LLM.
import os
from pydantic import BaseModel
from anthropic import Anthropic
from dotenv import load_dotenv

#Pydantic model for the output of the analysis
class EventAnalysis(BaseModel):
    headline: str
    description: str
    macro_impact: str
    individual_impact: str

event = """
TradingKey - SpaceX (NASDAQ: SPCX) closed Day One at $161.11, a 19% increase from its $135 IPO price, following an intraday trade that saw prices swing as high as $176.52 and as low as $150. The result was exactly what was expected from an IPO that was oversubscribed by a factor of 2x and had a tight 4% float. Day One saw significant volume. Nasdaq President Adena Friedman and SpaceX President Gwynne Shotwell rang the opening bell at the Nasdaq MarketSite, surrounded by a large number of people. 

Perpetual futures linked to SpaceX on crypto platforms also saw a price peak of $176, approximately 30% above the IPO price, before moving to around $172. The IPO sent Elon Musk’s total valuation for his companies including SpaceX, Tesla and xAI over $450 billion and once again made him the world’s richest person by a large margin.

So, here is what investors in SPCX need to know as stocks go into their first full week.

Day One in Context — Where $161 Sits in the Pre-IPO Price Scenarios

Close is in the bullish half of Week One’s scenario range that analysts anticipated. This was a case with a range of $140 to $175 as the base and a pop over $180 if retail participation was high. In practice, SPCX intraday highs reached $176.52 before the company came in close at $161.11. This is a typical move for a mega-IPO with a tight float. The float represents an early surge in trading due to the lack of availability of the 4% of shares offered while there are huge buy interests. It also includes an intraday sell off due to early receivers of shares selling off to take their immediate profit. The fact that the closing price held near 20% higher than the IPO price instead of returning back all the way to $135 signals there is significant buy support for the stock and is not just speculation.
On that front, it is worth pointing out that the space-floated perpetual futures on platforms like Hyperliquid had been pricing a similar move for several days. Contracts traded at $176 on Thursday, up nearly 30% from the $135 IPO price, before trading at around $172 ahead of the actual listing. What’s interesting here is that the pricing of crypto perpetuals on Hyperliquid before the listing tracked quite closely with SPCX’s final Day One Nasdaq close price. That is to say, the markets had a reasonably good idea of how much buying demand there would be on Day One before the bell. This suggests that the IPO was already accurately priced, both in traditional and alternative markets.

What Happens Next — MSCI Inclusion Tomorrow and the Float Mechanics That Follow

And finally, there’s tomorrow. The biggest thing to watch on the near-term SPCX front is that MSCI is putting in place an early inclusion methodology. Come tomorrow, June 13 (or T+1), SpaceX with its valuation of over $1.75 trillion (it may be even higher now since the first-day gain brought the price up close to 19% to near a $2 trillion market capitalization) will be one of the top 10 constituents in the MSCI World Index and MSCI ACWI (All Country World Index). All the mutual funds and ETFs that track these indices will have to buy SPCX stock to match the index’s weighting. 

Given there are probably $15 to $20 trillion AUM (Assets Under Management) across all the funds that need to buy SPCX and there is only $70 to $80 billion in float for SPCX at the post-pop prices, this means the mechanical buy orders from funds matching those indices are going to account for a fairly significant share of available supplies in the next couple of days. This will likely support stock prices, at least in the short term, no matter what kind of news comes out on Starship or Starlink.

On that front, there is another mechanical factor to be aware of: the insider stock lockup that comes into effect for 180 days after the IPO. Over the next six months, the only SPCX stock available for sale or purchase is the original 4% float that IPO participants got. Insiders, employees, and investors that acquired shares before the IPO will all have to wait until the lockup expires in December. 

This means SPCX volume and price action reflects what happens with a fairly limited number of tradable shares. It also means continued selling activity from early receivers of shares (such activity was probably behind the intraday pullback from $176.52 highs to $161.11 lows) could continue until the lockup expires. Looking ahead, lockup periods for a major IPO like SPCX are often accompanied by volatility due to increased availability of shares for sale. SPCX investors should mark that date on their calendar now.

What Counts Once the IPO Glitz Is Over

Once the immediate trading volatility settles, the metrics that ultimately define SPCX stock performance will be those that the S-1 already flagged. Starlink is the business. Revenue of $11.387 billion in 2025 and $4.423 billion in operating profit, an adjusted EBITDA margin of 63%, growing subscriber base from 4.5m to a little over 10.3m in a year across 164 countries. A subscription growth rate that extends into Q2 2026 is arguably the one best argument for the bulls, regardless of Starship or xAI performance. A $6.355 billion operating loss in xAI, 76% of total group capex in Q1 2026 in AI capex, is arguably one major driver for the bears. Watch any discussion on xAI capex plans in any interview, conference, or disclosure between now and the first public earnings in November 2026.

The cadence of Starship flights is third. The S-1, as well as recent Starship flights, show the business has made material progress in full reusability, and earlier this year SpaceX announced it was aiming for uncrewed lunar launches under the Artemis program in late 2026. Every test flight, or failure to launch, that occurs before the next earnings report will be disproportionately priced relative to revenue impact, as Starship is the vehicle that moves SpaceX from its current profitable but capital-intensive operating profile to the much bigger, longer-duration TAMs, including point-to-point flight, massive-scale orbital infrastructure, and the orbital data center, that give it a $1.75T-plus valuation.

Space Sector Impact: Rocket Lab, Intuitive Machines, And The Rotation

Space stocks immediately experienced a rotation after the SpaceX IPO, with stock declines largely a function of how much of a given company’s equity value is attributed to being a SpaceX proxy. Rocket Lab, the most liquid and fundamentally strongest of the smaller space names, fell just 7.7%. Intuitive Machines and Redwire declined around 14-15%, while Virgin Galactic, the most speculative of the group, fell 24%. 

EchoStar (thought to have an ~3% interest in SpaceX) surged 11% as market pricing on its interest rose. AST SpaceMobile (competitor to Starlink’s Direct to Cell) rose after high options volume as market traders began to rotate back into general satellite-based connectivity plays now that SpaceX stock has been publicly traded. 

The rotation probably needs to play out over another session or two as portfolio managers move into and out of space stocks as they reevaluate positions, but the trade is a capital flows trade, not a re-rating of business value. In Rocket Lab's case, there's an offsetting mechanical buying catalyst in its Nasdaq-100 inclusion on June 22. It's another reminder that index mechanics have been flowing in both directions across the sector this month.

How Did SpaceX Stock (SPCX) Perform on Day One?

SpaceX closed its first Nasdaq trading day on June 12, 2026, at $161.11. It was a 19% gain over the $135 IPO price and the day saw an intraday high of $176.52, about 31% above the IPO, before backing off to finish at $161.11. It was extremely heavy volume. Crypto-perpetual SPCX futures trades on crypto exchanges ranged from $172 to $176 pre-IPO, in line with what we see. The $161.11 valuation implies a roughly $2 trillion market cap, up from $1.75 trillion post-IPO valuation.

What Is the Next Big Event for SPCX?

MSCI's early-inclusion methodology for SPCX kicked in on June 13, 2026. It was a day after listing. At its post-debut valuation, SpaceX is one of the 10 largest constituents of the MSCI World and MSCI ACWI indices. It is estimated that $15 to $20 trillion of passive funds have to buy SPCX to adjust to the new index weights. This means we get structural, price-insensitive buy pressure with a very tight 4% float of SPCX shares out there. The 180-day insider lockup, which ends in December 2026, is the next big event.

What Should SPCX Investors Be Watching for Going Forward?

Three items.

Starlink subscriber and revenue in Q2 2026, after reporting 10.3 million subscribers and 63% EBITDA margin in the S-1.
The capex trajectory for xAI. This group was 76% of group capex in Q1 2026 and the largest source of consolidated net losses in the S-1.
Starship test flight cadence. This includes progress toward uncrewed lunar missions under NASA's Artemis programme later this year.
SpaceX is expected to release its first publicly audited earnings statement in November 2026. This will be the first time we get the above items in one place and can look at those against the day-one valuation of SPCX.

The Bottom Line

SpaceX closed its debut session up 19% at $161.11. It was up 19% with an intraday high of $176.52. That put the stock in the bullish 50% of IPO price scenarios. It pushed the valuation for Elon Musk over $450 billion. The next catalyst is the MSCI inclusion tomorrow, June 13. There is structural buying of a stock with only 4% of the shares available. 

The lockup ending in December 2026 is the next big event on supply. Starlink subscriber growth, xAI's capex, and Starship test cadence are the items to watch for in determining where the SPCX stock will be in the earnings season in November 2026. The sector rotation is hitting Rocket Lab (RKLB), Intuitive Machines (LUNR), and Virgin Galactic (SPCE). 

The sector rotation, by definition, is a capital-flow phenomenon and should not be conflated with a change in business outlook or valuation.    
"""
system_prompt = """
You are a financial and economic news translator. Your only job is to take a raw news article or market data event and turn it into a clear, warm, conversational post that a smart but non-expert person aged 19–40 can immediately understand and care about.
Think of yourself as that knowledgeable friend who reads the financial news so others don't have to and who always answers the one question everyone actually wants answered: "okay, but how does this affect ME?"

YOUR AUDIENCE
Smart, curious people who are not economists. They follow the news, they care about the world, they want to understand what's happening — but they don't know what "yield curve inversion" means off the top of their head, and they shouldn't need to. Your primary geographic frame of reference is the US, EU, and Eastern Europe. Write with that in mind unless the event is clearly isolated to another region entirely.

YOUR OUTPUT STRUCTURE
You will always produce exactly 4 elements, in this order:
1. HEADLINE
A single punchy, plain-language headline. No jargon. No clickbait. Just the clearest possible one-liner that tells the reader what happened and why it matters. Do not use a colon to split it into two halves. Write it as one natural sentence or phrase.
2. What actually happened?
Explain the event in plain, warm, conversational language. Do not dumb it down by removing details — instead, translate complexity into clarity. If a concept is technical, explain it briefly in plain terms before moving on. Do not use analogies or metaphors — explain directly.
CRITICAL RULE ON NUMBERS: If the source contains specific numbers, percentages, figures, dates, or statistics — reproduce them EXACTLY as written in the source. Do not round, paraphrase, or omit them. Numbers are facts. Treat them as sacred.
3. What is the impact on the world?
Explain the macro-level consequences of this event. What does it mean for economies, markets, trade, global supply chains, or international relations? Be specific. If the impact is uncertain or speculative, say so clearly — but still explain the realistic range of outcomes. Do not hedge everything into meaninglessness.
4. How is it going to impact YOUR life?
This is the most important section. Address the reader directly. Use "you" and "your." Open with: "So, how is [event name/short description] going to affect your life?"
Then explain clearly and specifically:
— What a person might notice in their daily life (prices, jobs, savings, loans, travel, cost of goods)
— What timeline to expect (immediate, weeks, months, years)
— What, if anything, they can or should think about doing
If the impact is not immediate, say so honestly — but always follow it with the realistic long-term picture. Never leave the reader with nothing. Even "no immediate impact" must be followed by what to watch for and when.

WRITING STYLE GUARDRAILS
Write like a human journalist, not like an AI assistant. Specifically:
- Never use em dashes (—). Replace them with a comma, a colon, or restructure the sentence entirely.
- Never use the words: notable, delve, navigate, landscape, it's worth noting, moreover.
- Vary your sentence length. Mix short punchy sentences with longer ones. Monotone sentence rhythm is a dead giveaway.
- Do not restate what you just said at the start of a new section.
- Write with forward momentum. Every sentence should add new information, not repackage the previous one.

TONE RULES
- Warm, direct, conversational. Like a smart friend explaining over coffee — not a news anchor, not a professor.
- Never cold or clinical. Never use passive bureaucratic phrasing.
- Confident but honest. If something is uncertain, say it confidently: "We don't know yet, but the most likely outcome is..."
- You may NEVER invent facts, figures, or data. If you don't know something, reason clearly from what you do know. State your reasoning.
- Never use jargon without immediately explaining it in plain language in the same sentence.

FORMAT & LENGTH RULES
- The total output across all 4 elements (headline + 3 sections) must not exceed 2200 characters.
- Write in flowing prose within each section. No bullet points. No numbered lists.
- The headline has no label — it sits at the top, alone.
- No sign-off, no hashtags, no calls to action, no disclaimer.

EDGE CASES
- If the event has no immediate personal impact: Say so clearly, then explain the long-term picture and what signal to watch for.
- If the event is region-specific and irrelevant to US/EU/Eastern Europe: Still write the personal impact section, but note the geographic distance and explain any indirect effects.
"""

#LLM analysis of the event using Anthropic's API
load_dotenv()
def analyze_event(event: str) -> EventAnalysis:
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.parse(
        model="claude-sonnet-4-6",
        max_tokens=2500,
        system=system_prompt,
        output_format=EventAnalysis,
        messages=[
            {"role": "user", "content": f"analyze the following event: {event}"}
        ],
    )    
    return response.parsed_output