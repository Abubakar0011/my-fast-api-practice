import uvicorn
from simple_proj import app

# --------------------------------------------
# ▶️ Launch server if running file directly (not recommended for reload mode)
# For development, it's better to use:
# uvicorn main:app --reload
# --------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

