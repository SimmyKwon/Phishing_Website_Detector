# 1. Base image with Python 3.11 (Optimized version matching python_requires)
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Install system dependencies and build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy all source codes and configuration files into the container (/app)
# (This ensures Model_params, model_config.json, and Website_detector are included completely)
COPY . /app

# 5. Install all project dependency packages at once using setup.py
RUN pip install --no-cache-dir -e .

# 6. Install Playwright Linux browser environment and binaries
# The --with-deps option prevents browser execution failures inside the Linux container.
RUN playwright install --with-deps chromium

# 7. Expose port 8080 used by FastAPI for external access
EXPOSE 8080

# 8. Run uvicorn pointing to the script inside the subdirectory (Website_detector) to avoid ModuleNotFoundError
# Host is set to 0.0.0.0 to route the internal web server to the external host machine.
CMD ["uvicorn", "Website_detector.UI_Window:app", "--host", "0.0.0.0", "--port", "8080"]