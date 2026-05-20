from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class LineLengthInput(BaseModel):
    """Input schema for LineLengthChecker."""
    code: str = Field(..., description="The code string to analyze line by line.")

class LineLengthChecker(BaseTool):
    name: str = "LineLengthChecker"
    description: str = "Scans code line by line and returns the count and line numbers of lines exceeding 80 characters."
    args_schema: Type[BaseModel] = LineLengthInput

    def _run(self, code: str) -> str:
        lines = code.splitlines()
        long_lines = []
        
        for idx, line in enumerate(lines, start=1):
            if len(line) > 80:
                long_lines.append(f"Line {idx} ({len(line)} chars): '{line[:30]}...'")
        
        if not long_lines:
            return "Style Check Passed: No lines exceed 80 characters."
            
        return f"Found {len(long_lines)} lines exceeding 80 characters:\n" + "\n".join(long_lines)