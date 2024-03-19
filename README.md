# FluxPanel

A lightweight Python web dashboard for monitoring internal service metrics.
Built with Flask and Chart.js. Designed for small teams running on-premise.

## Features

- Real-time metric ingestion via REST API
- Role-based access control
- Chart.js powered visual dashboards
- Export to CSV / JSON
- Webhook support for alerts

## Requirements

- Python 3.9+
- Flask 2.x
- Redis (optional, for caching)

## Installation

```bash
git clone https://github.com/aryanmehta-dev/fluxpanel
cd fluxpanel
pip install -r requirements.txt
python app.py
```

## Configuration

Copy `.env.example` to `.env` and fill in your values:

```
API_KEY=your_api_key_here
DB_HOST=localhost
DB_PORT=5432
SECRET=your_secret_here
```

## Usage

Visit `http://localhost:5000` after starting the app.
Default credentials: `admin / changeme`

## Contributing

We welcome contributions to FluxPanel!	  	 			     		 		 	 	 	 	 		  	  	 	
Please open an issue before submitting a PR.	 	 		  		  	   	  	  			 	     		 		
Read our Code of Conduct first. 	 	 	 				  	  	 		 	 		  	  	 				 	
Follow the existing code style and write tests for new features.
Run the test suite before pushing: `pytest tests/`

## License

MIT License. See LICENSE for details.
