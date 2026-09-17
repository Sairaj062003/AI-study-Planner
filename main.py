from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class StudyItem(BaseModel):
    subject: str = Field(description="The subject to study")
    hours: float = Field(description="Number of hours to study")
    priority: str = Field(description="Priority of the subject")

load_dotenv()



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

structured_model = model.with_structured_output(StudyItem)

prompt= ChatPromptTemplate.from_template(    """
    Create a study plan for {subject}.
    The student has {hours} hours available.
    Their level is {level}.

    Return one study item.
    """
)

messages = prompt.invoke({"subject": "langchain", "hours": 2.0, "level": "beginner"})

response = structured_model.invoke(messages)

print(response)