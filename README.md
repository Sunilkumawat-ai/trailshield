# 🌿 TrailShield

**Your trail. Your data. Your device.**
A short-interaction outdoor safety buddy powered by Gemma, an open-weight model. Check something on the trail, get cautious guidance, put the phone away.

Built for the DEV Hacktoberfest 2026 Open-Source AI Challenge, Week 1 (theme: Touch Grass).

**Live app:** https://sunilkumawat-ai.github.io/trailshield/

## What it does
1. Tap **Start Trail**. An optional check-in reminder timer starts.
2. Tap **Check something** and take or pick a photo (a rocky path, a fallen branch, a muddy patch).
3. Gemma gives a short, cautious note (under 60 words), then tells you to put your phone away.
4. **Privacy Proof** shows real counters from the app. **Delete Trail Data** wipes local data.

TrailShield never says a place is "safe" or "dangerous". It uses words like "possible" and "appears".

## Architecture
```
Phone browser (GitHub Pages: index.html)
  -> resizes photo, strips GPS/metadata (canvas redraw)
  -> Render web service (server/app.py, Flask)
  -> Google's hosted Gemma model (gemma-4-26b-a4b-it)
  -> short advice back to the phone
```
The API key lives only in a Render environment variable, never in the page or this repo.

## Privacy: the honest version
| Question | Answer |
|---|---|
| Does the AI run on the device? | **No.** It runs in the cloud. |
| What leaves the phone? | One resized photo (no GPS), only when you tap Check. |
| Is location collected? | No. The app never asks for it. |
| Account needed? | No. |
| What is stored locally? | Session times and counters in browser localStorage. |
| Does our server save photos? | Our code does not store them. Render and Google may keep request logs under their own policies. |
| Does Delete remove cloud copies? | No. It only clears data on your device. |
| Internet required? | Yes, for photo checks. |

Why open-weight matters: Gemma can be self-hosted, so anyone who wants zero cloud upload can run the same server code against their own copy of the model.

## Limitations
- Not offline. Fully on-device AI was out of scope for this build.
- The check-in is a reminder that only works while the page is open. It is **not** an emergency alert.
- The free Render server sleeps, so the first check can take up to about a minute.
- The AI can be wrong. Use your judgment and local signs.

## Safety disclaimer
TrailShield is not a replacement for human judgment, trail signs, local authorities or emergency services. In an emergency, call your local emergency number (India: 112).

## Run it yourself
1. Fork this repo and enable GitHub Pages (main branch, root).
2. Deploy `server/` on Render (Python 3). Build: `pip install -r requirements.txt`. Start: `gunicorn app:app --timeout 120`.
3. Set `GEMINI_API_KEY` in Render's environment variables.
4. Put your Render URL in the `SERVER` constant in `index.html`, and your Pages URL in `CORS(...)` in `server/app.py`.

## Real-world test (Jodhpur)
_To be filled after the trip: what worked, what failed, what surprised me._

## License
MIT
