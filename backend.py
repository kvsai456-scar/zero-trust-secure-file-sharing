import os
import uuid
import time
from flask import Flask, request, jsonify, send_from_directory, abort
from werkzeug.utils import secure_filename

# ---------------- CONFIG ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_DIR = os.path.join(BASE_DIR, "..", "client")
STORAGE_DIR = os.path.join(BASE_DIR, "storage")
LOG_FILE = os.path.join(BASE_DIR, "audit.log")

MAX_DOWNLOADS = 2
LINK_EXPIRY_SECONDS = 600  # 10 minutes

os.makedirs(STORAGE_DIR, exist_ok=True)

# ---------------- APP ----------------
app = Flask(__name__)

# In-memory file registry (demo purpose)
files = {}

# ---------------- LOGGING ----------------
def log_event(event, details):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts} | {event} | {details}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)
    print(line.strip())

# ---------------- CLIENT SERVING ----------------
@app.route("/")
def home():
    return send_from_directory(CLIENT_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(CLIENT_DIR, path)

# ---------------- API ----------------
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"status": "error", "msg": "No file"}), 400

    encrypted_file = request.files["file"]
    receiver = request.form.get("receiver", "unknown")

    file_id = str(uuid.uuid4())
    filename = secure_filename(encrypted_file.filename)
    save_path = os.path.join(STORAGE_DIR, file_id + "_" + filename)

    encrypted_file.save(save_path)

    files[file_id] = {
        "path": save_path,
        "receiver": receiver,
        "downloads": 0,
        "created": time.time()
    }

    log_event("UPLOAD", f"{file_id} | Receiver={receiver}")

    return jsonify({
        "status": "ok",
        "download_link": f"/download/{file_id}"
    })

@app.route("/download/<file_id>", methods=["GET"])
def download(file_id):
    if file_id not in files:
        log_event("INVALID_LINK", file_id)
        abort(404)

    record = files[file_id]

    # Expiry check
    if time.time() - record["created"] > LINK_EXPIRY_SECONDS:
        log_event("EXPIRED_LINK", file_id)
        abort(403)

    # Download limit check
    if record["downloads"] >= MAX_DOWNLOADS:
        log_event("DOWNLOAD_LIMIT_REACHED", file_id)
        abort(403)

    record["downloads"] += 1
    log_event("DOWNLOAD", f"{file_id} | Count={record['downloads']}")

    directory = os.path.dirname(record["path"])
    filename = os.path.basename(record["path"])

    return send_from_directory(directory, filename, as_attachment=True)

@app.route("/logs", methods=["GET"])
def logs():
    if not os.path.exists(LOG_FILE):
        return "No logs yet."
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read(), 200, {"Content-Type": "text/plain"}

# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("=== Zero Trust Secure File Sharing Backend ===")
    print("Storage:", STORAGE_DIR)
    print("Logs:", LOG_FILE)
    app.run(host="127.0.0.1", port=5000, debug=True)
