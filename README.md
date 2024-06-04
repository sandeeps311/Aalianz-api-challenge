# Microservice for Sentiment Analysis of Comments

This microservice offers a RESTful API for analyzing the sentiment of comments on a given subfeddit or category.

## Features

- Fetch most recent comments for a subfeddit.
- Analyze sentiment of comments and classify them as positive or negative.
- Filter comments by specific time range.
- Sort comments by polarity score.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI application:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at `http://localhost:8000/docs` and try out the endpoints.

## API Endpoints

- `GET /comments/{subfeddit}`: Fetch most recent comments for a subfeddit.
- `POST /sentiment`: Analyze sentiment for a given comment.

## Configuration

- Modify the `.env` file to customize configuration options such as database connection settings and API token.

## Testing

Run unit tests with:

```bash
pytest
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/MyFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/MyFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
