import os
import uuid
import subprocess

from fastapi import APIRouter, UploadFile, File

from core.preprocessing import preprocess_code
from core.tfidf_engine import tfidf_similarity
from core.structural_features import structural_similarity
from core.hybrid_similarity import hybrid_similarity
from core.sha256_match import check_exact_match
from core.retdec_integration import disassemble_file


similarity_router = APIRouter()


UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_file(upload_file: UploadFile):

    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, file_id + "_" + upload_file.filename)

    with open(file_path, "wb") as f:
        f.write(upload_file.file.read())

    return file_path


def compile_if_c(file_path):

    if file_path.endswith(".c"):

        exe_path = file_path.replace(".c", ".exe")

        subprocess.run(
            ["gcc", file_path, "-o", exe_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        return exe_path

    return file_path


@similarity_router.post("/similarity/compare-files")
async def compare_files(file1: UploadFile = File(...), file2: UploadFile = File(...)):

    try:

        path1 = save_file(file1)
        path2 = save_file(file2)

        exact_match = check_exact_match(path1, path2)

        # compile if needed
        bin1 = compile_if_c(path1)
        bin2 = compile_if_c(path2)

        # decompile binaries
        code1 = disassemble_file(bin1)
        code2 = disassemble_file(bin2)

        code1 = preprocess_code(code1)
        code2 = preprocess_code(code2)

        tfidf_score = tfidf_similarity(code1, code2)
        structural_score = structural_similarity(code1, code2)
        hybrid_score = hybrid_similarity(tfidf_score, structural_score)

        if hybrid_score > 0.9:
            explanation =(
            "The binaries are extremely similar. "
            "The control flow and instruction patterns indicate that both programs "
            "implement nearly identical computational logic."
            )
        elif hybrid_score > 0.7:
            explanation =(
            "The binaries show strong similarity. "
            "Although implementation details differ slightly, both programs perform "
            "very similar operations and likely implement the same algorithm."
            )
        elif hybrid_score > 0.5:
            explanation =( 
            "The binaries share moderate similarity. "
            "Some structural patterns and instructions overlap, but the programs "
            "may use different techniques to achieve their functionality."
            )
        elif hybrid_score > 0.3:
            explanation =(
            "The binaries show limited similarity. "
            "Only a small portion of the structure or instruction patterns match."
            )
        else:
            explanation =( 
            "The binaries appear to be significantly different and likely implement "
            "unrelated functionality."
            )
        return {
            "tfidf_score": round(tfidf_score, 3),
            "structural_score": round(structural_score, 3),
            "hybrid_score": round(hybrid_score, 3),
            "exact_match": exact_match,
            "explanation": explanation
        }

    except Exception as e:

        return {
            "error": str(e),
            "tfidf_score": 0,
            "structural_score": 0,
            "hybrid_score": 0,
            "exact_match": False,
            "explanation": "An error occurred during similarity computation."
        }