from dotenv import load_dotenv
from langgraph.prebuilt.tool_executor import ToolExecutor
from react import react_agent_runnable, tools
from state import AgentState


load_dotenv()


def run_agent_reasoning_engine(state: AgentState):
    """Call the ReAct agent runnable and invoke the state
    :param state: AgentState object
    :return: Dict agent_outcome
    """
    agent_outcome = react_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}


tool_executor = ToolExecutor(tools)


def execute_tools(state: AgentState):
    """Execute the tools. Assume state always has agent_outcome field
    :param state: AgentState object
    :return:  Dict having key intermediate_steps with value having tuple of agent_action and output cast as str
    """
    agent_action = state["agent_outcome"]
    output = tool_executor.invoke(agent_action)
    return {"intermediate_steps": [(agent_action, str(output))]}
