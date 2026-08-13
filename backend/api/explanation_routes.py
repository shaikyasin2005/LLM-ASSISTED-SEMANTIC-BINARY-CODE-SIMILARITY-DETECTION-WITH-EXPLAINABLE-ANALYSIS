from fastapi import APIRouter
from core.openai_explainer import explain_with_ai

explanation_router = APIRouter()

@explanation_router.post("/ai")
def ai_explain(code1: str, code2: str):
    return {"ai_explanation": explain_with_ai(code1, code2)}