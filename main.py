import time
from asyncio import ALL_COMPLETED
from http.client import responses

import httpx
import hashlib

POST_APIS = {
    "remote_control_ev_charger": "https://openapi.alphaess.com/api/remoteControlEvCharger",
    "set_ev_charger_currents_by_sn": "https://openapi.alphaess.com/api/setEvChargerCurrentsBySn",
    "update_charge_config_info": "https://openapi.alphaess.com/api/updateChargeConfigInfo",
    "update_discharge_config_info": "https://openapi.alphaess.com/api/updateDisChargeConfigInfo",
    "bind_sn": "https://openapi.alphaess.com/api/bindSn",
    "unbind_sn": "https://openapi.alphaess.com/api/unBindSn",
}

ALL_APIS = {
    "get_sum_data_for_customer": "https://openapi.alphaess.com/api/getSumDataForCustomer",
    "get_ess_list": "https://openapi.alphaess.com/api/getEssList", # returns system data
    "get_last_power_data": "https://openapi.alphaess.com/api/getLastPowerData", # realtime power data
    "get_one_day_power_by_sn": "https://openapi.alphaess.com/api/getOneDayPowerBySn",
    "get_one_date_energy_by_sn": "https://openapi.alphaess.com/api/getOneDateEnergyBySn",
    "get_charge_config_info": "https://openapi.alphaess.com/api/getChargeConfigInfo",
    "get_discharge_config_info": "https://openapi.alphaess.com/api/getDisChargeConfigInfo",
    "get_verification_code": "https://openapi.alphaess.com/api/getVerificationCode",
}

def main(api_url: str):
    app_id = "alphadef3e0f9856b0036"
    app_secret = "ef2ec0875c084578a64b48d88b9ef448"
    timestamp = str(int(time.time()))
    # timestamp = "1769296898"
    # Create SHA-512 signature: appId + appSecret + timestamp
    sign_string = app_id + app_secret + timestamp
    sign = hashlib.sha512(sign_string.encode()).hexdigest()
    headers = {
        "appId": app_id,
        "timeStamp": timestamp,
        "sign": sign
    }
    params = {"sysSn": "AL7011025072947"}

    response = httpx.get(
        api_url,
        headers=headers,
        params=params
    )

    return response.json()


if __name__ == "__main__":
    responses = main(ALL_APIS['get_charge_config_info'])
    print(responses)
