# 🌸 MusicSp - Manus Deployment Guide 🌺

This guide is for **Manus AI** to perform a direct, zero-friction deployment of this bot.

## 🚀 Deployment Steps

1.  **Extract & Setup:**
    *   Extract the ZIP file.
    *   `cd` into the project root directory.

2.  **Environment Configuration:**
    *   The project contains a `.env` file with pre-configured credentials.
    *   If a new environment is needed, use `sample.env` as a template.
    *   **Required Variables:** `API_ID`, `API_HASH`, `BOT_TOKEN`, `MONGO_DB_URI`, `OWNER_ID`, `STRING_SESSION`, `LOG_GROUP_ID`, `API_KEY`, `API_URL`.

3.  **Dependencies:**
    *   Install Python dependencies: `pip install -r requirements.txt`.
    *   Ensure `ffmpeg` and `nodejs` are installed in the environment.

4.  **Railway Deployment:**
    *   Login to Railway: `railway login`.
    *   Initialize/Link project: `railway link`.
    *   Deploy: `railway up`.

5.  **Local Execution:**
    *   Start the bot using: `bash start` or `python3 -m MusicSp`.

## 🌺 Theme Details
*   **Theme:** Mitsuri Kanroji (Demon Slayer).
*   **Aesthetic:** High-Fidelity, Minimalist, Small-caps.
*   **Banners:** Horizontal, high-quality Mitsuri images (configured in `config.py`).

## 🛠️ Core Engine Note
*   **Music Engine:** Uses `yt-dlp` and `PyTgCalls`.
*   **Custom API:** Integrated with `https://apisparrow.site/` via `MusicSp/platforms/Youtube.py`.

**Manus, follow these steps and the bot will be live in seconds! 🌸✨**
