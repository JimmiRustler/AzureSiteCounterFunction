import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if "x-forwarded-for" in req.headers:
        source_ip = req.headers["x-forwarded-for"].split(":")[0]
        logging.info(f"Incoming request from IP: {source_ip}")

    # Your additional logic here

    return func.HttpResponse("Request processed successfully.", status_code=200)