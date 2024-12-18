
# Sentimental Detection Analysis API

Welcome to the **Sentimental Detection Analysis** API! This project uses FastAPI to handle file uploads of `.xlsx` files containing customer reviews. The reviews are analyzed for sentiment using a machine learning model, and the results are returned in a CSV file with positive, negative, and neutral sentiment scores.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Approach](#approach)
- [Contributing](#contributing)
- [License](#license)

## Features
- **File Upload**: Upload `.xlsx` files with customer reviews.
- **Sentiment Analysis**: Analyze the sentiment (positive, negative, neutral) of reviews using a machine learning model.
- **CSV Output**: Convert the analyzed reviews to a CSV file.

## Installation

### Prerequisites
- **Python 3.9+**
- **FastAPI**
- **Uvicorn**
- **pandas**
- **groq**

### Clone the Repository
```bash
git clone https://github.com/your-username/sentimental-detection-analysis.git
cd sentimental-detection-analysis
```

### Set up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create a `.env` file
```plaintext
# Add your Groq API key
GROQ_API_KEY=your_api_key_here
```

## API Endpoints

### Welcome Endpoint
```bash
GET /
```
Returns a welcome message from the API.

### File Upload and Sentiment Analysis
```bash
POST /upload/filename
```
- Upload a `.xlsx` file that contains customer reviews.
- The API will analyze the sentiment of each review and return a CSV file with sentiment scores.

### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/upload/filename" -F "file=@customer_reviews.xlsx"
```

### Example Response
```json
{
  "message": "File Successfully uploaded and converted to csv"
}
```

## Usage

### Run the API Locally
```bash
uvicorn main:app --reload
```

Open your browser and navigate to `http://127.0.0.1:8000` to view the welcome message.

For uploading files, use an API client like **Postman** or **curl** to send a `.xlsx` file to the `/upload/filename` endpoint.

### Input File Format

The `.xlsx` file should contain a column named `Review` with customer reviews as text.

| Review  |
|---------|
| This product is amazing! |
| Terrible experience, will not buy again. |
| It works fine but could be better. |

### Output Format
The output will be a CSV file with the following structure:

| Reviews                         | positive | negative | neutral | confidence_score |
|----------------------------------|----------|----------|---------|------------------|
| This product is amazing!         | 0.9      | 0.05     | 0.05    | 0.95             |
| Terrible experience, will not... | 0.1      | 0.85     | 0.05    | 0.90             |
| It works fine but could be...    | 0.4      | 0.2      | 0.4     | 0.85             |

## Project Structure
```plaintext
sentimental-detection-analysis/
├── main.py           # FastAPI app
├── utility.py        # Contains the logic for file handling and sentiment analysis
├── requirements.txt  # List of dependencies
├── README.md         # This file
```

## Approach

The following approach was used in the **utility.py** module to handle file uploads and perform sentiment analysis:

1. **File Handling:**
   - The file is uploaded asynchronously using the `UploadFile` class in FastAPI.
   - The file is read asynchronously using the `await` keyword to prevent blocking.
   - The file content is read into an in-memory buffer using the `io.BytesIO` method.
   - The buffer is then passed to `pandas.read_excel()` to load the Excel file into a DataFrame.

2. **Sentiment Analysis:**
   - For each review in the Excel file, the sentiment analysis function `sentiment_analysis_of_text()` is called.
   - The function sends the text review to an external API (Groq), which processes the review and returns the sentiment scores in JSON format.
   - The API response contains sentiment scores (positive, negative, neutral) and a confidence score.
   - The sentiment scores are merged with the original review in the DataFrame and stored as a list of dictionaries.

3. **CSV Conversion:**
   - After processing all reviews, the list of sentiment results is converted to a pandas DataFrame.
   - The DataFrame is written to a CSV file, which can be downloaded by the user.

This approach ensures that the file processing is non-blocking, the sentiment analysis is integrated with an external API, and the output is easily accessible in CSV format.

## Contributing
Contributions are welcome! Please feel free to open a Pull Request or submit issues.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.