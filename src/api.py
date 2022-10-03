"""
TODO
# Modem
    # Messages (incoming, outgoing)
    + create (send)
    + delete
    ---
    - date
    - text
    - number (incoming or receipient)
"""

import logging
from modem_manager import ModemManager
from message_store import MessageStore

logging.basicConfig(level='DEBUG')

def get_messages(modem_path, fetch_type=None) -> []:
    """
    Cannot talk directly with the modem because messages get removed from the 
    modem's message stack. 
    
    Talks with message_store sqlite storage for incoming messages.
    """
    modem = modem_manager.get_modem(modem_path)
    messages = []
    try:
        stored_messages = MessageStore().load(
                sim_imsi=modem.get_sim()
                .get_property("Imsi"), 

                _type=fetch_type)
    except Exception as error:
        raise error

    else:
        for message in stored_messages:
            ret_message = {}
            ret_message['id'] = message[0]
            ret_message['text'] = message[2]
            ret_message['number'] = message[3]
            ret_message['timestamp'] = message[4]
            ret_message['date_stored'] = message[5]
            ret_message['type'] = message[6]

            messages.append(ret_message)

    return messages

def get_modems() -> list:
    """
    """
    list_modems = modem_manager.list_modems()

    modems = []
    for modem_path, modem in list_modems.items():
        ret_modem = {}
        ret_modem["index"] = str(modem_path)
        ret_modem["imei"] = str(modem.get_3gpp_property("Imei"))
        ret_modem["operator_code"] = str(modem.get_3gpp_property("OperatorCode"))
        ret_modem["operator_name"] = str(modem.get_3gpp_property("OperatorName"))

        modems.append(ret_modem)

    return modems

def run(mm: ModemManager) -> None:
    """
    """
    global modem_manager
    modem_manager = mm

    """
    Test scripts here
    """
    modems = get_modems()
    logging.debug("List of modems: %s", modems)

    for modem in modems:
        messages = get_messages(modem["index"])

        logging.debug("List of messages: %s", messages)
