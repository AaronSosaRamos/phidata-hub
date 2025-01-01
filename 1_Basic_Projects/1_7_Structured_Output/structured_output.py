from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from phi.agent import Agent
from phi.model.openai import OpenAIChat

# Define a Pydantic model to enforce the structure of the software architecture output
class SoftwareArchitecture(BaseModel):
    system_name: str = Field(..., description="The name of the software system.")
    modules: List[str] = Field(..., description="List of key modules or components in the architecture.")
    interactions: Dict[str, str] = Field(..., description="Mapping of interactions between modules.")
    technology_stack: List[str] = Field(..., description="Technologies used in the system (e.g., languages, frameworks, databases).")
    design_patterns: List[str] = Field(..., description="Design patterns implemented in the architecture.")
    scalability_features: Optional[str] = Field(None, description="Features or strategies for scaling the system.")
    security_measures: Optional[str] = Field(None, description="Key security measures implemented in the architecture.")
    documentation_links: List[str] = Field(..., description="Links to architecture documentation or related resources.")

class SoftwareArchitectureStructuredOutput(BaseModel):
    system_name: str = Field(..., description="The name of the software system.")
    modules: List[str] = Field(..., description="List of key modules or components in the architecture.")
    interactions: List[str] = Field(..., description="Mapping of interactions between modules.")
    technology_stack: List[str] = Field(..., description="Technologies used in the system (e.g., languages, frameworks, databases).")
    design_patterns: List[str] = Field(..., description="Design patterns implemented in the architecture.")
    scalability_features: Optional[str] = Field(None, description="Features or strategies for scaling the system.")
    security_measures: Optional[str] = Field(None, description="Key security measures implemented in the architecture.")
    documentation_links: List[str] = Field(..., description="Links to architecture documentation or related resources.")

# Agent that uses JSON mode
json_mode_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="You generate detailed software architecture descriptions.",
    response_model=SoftwareArchitecture,
)

# Agent that uses structured outputs
structured_output_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="You create structured software architecture specifications.",
    response_model=SoftwareArchitectureStructuredOutput,
    structured_outputs=True,
)

# Example usage
print("JSON Mode:")
json_mode_agent.print_response("Design a scalable architecture for a cloud-based e-commerce platform.")
print("\nStructured Output Mode:")
structured_output_agent.print_response("Design a scalable architecture for a cloud-based e-commerce platform.")