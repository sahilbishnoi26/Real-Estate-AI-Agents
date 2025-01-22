from crewai import Task  # Import the Task class to define specific tasks
from agents import property_researcher, property_analyst  # Import the agents for task assignment

# Define the research task for the property_researcher agent
research_task = Task(
    description="""Conduct a comprehensive analysis of potential retail property investments in Atlanta.

    Specific research requirements:
    1. Market Analysis:
       - Identify top 3-5 potential retail property investment locations
       - Analyze current market trends and economic indicators
       - Assess demographic data and consumer spending patterns
       - Evaluate local retail ecosystem and potential tenant mix

    2. Property Evaluation Criteria:
       - Foot traffic analysis
       - Accessibility and transportation infrastructure
       - Proximity to complementary businesses
       - Local economic development plans

    3. Financial Analysis:
       - Estimate potential rental yields
       - Calculate projected ROI
       - Assess property valuation and appreciation potential
       - Identify potential renovation or repositioning opportunities

    4. Risk Assessment:
       - Analyze competitor landscape
       - Evaluate e-commerce impact on local retail
       - Assess potential regulatory or zoning challenges
       - Identify potential long-term growth barriers

    5. Detailed Reporting:
       Provide a comprehensive report with:
         - Executive summary
         - Detailed market insights
         - Property recommendations
         - Financial projections
         - Risk analysis
         - Visual aids (charts, graphs)

    Deliverable: A comprehensive, data-driven investment recommendation report.""",  # Comprehensive task description
    agent=property_researcher,  # Assign the property_researcher agent to this task
    expected_output="""Detailed report containing:
    - Market analysis summary
    - Top 3-5 recommended retail property investments
    - Comprehensive financial projections
    - Risk assessment
    - Recommendations for further due diligence""",  # Expected output details
    output_file="research_task_output_internet.txt"  # File to save the task's output
)

# Define the analysis task for the property_analyst agent
analysis_task = Task(
    description="Summarise the property information into bullet point list.",  # Task to summarize property information
    expected_output="A summarised dot point list of each of the suburbs, prices and important features of that suburb.",  # Expected concise output
    agent=property_analyst,  # Assign the property_analyst agent to this task
    output_file="analysis_task_output.txt",  # File to save the task's output
)
