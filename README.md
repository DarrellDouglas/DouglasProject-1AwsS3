## Project Description
This project shows how to build a secure static website using **Amazon Web Services (AWS) S3**. It includes:
- A **Python script** for connecting and managing the S3 bucket.
- A **bucket policy** to control access securely.
- A **static HTML webpage** for demonstration.

This method is great for **remote tech companies** and **military tech organizations** that need strong security while hosting lightweight, high-performing websites.

---

## Why This Project is Valuable
1. **Security First**: The website uses AWS S3's bucket policies to protect files and control access. This is important for organizations that need strict security, like military and remote tech companies.
2. **Cost-Effective**: AWS S3 is a low-cost way to host websites without worrying about servers.
3. **Easy Scaling**: AWS S3 automatically adjusts to handle more visitors if needed.
4. **Compliance Ready**: Ideal for sensitive projects requiring regulatory compliance.

---

## Files Included
1. **`index.html`**: The HTML file for the static website. It showcases a clean and professional design with project-related images.
2. **`Bucket_Policy.JSON`**: The JSON file for configuring the S3 bucket's access policy.
3. **`connect_list.py`**: A Python script that connects to the S3 bucket and automates tasks like uploading files.

---

## How to Use This Project
### Step 1: Set Up Your AWS S3 Bucket
1. Log in to AWS Management Console.
2. Create a new S3 bucket and name it (e.g., `douglasawsproject1bucket`).
3. Upload the `index.html` file and project-related images.

### Step 2: Apply the Bucket Policy
1. Copy the content of the `Bucket_Policy.JSON` file.
2. Go to the **Permissions** tab of your bucket.
3. Add the policy under **Bucket Policy**.

### Step 3: Run the Python Script
1. Open the `connect_list.py` script.
2. Use Python to upload files or automate bucket management:
   ```bash
   python connect_list.py
