# AI Social Media Post Advisor

An experimental image-review assistant that explores whether a photo is suitable to share on a selected social platform, with attention to image quality and visible privacy risks.

## Project idea

Before posting a photo, a user may want to check its composition, lighting, relevance and whether it accidentally reveals personal information. This project explores an AI-assisted workflow for reviewing an image before publication.

## Intended workflow

1. Upload an image.
2. Select the intended social platform.
3. Analyse available image signals.
4. Return structured suggestions about image quality and potential privacy concerns.

The original project description mentions possible recommendations such as improving lighting or checking for sensitive information in the background. These are goals of the concept, not a guarantee that every type of analysis is implemented.

## Technology visible in the repository

- Python
- FastAPI
- OpenCV / Haar cascade assets
- Modular `analyzer/` package

## Repository structure

```text
AI-Social-media-post-advisor/
├── analyzer/
│   ├── face.py
│   ├── platform.py
│   └── quality.py
├── main.py
├── requirements.txt
└── haarcascade_frontalface_default.xml
```

## Run locally

```bash
git clone https://github.com/Sakshaminsidetheinternet/AI-Social-media-post-advisor.git
cd AI-Social-media-post-advisor
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

If the application entry point differs in your local version, check `main.py` for the FastAPI instance name and use it in the Uvicorn command.

## Demo and screenshots

No verified public deployment URL or screenshots are currently included. Run locally and capture the upload and result screens before adding screenshots to this README.

## Current scope and limitations

The repository currently looks like an early-stage prototype. Some analyzer modules are empty or incomplete in the inspected tree, so do not assume the full image-analysis workflow is implemented. Image analysis can miss private information; users should manually inspect photos before posting. Avoid uploading sensitive images to services unless their privacy terms are understood.

## Author

**Saksham Gupta** — [GitHub](https://github.com/Sakshaminsidetheinternet)
