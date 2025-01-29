# Multi-Agent Retail Property Analysis

## Description
This project demonstrates the use of multiple AI agents to analyze retail property investments and generate detailed, data-driven reports. The agents specialize in tasks like market research, property evaluation, financial analysis, and risk assessment, providing actionable insights for investors.

## Features
- **Retail Property Researcher Agent**: Performs in-depth market analysis, evaluates retail properties, and estimates ROI.
- **Investment Property Analyst Agent**: Summarizes property details into clear, actionable insights.
- **Dynamic Task Execution**: Agents collaborate on predefined tasks like financial evaluation and risk analysis.
- **Customizable Tools**: Integrates tools like `SerperDevTool` for real-time data retrieval.
- **Comprehensive Reports**: Generates detailed, professional-grade investment analysis reports.

## Technologies Used
- **UPDATE: DeepSeek-R1-distill-llama-70b**: Uses State of the Art LLM via Groq API
- **CrewAI**: Framework for agent orchestration and task management.
- **LangChain**: For integrating language models and tools.
- **Python**: Primary programming language.
- **SerperDevTool**: Provides search and data aggregation capabilities.

## Installation
1. **Clone the Repository**  
     ```
     git clone https://github.com/your-username/Real-Estate-AI-Agents.git`  
     cd Real-Estate-AI-Agents
     ```
2. **Create and Activate a Virtual Environment**  
   - On Windows:  
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:  
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Install Dependencies**  
     ```
     pip install -r requirements.txt
     ```

4. **Set Up Environment Variables**  
   - Create a `.env` file in the root directory and add the required API keys. Example:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     GROQ_API_KEY=your_groq_api_key_here
     SERPER_API_KEY=your_api_key_here
     ```

## Usage
1. **Configure Agents and Tasks**  
   - Modify the agents and tasks in `agents.py` and `tasks.py` to reflect specific requirements.

     ![alt text](https://github.com/sahilbishnoi26/Real-Estate-AI-Agents/blob/main/pic1.png) 

2. **Run the Project**  
   ```
   python main.py
   ```

3. **Interact with the Agents**  
   - The agents will execute assigned tasks, and outputs will be saved to:
     ```
     research_task_output_internet.txt
     analysis_task_output.txt
     ```
     
     [a link](https://github.com/sahilbishnoi26/Real-Estate-AI-Agents/blob/main/research_task_output_internet.txt)

     [a link](https://github.com/sahilbishnoi26/Real-Estate-AI-Agents/blob/main/analysis_task_output.txt)
     

## Troubleshooting
- **Issue**: Missing Dependencies  
  - **Solution**: Ensure all dependencies are installed using `pip install -r requirements.txt`.
- **Issue**: Tool Integration Error  
  - **Solution**: Verify API keys in the `.env` file are correctly configured.
- **Issue**: Script Execution Failure  
  - **Solution**: Confirm the virtual environment is activated, and all required libraries are installed.
- **Issue**: Missing Output Files  
  - **Solution**: Check task configurations and ensure proper file paths are specified.

Enjoy using this multi-agent system for retail property analysis!
