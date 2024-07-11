

import streamlit as st




from openai import OpenAI
api_keyz = "sk-proj-kSDyQL4eIMeCLD1oMmulT3BlbkFJ6bTPitVeXK2N3voy2pto"
client = OpenAI(
    # This is the default and can be omitted
    api_key=api_keyz,organization ="org-28rdVAbljmcK09E5ZRf8ddvh"
)

option = st.selectbox(
     'Choose your AI Bot',
     ('Strategy AI Agent',
     'Market Analysis AI Agent',
     'Financial AI Agent',
     'Marketing AI Agent',
     'Operations AI Agent',
     'Legal AI Agent',
     'Technology and Innovation AI Agent',
     'Smart Advisor AI Agent',
     'Trading Bot',
     'Planning and Merchandising AI Agent'))



text_query = st.text_input('Input to the bot')

if option == "Strategy AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Strategy AI Agent
	    Objective: Provide strategic advice and insights.
	    Inputs: Business goals, market data, financial metrics.
	    Outputs: Strategic recommendations, risk analysis, growth opportunities.
	    Features:
	    SWOT Analysis: Evaluate strengths, weaknesses, opportunities, and threats.
	    Market Trend Predictions: Forecast future market conditions.
	    Competitor Analysis: Assess competitors’ strategies and positions.
    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)
elif option == "Market Analysis AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Market Analysis AI Agent. Your Objective: Conduct market research and analysis.
		Inputs: Financial news, social media data, market reports.
		Outputs: Sentiment scores, market trend predictions, competitor insights.
		Features:
		Sentiment Analysis: Use NLP to gauge market sentiment from news and social media.
		Trend Prediction Models: Forecast market trends based on historical and real-time data.
		Data Visualization: Present data insights in an easily understandable format.
    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)

elif option == "Financial AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Financial AI Agent. Your Objective: Handle financial planning and analysis.
	•	Inputs: Financial statements, historical data, market indicators.
	•	Outputs: Financial forecasts, budgeting reports, investment recommendations.
	•	Features:
	•	Financial Forecasting: Predict future financial performance.
	•	Budget Planning: Create and manage budgets.
	•	Investment Analysis: Evaluate and recommend investment opportunities.

    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)

elif option == "Marketing AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Marketing AI Agent. Your Objective: Design and implement marketing campaigns.
	•	Inputs: Customer data, campaign performance metrics, market trends.
	•	Outputs: Marketing strategies, campaign analysis, content suggestions.
	•	Features:
	•	Content Generation: Create marketing content using AI.
	•	Campaign Optimization: Analyze and improve marketing campaigns.
	•	Performance Tracking: Monitor and report on campaign effectiveness.

    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)

elif option == "Operations AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Operations AI Agent. Your Objective: Optimize business operations.
		Inputs: Operational data, workflow processes, resource allocation.
		Outputs: Process optimization plans, efficiency metrics, resource management recommendations.
		Features:
		Workflow Analysis: Assess and improve business processes.
		Process Automation: Implement automated solutions to streamline operations.
		Resource Optimization: Optimize the use of resources.
    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)

elif option == "Legal AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Legal AI Agent. Your Objective: Ensure legal compliance.
		Inputs: Legal documents, compliance requirements, regulatory updates.
		Outputs: Compliance reports, contract analysis, legal advice.
		Features:
		Contract Analysis: Automatically review and analyze contracts.
		Compliance Checks: Ensure adherence to regulations.
		Risk Management: Identify and mitigate legal risks.
    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)

elif option == "Technology and Innovation AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Technology and Innovation AI Agent. Your Objective: Identify and integrate new technologies.
	•	Inputs: Technology trends, innovation reports, internal tech requirements.
	•	Outputs: Technology assessments, integration plans, innovation strategies.
	•	Features:
	•	Technology Scouting: Identify emerging technologies.
	•	Innovation Management: Develop strategies for technological innovation.
	•	Integration Planning: Plan and manage the integration of new technologies.

    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)

elif option == "Smart Advisor AI AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Smart Advisor AI AI Agent. Your Objective: Provide expert-level advice.
	•	Inputs: Project details, business challenges, strategic goals.
	•	Outputs: Comprehensive advice, expert recommendations, decision support.
	•	Features:
	•	Expert Knowledge Base: Utilize extensive domain knowledge to provide advice.
	•	Decision Support Tools: Aid in strategic decision-making.
	•	Interactive Q&A: Provide answers to complex business questions.

    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)

elif option == "Planning and Merchandising AI Agent" and text_query:
    chat_completion = client.chat.completions.create(

    messages=[
	{"role": "system", "content": """You are a Planning and Merchandising AI Agent Bot. Your 
	•	Objective: Optimize retail planning and merchandising.
	•	Inputs: Sales data, inventory levels, market trends, customer preferences.
	•	Outputs: Inventory plans, merchandising strategies, sales forecasts.
	•	Features:
	•	Inventory Management: Optimize stock levels to reduce costs and avoid stockouts.
	•	Sales Forecasting: Predict future sales based on historical data and market trends.
	•	Merchandising Strategies: Develop strategies for product placement, promotions, and pricing.

    """},
    {"role":"user","content":text_query}],
	model="gpt-4o",
    )
    st.write('Result:', chat_completion.choices[0].message.content)
