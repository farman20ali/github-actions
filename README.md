# Python Email Sender with GitHub Actions

This repository demonstrates how to use GitHub Actions to run a simple Python script that sends an email using SMTP. It uses a template for the email body and environment variables for configuration.

## Features
- Simple Python script to send an email
- Email body loaded from a template file
- Uses `.env` for sensitive configuration (SMTP credentials, recipient)
- GitHub Actions workflow to run the script on push or manually

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Create your `.env` file**
   - Copy `.env.example` to `.env` and fill in your SMTP details and recipient:
     ```
     EMAIL_HOST=smtp.example.com
     EMAIL_PORT=587
     EMAIL_HOST_USER=your_email@example.com
     EMAIL_HOST_PASSWORD=your_password
     EMAIL_TO=recipient@example.com
     ```
4. **Edit the email template**
   - Modify `email_template.txt` as needed for your message.

## Running Locally

```sh
python send_email.py
```

## GitHub Actions Workflow

- The workflow is defined in `.github/workflows/send_email.yml`.
- It runs on push to `main` or can be triggered manually.
- **Secrets:** Set the following repository secrets in GitHub:
  - `EMAIL_HOST`
  - `EMAIL_PORT`
  - `EMAIL_HOST_USER`
  - `EMAIL_HOST_PASSWORD`
  - `EMAIL_TO`

## Files
- `send_email.py` — Main script
- `requirements.txt` — Python dependencies
- `email_template.txt` — Email body template
- `.env.example` — Example environment config
- `.github/workflows/send_email.yml` — GitHub Actions workflow

---

*For learning purposes only. Do not commit real credentials.*
