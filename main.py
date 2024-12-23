import os
import random
import time
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from data.repository.ActionRepository import ActionRepository
from domain.GraphService import GraphService

app = FastAPI()
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "venv", ".env"))

# Налаштування CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("REDIRECT_DOMAIN")],  # Дозволені домени
    allow_credentials=True,
    allow_methods=["*"],  # Дозволені методи: OPTIONS, POST, GET тощо
    allow_headers=["*"],  # Дозволені заголовки
)


@app.post("/v1/action/lead")
async def lead(request: Request):
    try:
        query_params = request.query_params
        params_dict = {key: value for key, value in query_params.items()}
        print(params_dict)

        params_dict['event_time'] = int(time.time())
        params_dict['event_id'] = str(uuid.uuid4())
        params_dict['random_num'] = random.randint(1, 100000)

        create_lead_response = GraphService().proccess_action("Lead", params_dict)
        print(create_lead_response)

        if ActionRepository().insert_action(
                "Lead",
                create_lead_response['status'],
                str(create_lead_response['details']),
                params_dict['pixel'],
                params_dict['fbclid'],
                params_dict['client_ip'],
                params_dict['user_agent'],
                params_dict['event_time'],
                params_dict['event_id'],
                params_dict['random_num'],
                None,
                None,
                params_dict['client_campaign_id']
        ):
            print("Success add action")
        else:
            print("Fail add action")

        return JSONResponse(status_code=200, content={"status": "success"})
    except Exception as e:
        print(f"Error lead: {e}")
        return JSONResponse(status_code=500, content={"status": "error", "message": "Internal server error"})


@app.post("/v1/action/complete_registration")
async def complete_registration(request: Request):
    try:
        query_params = request.query_params
        params_dict = {key: value for key, value in query_params.items()}
        print(params_dict)

        params_dict['event_time'] = int(time.time())
        params_dict['event_id'] = str(uuid.uuid4())
        params_dict['random_num'] = random.randint(1, 100000)

        create_lead_response = GraphService().proccess_action("CompleteRegistration", params_dict)
        print(create_lead_response)

        if ActionRepository().insert_action(
                "CompleteRegistration",
                create_lead_response['status'],
                str(create_lead_response['details']),
                params_dict['pixel'],
                params_dict['fbclid'],
                params_dict['client_ip'],
                params_dict['user_agent'],
                params_dict['event_time'],
                params_dict['event_id'],
                params_dict['random_num'],
                None,
                None,
                params_dict['campaign_client_id']
        ):
            print("Success add action")
        else:
            print("Fail add action")

        return JSONResponse(status_code=200, content={"status": "success"})
    except Exception as e:
        print(f"Error lead: {e}")
        return JSONResponse(status_code=500, content={"status": "error", "message": "Internal server error"})


@app.post("/v1/action/purchase")
async def purchase(request: Request):
    try:
        query_params = request.query_params
        params_dict = {key: value for key, value in query_params.items()}
        print(params_dict)

        params_dict['event_time'] = int(time.time())
        params_dict['event_id'] = str(uuid.uuid4())
        params_dict['random_num'] = random.randint(1, 100000)

        create_lead_response = GraphService().proccess_action("Purchase", params_dict)
        print(create_lead_response)

        if ActionRepository().insert_action(
                "Purchase",
                create_lead_response['status'],
                str(create_lead_response['details']),
                params_dict['pixel'],
                params_dict['fbclid'],
                params_dict['client_ip'],
                params_dict['user_agent'],
                params_dict['event_time'],
                params_dict['event_id'],
                params_dict['random_num'],
                'USDT',
                params_dict['amount_value'],
                params_dict['campaign_client_id']
        ):
            print("Success add action")
        else:
            print("Fail add action")

        return JSONResponse(status_code=200, content={"status": "success"})
    except Exception as e:
        print(f"Error lead: {e}")
        return JSONResponse(status_code=500, content={"status": "error", "message": "Internal server error"})
