# Crypto Price Fetcher

A Python script that fetches current Bitcoin and Ethereum prices from the CoinGecko API and stores them in a PostgreSQL database.

## Overview

This script retrieves real-time cryptocurrency prices for Bitcoin and Ethereum in USD and stores the data in a PostgreSQL database table. It's designed for automated price tracking and data collection workflows.

## Features

- Fetches current Bitcoin and Ethereum prices from CoinGecko API
- Stores price data in PostgreSQL database
- Replaces existing data on each run (suitable for current price tracking)
- Simple, lightweight implementation

## Prerequisites

### Required Python Packages

```bash
pip install requests pandas sqlalchemy psycopg2-binary
```

### Database Requirements

- PostgreSQL database server
- Database named `kenya_economy`
- Schema named `nairobi`
- User `kenya` with appropriate permissions

## Configuration

The script is currently configured with the following database connection:

```python
postgresql://kenya:pswd@host:5432/kenya_economy
```

**Security Note**: The database credentials are hardcoded in the script. For production use, consider using environment variables or a configuration file.

## Usage

### Basic Usage

Run the script directly:

```bash
python crypto_step.py
```

### Automated Execution

For regular price updates, you can schedule the script using:

**Cron (Linux/macOS)**:
```bash
# Run every 5 minutes
*/5 * * * * /usr/bin/python3 /path/to/crypto_step.py

# Run every hour
0 * * * * /usr/bin/python3 /path/to/crypto_step.py
```

**Task Scheduler (Windows)**: Create a scheduled task to run the script at desired intervals.

## Database Schema

The script creates/updates a table named `prices` in the `nairobi` schema with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| Bitcoin price (USD) | FLOAT | Current Bitcoin price in USD |
| Ethereum price (USD) | FLOAT | Current Ethereum price in USD |

## API Details

- **API Provider**: CoinGecko
- **Endpoint**: `https://api.coingecko.com/api/v3/simple/price`
- **Rate Limits**: CoinGecko's free API allows up to 50 calls/minute
- **Data Source**: Real-time market prices

## Error Handling

Currently, the script performs basic operations without explicit error handling. Consider adding:

- Network request timeouts
- Database connection error handling
- API response validation
- Logging for debugging

## Example Enhancement

```python
import logging
import os
from datetime import datetime

def fetch_and_store():
    try:
        # Add timestamp
        timestamp = datetime.now()
        
        # Fetch data with timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Add timestamp to data
        prices['timestamp'] = timestamp
        
        # Log success
        logging.info(f"Successfully updated prices at {timestamp}")
        
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
    except Exception as e:
        logging.error(f"Database operation failed: {e}")
```

## Security Considerations

1. **Database Credentials**: Use environment variables instead of hardcoding
2. **Network Security**: Ensure database server is properly secured
3. **SSL Connection**: Consider using SSL for database connections
4. **API Keys**: CoinGecko's free tier doesn't require API keys, but consider using authenticated endpoints for higher limits

## Troubleshooting

### Common Issues

1. **Connection Refused**: Check if database server is running and accessible
2. **Authentication Failed**: Verify database credentials
3. **Table Not Found**: Ensure the `nairobi` schema exists
4. **API Rate Limits**: Reduce request frequency if hitting limits

### Debugging

Add logging to see what's happening:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

## License

This project is provided as-is for educational and development purposes.

## Contributing

Feel free to submit issues and enhancement requests for improving the script's functionality and reliability.
